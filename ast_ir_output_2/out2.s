	.text
	.file	"ir2.ll"
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
	movl	$.str.5790171083117608925, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.3514099826871306073, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.5790171083117608925,@object # @.str.5790171083117608925
	.section	.rodata,"a",@progbits
.str.5790171083117608925:
	.asciz	"%d"
	.size	.str.5790171083117608925, 3

	.type	.str.3106326101400431079,@object # @.str.3106326101400431079
.str.3106326101400431079:
	.asciz	"%f"
	.size	.str.3106326101400431079, 3

	.type	.str.8444532226840933137,@object # @.str.8444532226840933137
.str.8444532226840933137:
	.asciz	"%s"
	.size	.str.8444532226840933137, 3

	.type	.str.3514099826871306073,@object # @.str.3514099826871306073
.str.3514099826871306073:
	.asciz	"\n"
	.size	.str.3514099826871306073, 2

	.type	a,@object                       # @a
	.comm	a,4,4
	.type	b,@object                       # @b
	.comm	b,4,4
	.section	".note.GNU-stack","",@progbits
