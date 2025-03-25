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


    # Visit a parse tree produced by MyLangParser#expr.
    def visitExpr(self, ctx:MyLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#term.
    def visitTerm(self, ctx:MyLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#factor.
    def visitFactor(self, ctx:MyLangParser.FactorContext):
        return self.visitChildren(ctx)



del MyLangParser