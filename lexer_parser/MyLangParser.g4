parser grammar MyLangParser;

options { tokenVocab=MyLangLexer; }

program : statement+;

statement : declaration | assignment | printFunc | readFunc;

declaration : (INT | FLOAT) ID SEMICOLON;
assignment : ID EQUALITY expr SEMICOLON;
printFunc : PRINT expr SEMICOLON;
readFunc : READ expr SEMICOLON;
expr : NUMBER | ID | expr (PLUS|MINUS|MULTIPLY|DIVIDE) expr;
