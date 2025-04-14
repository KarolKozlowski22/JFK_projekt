	.text
	.file	"ir6.ll"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3, 0x0                          # -- Begin function main
.LCPI0_0:
	.quad	0x4016000000000000              # double 5.5
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movabsq	$4617878467915022336, %rax      # imm = 0x4016000000000000
	movq	%rax, (%rsp)
	movsd	.LCPI0_0(%rip), %xmm0           # xmm0 = [5.5E+0,0.0E+0]
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
