parser grammar MyLangParser;

options { tokenVocab = MyLangLexer; }

/* ───────────────────────────── Program ─────────────────────────────── */
program
    : statement+ EOF
    ;

/* ───────────────────────────── Statements ──────────────────────────── */
statement
    : declaration
    | structDecl
    | assignment
    | printFunc
    | readFunc
    | ifStatement
    | whileStatement
    | functionDecl
    | returnStatement
    | exprStatement
    ;

/* ───────────────────────────── Struktury ───────────────────────────── */
structDecl
    : STRUCT ID CURLY_BRACKET_OPEN structMember+ CURLY_BRACKET_CLOSE SEMICOLON
    ;

structMember
    : typeName ID SEMICOLON
    ;

/* ─────────────────────────── Deklaracje / l-value ──────────────────── */
typeName
    : INT
    | FLOAT32
    | FLOAT64
    | STRING_TYPE
    | ID                       // nazwa wcześniej zadeklarowanej struktury
    ;

declaration
    : typeName ID (EQUALITY expr)?
      SEMICOLON
    ;

/* l-value obsługuje dowolny łańcuch pól, np. a.b.c */
lvalue
    : ID (DOT ID)*
    ;

assignment
    : lvalue EQUALITY expr SEMICOLON
    ;

/* ───────────────────────────── Pozostałe ───────────────────────────── */
exprStatement
    : expr SEMICOLON
    ;

printFunc
    : PRINT expr SEMICOLON
    ;

readFunc
    : READ expr SEMICOLON
    ;

ifStatement
    : IF LP expr RP block (ELSE block)?
    ;

whileStatement
    : WHILE LP expr RP block
    ;

functionDecl
    : DEF ID LP (ID (COMMA ID)*)? RP block
    ;

returnStatement
    : RETURN expr SEMICOLON
    ;

block
    : CURLY_BRACKET_OPEN statement* CURLY_BRACKET_CLOSE
    ;

/* ───────────────────────────────  Wyrażenia ────────────────────────── */
expr
    : logicalExpr
    ;

// operatory logiczne z priorytetami
logicalExpr
    : logicalExpr AND logicalExpr         
    | logicalExpr OR  logicalExpr         
    | logicalExpr XOR logicalExpr         
    | NEG logicalExpr                     
    | relationalExpr                      
    ;

relationalExpr
    : arithmeticExpr ((LT | GT | LE | GE | EQ | NEQ) arithmeticExpr)?
    ;

arithmeticExpr
    : arithmeticExpr PLUS  term           
    | arithmeticExpr MINUS term           
    | term                                
    ;

term
    : term MULTIPLY factor               
    | term DIVIDE   factor                
    | factor                              
    ;

/* factor →  primary ('.' ID)*  pozwala na kaskadę odwołań do pól        */
factor
    : primary (DOT ID)*                   
    ;

primary
    : ID LP expr (COMMA expr)* RP         
    | ID LP RP                            
    | NUMBER                             
    | ID                                 
    | STRING                              
    | LP expr RP                         
    | NEG factor                         
    ;
