	.text
	.file	"ir8.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$3, 4(%rsp)
	movl	$1080033280, (%rsp)             # imm = 0x40600000
	movl	$.str.7397556834030168284, %edi
	movl	$3, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.8700303344908842345, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movss	(%rsp), %xmm0                   # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movl	$.str.7383418316188768217, %edi
	movb	$1, %al
	callq	printf@PLT
	movl	$.str.8700303344908842345, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.7397556834030168284,@object # @.str.7397556834030168284
	.section	.rodata,"a",@progbits
.str.7397556834030168284:
	.asciz	"%d"
	.size	.str.7397556834030168284, 3

	.type	.str.7383418316188768217,@object # @.str.7383418316188768217
.str.7383418316188768217:
	.asciz	"%f"
	.size	.str.7383418316188768217, 3

	.type	.str.6509151619883873605,@object # @.str.6509151619883873605
.str.6509151619883873605:
	.asciz	"%s"
	.size	.str.6509151619883873605, 3

	.type	.str.8700303344908842345,@object # @.str.8700303344908842345
.str.8700303344908842345:
	.asciz	"\n"
	.size	.str.8700303344908842345, 2

	.section	".note.GNU-stack","",@progbits
