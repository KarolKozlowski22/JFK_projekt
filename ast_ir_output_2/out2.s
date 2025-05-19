	.text
	.file	"ir2.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$3, %edi
	movl	$4, %esi
	callq	add@PLT
	movl	%eax, result(%rip)
	movl	$.str.8341731685562686835, %edi
	movl	%eax, %esi
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
	.globl	add                             # -- Begin function add
	.p2align	4, 0x90
	.type	add,@function
add:                                    # @add
	.cfi_startproc
# %bb.0:                                # %entry
                                        # kill: def $esi killed $esi def $rsi
                                        # kill: def $edi killed $edi def $rdi
	movl	%edi, -4(%rsp)
	movl	%esi, -8(%rsp)
	leal	(%rdi,%rsi), %eax
	retq
.Lfunc_end1:
	.size	add, .Lfunc_end1-add
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

	.type	result,@object                  # @result
	.local	result
	.comm	result,4,4
	.section	".note.GNU-stack","",@progbits
