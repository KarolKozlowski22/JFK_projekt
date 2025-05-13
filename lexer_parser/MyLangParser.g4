parser grammar MyLangParser;

options { tokenVocab=MyLangLexer; }

program : statement+;

statement : declaration | assignment | printFunc | readFunc;

declaration : (INT | FLOAT32 | FLOAT64 | STRING_TYPE) ID (EQUALITY expr)? SEMICOLON;
assignment : ID EQUALITY expr SEMICOLON;
printFunc : PRINT expr SEMICOLON;
readFunc : READ expr SEMICOLON;
// expr : term ((PLUS | MINUS) term)*;
// term : factor ((MULTIPLY | DIVIDE) factor)*;
// factor : NUMBER | ID | LP expr RP;

expr : logicalExpr;

logicalExpr
    : logicalExpr AND logicalExpr   
    | logicalExpr OR logicalExpr    
    | logicalExpr XOR logicalExpr   
    | NEG logicalExpr               
    | arithmeticExpr                
    ;

arithmeticExpr
    : arithmeticExpr PLUS term      
    | arithmeticExpr MINUS term     
    | term                          
    ;

term : term MULTIPLY factor          
     | term DIVIDE factor            
     | factor                        
     ;

factor : NUMBER | ID | STRING | LP expr RP;
