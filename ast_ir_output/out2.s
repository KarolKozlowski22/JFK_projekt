	.text
	.file	"ir2.ll"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3, 0x0                          # -- Begin function main
.LCPI0_0:
	.quad	0x4031000000000000              # double 17
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$1099431936, 4(%rsp)            # imm = 0x41880000
	movsd	.LCPI0_0(%rip), %xmm0           # xmm0 = [1.7E+1,0.0E+0]
	movl	$.str.6650026928202722788, %edi
	movb	$1, %al
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
