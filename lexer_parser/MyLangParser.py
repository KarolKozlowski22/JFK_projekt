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
        4,1,39,248,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,1,2,1,2,4,
        2,70,8,2,11,2,12,2,71,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,
        5,1,5,1,5,3,5,87,8,5,1,5,1,5,1,6,1,6,1,6,5,6,94,8,6,10,6,12,6,97,
        9,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,122,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,136,8,
        13,10,13,12,13,139,9,13,3,13,141,8,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,15,1,15,5,15,152,8,15,10,15,12,15,155,9,15,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,17,3,17,165,8,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,5,17,176,8,17,10,17,12,17,179,9,17,1,18,1,
        18,1,18,3,18,184,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,5,19,195,8,19,10,19,12,19,198,9,19,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,5,20,209,8,20,10,20,12,20,212,9,20,1,21,1,21,1,
        21,5,21,217,8,21,10,21,12,21,220,9,21,1,22,1,22,1,22,1,22,1,22,5,
        22,227,8,22,10,22,12,22,230,9,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,246,8,22,1,22,0,3,34,
        38,40,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,0,2,2,0,7,10,37,37,1,0,17,22,258,0,47,1,0,0,0,2,63,1,0,
        0,0,4,65,1,0,0,0,6,76,1,0,0,0,8,80,1,0,0,0,10,82,1,0,0,0,12,90,1,
        0,0,0,14,98,1,0,0,0,16,103,1,0,0,0,18,106,1,0,0,0,20,110,1,0,0,0,
        22,114,1,0,0,0,24,123,1,0,0,0,26,129,1,0,0,0,28,145,1,0,0,0,30,149,
        1,0,0,0,32,158,1,0,0,0,34,164,1,0,0,0,36,180,1,0,0,0,38,185,1,0,
        0,0,40,199,1,0,0,0,42,213,1,0,0,0,44,245,1,0,0,0,46,48,3,2,1,0,47,
        46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,
        0,51,52,5,0,0,1,52,1,1,0,0,0,53,64,3,10,5,0,54,64,3,4,2,0,55,64,
        3,14,7,0,56,64,3,18,9,0,57,64,3,20,10,0,58,64,3,22,11,0,59,64,3,
        24,12,0,60,64,3,26,13,0,61,64,3,28,14,0,62,64,3,16,8,0,63,53,1,0,
        0,0,63,54,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,
        1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,
        64,3,1,0,0,0,65,66,5,1,0,0,66,67,5,37,0,0,67,69,5,33,0,0,68,70,3,
        6,3,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,
        73,1,0,0,0,73,74,5,34,0,0,74,75,5,30,0,0,75,5,1,0,0,0,76,77,3,8,
        4,0,77,78,5,37,0,0,78,79,5,30,0,0,79,7,1,0,0,0,80,81,7,0,0,0,81,
        9,1,0,0,0,82,83,3,8,4,0,83,86,5,37,0,0,84,85,5,27,0,0,85,87,3,32,
        16,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,30,0,0,89,
        11,1,0,0,0,90,95,5,37,0,0,91,92,5,28,0,0,92,94,5,37,0,0,93,91,1,
        0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,13,1,0,0,0,97,
        95,1,0,0,0,98,99,3,12,6,0,99,100,5,27,0,0,100,101,3,32,16,0,101,
        102,5,30,0,0,102,15,1,0,0,0,103,104,3,32,16,0,104,105,5,30,0,0,105,
        17,1,0,0,0,106,107,5,11,0,0,107,108,3,32,16,0,108,109,5,30,0,0,109,
        19,1,0,0,0,110,111,5,12,0,0,111,112,3,32,16,0,112,113,5,30,0,0,113,
        21,1,0,0,0,114,115,5,3,0,0,115,116,5,31,0,0,116,117,3,32,16,0,117,
        118,5,32,0,0,118,121,3,30,15,0,119,120,5,4,0,0,120,122,3,30,15,0,
        121,119,1,0,0,0,121,122,1,0,0,0,122,23,1,0,0,0,123,124,5,5,0,0,124,
        125,5,31,0,0,125,126,3,32,16,0,126,127,5,32,0,0,127,128,3,30,15,
        0,128,25,1,0,0,0,129,130,5,2,0,0,130,131,5,37,0,0,131,140,5,31,0,
        0,132,137,5,37,0,0,133,134,5,29,0,0,134,136,5,37,0,0,135,133,1,0,
        0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,141,1,0,
        0,0,139,137,1,0,0,0,140,132,1,0,0,0,140,141,1,0,0,0,141,142,1,0,
        0,0,142,143,5,32,0,0,143,144,3,30,15,0,144,27,1,0,0,0,145,146,5,
        6,0,0,146,147,3,32,16,0,147,148,5,30,0,0,148,29,1,0,0,0,149,153,
        5,33,0,0,150,152,3,2,1,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,
        5,34,0,0,157,31,1,0,0,0,158,159,3,34,17,0,159,33,1,0,0,0,160,161,
        6,17,-1,0,161,162,5,16,0,0,162,165,3,34,17,2,163,165,3,36,18,0,164,
        160,1,0,0,0,164,163,1,0,0,0,165,177,1,0,0,0,166,167,10,5,0,0,167,
        168,5,13,0,0,168,176,3,34,17,6,169,170,10,4,0,0,170,171,5,14,0,0,
        171,176,3,34,17,5,172,173,10,3,0,0,173,174,5,15,0,0,174,176,3,34,
        17,4,175,166,1,0,0,0,175,169,1,0,0,0,175,172,1,0,0,0,176,179,1,0,
        0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,35,1,0,0,0,179,177,1,0,0,
        0,180,183,3,38,19,0,181,182,7,1,0,0,182,184,3,38,19,0,183,181,1,
        0,0,0,183,184,1,0,0,0,184,37,1,0,0,0,185,186,6,19,-1,0,186,187,3,
        40,20,0,187,196,1,0,0,0,188,189,10,3,0,0,189,190,5,23,0,0,190,195,
        3,40,20,0,191,192,10,2,0,0,192,193,5,24,0,0,193,195,3,40,20,0,194,
        188,1,0,0,0,194,191,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,
        197,1,0,0,0,197,39,1,0,0,0,198,196,1,0,0,0,199,200,6,20,-1,0,200,
        201,3,42,21,0,201,210,1,0,0,0,202,203,10,3,0,0,203,204,5,25,0,0,
        204,209,3,42,21,0,205,206,10,2,0,0,206,207,5,26,0,0,207,209,3,42,
        21,0,208,202,1,0,0,0,208,205,1,0,0,0,209,212,1,0,0,0,210,208,1,0,
        0,0,210,211,1,0,0,0,211,41,1,0,0,0,212,210,1,0,0,0,213,218,3,44,
        22,0,214,215,5,28,0,0,215,217,5,37,0,0,216,214,1,0,0,0,217,220,1,
        0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,43,1,0,0,0,220,218,1,0,
        0,0,221,222,5,37,0,0,222,223,5,31,0,0,223,228,3,32,16,0,224,225,
        5,29,0,0,225,227,3,32,16,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,1,0,0,0,231,232,
        5,32,0,0,232,246,1,0,0,0,233,234,5,37,0,0,234,235,5,31,0,0,235,246,
        5,32,0,0,236,246,5,36,0,0,237,246,5,37,0,0,238,246,5,35,0,0,239,
        240,5,31,0,0,240,241,3,32,16,0,241,242,5,32,0,0,242,246,1,0,0,0,
        243,244,5,16,0,0,244,246,3,42,21,0,245,221,1,0,0,0,245,233,1,0,0,
        0,245,236,1,0,0,0,245,237,1,0,0,0,245,238,1,0,0,0,245,239,1,0,0,
        0,245,243,1,0,0,0,246,45,1,0,0,0,20,49,63,71,86,95,121,137,140,153,
        164,175,177,183,194,196,208,210,218,228,245
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'def'", "'if'", "'else'", 
                     "'while'", "'return'", "'int'", "'float32'", "'float64'", 
                     "'string'", "'print'", "'read'", "'&&'", "'||'", "'^'", 
                     "'!'", "'<='", "'>='", "'=='", "'!='", "'<'", "'>'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'.'", "','", "';'", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "STRUCT", "DEF", "IF", "ELSE", "WHILE", 
                      "RETURN", "INT", "FLOAT32", "FLOAT64", "STRING_TYPE", 
                      "PRINT", "READ", "AND", "OR", "XOR", "NEG", "LE", 
                      "GE", "EQ", "NEQ", "LT", "GT", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "EQUALITY", "DOT", "COMMA", "SEMICOLON", 
                      "LP", "RP", "CURLY_BRACKET_OPEN", "CURLY_BRACKET_CLOSE", 
                      "STRING", "NUMBER", "ID", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_structDecl = 2
    RULE_structMember = 3
    RULE_typeName = 4
    RULE_declaration = 5
    RULE_lvalue = 6
    RULE_assignment = 7
    RULE_exprStatement = 8
    RULE_printFunc = 9
    RULE_readFunc = 10
    RULE_ifStatement = 11
    RULE_whileStatement = 12
    RULE_functionDecl = 13
    RULE_returnStatement = 14
    RULE_block = 15
    RULE_expr = 16
    RULE_logicalExpr = 17
    RULE_relationalExpr = 18
    RULE_arithmeticExpr = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_primary = 22

    ruleNames =  [ "program", "statement", "structDecl", "structMember", 
                   "typeName", "declaration", "lvalue", "assignment", "exprStatement", 
                   "printFunc", "readFunc", "ifStatement", "whileStatement", 
                   "functionDecl", "returnStatement", "block", "expr", "logicalExpr", 
                   "relationalExpr", "arithmeticExpr", "term", "factor", 
                   "primary" ]

    EOF = Token.EOF
    STRUCT=1
    DEF=2
    IF=3
    ELSE=4
    WHILE=5
    RETURN=6
    INT=7
    FLOAT32=8
    FLOAT64=9
    STRING_TYPE=10
    PRINT=11
    READ=12
    AND=13
    OR=14
    XOR=15
    NEG=16
    LE=17
    GE=18
    EQ=19
    NEQ=20
    LT=21
    GT=22
    PLUS=23
    MINUS=24
    MULTIPLY=25
    DIVIDE=26
    EQUALITY=27
    DOT=28
    COMMA=29
    SEMICOLON=30
    LP=31
    RP=32
    CURLY_BRACKET_OPEN=33
    CURLY_BRACKET_CLOSE=34
    STRING=35
    NUMBER=36
    ID=37
    LINE_COMMENT=38
    WS=39

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

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 242665725934) != 0)):
                    break

            self.state = 51
            self.match(MyLangParser.EOF)
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


        def structDecl(self):
            return self.getTypedRuleContext(MyLangParser.StructDeclContext,0)


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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.structDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.printFunc()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.readFunc()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.functionDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 61
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 62
                self.exprStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MyLangParser.STRUCT, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def CURLY_BRACKET_OPEN(self):
            return self.getToken(MyLangParser.CURLY_BRACKET_OPEN, 0)

        def CURLY_BRACKET_CLOSE(self):
            return self.getToken(MyLangParser.CURLY_BRACKET_CLOSE, 0)

        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StructMemberContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_structDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDecl" ):
                listener.enterStructDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDecl" ):
                listener.exitStructDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = MyLangParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MyLangParser.STRUCT)
            self.state = 66
            self.match(MyLangParser.ID)
            self.state = 67
            self.match(MyLangParser.CURLY_BRACKET_OPEN)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.structMember()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 137438955392) != 0)):
                    break

            self.state = 73
            self.match(MyLangParser.CURLY_BRACKET_CLOSE)
            self.state = 74
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(MyLangParser.TypeNameContext,0)


        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_structMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructMember" ):
                listener.enterStructMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructMember" ):
                listener.exitStructMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMember" ):
                return visitor.visitStructMember(self)
            else:
                return visitor.visitChildren(self)




    def structMember(self):

        localctx = MyLangParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_structMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.typeName()
            self.state = 77
            self.match(MyLangParser.ID)
            self.state = 78
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT32(self):
            return self.getToken(MyLangParser.FLOAT32, 0)

        def FLOAT64(self):
            return self.getToken(MyLangParser.FLOAT64, 0)

        def STRING_TYPE(self):
            return self.getToken(MyLangParser.STRING_TYPE, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = MyLangParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137438955392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def typeName(self):
            return self.getTypedRuleContext(MyLangParser.TypeNameContext,0)


        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MyLangParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 10, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.typeName()
            self.state = 83
            self.match(MyLangParser.ID)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 84
                self.match(MyLangParser.EQUALITY)
                self.state = 85
                self.expr()


            self.state = 88
            self.match(MyLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.DOT)
            else:
                return self.getToken(MyLangParser.DOT, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = MyLangParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MyLangParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 91
                self.match(MyLangParser.DOT)
                self.state = 92
                self.match(MyLangParser.ID)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def lvalue(self):
            return self.getTypedRuleContext(MyLangParser.LvalueContext,0)


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
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.lvalue()
            self.state = 99
            self.match(MyLangParser.EQUALITY)
            self.state = 100
            self.expr()
            self.state = 101
            self.match(MyLangParser.SEMICOLON)
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
        self.enterRule(localctx, 16, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expr()
            self.state = 104
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
        self.enterRule(localctx, 18, self.RULE_printFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MyLangParser.PRINT)
            self.state = 107
            self.expr()
            self.state = 108
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
        self.enterRule(localctx, 20, self.RULE_readFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(MyLangParser.READ)
            self.state = 111
            self.expr()
            self.state = 112
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
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MyLangParser.IF)
            self.state = 115
            self.match(MyLangParser.LP)
            self.state = 116
            self.expr()
            self.state = 117
            self.match(MyLangParser.RP)
            self.state = 118
            self.block()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 119
                self.match(MyLangParser.ELSE)
                self.state = 120
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
        self.enterRule(localctx, 24, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MyLangParser.WHILE)
            self.state = 124
            self.match(MyLangParser.LP)
            self.state = 125
            self.expr()
            self.state = 126
            self.match(MyLangParser.RP)
            self.state = 127
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
        self.enterRule(localctx, 26, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MyLangParser.DEF)
            self.state = 130
            self.match(MyLangParser.ID)
            self.state = 131
            self.match(MyLangParser.LP)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 132
                self.match(MyLangParser.ID)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==29:
                    self.state = 133
                    self.match(MyLangParser.COMMA)
                    self.state = 134
                    self.match(MyLangParser.ID)
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 142
            self.match(MyLangParser.RP)
            self.state = 143
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
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MyLangParser.RETURN)
            self.state = 146
            self.expr()
            self.state = 147
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
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MyLangParser.CURLY_BRACKET_OPEN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 242665725934) != 0):
                self.state = 150
                self.statement()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
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
        self.enterRule(localctx, 32, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_logicalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 161
                self.match(MyLangParser.NEG)
                self.state = 162
                self.logicalExpr(2)
                pass

            elif la_ == 2:
                self.state = 163
                self.relationalExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 166
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 167
                        self.match(MyLangParser.AND)
                        self.state = 168
                        self.logicalExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 169
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 170
                        self.match(MyLangParser.OR)
                        self.state = 171
                        self.logicalExpr(5)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.LogicalExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                        self.state = 172
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 173
                        self.match(MyLangParser.XOR)
                        self.state = 174
                        self.logicalExpr(4)
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.arithmeticExpr(0)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 181
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_arithmeticExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 188
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 189
                        self.match(MyLangParser.PLUS)
                        self.state = 190
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ArithmeticExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                        self.state = 191
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 192
                        self.match(MyLangParser.MINUS)
                        self.state = 193
                        self.term(0)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 202
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 203
                        self.match(MyLangParser.MULTIPLY)
                        self.state = 204
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 205
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 206
                        self.match(MyLangParser.DIVIDE)
                        self.state = 207
                        self.factor()
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def primary(self):
            return self.getTypedRuleContext(MyLangParser.PrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.DOT)
            else:
                return self.getToken(MyLangParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

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
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.primary()
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self.match(MyLangParser.DOT)
                    self.state = 215
                    self.match(MyLangParser.ID) 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
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
            return MyLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MyLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MyLangParser.ID)
                self.state = 222
                self.match(MyLangParser.LP)
                self.state = 223
                self.expr()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==29:
                    self.state = 224
                    self.match(MyLangParser.COMMA)
                    self.state = 225
                    self.expr()
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 231
                self.match(MyLangParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(MyLangParser.ID)
                self.state = 234
                self.match(MyLangParser.LP)
                self.state = 235
                self.match(MyLangParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(MyLangParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.match(MyLangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 238
                self.match(MyLangParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(MyLangParser.LP)
                self.state = 240
                self.expr()
                self.state = 241
                self.match(MyLangParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 243
                self.match(MyLangParser.NEG)
                self.state = 244
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
        self._predicates[17] = self.logicalExpr_sempred
        self._predicates[19] = self.arithmeticExpr_sempred
        self._predicates[20] = self.term_sempred
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
         




