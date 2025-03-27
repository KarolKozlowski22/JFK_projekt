from lexer_parser.MyLangParserVisitor import MyLangParserVisitor
from lexer_parser.MyLangParser import MyLangParser
from compiler.ir_generator import IRGenerator

class ASTBuilder(MyLangParserVisitor):
    def __init__(self):
        super().__init__()
        self.ir_gen=IRGenerator()

    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        ast = [self.visit(child) for child in ctx.statement()]
        ir_module = self.ir_gen.generate(ast)
        return ast, ir_module
    
    def visitDeclaration(self, ctx):
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
        return ('assignment', ctx.ID().getText(), self.visit(ctx.expr()))
    
    def visitPrintFunc(self, ctx: MyLangParser.PrintFuncContext):
        return ('print', self.visit(ctx.expr()))
    
    def visitReadFunc(self, ctx: MyLangParser.ReadFuncContext):
        return ('read', self.visit(ctx.expr()))
    
    def visitExpr(self, ctx: MyLangParser.ExprContext):
        node = self.visit(ctx.term(0))  
        for i in range(1, ctx.getChildCount(), 2): 
            op = ctx.getChild(i).getText() 
            right = self.visit(ctx.term((i+1) // 2))  
            node = (op, node, right)  
        return node

    
    def visitTerm(self, ctx: MyLangParser.TermContext):
        node = self.visit(ctx.factor(0))  
        for i in range(1, ctx.getChildCount(), 2):  
            op = ctx.getChild(i).getText()  
            right = self.visit(ctx.factor((i+1) // 2))  
            node = (op, node, right) 
        return node

    
    def visitFactor(self, ctx: MyLangParser.FactorContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        elif ctx.ID():
            return ctx.ID().getText()
        else:
            return self.visit(ctx.expr())
