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
        4,1,36,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,3,3,60,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,84,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,98,8,9,10,9,12,9,101,
        9,9,3,9,103,8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,5,11,114,
        8,11,10,11,12,11,117,9,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,
        3,13,127,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        138,8,13,10,13,12,13,141,9,13,1,14,1,14,1,14,3,14,146,8,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,157,8,15,10,15,12,15,
        160,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,171,8,
        16,10,16,12,16,174,9,16,1,17,1,17,1,17,1,17,1,17,5,17,181,8,17,10,
        17,12,17,184,9,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,3,17,200,8,17,1,17,0,3,26,30,32,18,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,2,0,1,3,7,7,1,0,16,
        21,213,0,37,1,0,0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,55,1,0,0,0,8,63,
        1,0,0,0,10,68,1,0,0,0,12,72,1,0,0,0,14,76,1,0,0,0,16,85,1,0,0,0,
        18,91,1,0,0,0,20,107,1,0,0,0,22,111,1,0,0,0,24,120,1,0,0,0,26,126,
        1,0,0,0,28,142,1,0,0,0,30,147,1,0,0,0,32,161,1,0,0,0,34,199,1,0,
        0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,1,1,0,0,0,41,51,3,6,3,0,42,51,3,8,4,0,43,51,3,10,5,0,
        44,51,3,12,6,0,45,51,3,14,7,0,46,51,3,16,8,0,47,51,3,18,9,0,48,51,
        3,20,10,0,49,51,3,4,2,0,50,41,1,0,0,0,50,42,1,0,0,0,50,43,1,0,0,
        0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,
        1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,3,24,12,0,53,54,5,26,0,
        0,54,5,1,0,0,0,55,56,7,0,0,0,56,59,5,35,0,0,57,58,5,27,0,0,58,60,
        3,24,12,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,26,0,
        0,62,7,1,0,0,0,63,64,5,35,0,0,64,65,5,27,0,0,65,66,3,24,12,0,66,
        67,5,26,0,0,67,9,1,0,0,0,68,69,5,4,0,0,69,70,3,24,12,0,70,71,5,26,
        0,0,71,11,1,0,0,0,72,73,5,5,0,0,73,74,3,24,12,0,74,75,5,26,0,0,75,
        13,1,0,0,0,76,77,5,8,0,0,77,78,5,32,0,0,78,79,3,24,12,0,79,80,5,
        33,0,0,80,83,3,22,11,0,81,82,5,9,0,0,82,84,3,22,11,0,83,81,1,0,0,
        0,83,84,1,0,0,0,84,15,1,0,0,0,85,86,5,10,0,0,86,87,5,32,0,0,87,88,
        3,24,12,0,88,89,5,33,0,0,89,90,3,22,11,0,90,17,1,0,0,0,91,92,5,11,
        0,0,92,93,5,35,0,0,93,102,5,32,0,0,94,99,5,35,0,0,95,96,5,15,0,0,
        96,98,5,35,0,0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,
        1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,102,94,1,0,0,0,102,103,1,
        0,0,0,103,104,1,0,0,0,104,105,5,33,0,0,105,106,3,22,11,0,106,19,
        1,0,0,0,107,108,5,14,0,0,108,109,3,24,12,0,109,110,5,26,0,0,110,
        21,1,0,0,0,111,115,5,12,0,0,112,114,3,2,1,0,113,112,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,
        115,1,0,0,0,118,119,5,13,0,0,119,23,1,0,0,0,120,121,3,26,13,0,121,
        25,1,0,0,0,122,123,6,13,-1,0,123,124,5,25,0,0,124,127,3,26,13,2,
        125,127,3,28,14,0,126,122,1,0,0,0,126,125,1,0,0,0,127,139,1,0,0,
        0,128,129,10,5,0,0,129,130,5,22,0,0,130,138,3,26,13,6,131,132,10,
        4,0,0,132,133,5,23,0,0,133,138,3,26,13,5,134,135,10,3,0,0,135,136,
        5,24,0,0,136,138,3,26,13,4,137,128,1,0,0,0,137,131,1,0,0,0,137,134,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,27,1,
        0,0,0,141,139,1,0,0,0,142,145,3,30,15,0,143,144,7,1,0,0,144,146,
        3,30,15,0,145,143,1,0,0,0,145,146,1,0,0,0,146,29,1,0,0,0,147,148,
        6,15,-1,0,148,149,3,32,16,0,149,158,1,0,0,0,150,151,10,3,0,0,151,
        152,5,28,0,0,152,157,3,32,16,0,153,154,10,2,0,0,154,155,5,29,0,0,
        155,157,3,32,16,0,156,150,1,0,0,0,156,153,1,0,0,0,157,160,1,0,0,
        0,158,156,1,0,0,0,158,159,1,0,0,0,159,31,1,0,0,0,160,158,1,0,0,0,
        161,162,6,16,-1,0,162,163,3,34,17,0,163,172,1,0,0,0,164,165,10,3,
        0,0,165,166,5,30,0,0,166,171,3,34,17,0,167,168,10,2,0,0,168,169,
        5,31,0,0,169,171,3,34,17,0,170,164,1,0,0,0,170,167,1,0,0,0,171,174,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,33,1,0,0,0,174,172,1,
        0,0,0,175,176,5,35,0,0,176,177,5,32,0,0,177,182,3,24,12,0,178,179,
        5,15,0,0,179,181,3,24,12,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,186,
        5,33,0,0,186,200,1,0,0,0,187,188,5,35,0,0,188,189,5,32,0,0,189,200,
        5,33,0,0,190,200,5,34,0,0,191,200,5,35,0,0,192,200,5,6,0,0,193,194,
        5,32,0,0,194,195,3,24,12,0,195,196,5,33,0,0,196,200,1,0,0,0,197,
        198,5,25,0,0,198,200,3,34,17,0,199,175,1,0,0,0,199,187,1,0,0,0,199,
        190,1,0,0,0,199,191,1,0,0,0,199,192,1,0,0,0,199,193,1,0,0,0,199,
        197,1,0,0,0,200,35,1,0,0,0,17,39,50,59,83,99,102,115,126,137,139,
        145,156,158,170,172,182,199
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float32'", "'float64'", "'print'", 
                     "'read'", "<INVALID>", "'string'", "'if'", "'else'", 
                     "'while'", "'def'", "'{'", "'}'", "'return'", "','", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", 
                     "'||'", "'^'", "'!'", "';'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT32", "FLOAT64", "PRINT", 
                      "READ", "STRING", "STRING_TYPE", "IF", "ELSE", "WHILE", 
                      "DEF", "CURLY_BRACKET_OPEN", "CURLY_BRACKET_CLOSE", 
                      "RETURN", "COMMA", "LT", "GT", "LE", "GE", "EQ", "NEQ", 
                      "AND", "OR", "XOR", "NEG", "SEMICOLON", "EQUALITY", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LP", "RP", 
                      "NUMBER", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_exprStatement = 2
    RULE_declaration = 3
    RULE_assignment = 4
    RULE_printFunc = 5
    RULE_readFunc = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_functionDecl = 9
    RULE_returnStatement = 10
    RULE_block = 11
    RULE_expr = 12
    RULE_logicalExpr = 13
    RULE_relationalExpr = 14
    RULE_arithmeticExpr = 15
    RULE_term = 16
    RULE_factor = 17

    ruleNames =  [ "program", "statement", "exprStatement", "declaration", 
                   "assignment", "printFunc", "readFunc", "ifStatement", 
                   "whileStatement", "functionDecl", "returnStatement", 
                   "block", "expr", "logicalExpr", "relationalExpr", "arithmeticExpr", 
                   "term", "factor" ]

    EOF = Token.EOF
    INT=1
    FLOAT32=2
    FLOAT64=3
    PRINT=4
    READ=5
    STRING=6
    STRING_TYPE=7
    IF=8
    ELSE=9
    WHILE=10
    DEF=11
    CURLY_BRACKET_OPEN=12
    CURLY_BRACKET_CLOSE=13
    RETURN=14
    COMMA=15
    LT=16
    GT=17
    LE=18
    GE=19
    EQ=20
    NEQ=21
    AND=22
    OR=23
    XOR=24
    NEG=25
    SEMICOLON=26
    EQUALITY=27
    PLUS=28
    MINUS=29
    MULTIPLY=30
    DIVIDE=31
    LP=32
    RP=33
    NUMBER=34
    ID=35
    WS=36

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 55868149246) != 0)):
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


        def ifStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(MyLangParser.FunctionDeclContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MyLangParser.ReturnStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(MyLangParser.ExprStatementContext,0)


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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.printFunc()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.readFunc()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.functionDecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 48
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 49
                self.exprStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)




    def exprStatement(self):

        localctx = MyLangParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr()
            self.state = 53
            self.match(MyLangParser.SEMICOLON)
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
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 142) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.match(MyLangParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 57
                self.match(MyLangParser.EQUALITY)
                self.state = 58
                self.expr()


            self.state = 61
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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MyLangParser.ID)
            self.state = 64
            self.match(MyLangParser.EQUALITY)
            self.state = 65
            self.expr()
            self.state = 66
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
        self.enterRule(localctx, 10, self.RULE_printFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MyLangParser.PRINT)
            self.state = 69
            self.expr()
            self.state = 70
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
        self.enterRule(localctx, 12, self.RULE_readFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MyLangParser.READ)
            self.state = 73
            self.expr()
            self.state = 74
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def LP(self):
            return self.getToken(MyLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(MyLangParser.RP, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MyLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MyLangParser.IF)
            self.state = 77
            self.match(MyLangParser.LP)
            self.state = 78
            self.expr()
            self.state = 79
            self.match(MyLangParser.RP)
            self.state = 80
            self.block()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 81
                self.match(MyLangParser.ELSE)
                self.state = 82
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def LP(self):
            return self.getToken(MyLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(MyLangParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MyLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MyLangParser.WHILE)
            self.state = 86
            self.match(MyLangParser.LP)
            self.state = 87
            self.expr()
            self.state = 88
            self.match(MyLangParser.RP)
            self.state = 89
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(MyLangParser.DEF, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

        def LP(self):
            return self.getToken(MyLangParser.LP, 0)

        def RP(self):
            return self.getToken(MyLangParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = MyLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MyLangParser.DEF)
            self.state = 92
            self.match(MyLangParser.ID)
            self.state = 93
            self.match(MyLangParser.LP)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 94
                self.match(MyLangParser.ID)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 95
                    self.match(MyLangParser.COMMA)
                    self.state = 96
                    self.match(MyLangParser.ID)
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 104
            self.match(MyLangParser.RP)
            self.state = 105
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MyLangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MyLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MyLangParser.RETURN)
            self.state = 108
            self.expr()
            self.state = 109
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_BRACKET_OPEN(self):
            return self.getToken(MyLangParser.CURLY_BRACKET_OPEN, 0)

        def CURLY_BRACKET_CLOSE(self):
            return self.getToken(MyLangParser.CURLY_BRACKET_CLOSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MyLangParser.CURLY_BRACKET_OPEN)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 55868149246) != 0):
                self.state = 112
                self.statement()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(MyLangParser.CURLY_BRACKET_CLOSE)
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
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
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


        def relationalExpr(self):
            return self.getTypedRuleContext(MyLangParser.RelationalExprContext,0)


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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_logicalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 123
                self.match(MyLangParser.NEG)
                self.state = 124
                self.logicalExpr(2)
                pass

            elif la_ == 2:
                self.state = 125
                self.relationalExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 137
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 128
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 129
                        self.match(MyLangParser.AND)
                        self.state = 130
                        self.logicalExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        self.match(MyLangParser.OR)
                        self.state = 133
                        self.logicalExpr(5)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 134
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 135
                        self.match(MyLangParser.XOR)
                        self.state = 136
                        self.logicalExpr(4)
                        pass

             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ArithmeticExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ArithmeticExprContext,i)


        def LT(self):
            return self.getToken(MyLangParser.LT, 0)

        def GT(self):
            return self.getToken(MyLangParser.GT, 0)

        def LE(self):
            return self.getToken(MyLangParser.LE, 0)

        def GE(self):
            return self.getToken(MyLangParser.GE, 0)

        def EQ(self):
            return self.getToken(MyLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MyLangParser.NEQ, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = MyLangParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.arithmeticExpr(0)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 143
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.arithmeticExpr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_arithmeticExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 156
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 150
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 151
                        self.match(MyLangParser.PLUS)
                        self.state = 152
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 153
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 154
                        self.match(MyLangParser.MINUS)
                        self.state = 155
                        self.term(0)
                        pass

             
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 170
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 164
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 165
                        self.match(MyLangParser.MULTIPLY)
                        self.state = 166
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 167
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 168
                        self.match(MyLangParser.DIVIDE)
                        self.state = 169
                        self.factor()
                        pass

             
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LP(self):
            return self.getToken(MyLangParser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def RP(self):
            return self.getToken(MyLangParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def NEG(self):
            return self.getToken(MyLangParser.NEG, 0)

        def factor(self):
            return self.getTypedRuleContext(MyLangParser.FactorContext,0)


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
        self.enterRule(localctx, 34, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(MyLangParser.ID)
                self.state = 176
                self.match(MyLangParser.LP)
                self.state = 177
                self.expr()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 178
                    self.match(MyLangParser.COMMA)
                    self.state = 179
                    self.expr()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 185
                self.match(MyLangParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(MyLangParser.ID)
                self.state = 188
                self.match(MyLangParser.LP)
                self.state = 189
                self.match(MyLangParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(MyLangParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(MyLangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.match(MyLangParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.match(MyLangParser.LP)
                self.state = 194
                self.expr()
                self.state = 195
                self.match(MyLangParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
                self.match(MyLangParser.NEG)
                self.state = 198
                self.factor()
                pass


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
        self._predicates[13] = self.logicalExpr_sempred
        self._predicates[15] = self.arithmeticExpr_sempred
        self._predicates[16] = self.term_sempred
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
         




