from antlr4 import *
from lexer_parser.MyLangLexer import MyLangLexer
from lexer_parser.MyLangParser import MyLangParser
from AST.AST import ASTBuilder
from helpers.helpers import read_examples, save_ir_module, save_ast, compile_ir

def main():
    examples=read_examples()
    it=1
    for example in examples:
        input_stream = InputStream(example[0])
        lexer = MyLangLexer(input_stream)
        tokens= CommonTokenStream(lexer)
        parser = MyLangParser(tokens)
        tree = parser.program()

        # print("Parse Tree:")
        # print(tree.toStringTree(recog=parser))
        
        ast_builder = ASTBuilder()
        ast, ir_module = ast_builder.visit(tree)

        save_ast(ast, it)
        save_ir_module(ir_module, it)
        compile_ir(it)
        it+=1



if __name__ == '__main__':
    main()