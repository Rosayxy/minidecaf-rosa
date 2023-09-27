	.file	"foo.c"
	.option nopic
	.attribute arch, "rv32i2p0_m2p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	foo
	.type	foo, @function
foo:
	beq	a0,a1,.L3
	li	a0,8
	ret
.L3:
	li	a0,6
	ret
	.size	foo, .-foo
	.ident	"GCC: (SiFive GCC 10.1.0-2020.08.2) 10.1.0"
