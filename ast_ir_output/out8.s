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
	movl	$.str.3948252993100881646, %edi
	movl	$3, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movss	(%rsp), %xmm0                   # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movl	$.str.1444584550978747635, %edi
	movb	$1, %al
	callq	printf@PLT
	popq	%rax
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
