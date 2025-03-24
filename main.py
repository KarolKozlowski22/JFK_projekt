from antlr4 import *
from lexer_parser.MyLangLexer import MyLangLexer
from lexer_parser.MyLangParser import MyLangParser

def main():
    input_stream = InputStream("int x; x = 5 + 3; print x;")
    lexer = MyLangLexer(input_stream)
    tokens= CommonTokenStream(lexer)
    parser = MyLangParser(tokens)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()