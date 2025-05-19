parser grammar MyLangParser;

options { tokenVocab=MyLangLexer; }

program : statement+;

statement
    : declaration
    | assignment
    | printFunc
    | readFunc
    | ifStatement
    | whileStatement
    | functionDecl
    | returnStatement
    | exprStatement
    ;

exprStatement : expr SEMICOLON;

declaration : (INT | FLOAT32 | FLOAT64 | STRING_TYPE) ID (EQUALITY expr)? SEMICOLON;
assignment : ID EQUALITY expr SEMICOLON;
printFunc : PRINT expr SEMICOLON;
readFunc : READ expr SEMICOLON;
ifStatement : IF LP expr RP block (ELSE block)?;
whileStatement : WHILE LP expr RP block;
functionDecl : DEF ID LP (ID (COMMA ID)*)? RP block;
returnStatement : RETURN expr SEMICOLON;

block : CURLY_BRACKET_OPEN statement* CURLY_BRACKET_CLOSE;

expr : logicalExpr;

logicalExpr
    : logicalExpr AND logicalExpr   
    | logicalExpr OR logicalExpr    
    | logicalExpr XOR logicalExpr   
    | NEG logicalExpr               
    | relationalExpr                
    ;

relationalExpr
    : arithmeticExpr ( (LT | GT | LE | GE | EQ | NEQ) arithmeticExpr )?
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

factor
    : ID LP expr (COMMA expr)* RP     
    | ID LP RP                        
    | NUMBER
    | ID
    | STRING
    | LP expr RP
    | NEG factor
    ;


