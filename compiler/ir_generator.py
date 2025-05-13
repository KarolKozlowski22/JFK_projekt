from llvmlite import ir

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
        
        self.fmt_int = self._create_unique_global_string("%d")
        self.fmt_float = self._create_unique_global_string("%f")
        self.fmt_string = self._create_unique_global_string("%s")
        self.fmt_newline = self._create_unique_global_string("\n")

    def _create_unique_global_string(self, text):
        text_bytes = bytearray(text.encode() + b'\x00')
        arr_type = ir.ArrayType(ir.IntType(8), len(text_bytes))
        unique_name = f".str.{abs(hash(text))}"
        
        global_str = ir.GlobalVariable(
            self.module,
            arr_type,
            unique_name
        )
        global_str.initializer = ir.Constant(arr_type, text_bytes)
        global_str.linkage = 'internal'
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
    
    def _create_string(self, text):
        text_bytes = bytearray(text.encode() + b'\x00')
        arr_type = ir.ArrayType(ir.IntType(8), len(text_bytes))
        global_str = ir.GlobalVariable(self.module, arr_type, name=f".str.{abs(hash(text))}")
        global_str.initializer = ir.Constant(arr_type, text_bytes)
        global_str.linkage = 'internal'
        global_str.global_constant = True
        return self.builder.bitcast(global_str, ir.PointerType(ir.IntType(8)))


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
        var_type = None
        if node[1] == 'int':
            var_type = ir.IntType(32)
            init_value = ir.Constant(var_type, 0)
        elif node[1] == 'float32':
            var_type = ir.FloatType()
            init_value = ir.Constant(var_type, 0.0)
        elif node[1] == 'float64':
            var_type = ir.DoubleType()
            init_value = ir.Constant(var_type, 0.0)
        elif node[1] == 'string':
            var_type = ir.PointerType(ir.IntType(8))
            init_value = ir.Constant(var_type, None)
        var_name = node[2]
        
        # init_value = ir.Constant(var_type, 0.0 if isinstance(var_type, (ir.FloatType, ir.DoubleType)) else 0)

        if len(node) > 3 and node[3] == '=':
            init_value = self.evaluate_expr(node[4])
            if isinstance(var_type, ir.FloatType) and str(init_value.type) == 'double':
                init_value = self.builder.fptrunc(init_value, ir.FloatType())  
            elif isinstance(var_type, ir.DoubleType) and str(init_value.type) == 'float':
                init_value = self.builder.fpext(init_value, ir.DoubleType())  
            elif isinstance(var_type, ir.FloatType) and str(init_value.type) == 'i32':
                init_value = self.builder.sitofp(init_value, ir.FloatType())  
            elif isinstance(var_type, ir.DoubleType) and str(init_value.type) == 'i32':
                init_value = self.builder.sitofp(init_value, ir.DoubleType())  
        # if len(node) > 3 and node[3] == '=':
        #     init_value = self.evaluate_expr(node[4])
        #     if var_type == ir.FloatType() and str(init_value.type) == 'i32':
        #         init_value = self.builder.sitofp(init_value, ir.FloatType())
        
        alloca = self.builder.alloca(var_type, name=var_name)
        self.builder.store(init_value, alloca)
        self.vars[var_name] = alloca


    def handle_assignment(self, node):
        var_name = node[1]
        value = self.evaluate_expr(node[2])
        if str(value.type) != str(self.vars[var_name].type.pointee):
            raise TypeError(f"Type mismatch in assignment to {var_name}")
        self.builder.store(value, self.vars[var_name])

    def handle_print(self, node):
        value = self.evaluate_expr(node[1])
        newline_ptr = self.builder.bitcast(self.fmt_newline, ir.PointerType(ir.IntType(8)))
        if isinstance(node[1], str) and node[1] not in self.vars:
            raise NameError(f"Variable '{node[1]}' is not declared.")

        if str(value.type) == 'i32':
            fmt_ptr = self.builder.bitcast(self.fmt_int, ir.PointerType(ir.IntType(8)))
            self.builder.call(self.printf, [fmt_ptr, value])
            self.builder.call(self.printf, [newline_ptr])
        elif str(value.type) == 'float':
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
            value = self.builder.fpext(value, ir.DoubleType())
            self.builder.call(self.printf, [fmt_ptr, value])
            self.builder.call(self.printf, [newline_ptr])
        elif str(value.type) == 'double':
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
            self.builder.call(self.printf, [fmt_ptr, value])
            self.builder.call(self.printf, [newline_ptr])
        elif str(value.type) == 'i8*':
            fmt_ptr = self.builder.bitcast(self.fmt_string, ir.PointerType(ir.IntType(8)))
            self.builder.call(self.printf, [fmt_ptr, value])
            self.builder.call(self.printf, [newline_ptr])
        else:
            raise TypeError(f"Unsupported type for print: {value.type}")

        # if str(value.type) == 'i32':
        #     fmt_ptr = self.builder.bitcast(self.fmt_int, ir.PointerType(ir.IntType(8)))
        #     self.builder.call(self.printf, [fmt_ptr, value])
        #     self.builder.call(self.printf, [newline_ptr])
        # elif str(value.type) == 'string':
        #     self.builder.call(self.printf, [value])
        #     self.builder.call(self.printf, [newline_ptr])
        # else:
        #     fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))

        #     if str(value.type) == 'float':
        #         value = self.builder.fpext(value, ir.DoubleType())
        #     self.builder.call(self.printf, [fmt_ptr, value])
        #     self.builder.call(self.printf, [newline_ptr])

    def handle_read(self, node):
        var_name = node[1]
        if var_name not in self.vars:
            raise NameError(f"Variable '{var_name}' is not declared.")  

        var = self.vars[var_name]
        var_type = str(var.type.pointee)

        if var_type == 'i32':  
            fmt_ptr = self.builder.bitcast(self.fmt_int, ir.PointerType(ir.IntType(8)))
        elif var_type == 'float':  
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
        elif var_type == 'double':  
            fmt_ptr = self.builder.bitcast(self.fmt_float, ir.PointerType(ir.IntType(8)))
        elif var_type == 'i8*':  
            fmt_ptr = self.builder.bitcast(self.fmt_string, ir.PointerType(ir.IntType(8)))
        else:
            raise TypeError(f"Unsupported type for read: {var_type}")

        fflush = ir.Function(
            self.module,
            ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))]),
            "fflush"
        )
        self.builder.call(fflush, [ir.Constant(ir.PointerType(ir.IntType(8)), None)])

        self.builder.call(self.scanf, [fmt_ptr, var])

    def evaluate_expr(self, expr):
        if isinstance(expr, (int, float)):
            if isinstance(expr, int):
                return ir.Constant(ir.IntType(32), expr)
            else:
                return ir.Constant(ir.FloatType(), expr)

        elif isinstance(expr, str):
            if expr not in self.vars:
                return self._create_string(expr)
            #     raise NameError(f"Variable '{expr}' is not declared.") 
            return self.builder.load(self.vars[expr])

        elif isinstance(expr, tuple):
            op = expr[0]

            if op == '!':
                val = self.evaluate_expr(expr[1])
                bool_val = self.builder.icmp_unsigned('!=', val, ir.Constant(val.type, 0))
                result = self.builder.xor(bool_val, ir.Constant(ir.IntType(1), 1))
                return self.builder.zext(result, ir.IntType(32))

            if op == '&&':
                left_val = self.evaluate_expr(expr[1])
                left_bool = self.builder.icmp_unsigned('!=', left_val, ir.Constant(left_val.type, 0))
                left_block = self.builder.block  

                right_block = self.builder.append_basic_block("and.right")
                end_block = self.builder.append_basic_block("and.end")

                self.builder.cbranch(left_bool, right_block, end_block)

                self.builder.position_at_start(right_block)
                right_val = self.evaluate_expr(expr[2])
                right_bool = self.builder.icmp_unsigned('!=', right_val, ir.Constant(right_val.type, 0))
                right_eval_block = self.builder.block  
                self.builder.branch(end_block)

                self.builder.position_at_start(end_block)
                phi = self.builder.phi(ir.IntType(1))
                phi.add_incoming(ir.Constant(ir.IntType(1), 0), left_block)         
                phi.add_incoming(right_bool, right_eval_block)                      
                return self.builder.zext(phi, ir.IntType(32))

            if op == '||':
                left_val = self.evaluate_expr(expr[1])
                left_bool = self.builder.icmp_unsigned('!=', left_val, ir.Constant(left_val.type, 0))
                left_block = self.builder.block 

                right_block = self.builder.append_basic_block("or.right")
                end_block = self.builder.append_basic_block("or.end")

                self.builder.cbranch(left_bool, end_block, right_block)

                self.builder.position_at_start(right_block)
                right_val = self.evaluate_expr(expr[2])
                right_bool = self.builder.icmp_unsigned('!=', right_val, ir.Constant(right_val.type, 0))
                right_eval_block = self.builder.block  
                self.builder.branch(end_block)

                self.builder.position_at_start(end_block)
                phi = self.builder.phi(ir.IntType(1))
                phi.add_incoming(ir.Constant(ir.IntType(1), 1), left_block)        
                phi.add_incoming(right_bool, right_eval_block)                      
                return self.builder.zext(phi, ir.IntType(32))

            if op == '^':
                left_val = self.evaluate_expr(expr[1])
                right_val = self.evaluate_expr(expr[2])
                left_bool = self.builder.icmp_unsigned('!=', left_val, ir.Constant(left_val.type, 0))
                right_bool = self.builder.icmp_unsigned('!=', right_val, ir.Constant(right_val.type, 0))
                xor_val = self.builder.xor(left_bool, right_bool)
                return self.builder.zext(xor_val, ir.IntType(32))

            left_val = self.evaluate_expr(expr[1])
            right_val = self.evaluate_expr(expr[2])

            if left_val.type != right_val.type:
                if isinstance(left_val.type, ir.IntType) and isinstance(right_val.type, (ir.FloatType, ir.DoubleType)):
                    left_val = self.builder.sitofp(left_val, right_val.type)
                elif isinstance(left_val.type, (ir.FloatType, ir.DoubleType)) and isinstance(right_val.type, ir.IntType):
                    right_val = self.builder.sitofp(right_val, left_val.type)

            if op == '+':
                return self.builder.fadd(left_val, right_val) if isinstance(left_val.type, ir.FloatType) else self.builder.add(left_val, right_val)
            elif op == '-':
                return self.builder.fsub(left_val, right_val) if isinstance(left_val.type, ir.FloatType) else self.builder.sub(left_val, right_val)
            elif op == '*':
                return self.builder.fmul(left_val, right_val) if isinstance(left_val.type, ir.FloatType) else self.builder.mul(left_val, right_val)
            elif op == '/':
                return self.builder.fdiv(left_val, right_val) if isinstance(left_val.type, ir.FloatType) else self.builder.sdiv(left_val, right_val)

        raise ValueError(f"Unsupported expression: {expr}")

