lexer grammar MyLangLexer;

INT : 'int';
FLOAT32: 'float32';
FLOAT64 : 'float64';
PRINT : 'print';
READ : 'read';
STRING : '"' (~["\\] | '\\' .)* '"';
STRING_TYPE : 'string';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
DEF : 'def';
CURLY_BRACKET_OPEN : '{';
CURLY_BRACKET_CLOSE : '}';
RETURN : 'return';
COMMA : ',';

LT : '<';
GT : '>';
LE : '<=';
GE : '>=';
EQ : '==';
NEQ: '!=';


AND : '&&';
OR : '||';
XOR : '^';
NEG : '!';

SEMICOLON : ';';
EQUALITY : '=';
PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';
LP : '(';
RP : ')';

NUMBER : [0-9]+('.'[0-9]+)?;
ID : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;