	.text
	.file	"ir3.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	pushq	%r14
	pushq	%rbx
	subq	$16, %rsp
	.cfi_offset %rbx, -32
	.cfi_offset %r14, -24
	movl	$1, -24(%rbp)
	movl	$0, -20(%rbp)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB0_2
# %bb.1:                                # %and.right
	cmpl	$0, -20(%rbp)
	setne	%al
.LBB0_2:                                # %and.end
	movzbl	%al, %ecx
	movq	%rsp, %rdx
	leaq	-16(%rdx), %rax
	movq	%rax, %rsp
	movl	%ecx, -16(%rdx)
	movb	$1, %cl
	cmpl	$0, -24(%rbp)
	jne	.LBB0_4
# %bb.3:                                # %or.right
	cmpl	$0, -20(%rbp)
	setne	%cl
.LBB0_4:                                # %or.end
	movzbl	%cl, %ecx
	movq	%rsp, %rbx
	leaq	-16(%rbx), %rsp
	movl	%ecx, -16(%rbx)
	cmpl	$0, -24(%rbp)
	setne	%cl
	cmpl	$0, -20(%rbp)
	setne	%dl
	xorb	%cl, %dl
	movzbl	%dl, %ecx
	movq	%rsp, %r14
	leaq	-16(%r14), %rsp
	movl	%ecx, -16(%r14)
	movl	(%rax), %esi
	movl	$.str.8372795069725211921, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.332649807079450794, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	-16(%rbx), %esi
	movl	$.str.8372795069725211921, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.332649807079450794, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	-16(%r14), %esi
	movl	$.str.8372795069725211921, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.332649807079450794, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	leaq	-16(%rbp), %rsp
	popq	%rbx
	popq	%r14
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.8372795069725211921,@object # @.str.8372795069725211921
	.section	.rodata,"a",@progbits
.str.8372795069725211921:
	.asciz	"%d"
	.size	.str.8372795069725211921, 3

	.type	.str.170774002489608625,@object # @.str.170774002489608625
.str.170774002489608625:
	.asciz	"%f"
	.size	.str.170774002489608625, 3

	.type	.str.3693790085204977514,@object # @.str.3693790085204977514
.str.3693790085204977514:
	.asciz	"%s"
	.size	.str.3693790085204977514, 3

	.type	.str.332649807079450794,@object # @.str.332649807079450794
.str.332649807079450794:
	.asciz	"\n"
	.size	.str.332649807079450794, 2

	.section	".note.GNU-stack","",@progbits
