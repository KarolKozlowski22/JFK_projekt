	.text
	.file	"ir4.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset %rbx, -16
	movq	i@GOTPCREL(%rip), %rbx
	cmpl	$9, (%rbx)
	jg	.LBB0_3
	.p2align	4, 0x90
.LBB0_2:                                # %while.body
                                        # =>This Inner Loop Header: Depth=1
	movl	(%rbx), %esi
	movl	$.str.8341731685562686835, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.4313221362129951564, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	incl	(%rbx)
	cmpl	$9, (%rbx)
	jle	.LBB0_2
.LBB0_3:                                # %while.after
	popq	%rbx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.8341731685562686835,@object # @.str.8341731685562686835
	.section	.rodata,"a",@progbits
.str.8341731685562686835:
	.asciz	"%d"
	.size	.str.8341731685562686835, 3

	.type	.str.8084496673346794580,@object # @.str.8084496673346794580
.str.8084496673346794580:
	.asciz	"%f"
	.size	.str.8084496673346794580, 3

	.type	.str.8515177546619091338,@object # @.str.8515177546619091338
.str.8515177546619091338:
	.asciz	"%s"
	.size	.str.8515177546619091338, 3

	.type	.str.4313221362129951564,@object # @.str.4313221362129951564
.str.4313221362129951564:
	.asciz	"\n"
	.size	.str.4313221362129951564, 2

	.type	i,@object                       # @i
	.comm	i,4,4
	.section	".note.GNU-stack","",@progbits
