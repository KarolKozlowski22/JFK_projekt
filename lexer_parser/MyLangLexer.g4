lexer grammar MyLangLexer;

INT : 'int';
FLOAT32: 'float32';
FLOAT64 : 'float64';
PRINT : 'print';
READ : 'read';
STRING : '"' (~["\\] | '\\' .)* '"';
STRING_TYPE : 'string';


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
