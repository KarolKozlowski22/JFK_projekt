	.text
	.file	"ir5.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$0, 4(%rsp)
	movl	$1, (%rsp)
	movl	$.str.8372795069725211921, %edi
	movl	$1, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.332649807079450794, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.8372795069725211921,@object # @.str.8372795069725211921
	.section	.rodata,"a",@progbits
.str.8372795069725211921:
	.asciz	"%d"
	.size	.str.8372795069725211921, 3

	.type	.str.170774002489608625,@object # @.str.170774002489608625
.str.170774002489608625:
	.asciz	"%f"
	.size	.str.170774002489608625, 3

	.type	.str.3693790085204977514,@object # @.str.3693790085204977514
.str.3693790085204977514:
	.asciz	"%s"
	.size	.str.3693790085204977514, 3

	.type	.str.332649807079450794,@object # @.str.332649807079450794
.str.332649807079450794:
	.asciz	"\n"
	.size	.str.332649807079450794, 2

	.section	".note.GNU-stack","",@progbits
