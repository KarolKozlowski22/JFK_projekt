	.text
	.file	"ir1.ll"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3, 0x0                          # -- Begin function main
.LCPI0_0:
	.quad	0x4024000000000000              # double 10
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movabsq	$4621819117588971520, %rax      # imm = 0x4024000000000000
	movq	%rax, (%rsp)
	movsd	.LCPI0_0(%rip), %xmm0           # xmm0 = [1.0E+1,0.0E+0]
	movl	$.str.170774002489608625, %edi
	movb	$1, %al
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
