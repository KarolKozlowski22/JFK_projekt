# Generated from MyLangParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,5,6,50,8,6,10,6,12,6,53,9,6,1,7,1,7,1,7,
        5,7,58,8,7,10,7,12,7,61,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,69,8,8,1,
        8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,1,2,1,0,7,8,1,0,9,10,69,0,
        19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,33,1,0,0,0,8,38,1,0,0,0,10,
        42,1,0,0,0,12,46,1,0,0,0,14,54,1,0,0,0,16,68,1,0,0,0,18,20,3,2,1,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,
        0,0,0,23,28,3,4,2,0,24,28,3,6,3,0,25,28,3,8,4,0,26,28,3,10,5,0,27,
        23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,
        0,29,30,7,0,0,0,30,31,5,14,0,0,31,32,5,5,0,0,32,5,1,0,0,0,33,34,
        5,14,0,0,34,35,5,6,0,0,35,36,3,12,6,0,36,37,5,5,0,0,37,7,1,0,0,0,
        38,39,5,3,0,0,39,40,3,12,6,0,40,41,5,5,0,0,41,9,1,0,0,0,42,43,5,
        4,0,0,43,44,3,12,6,0,44,45,5,5,0,0,45,11,1,0,0,0,46,51,3,14,7,0,
        47,48,7,1,0,0,48,50,3,14,7,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,13,1,0,0,0,53,51,1,0,0,0,54,59,3,16,8,0,55,
        56,7,2,0,0,56,58,3,16,8,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,
        0,0,59,60,1,0,0,0,60,15,1,0,0,0,61,59,1,0,0,0,62,69,5,13,0,0,63,
        69,5,14,0,0,64,65,5,11,0,0,65,66,3,12,6,0,66,67,5,12,0,0,67,69,1,
        0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,69,17,1,0,0,0,5,
        21,27,51,59,68
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'print'", "'read'", 
                     "';'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "PRINT", "READ", "SEMICOLON", 
                      "EQUALITY", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "LP", "RP", "NUMBER", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_assignment = 3
    RULE_printFunc = 4
    RULE_readFunc = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "program", "statement", "declaration", "assignment", 
                   "printFunc", "readFunc", "expr", "term", "factor" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    PRINT=3
    READ=4
    SEMICOLON=5
    EQUALITY=6
    PLUS=7
    MINUS=8
    MULTIPLY=9
    DIVIDE=10
    LP=11
    RP=12
    NUMBER=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16414) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MyLangParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def printFunc(self):
            return self.getTypedRuleContext(MyLangParser.PrintFuncContext,0)


        def readFunc(self):
            return self.getTypedRuleContext(MyLangParser.ReadFuncContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.declaration()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.printFunc()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.readFunc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyLangParser.FLOAT, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MyLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self.match(MyLangParser.ID)
            self.state = 31
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def EQUALITY(self):
            return self.getToken(MyLangParser.EQUALITY, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MyLangParser.ID)
            self.state = 34
            self.match(MyLangParser.EQUALITY)
            self.state = 35
            self.expr()
            self.state = 36
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyLangParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_printFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunc" ):
                listener.enterPrintFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunc" ):
                listener.exitPrintFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFunc" ):
                return visitor.visitPrintFunc(self)
            else:
                return visitor.visitChildren(self)




    def printFunc(self):

        localctx = MyLangParser.PrintFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MyLangParser.PRINT)
            self.state = 39
            self.expr()
            self.state = 40
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(MyLangParser.READ, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_readFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadFunc" ):
                listener.enterReadFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadFunc" ):
                listener.exitReadFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadFunc" ):
                return visitor.visitReadFunc(self)
            else:
                return visitor.visitChildren(self)




    def readFunc(self):

        localctx = MyLangParser.ReadFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MyLangParser.READ)
            self.state = 43
            self.expr()
            self.state = 44
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.TermContext)
            else:
                return self.getTypedRuleContext(MyLangParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.PLUS)
            else:
                return self.getToken(MyLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.MINUS)
            else:
                return self.getToken(MyLangParser.MINUS, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MyLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.term()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.term()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.FactorContext)
            else:
                return self.getTypedRuleContext(MyLangParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.MULTIPLY)
            else:
                return self.getToken(MyLangParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.DIVIDE)
            else:
                return self.getToken(MyLangParser.DIVIDE, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MyLangParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.factor()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.factor()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LP(self):
            return self.getToken(MyLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(MyLangParser.RP, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MyLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(MyLangParser.NUMBER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(MyLangParser.ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(MyLangParser.LP)
                self.state = 65
                self.expr()
                self.state = 66
                self.match(MyLangParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





