# Generated from MyLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#exprStatement.
    def enterExprStatement(self, ctx:MyLangParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#exprStatement.
    def exitExprStatement(self, ctx:MyLangParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#declaration.
    def enterDeclaration(self, ctx:MyLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyLangParser#declaration.
    def exitDeclaration(self, ctx:MyLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyLangParser#assignment.
    def enterAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLangParser#assignment.
    def exitAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLangParser#printFunc.
    def enterPrintFunc(self, ctx:MyLangParser.PrintFuncContext):
        pass

    # Exit a parse tree produced by MyLangParser#printFunc.
    def exitPrintFunc(self, ctx:MyLangParser.PrintFuncContext):
        pass


    # Enter a parse tree produced by MyLangParser#readFunc.
    def enterReadFunc(self, ctx:MyLangParser.ReadFuncContext):
        pass

    # Exit a parse tree produced by MyLangParser#readFunc.
    def exitReadFunc(self, ctx:MyLangParser.ReadFuncContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifStatement.
    def enterIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifStatement.
    def exitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileStatement.
    def enterWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileStatement.
    def exitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:MyLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MyLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:MyLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MyLangParser#returnStatement.
    def enterReturnStatement(self, ctx:MyLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#returnStatement.
    def exitReturnStatement(self, ctx:MyLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#expr.
    def enterExpr(self, ctx:MyLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#expr.
    def exitExpr(self, ctx:MyLangParser.ExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#logicalExpr.
    def enterLogicalExpr(self, ctx:MyLangParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#logicalExpr.
    def exitLogicalExpr(self, ctx:MyLangParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#relationalExpr.
    def enterRelationalExpr(self, ctx:MyLangParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#relationalExpr.
    def exitRelationalExpr(self, ctx:MyLangParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:MyLangParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:MyLangParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#term.
    def enterTerm(self, ctx:MyLangParser.TermContext):
        pass

    # Exit a parse tree produced by MyLangParser#term.
    def exitTerm(self, ctx:MyLangParser.TermContext):
        pass


    # Enter a parse tree produced by MyLangParser#factor.
    def enterFactor(self, ctx:MyLangParser.FactorContext):
        pass

    # Exit a parse tree produced by MyLangParser#factor.
    def exitFactor(self, ctx:MyLangParser.FactorContext):
        pass



del MyLangParser