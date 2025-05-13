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
        4,1,22,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,
        7,1,7,1,7,3,7,61,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,72,
        8,7,10,7,12,7,75,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,86,
        8,8,10,8,12,8,89,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,100,
        8,9,10,9,12,9,103,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,112,
        8,10,1,10,0,3,14,16,18,11,0,2,4,6,8,10,12,14,16,18,20,0,1,2,0,1,
        3,7,7,118,0,23,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,41,1,0,0,0,8,
        46,1,0,0,0,10,50,1,0,0,0,12,54,1,0,0,0,14,60,1,0,0,0,16,76,1,0,0,
        0,18,90,1,0,0,0,20,111,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,32,3,4,2,0,28,
        32,3,6,3,0,29,32,3,8,4,0,30,32,3,10,5,0,31,27,1,0,0,0,31,28,1,0,
        0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,7,0,0,0,34,37,
        5,21,0,0,35,36,5,13,0,0,36,38,3,12,6,0,37,35,1,0,0,0,37,38,1,0,0,
        0,38,39,1,0,0,0,39,40,5,12,0,0,40,5,1,0,0,0,41,42,5,21,0,0,42,43,
        5,13,0,0,43,44,3,12,6,0,44,45,5,12,0,0,45,7,1,0,0,0,46,47,5,4,0,
        0,47,48,3,12,6,0,48,49,5,12,0,0,49,9,1,0,0,0,50,51,5,5,0,0,51,52,
        3,12,6,0,52,53,5,12,0,0,53,11,1,0,0,0,54,55,3,14,7,0,55,13,1,0,0,
        0,56,57,6,7,-1,0,57,58,5,11,0,0,58,61,3,14,7,2,59,61,3,16,8,0,60,
        56,1,0,0,0,60,59,1,0,0,0,61,73,1,0,0,0,62,63,10,5,0,0,63,64,5,8,
        0,0,64,72,3,14,7,6,65,66,10,4,0,0,66,67,5,9,0,0,67,72,3,14,7,5,68,
        69,10,3,0,0,69,70,5,10,0,0,70,72,3,14,7,4,71,62,1,0,0,0,71,65,1,
        0,0,0,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,
        15,1,0,0,0,75,73,1,0,0,0,76,77,6,8,-1,0,77,78,3,18,9,0,78,87,1,0,
        0,0,79,80,10,3,0,0,80,81,5,14,0,0,81,86,3,18,9,0,82,83,10,2,0,0,
        83,84,5,15,0,0,84,86,3,18,9,0,85,79,1,0,0,0,85,82,1,0,0,0,86,89,
        1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,17,1,0,0,0,89,87,1,0,0,0,
        90,91,6,9,-1,0,91,92,3,20,10,0,92,101,1,0,0,0,93,94,10,3,0,0,94,
        95,5,16,0,0,95,100,3,20,10,0,96,97,10,2,0,0,97,98,5,17,0,0,98,100,
        3,20,10,0,99,93,1,0,0,0,99,96,1,0,0,0,100,103,1,0,0,0,101,99,1,0,
        0,0,101,102,1,0,0,0,102,19,1,0,0,0,103,101,1,0,0,0,104,112,5,20,
        0,0,105,112,5,21,0,0,106,112,5,6,0,0,107,108,5,18,0,0,108,109,3,
        12,6,0,109,110,5,19,0,0,110,112,1,0,0,0,111,104,1,0,0,0,111,105,
        1,0,0,0,111,106,1,0,0,0,111,107,1,0,0,0,112,21,1,0,0,0,11,25,31,
        37,60,71,73,85,87,99,101,111
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float32'", "'float64'", "'print'", 
                     "'read'", "<INVALID>", "'string'", "'&&'", "'||'", 
                     "'^'", "'!'", "';'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT32", "FLOAT64", "PRINT", 
                      "READ", "STRING", "STRING_TYPE", "AND", "OR", "XOR", 
                      "NEG", "SEMICOLON", "EQUALITY", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "LP", "RP", "NUMBER", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_assignment = 3
    RULE_printFunc = 4
    RULE_readFunc = 5
    RULE_expr = 6
    RULE_logicalExpr = 7
    RULE_arithmeticExpr = 8
    RULE_term = 9
    RULE_factor = 10

    ruleNames =  [ "program", "statement", "declaration", "assignment", 
                   "printFunc", "readFunc", "expr", "logicalExpr", "arithmeticExpr", 
                   "term", "factor" ]

    EOF = Token.EOF
    INT=1
    FLOAT32=2
    FLOAT64=3
    PRINT=4
    READ=5
    STRING=6
    STRING_TYPE=7
    AND=8
    OR=9
    XOR=10
    NEG=11
    SEMICOLON=12
    EQUALITY=13
    PLUS=14
    MINUS=15
    MULTIPLY=16
    DIVIDE=17
    LP=18
    RP=19
    NUMBER=20
    ID=21
    WS=22

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2097342) != 0)):
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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.declaration()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assignment()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.printFunc()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
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

        def FLOAT32(self):
            return self.getToken(MyLangParser.FLOAT32, 0)

        def FLOAT64(self):
            return self.getToken(MyLangParser.FLOAT64, 0)

        def STRING_TYPE(self):
            return self.getToken(MyLangParser.STRING_TYPE, 0)

        def EQUALITY(self):
            return self.getToken(MyLangParser.EQUALITY, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


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
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 142) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 34
            self.match(MyLangParser.ID)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 35
                self.match(MyLangParser.EQUALITY)
                self.state = 36
                self.expr()


            self.state = 39
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
            self.state = 41
            self.match(MyLangParser.ID)
            self.state = 42
            self.match(MyLangParser.EQUALITY)
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
            self.state = 46
            self.match(MyLangParser.PRINT)
            self.state = 47
            self.expr()
            self.state = 48
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
            self.state = 50
            self.match(MyLangParser.READ)
            self.state = 51
            self.expr()
            self.state = 52
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

        def logicalExpr(self):
            return self.getTypedRuleContext(MyLangParser.LogicalExprContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.logicalExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(MyLangParser.NEG, 0)

        def logicalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.LogicalExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.LogicalExprContext,i)


        def arithmeticExpr(self):
            return self.getTypedRuleContext(MyLangParser.ArithmeticExprContext,0)


        def AND(self):
            return self.getToken(MyLangParser.AND, 0)

        def OR(self):
            return self.getToken(MyLangParser.OR, 0)

        def XOR(self):
            return self.getToken(MyLangParser.XOR, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_logicalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.LogicalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_logicalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 57
                self.match(MyLangParser.NEG)
                self.state = 58
                self.logicalExpr(2)
                pass
            elif token in [6, 18, 20, 21]:
                self.state = 59
                self.arithmeticExpr(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 62
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 63
                        self.match(MyLangParser.AND)
                        self.state = 64
                        self.logicalExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 65
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 66
                        self.match(MyLangParser.OR)
                        self.state = 67
                        self.logicalExpr(5)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 68
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 69
                        self.match(MyLangParser.XOR)
                        self.state = 70
                        self.logicalExpr(4)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MyLangParser.TermContext,0)


        def arithmeticExpr(self):
            return self.getTypedRuleContext(MyLangParser.ArithmeticExprContext,0)


        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_arithmeticExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ArithmeticExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_arithmeticExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 79
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 80
                        self.match(MyLangParser.PLUS)
                        self.state = 81
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 82
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 83
                        self.match(MyLangParser.MINUS)
                        self.state = 84
                        self.term(0)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MyLangParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(MyLangParser.TermContext,0)


        def MULTIPLY(self):
            return self.getToken(MyLangParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MyLangParser.DIVIDE, 0)

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



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 93
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 94
                        self.match(MyLangParser.MULTIPLY)
                        self.state = 95
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 96
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 97
                        self.match(MyLangParser.DIVIDE)
                        self.state = 98
                        self.factor()
                        pass

             
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

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
        self.enterRule(localctx, 20, self.RULE_factor)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(MyLangParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(MyLangParser.ID)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(MyLangParser.STRING)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(MyLangParser.LP)
                self.state = 108
                self.expr()
                self.state = 109
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.logicalExpr_sempred
        self._predicates[8] = self.arithmeticExpr_sempred
        self._predicates[9] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpr_sempred(self, localctx:LogicalExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def arithmeticExpr_sempred(self, localctx:ArithmeticExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




