	.text
	.file	"ir1.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$0, 4(%rsp)
	movl	$0, (%rsp)
	movb	$1, %al
	testb	%al, %al
	jne	.LBB0_2
# %bb.1:                                # %if.then
	movl	$1, (%rsp)
	jmp	.LBB0_3
.LBB0_2:                                # %if.else
	movl	$2, (%rsp)
.LBB0_3:                                # %if.end
	movl	(%rsp), %esi
	movl	$.str.6658440445434400440, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.3347073341543062685, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.6658440445434400440,@object # @.str.6658440445434400440
	.section	.rodata,"a",@progbits
.str.6658440445434400440:
	.asciz	"%d"
	.size	.str.6658440445434400440, 3

	.type	.str.9011845808571790903,@object # @.str.9011845808571790903
.str.9011845808571790903:
	.asciz	"%f"
	.size	.str.9011845808571790903, 3

	.type	.str.3758218351999552703,@object # @.str.3758218351999552703
.str.3758218351999552703:
	.asciz	"%s"
	.size	.str.3758218351999552703, 3

	.type	.str.3347073341543062685,@object # @.str.3347073341543062685
.str.3347073341543062685:
	.asciz	"\n"
	.size	.str.3347073341543062685, 2

	.section	".note.GNU-stack","",@progbits
