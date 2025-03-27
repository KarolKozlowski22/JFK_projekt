from llvmlite import ir
from llvmlite import binding as llvm

class IRGenerator:
    def __init__(self):
        self.module = ir.Module("my_lang")
        self.builder = None
        self.vars = {}
        self.module.triple = "x86_64-pc-linux-gnu" 
        self.module.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"       
        voidptr = ir.PointerType(ir.IntType(8))
        i32 = ir.IntType(32)
        
        self.printf = ir.Function(
            self.module,
            ir.FunctionType(i32, [voidptr], var_arg=True),
            "printf"
        )
        
        self.scanf = ir.Function(
            self.module,
            ir.FunctionType(i32, [voidptr], var_arg=True),
            "scanf"
        )
        
        self.fmt_int = self._create_unique_global_string("%d\n")
        self.fmt_float = self._create_unique_global_string("%f\n")

    def _create_unique_global_string(self, text):
        """Tworzy globalny string z unikalną nazwą"""
        text_bytes = bytearray(text.encode() + b'\x00')
        arr_type = ir.ArrayType(ir.IntType(8), len(text_bytes))
        unique_name = f".str.{hash(text)}"
        
        global_str = ir.GlobalVariable(
            self.module,
            arr_type,
            unique_name
        )
        global_str.initializer = ir.Constant(arr_type, text_bytes)
        global_str.linkage = 'private'
        global_str.global_constant = True
        return global_str

    def generate(self, ast):
        main_func = ir.Function(
            self.module,
            ir.FunctionType(ir.VoidType(), []),
            "main"
        )
        entry_block = main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_block)
        
        for node in ast:
            self.process_node(node)
            
        self.builder.ret_void()
        return self.module

    def process_node(self, node):
        if node[0] == 'declaration':
            self.handle_declaration(node)
        elif node[0] == 'assignment':
            self.handle_assignment(node)
        elif node[0] == 'print':
            self.handle_print(node)
        elif node[0] == 'read':
            self.handle_read(node)

    def handle_declaration(self, node):
        var_type = ir.IntType(32) if node[1] == 'int' else ir.FloatType()
        var_name = node[2]
        
        init_value = ir.Constant(var_type, 0)
        
        if len(node) > 3 and node[3] == '=':
            init_value = self.evaluate_expr(node[4])
        
        self.vars[var_name] = ir.GlobalVariable(
            self.module,
            var_type,
            var_name
        )
        self.vars[var_name].initializer = init_value

    def handle_assignment(self, node):
        var_name = node[1]
        value = self.evaluate_expr(node[2])
        self.builder.store(value, self.vars[var_name])

    def handle_print(self, node):
        value = self.evaluate_expr(node[1])
        
        if str(value.type) == 'i32':
            fmt_ptr = self.builder.bitcast(self.fmt_int, ir.PointerType(ir.IntType(8)))
        else:
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
        
        self.builder.call(self.printf, [fmt_ptr, value])

    def handle_read(self, node):
        var_name = node[1]
        var = self.vars[var_name]
        
        if str(var.type.pointee) == 'i32':
            fmt_ptr = self.builder.bitcast(self.fmt_int, ir.PointerType(ir.IntType(8)))
        else:
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
        
        self.builder.call(self.scanf, [fmt_ptr, var])

    def evaluate_expr(self, expr):
        if isinstance(expr, int):
            return ir.Constant(ir.IntType(32), expr)
        elif isinstance(expr, float):
            return ir.Constant(ir.FloatType(), expr)
        elif isinstance(expr, str): 
            return self.builder.load(self.vars[expr])
        elif isinstance(expr, tuple): 
            left = self.evaluate_expr(expr[1])
            right = self.evaluate_expr(expr[2])
            op = expr[0]
            
            if op == '+':
                return self.builder.add(left, right)
            elif op == '-':
                return self.builder.sub(left, right)
            elif op == '*':
                return self.builder.mul(left, right)
            elif op == '/':
                if str(left.type) == 'i32':
                    return self.builder.sdiv(left, right)
                else:
                    return self.builder.fdiv(left, right)