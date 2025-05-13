	.text
	.file	"ir6.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movq	$.str.5763952219968936785, (%rsp)
	movl	$.str.966308075288711710, %edi
	movl	$.str.5763952219968936785, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$.str.8146335450369478114, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.str.4593572070920732383,@object # @.str.4593572070920732383
	.section	.rodata,"a",@progbits
.str.4593572070920732383:
	.asciz	"%d"
	.size	.str.4593572070920732383, 3

	.type	.str.1495783277522668851,@object # @.str.1495783277522668851
.str.1495783277522668851:
	.asciz	"%f"
	.size	.str.1495783277522668851, 3

	.type	.str.966308075288711710,@object # @.str.966308075288711710
.str.966308075288711710:
	.asciz	"%s"
	.size	.str.966308075288711710, 3

	.type	.str.8146335450369478114,@object # @.str.8146335450369478114
.str.8146335450369478114:
	.asciz	"\n"
	.size	.str.8146335450369478114, 2

	.type	.str.5763952219968936785,@object # @.str.5763952219968936785
.str.5763952219968936785:
	.asciz	"Hello, World!"
	.size	.str.5763952219968936785, 14

	.section	".note.GNU-stack","",@progbits
