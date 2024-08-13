
`gcc hello.c -o hello.asm -S` compile to asm!


### Registers

General purpose
RAX
RBX
RCX
RDX

Index registers
RSI
RDI
RBP
RSP

Integer registers
R8 - R15

32 bit versions
EAX.. ESI..
R8D-R15D

16 bit versions
ax = ah + al
...

### Lenghts (for AT&T)

| Intel Data Type  | Suffix | Size(bytes) |
| ---------------- | ------ | ----------- |
| Byte             | b      | 1           |
| Word             | w      | 2           |
| Double Word      | l      | 4           |
| Quad Word        | q      | 8           |
| Single Precision | s      | 4           |
| Double Precision | l      | 8           |

### Instructions

*AT&T do source destination + Intel do destination source = the notes will be messy
And there's the % characters all the other things that differ...*

movq %rax (%rbx)
movq source, destination
● Transferring constants(which are prefixed using the $ operator) e.g. movq $3 rax would
move the constant 3 to the register
● Transferring values from a register e.g. movq %rax %rbx which involves moving value from
rax to rbx
● Transferring values from memory which is shown by putting registers inside brackets e.g.
movq %rax (%rbx) which means move value stored in %rax to memory location
represented by %rbx.

Some other important instructions are:
● leaq source, destination: this instruction sets destination to the address denoted by the
expression in source
● addq source, destination: destination = destination + source
● subq source, destination: destination = destination - source
● imulq source, destination: destination = destination * source
● salq source, destination: destination = destination &lt;&lt; source where &lt;&lt; is the left bit shifting
operator
● sarq source, destination: destination = destination &gt;&gt; source where &gt;&gt; is the right bit
shifting operator
● xorq source, destination: destination = destination XOR source
● andq source, destination: destination = destination &amp; source
● orq source, destination: destination = destination | source

If statements use 3 important instructions in assembly:
- cmpq source2, source1: it is like computing a-b without setting destination
- testq source2, source1: it is like computing a&b without setting destination

Jump instructions are used to transfer control to different instructions, and there are different types of jumps:

| Jump Type | Description        |
| --------- | ------------------ |
| jmp       | Unconditional      |
| je        | Equal/Zero         |
| jne       | Not Equal/Not Zero |
| js        | Negative           |
| jns       | Nonnegative        |
| jg        | Greater            |
| jge       | Greater or Equal   |
| jl        | Less               |
| jle       | Less or Equal      |
| ja        | Above(unsigned)    |
| jb        | Below(unsigned)    |


### Syscalls list

https://www.chromium.org/chromium-os/developer-library/reference/linux-constants/syscalls/#x86_64-64-bit




![[Images/Pasted image 20230829162650.png|1000]]
![[Images/Pasted image 20230829162741.png]]
