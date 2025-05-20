lexer grammar MyLangLexer;

/* ───────────────────── Słowa kluczowe & typy ─────────────────────── */
STRUCT          : 'struct';
DEF             : 'def';
IF              : 'if';
ELSE            : 'else';
WHILE           : 'while';
RETURN          : 'return';

INT             : 'int';
FLOAT32         : 'float32';
FLOAT64         : 'float64';
STRING_TYPE     : 'string';
PRINT           : 'print';
READ            : 'read';

/* ───────────────────────── Operatory & znaki ─────────────────────── */
AND             : '&&';
OR              : '||';
XOR             : '^';
NEG             : '!';

LE              : '<=';
GE              : '>=';
EQ              : '==';
NEQ             : '!=';

LT              : '<';
GT              : '>';
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
EQUALITY        : '=';

DOT             : '.';
COMMA           : ',';
SEMICOLON       : ';';

LP              : '(';
RP              : ')';
CURLY_BRACKET_OPEN  : '{';
CURLY_BRACKET_CLOSE : '}';

/* ───────────────────────── Literały ──────────────────────────────── */
STRING
    : '"' ( ~["\\] | '\\' . )* '"'
    ;

NUMBER
    : [0-9]+ ( '.' [0-9]+ )?
    ;

/* ───────────────────────── Inne tokeny ───────────────────────────── */
ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

/* ───────────────────────── Komentarze & białe znaki ──────────────── */
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
