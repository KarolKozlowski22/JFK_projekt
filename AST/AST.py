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
            return self.visit(ctx.arithmeticExpr())
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

    
    def visitFactor(self, ctx: MyLangParser.FactorContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.LP():
            return self.visit(ctx.expr())
        elif ctx.NEG():
            return ('NEG', self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr())
