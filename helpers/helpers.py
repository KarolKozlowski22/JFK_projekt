import os 

def read_examples():
    try:
        os.chdir("./examples_2")
    except FileNotFoundError:
        print("No such directory")
        return
    examples=[]

    for file in os.listdir():
        example=[]
        if file.endswith(".mylang"):
            with open(file, "r") as f:
                example.append(f.read())
        examples.append(example)
    os.chdir("..")
    return examples

def save_ir_module(ir_module, it):
    try:
        os.chdir("./ast_ir_output_2")
    except FileNotFoundError:
        print("No such directory")
        return
    
    filename = f"ir{it}.ll"
    try:
        with open(filename, "w") as f:
            f.write(str(ir_module))
    except FileNotFoundError:
        print("No such file")
    os.chdir("..")

def save_ast(node, it):
    try:
        os.chdir("./ast_ir_output_2")
    except FileNotFoundError:
        print("No such directory")
        return
    filename = f"ast{it}.txt"
    try:
        with open(filename, "w") as f:
            f.write(str(node))
    except FileNotFoundError:
        print("No such file")
    os.chdir("..")

def compile_ir(it):
    try:
        os.chdir("./ast_ir_output_2")
    except FileNotFoundError:
        print("No such directory")
    if os.path.exists(f"ir{it}.ll"):
        print(f"Translating ir{it}.ll to assembly")
        os.system(f"llc ir{it}.ll -o out{it}.s")
        if os.path.exists(f"out{it}.s"):
            print(f"Compiling out{it}.s to out{it}")
            os.system(f"gcc -no-pie out{it}.s -o out{it}")
        else:
            print(f"out{it}.s does not exist")
    else:
        print(f"ir{it}.ll does not exist")
    os.chdir("..")