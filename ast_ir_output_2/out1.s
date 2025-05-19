	.text
	.file	"ir1.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	movq	a@GOTPCREL(%rip), %rax
	cmpl	$0, (%rax)
	je	.LBB0_2
# %bb.1:                                # %if.then
	movq	b@GOTPCREL(%rip), %rax
	movl	$1, (%rax)
	jmp	.LBB0_3
.LBB0_2:                                # %if.else
	movq	b@GOTPCREL(%rip), %rax
	movl	$2, (%rax)
.LBB0_3:                                # %if.end
	pushq	%rax
	.cfi_def_cfa_offset 16
	movq	b@GOTPCREL(%rip), %rax
	movl	(%rax), %esi
	movl	$.str.8341731685562686835, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.4313221362129951564, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
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

	.type	a,@object                       # @a
	.comm	a,4,4
	.type	b,@object                       # @b
	.comm	b,4,4
	.section	".note.GNU-stack","",@progbits
