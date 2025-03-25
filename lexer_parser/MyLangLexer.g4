lexer grammar MyLangLexer;

INT : 'int';
FLOAT : 'float';
PRINT : 'print';
READ : 'read';

SEMICOLON : ';';
EQUALITY : '=';
PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';

NUMBER : [0-9]+('.'[0-9]+)?;
ID : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;
