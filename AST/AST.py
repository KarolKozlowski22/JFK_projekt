# AST.py
from lexer_parser.MyLangParserVisitor import MyLangParserVisitor
from lexer_parser.MyLangParser import MyLangParser
from compiler.ir_generator import IRGenerator


class ASTBuilder(MyLangParserVisitor):
    """
    Buduje uproszczone drzewo AST (lista krotek) z parse-tree Antlr
    i od razu przekazuje je do IRGenerator.
    """

    def __init__(self):
        super().__init__()
        self.ir_gen = IRGenerator()

    # ─────────────────────────────  GŁÓWNY WEJŚCIE  ──────────────────────────
    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        ast: list[tuple] = []
        for st in ctx.statement():
            node = self.visit(st)
            if node is not None:
                ast.append(node)

        ir_module = self.ir_gen.generate(ast)
        return ast, ir_module

    # ─────────────────────────────  DEKLARACJE  ─────────────────────────────
    def visitDeclaration(self, ctx: MyLangParser.DeclarationContext):
        var_type = ctx.typeName().getText()
        name = ctx.ID().getText()

        if ctx.expr():
            return ("declaration", var_type, name, "=", self.visit(ctx.expr()))
        return ("declaration", var_type, name)

    # ─────────────────────────────  STRUKTURY  ──────────────────────────────
    def visitStructDecl(self, ctx: MyLangParser.StructDeclContext):
        name = ctx.ID().getText()
        fields = [
            (f.typeName().getText(), f.ID().getText())  # (typ, nazwa)
            for f in ctx.structMember()
        ]
        return ("struct_decl", name, fields)

    # ─────────────────────────────  L-VALUE  & ASSIGN  ──────────────────────
    def _lvalue_to_ast(self, lv_ctx: MyLangParser.LvalueContext):
        """
        Zamienia lvalue (ID ('.' ID)*) → łańcuch pól:
        a.b.c  →  ('field', ('field', 'a', 'b'), 'c')
        """
        ids = [tok.getText() for tok in lv_ctx.ID()]
        base = ids[0]
        for fld in ids[1:]:
            base = ("field", base, fld)
        return base

    def visitAssignment(self, ctx: MyLangParser.AssignmentContext):
        lv_expr = self._lvalue_to_ast(ctx.lvalue())
        rhs = self.visit(ctx.expr())

        # uproszczenie: jeśli kropka nie występuje, zwracamy zwykłe assignment
        if isinstance(lv_expr, str):
            return ("assignment", lv_expr, rhs)

        # jeden poziom: a.b = …
        if isinstance(lv_expr, tuple) and lv_expr[0] == "field":
            base, fld = lv_expr[1], lv_expr[2]
            if not isinstance(base, str):
                raise NotImplementedError(
                    "Wielopoziomowe przypisania (a.b.c = …) wymagają "
                    "rozszerzenia IRGenerator."
                )
            return ("field_assignment", base, fld, rhs)

        raise NotImplementedError(
            "Nieobsługiwany lvalue – rozbuduj ASTBuilder/IRGenerator."
        )

    # ─────────────────────────────  IO  ─────────────────────────────────────
    def visitPrintFunc(self, ctx: MyLangParser.PrintFuncContext):
        return ("print", self.visit(ctx.expr()))

    def visitReadFunc(self, ctx: MyLangParser.ReadFuncContext):
        return ("read", self.visit(ctx.expr()))

    # ─────────────────────────────  WYRAŻENIA  ──────────────────────────────
    # logicExpr → delegacja do pod-reguł
    def visitExpr(self, ctx: MyLangParser.ExprContext):
        return self.visit(ctx.logicalExpr())

    # logic (||, &&, ^, !)
    def visitLogicalExpr(self, ctx: MyLangParser.LogicalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpr())

        if ctx.getChildCount() == 2:  # !expr
            op = ctx.NEG().getText()
            return (op, self.visit(ctx.logicalExpr(0)))

        left = self.visit(ctx.logicalExpr(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.logicalExpr(1))
        return (op, left, right)

    # relational (<, <=, …)
    def visitRelationalExpr(self, ctx: MyLangParser.RelationalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arithmeticExpr(0))

        left = self.visit(ctx.arithmeticExpr(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.arithmeticExpr(1))
        return (op, left, right)

    # arith (+, -)
    def visitArithmeticExpr(self, ctx: MyLangParser.ArithmeticExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())

        left = self.visit(ctx.arithmeticExpr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.term())
        return (op, left, right)

    # term (*, /)
    def visitTerm(self, ctx: MyLangParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())

        left = self.visit(ctx.term())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.factor())
        return (op, left, right)

    # factor = primary ('.' ID)*
    def visitFactor(self, ctx: MyLangParser.FactorContext):
        # Łańcuch pól
        base = self.visit(ctx.primary())
        for dot_id in ctx.ID():
            base = ("field", base, dot_id.getText())
        return base

    # ─────────────────────────────  PRIMARY  ───────────────────────────────
    # --- zamień całą dotychczasową metodę visitPrimary na tę -----------------
    def visitPrimary(self, ctx: MyLangParser.PrimaryContext):
        # -----------------------------------------------------------
        # 1.  Wywołanie funkcji  foo(...)   – z argumentami LUB bez
        # -----------------------------------------------------------
        if ctx.LP():                          # jeżeli w ogóle występuje '('
            name = ctx.ID().getText()
            if ctx.expr():                    # są argumenty w środku
                args = [self.visit(e) for e in ctx.expr()]
            else:                             # puste nawiasy  foo()
                args = []
            return ("call", name, args)

        # -----------------------------------------------------------
        # 2.  Literały numeryczne
        # -----------------------------------------------------------
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            return float(txt) if "." in txt else int(txt)

        # -----------------------------------------------------------
        # 3.  Literał string
        # -----------------------------------------------------------
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        # -----------------------------------------------------------
        # 4.  Pojedynczy identyfikator
        # -----------------------------------------------------------
        if ctx.ID():
            return ctx.ID().getText()

        # -----------------------------------------------------------
        # 5.  (expr)
        # -----------------------------------------------------------
        if ctx.expr():
            return self.visit(ctx.expr())

        # -----------------------------------------------------------
        # 6.  !factor   (unary negacja)
        # -----------------------------------------------------------
        if ctx.NEG():
            return ("!", self.visit(ctx.factor()))

        raise ValueError("Nieobsłużona konstrukcja w Primary")


    # ─────────────────────────────  INSTR. STER.  ──────────────────────────
    def visitIfStatement(self, ctx: MyLangParser.IfStatementContext):
        cond = self.visit(ctx.expr())
        then_blk = [self.visit(s) for s in ctx.block(0).statement()]
        else_blk = (
            [self.visit(s) for s in ctx.block(1).statement()]
            if ctx.block(1)
            else []
        )
        return ("if", cond, then_blk, else_blk)

    def visitWhileStatement(self, ctx: MyLangParser.WhileStatementContext):
        cond = self.visit(ctx.expr())
        body = [self.visit(s) for s in ctx.block().statement()]
        return ("while", cond, body)

    # ─────────────────────────────  FUNKCJE  ───────────────────────────────
    def visitFunctionDecl(self, ctx: MyLangParser.FunctionDeclContext):
        ids = ctx.ID()
        name = ids[0].getText()
        params = [tok.getText() for tok in ids[1:]]
        body = [self.visit(s) for s in ctx.block().statement()]
        return ("function", name, params, body)

    def visitReturnStatement(self, ctx: MyLangParser.ReturnStatementContext):
        return ("return", self.visit(ctx.expr()))

    # ─────────────────────────────  INNE  ──────────────────────────────────
    def visitExprStatement(self, ctx: MyLangParser.ExprStatementContext):
        return self.visit(ctx.expr())
