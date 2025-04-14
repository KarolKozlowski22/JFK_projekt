import os

def clean():
    try:
        os.chdir("../ast_ir_output")
    except FileNotFoundError:
        print("No such directory")
        return
    os.system("rm *")

clean()
