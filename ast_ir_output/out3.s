	.text
	.file	"ir3.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$5, (%rsp)
	movl	$60, 4(%rsp)
	movl	$.str.3030070452323609682, %edi
	movl	$60, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.3030070452323609682,@object # @.str.3030070452323609682
	.section	.rodata,"a",@progbits
.str.3030070452323609682:
	.asciz	"%d\n"
	.size	.str.3030070452323609682, 4

	.type	.str.6390100985560808981,@object # @.str.6390100985560808981
.str.6390100985560808981:
	.asciz	"%f\n"
	.size	.str.6390100985560808981, 4

	.section	".note.GNU-stack","",@progbits
