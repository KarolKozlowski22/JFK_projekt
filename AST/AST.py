from lexer_parser.MyLangParserVisitor import MyLangParserVisitor
from lexer_parser.MyLangParser import MyLangParser
from compiler.ir_generator import IRGenerator

class ASTBuilder(MyLangParserVisitor):
    def __init__(self):
        super().__init__()
        self.ir_gen=IRGenerator()
        self.declared_vars = set() 

    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        ast = [self.visit(child) for child in ctx.statement()]
        ir_module = self.ir_gen.generate(ast)
        return ast, ir_module
    
    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        self.declared_vars.add(var_name)
        if ctx.expr(): 
            return (
                'declaration', 
                ctx.getChild(0).getText(), 
                ctx.ID().getText(),         
                '=',                        
                self.visit(ctx.expr())      
            )
        else:  
            return (
                'declaration',
                ctx.getChild(0).getText(),
                ctx.ID().getText()
            )
    
    def visitAssignment(self, ctx: MyLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        self.declared_vars.add(var_name)
        return ('assignment', ctx.ID().getText(), self.visit(ctx.expr()))
    
    def visitPrintFunc(self, ctx: MyLangParser.PrintFuncContext):
        return ('print', self.visit(ctx.expr()))
    
    def visitReadFunc(self, ctx: MyLangParser.ReadFuncContext):
        return ('read', self.visit(ctx.expr()))
    
    def visitExpr(self, ctx: MyLangParser.ExprContext):
        return self.visit(ctx.logicalExpr())
    
    def visitLogicalExpr(self, ctx: MyLangParser.LogicalExprContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.relationalExpr())
        elif ctx.getChildCount() == 2:  
            op = ctx.getChild(0).getText()  
            right = self.visit(ctx.getChild(1))
            return (op, right)
        elif ctx.getChildCount() == 3:  
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()  
            right = self.visit(ctx.getChild(2))
            return (op, left, right)
    
    def visitArithmeticExpr(self, ctx: MyLangParser.ArithmeticExprContext):
        if ctx.getChildCount() == 1:  
            return self.visit(ctx.term())
        elif ctx.getChildCount() == 3:  
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()  
            right = self.visit(ctx.getChild(2))
            return (op, left, right)

    def visitTerm(self, ctx: MyLangParser.TermContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.factor())
        elif ctx.getChildCount() == 3:  
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText() 
            right = self.visit(ctx.getChild(2))
            return (op, left, right)
        
    def visitExprStatement(self, ctx):
        return self.visit(ctx.expr())
        
    def visitFactor(self, ctx: MyLangParser.FactorContext):
    # 1. literały
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if '.' in text else int(text)
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        # 2. ID [+ optional call]
        if ctx.ID():
            name = ctx.ID().getText()
            if ctx.LP():                      # wywołanie funkcji
                args = [self.visit(e) for e in ctx.expr()]  # będzie pusta lista dla foo()
                return ('call', name, args)
            else:                             # zwykła zmienna
                return name

        # 3. (  expr  )
        if ctx.LP():
            return self.visit(ctx.expr(0))    # tu już wiemy, że expr istnieje

        # 4. !factor  (negacja)
        if ctx.getChild(0).getText() == '!':
            return ('!', self.visit(ctx.getChild(1)))

        # nie powinno się zdarzyć
        raise ValueError("Nieobsłużona konstrukcja w factor")




    
    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.expr())
        then_block = [self.visit(s) for s in ctx.block(0).statement()]
        else_block = [self.visit(s) for s in ctx.block(1).statement()] if ctx.block(1) else []
        return ('if', cond, then_block, else_block)
    
    def visitWhileStatement(self, ctx):
        cond = self.visit(ctx.expr())
        body = [self.visit(s) for s in ctx.block().statement()]
        return ('while', cond, body)

    def visitFunctionDecl(self, ctx):
        ids = ctx.ID()
        name = ids[0].getText()
        params = [p.getText() for p in ids[1:]]  # wszystkie poza nazwą funkcji
        body = [self.visit(s) for s in ctx.block().statement()]
        return ('function', name, params, body)
    
    def visitReturnStatement(self, ctx):
        return ('return', self.visit(ctx.expr()))
    
    def visitFuncCall(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expr()]
        return ('call', func_name, args)
    
    def visitNegation(self, ctx):
        return ('!', self.visit(ctx.factor()))
    
    def visitRelationalExpr(self, ctx: MyLangParser.RelationalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arithmeticExpr(0))
        else:
            left = self.visit(ctx.arithmeticExpr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.arithmeticExpr(1))
            return (op, left, right)
