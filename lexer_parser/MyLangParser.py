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
        4,1,13,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,3,6,46,8,6,1,6,1,6,1,6,5,6,51,8,6,10,6,12,6,54,9,6,1,6,0,
        1,12,7,0,2,4,6,8,10,12,0,2,1,0,1,2,1,0,7,10,54,0,15,1,0,0,0,2,23,
        1,0,0,0,4,25,1,0,0,0,6,29,1,0,0,0,8,34,1,0,0,0,10,38,1,0,0,0,12,
        45,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,
        0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,3,4,2,0,20,24,3,6,3,0,21,24,3,
        8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,
        22,1,0,0,0,24,3,1,0,0,0,25,26,7,0,0,0,26,27,5,12,0,0,27,28,5,5,0,
        0,28,5,1,0,0,0,29,30,5,12,0,0,30,31,5,6,0,0,31,32,3,12,6,0,32,33,
        5,5,0,0,33,7,1,0,0,0,34,35,5,3,0,0,35,36,3,12,6,0,36,37,5,5,0,0,
        37,9,1,0,0,0,38,39,5,4,0,0,39,40,3,12,6,0,40,41,5,5,0,0,41,11,1,
        0,0,0,42,43,6,6,-1,0,43,46,5,11,0,0,44,46,5,12,0,0,45,42,1,0,0,0,
        45,44,1,0,0,0,46,52,1,0,0,0,47,48,10,1,0,0,48,49,7,1,0,0,49,51,3,
        12,6,2,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,
        13,1,0,0,0,54,52,1,0,0,0,4,17,23,45,52
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'print'", "'read'", 
                     "';'", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "PRINT", "READ", "SEMICOLON", 
                      "EQUALITY", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "NUMBER", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_assignment = 3
    RULE_printFunc = 4
    RULE_readFunc = 5
    RULE_expr = 6

    ruleNames =  [ "program", "statement", "declaration", "assignment", 
                   "printFunc", "readFunc", "expr" ]

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
    NUMBER=11
    ID=12
    WS=13

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




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4126) != 0)):
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




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.declaration()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.printFunc()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
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




    def declaration(self):

        localctx = MyLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 26
            self.match(MyLangParser.ID)
            self.state = 27
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




    def assignment(self):

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MyLangParser.ID)
            self.state = 30
            self.match(MyLangParser.EQUALITY)
            self.state = 31
            self.expr(0)
            self.state = 32
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




    def printFunc(self):

        localctx = MyLangParser.PrintFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MyLangParser.PRINT)
            self.state = 35
            self.expr(0)
            self.state = 36
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




    def readFunc(self):

        localctx = MyLangParser.ReadFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MyLangParser.READ)
            self.state = 39
            self.expr(0)
            self.state = 40
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

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(MyLangParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MyLangParser.DIVIDE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 43
                self.match(MyLangParser.NUMBER)
                pass
            elif token in [12]:
                self.state = 44
                self.match(MyLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 47
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 48
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 49
                    self.expr(2) 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




