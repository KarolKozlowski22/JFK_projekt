	.text
	.file	"ir1.ll"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3, 0x0                          # -- Begin function main
.LCPI0_0:
	.quad	0x4039666660000000              # double 25.399999618530273
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movsd	.LCPI0_0(%rip), %xmm0           # xmm0 = [2.5399999618530273E+1,0.0E+0]
	movl	$.str.6390100985560808981, %edi
	movb	$1, %al
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
