	.text
	.file	"ir5.ll"
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
	movl	$.str.5790171083117608925, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.3514099826871306073, %edi
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

	.type	i,@object                       # @i
	.comm	i,4,4
	.section	".note.GNU-stack","",@progbits
