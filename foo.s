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
	rem	a0,a0,a1
	ret
	.size	foo, .-foo
	.ident	"GCC: (SiFive GCC 10.1.0-2020.08.2) 10.1.0"
