# Generated from MyLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#exprStatement.
    def visitExprStatement(self, ctx:MyLangParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#declaration.
    def visitDeclaration(self, ctx:MyLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignment.
    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#printFunc.
    def visitPrintFunc(self, ctx:MyLangParser.PrintFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#readFunc.
    def visitReadFunc(self, ctx:MyLangParser.ReadFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifStatement.
    def visitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:MyLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#returnStatement.
    def visitReturnStatement(self, ctx:MyLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expr.
    def visitExpr(self, ctx:MyLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#logicalExpr.
    def visitLogicalExpr(self, ctx:MyLangParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MyLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:MyLangParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#term.
    def visitTerm(self, ctx:MyLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#factor.
    def visitFactor(self, ctx:MyLangParser.FactorContext):
        return self.visitChildren(ctx)



del MyLangParser