from llvmlite import ir


class IRGenerator:
    # ─────────────────────────────── Init ────────────────────────────────
    def __init__(self):
        self.module = ir.Module(name="my_lang")
        self.module.triple = "x86_64-pc-linux-gnu"
        self.module.data_layout = (
            "e-m:e-p270:32:32-p271:32:32-p272:64:64-"
            "i64:64-f80:128-n8:16:32:64-S128"
        )

        self.builder = None           # current IRBuilder
        self.env_stack = [{}]         # symbol tables stack (0 = global)
        self.pending_inits = []
        self.struct_defs = {}        # delayed initialisations for globals

        # libc printf / scanf
        voidptr = ir.PointerType(ir.IntType(8))
        i32 = ir.IntType(32)
        self.printf = ir.Function(
            self.module,
            ir.FunctionType(i32, [voidptr], var_arg=True),
            name="printf",
        )
        self.scanf = ir.Function(
            self.module,
            ir.FunctionType(i32, [voidptr], var_arg=True),
            name="scanf",
        )

        # format strings
        self.fmt_int    = self._gstr("%d")
        self.fmt_float  = self._gstr("%f")
        self.fmt_string = self._gstr("%s")
        self.fmt_nl     = self._gstr("\n")

    # ───────────────────────────── Helpers ───────────────────────────────
    def _gstr(self, txt: str) -> ir.GlobalVariable:
        """Create an internal NUL-terminated string."""
        arr_t = ir.ArrayType(ir.IntType(8), len(txt) + 1)
        g = ir.GlobalVariable(self.module, arr_t, name=f".str.{abs(hash(txt))}")
        g.linkage = "internal"
        g.global_constant = True
        g.initializer = ir.Constant(arr_t, bytearray(txt.encode() + b"\x00"))
        return g

    def _str_ptr(self, g):
        return self.builder.bitcast(g, ir.PointerType(ir.IntType(8)))

    def _in_global_scope(self) -> bool:
        return (
            len(self.env_stack) == 1
            and self.builder
            and self.builder.function.name == "main"
        )

    # ───────────────────────────── Generate ──────────────────────────────
    def generate(self, ast):
        """
        Czteroprzebiegowe generowanie modułu:
           0) struktury          – muszą być znane przed typowaniem zmiennych
           1) deklaracje glob.   – tworzy zmienne i ewentualnie odkłada init
           2) funkcje            – prototyp + ciało
           2.5) opóźnione inicjalizacje globali (non-const)
           3) pozostałe instrukcje top-level (wykonywane w main)
        """
        # ── setup funkcji main ───────────────────────────────────────────
        main = ir.Function(self.module,
                           ir.FunctionType(ir.VoidType(), []),
                           name="main")
        entry = main.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry)

        # ── Pass 0 – struktury ───────────────────────────────────────────
        for n in ast:
            if n[0] == "struct_decl":
                # (name, fields) = (n[1], n[2])
                self._handle_struct_decl(n[1], n[2])

        # ── Pass 1 – deklaracje globalne ────────────────────────────────
        for n in ast:
            if n[0] == "declaration":
                self._handle_declaration(n)

        # ── Pass 2 – funkcje ─────────────────────────────────────────────
        for n in ast:
            if n[0] == "function":
                self._handle_function(n[1], n[2], n[3])

        # ── Pass 2.5 – opóźnione inicjalizacje globali ───────────────────
        for a in self.pending_inits:
            self._handle_assignment(a)

        # ── Pass 3 – instrukcje top-level ────────────────────────────────
        for n in ast:
            if n[0] not in ("struct_decl", "declaration", "function"):
                self._process(n)

        self.builder.ret_void()
        return self.module

    # ───────────────────────── Dispatcher ────────────────────────────────
    def _process(self, node):
        match node:
            # ─── deklaracje i struktury ───────────────────────────────
            case ("declaration", *_):
                self._handle_declaration(node)
            case ("struct_decl", name, fields):
                self._handle_struct_decl(name, fields)

            # ─── przypisania: zwykłe i do pola ────────────────────────
            case ("assignment" | "field_assignment", *_):
                self._handle_assignment(node)

            # ─── pozostałe węzły ───────────────────────────────────────
            case ("print", *_):
                self._handle_print(node)
            case ("read", *_):
                self._handle_read(node)
            case ("if", cond, then_b, else_b):
                self._handle_if(cond, then_b, else_b)
            case ("while", cond, body):
                self._handle_while(cond, body)
            case ("function", name, params, body):
                self._handle_function(name, params, body)
            case ("return", expr):
                self._handle_return(expr)
            case ("call", fname, args):
                self._eval(("call", fname, args))
            case _:
                raise ValueError(f"Unknown AST node: {node}")

            
    def _handle_struct_decl(self, name, fields):
        llvm_fields = [self._llvm_type(t)[0] for t, _ in fields]
        st = ir.LiteralStructType(llvm_fields)
        idx_map = {fname: i for i, (_, fname) in enumerate(fields)}
        self.struct_defs[name] = (st, idx_map)

    def _field_ptr(self, obj_ptr, field_name):
        stype = obj_ptr.type.pointee
        for _, (llvm_stype, idx_map) in self.struct_defs.items():
            if llvm_stype is stype:
                idx = idx_map[field_name]
                break
        else:
            raise KeyError("Struct type not registered")
        zero = ir.Constant(ir.IntType(32), 0)
        return self.builder.gep(obj_ptr, [zero, ir.Constant(ir.IntType(32), idx)])


    # ─────────────────────── Declarations & assign ───────────────────────
    def _llvm_type(self, kwd):
        if kwd == "int":
            return ir.IntType(32), ir.Constant(ir.IntType(32), 0)
        if kwd == "float32":
            return ir.FloatType(), ir.Constant(ir.FloatType(), 0.0)
        if kwd == "float64":
            return ir.DoubleType(), ir.Constant(ir.DoubleType(), 0.0)
        if kwd == "string":
            t = ir.PointerType(ir.IntType(8))
            return t, ir.Constant(t, None)
        if kwd in self.struct_defs:
            stype = self.struct_defs[kwd][0]
            zero = ir.Constant(stype, None) 
            return stype, zero
        raise ValueError("unknown type")

    def _handle_declaration(self, node):
        _, typ_kwd, name, *tail = node
        llvm_t, zero = self._llvm_type(typ_kwd)
        init_expr = tail[1] if tail and tail[0] == "=" else None

        # ─── Global ──────────────────────────────────────────────
        if self._in_global_scope():
            g = ir.GlobalVariable(self.module, llvm_t, name)
            if typ_kwd in self.struct_defs:
                g.linkage = "internal"
                g.initializer = zero  

            if init_expr is None or (isinstance(init_expr, (int, float)) and init_expr == 0):
                g.linkage = "common" 
            else:
                g.linkage = "internal"
            g.initializer = zero
            self.env_stack[0][name] = g
            if init_expr is not None:
                if isinstance(init_expr, (int, float)):
                    g.initializer = self._eval(init_expr)
                else:
                    # non-constant ⇒ store later in main
                    self.pending_inits.append(("assignment", name, init_expr))
            return

        # ─── Local ───────────────────────────────────────────────
        ptr = self.builder.alloca(llvm_t, name=name)
        val = self._eval(init_expr) if init_expr is not None else zero
        self.builder.store(val, ptr)
        self._cur_scope()[name] = ptr

    def _handle_assignment(self, node):
        tag = node[0]
        if tag == "assignment":
            _, name, expr = node
            val = self._eval(expr)
            ptr = self._lookup(name)
            self.builder.store(val, ptr)
        elif tag == "field_assignment":
            _, obj_name, field, expr = node
            val = self._eval(expr)
            obj_ptr = self._lookup(obj_name)
            fptr = self._field_ptr(obj_ptr, field)   # ← tylko 2 arg.
            self.builder.store(val, fptr)

    # ───────────────────────────── I/O ────────────────────────────────────
    def _handle_print(self, node):
        _, expr = node
        v = self._eval(expr)
        t = str(v.type)

        if t == "i32":
            fmt = self._str_ptr(self.fmt_int)
            args = [fmt, v]
        elif t in ("float", "double"):
            fmt = self._str_ptr(self.fmt_float)
            v2 = (
                self.builder.fpext(v, ir.DoubleType())
                if t == "float"
                else v
            )
            args = [fmt, v2]
        elif t == "i8*":
            fmt = self._str_ptr(self.fmt_string)
            args = [fmt, v]
        else:
            raise TypeError("print: unsupported type")

        self.builder.call(self.printf, args)
        self.builder.call(self.printf, [self._str_ptr(self.fmt_nl)])

    def _handle_read(self, node):
        _, name = node
        ptr = self._lookup(name)
        p = str(ptr.type.pointee)
        fmt = (
            self._str_ptr(self.fmt_int)
            if p == "i32"
            else self._str_ptr(self.fmt_float)
            if p in ("float", "double")
            else self._str_ptr(self.fmt_string)
            if p == "i8*"
            else None
        )
        if fmt is None:
            raise TypeError("read: unsupported type")
        self.builder.call(self.scanf, [fmt, ptr])

    # ───────────────────────────── Eval ───────────────────────────────────
    def _eval(self, expr):
        # literals / identifier
        if expr is None:
            raise ValueError("eval(None)")
        if isinstance(expr, int):
            return ir.Constant(ir.IntType(32), expr)
        if isinstance(expr, float):
            return ir.Constant(ir.FloatType(), expr)
        if isinstance(expr, str):
            return self.builder.load(self._lookup(expr))

        op = expr[0]

        # call
        if op == "call":
            _, fname, args_ast = expr
            func = self._lookup(fname)
            args = [self._eval(a) for a in args_ast]
            return self.builder.call(func, args)

        # unary !
        if op == "!":
            v = self._eval(expr[1])
            cmp = self.builder.icmp_unsigned("!=", v, ir.Constant(v.type, 0))
            inv = self.builder.xor(cmp, ir.Constant(ir.IntType(1), 1))
            return self.builder.zext(inv, ir.IntType(32))
        
        if op == "field":
            _, base_expr, field = expr
            base_ptr = (self._lookup(base_expr) if isinstance(base_expr, str) else self._eval(base_expr))
            fptr = self._field_ptr(base_ptr, field)   # ← tylko 2 arg.
            return self.builder.load(fptr)
        # binary
        left = self._eval(expr[1])
        right = self._eval(expr[2])

        # auto-cast int→float
        if left.type != right.type:
            if isinstance(left.type, ir.IntType):
                left = self.builder.sitofp(left, right.type)
            elif isinstance(right.type, ir.IntType):
                right = self.builder.sitofp(right, left.type)

        if op in {"+", "-", "*", "/"}:
            if op == "+":
                return (
                    self.builder.add(left, right)
                    if isinstance(left.type, ir.IntType)
                    else self.builder.fadd(left, right)
                )
            if op == "-":
                return (
                    self.builder.sub(left, right)
                    if isinstance(left.type, ir.IntType)
                    else self.builder.fsub(left, right)
                )
            if op == "*":
                return (
                    self.builder.mul(left, right)
                    if isinstance(left.type, ir.IntType)
                    else self.builder.fmul(left, right)
                )
            if op == "/":
                return (
                    self.builder.sdiv(left, right)
                    if isinstance(left.type, ir.IntType)
                    else self.builder.fdiv(left, right)
                )

        if op in {"<", "<=", ">", ">=", "==", "!="}:
            cmp = (
                self.builder.icmp_signed(op, left, right)
                if isinstance(left.type, ir.IntType)
                else self.builder.fcmp_ordered(op, left, right)
            )
            return self.builder.zext(cmp, ir.IntType(32))

        raise ValueError(f"unsupported expr op {op}")

    # ──────────────────────── Control Flow ───────────────────────────────
    def _handle_while(self, cond, body):
        f = self.builder.function
        b_cond = f.append_basic_block("while.cond")
        b_body = f.append_basic_block("while.body")
        b_after = f.append_basic_block("while.after")

        self.builder.branch(b_cond)

        self.builder.position_at_start(b_cond)
        c = self._eval(cond)
        cb = self.builder.icmp_unsigned("!=", c, ir.Constant(c.type, 0))
        self.builder.cbranch(cb, b_body, b_after)

        self.builder.position_at_start(b_body)
        self._push()
        for st in body:
            self._process(st)
        self._pop()
        self.builder.branch(b_cond)

        self.builder.position_at_start(b_after)

    def _handle_if(self, cond, then_b, else_b):
        f = self.builder.function
        b_then = f.append_basic_block("if.then")
        b_else = f.append_basic_block("if.else") if else_b else None
        b_end = f.append_basic_block("if.end")

        c = self._eval(cond)
        cb = self.builder.icmp_unsigned("!=", c, ir.Constant(c.type, 0))
        self.builder.cbranch(cb, b_then, b_else if else_b else b_end)

        # THEN
        self.builder.position_at_start(b_then)
        self._push()
        for st in then_b:
            self._process(st)
        self._pop()
        self.builder.branch(b_end)

        # ELSE
        if else_b:
            self.builder.position_at_start(b_else)
            self._push()
            for st in else_b:
                self._process(st)
            self._pop()
            self.builder.branch(b_end)

        self.builder.position_at_start(b_end)

    # ──────────────────────── Functions & return ─────────────────────────
    def _handle_function(self, name, params, body):
        func_t = ir.FunctionType(ir.IntType(32), [ir.IntType(32)] * len(params))
        func = ir.Function(self.module, func_t, name=name)
        self._cur_scope()[name] = func

        bb_entry = func.append_basic_block("entry")
        old_builder = self.builder
        self.builder = ir.IRBuilder(bb_entry)

        self._push()
        for arg, pname in zip(func.args, params):
            arg.name = pname
            ptr = self.builder.alloca(ir.IntType(32), name=pname)
            self.builder.store(arg, ptr)
            self._cur_scope()[pname] = ptr

        for st in body:
            self._process(st)
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))
        self._pop()
        self.builder = old_builder

    def _handle_return(self, expr):
        self.builder.ret(self._eval(expr))

    # ───────────────────────── Scope helpers ────────────────────────────
    def _cur_scope(self):
        return self.env_stack[-1]

    def _push(self):
        self.env_stack.append({})

    def _pop(self):
        self.env_stack.pop()

    def _lookup(self, name):
        for scope in reversed(self.env_stack):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable '{name}' is not declared.")
