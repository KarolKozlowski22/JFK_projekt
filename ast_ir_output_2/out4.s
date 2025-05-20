	.text
	.file	"ir4.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	callq	test_scope@PLT
	callq	test_local_scope@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.globl	test_scope                      # -- Begin function test_scope
	.p2align	4, 0x90
	.type	test_scope,@function
test_scope:                             # @test_scope
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	x(%rip), %esi
	movl	$.str.5790171083117608925, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.3514099826871306073, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	test_scope, .Lfunc_end1-test_scope
	.cfi_endproc
                                        # -- End function
	.globl	test_local_scope                # -- Begin function test_local_scope
	.p2align	4, 0x90
	.type	test_local_scope,@function
test_local_scope:                       # @test_local_scope
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$20, 4(%rsp)
	movl	$.str.5790171083117608925, %edi
	movl	$20, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.3514099826871306073, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end2:
	.size	test_local_scope, .Lfunc_end2-test_local_scope
	.cfi_endproc
                                        # -- End function
	.type	.str.5790171083117608925,@object # @.str.5790171083117608925
	.section	.rodata,"a",@progbits
.str.5790171083117608925:
	.asciz	"%d"
	.size	.str.5790171083117608925, 3

	.type	.str.3106326101400431079,@object # @.str.3106326101400431079
.str.3106326101400431079:
	.asciz	"%f"
	.size	.str.3106326101400431079, 3

	.type	.str.8444532226840933137,@object # @.str.8444532226840933137
.str.8444532226840933137:
	.asciz	"%s"
	.size	.str.8444532226840933137, 3

	.type	.str.3514099826871306073,@object # @.str.3514099826871306073
.str.3514099826871306073:
	.asciz	"\n"
	.size	.str.3514099826871306073, 2

	.type	x,@object                       # @x
	.data
	.p2align	2, 0x0
x:
	.long	10                              # 0xa
	.size	x, 4

	.section	".note.GNU-stack","",@progbits
