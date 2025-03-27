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
	movq	x@GOTPCREL(%rip), %rax
	movl	(%rax), %esi
	movl	$".L.str.-2452015952092396623", %edi
	xorl	%eax, %eax
	callq	printf@PLT
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	".L.str.-2452015952092396623",@object # @.str.-2452015952092396623
	.section	.rodata,"a",@progbits
".L.str.-2452015952092396623":
	.asciz	"%d\n"
	.size	".L.str.-2452015952092396623", 4

	.type	".L.str.-774703926669740791",@object # @.str.-774703926669740791
".L.str.-774703926669740791":
	.asciz	"%f\n"
	.size	".L.str.-774703926669740791", 4

	.type	x,@object                       # @x
	.data
	.globl	x
	.p2align	2, 0x0
x:
	.long	42                              # 0x2a
	.size	x, 4

	.section	".note.GNU-stack","",@progbits
