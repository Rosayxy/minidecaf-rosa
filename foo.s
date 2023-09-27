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
	mv	a4,a0
	mv	a0,a1
	ble	a4,zero,.L2
	li	a5,0
.L3:
	addi	a5,a5,1
	slli	a0,a0,1
	bne	a4,a5,.L3
.L2:
	ret
	.size	foo, .-foo
	.ident	"GCC: (SiFive GCC 10.1.0-2020.08.2) 10.1.0"
