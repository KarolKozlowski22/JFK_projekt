from antlr4 import *
from lexer_parser.MyLangLexer import MyLangLexer
from lexer_parser.MyLangParser import MyLangParser
from AST.AST import ASTBuilder

def main():
    input_stream = InputStream("int x; x = 5 + 3; print x;")
    lexer = MyLangLexer(input_stream)
    tokens= CommonTokenStream(lexer)
    parser = MyLangParser(tokens)
    tree = parser.program()

    print("Parse Tree:")
    print(tree.toStringTree(recog=parser))
    
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)

    print("AST Tree:")
    for node in ast:
        print(node)

if __name__ == '__main__':
    main()