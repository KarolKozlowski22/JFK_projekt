	.text
	.file	"ir3.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	movl	$1, 20(%rsp)
	movl	$0, 16(%rsp)
	movl	$0, 12(%rsp)
	movl	$1, 8(%rsp)
	movl	$1, 4(%rsp)
	movl	$.str.3948252993100881646, %edi
	xorl	%esi, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	8(%rsp), %esi
	movl	$.str.3948252993100881646, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	4(%rsp), %esi
	movl	$.str.3948252993100881646, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.3948252993100881646,@object # @.str.3948252993100881646
	.section	.rodata,"a",@progbits
.str.3948252993100881646:
	.asciz	"%d"
	.size	.str.3948252993100881646, 3

	.type	.str.1444584550978747635,@object # @.str.1444584550978747635
.str.1444584550978747635:
	.asciz	"%f"
	.size	.str.1444584550978747635, 3

	.section	".note.GNU-stack","",@progbits
