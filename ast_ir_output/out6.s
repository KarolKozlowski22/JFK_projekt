	.text
	.file	"ir6.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$0, 4(%rsp)
	xorl	%edi, %edi
	callq	fflush@PLT
	leaq	4(%rsp), %rsi
	movl	$.str.7951315541544645107, %edi
	xorl	%eax, %eax
	callq	scanf@PLT
	movl	4(%rsp), %esi
	movl	$.str.7951315541544645107, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.7951315541544645107,@object # @.str.7951315541544645107
	.section	.rodata,"a",@progbits
.str.7951315541544645107:
	.asciz	"%d"
	.size	.str.7951315541544645107, 3

	.type	.str.6650026928202722788,@object # @.str.6650026928202722788
.str.6650026928202722788:
	.asciz	"%f"
	.size	.str.6650026928202722788, 3

	.section	".note.GNU-stack","",@progbits
