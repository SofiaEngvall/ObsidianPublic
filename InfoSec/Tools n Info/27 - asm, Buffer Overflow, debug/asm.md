
https://c9x.me/x86/
https://www.felixcloutier.com/x86/

`gcc hello.c -o hello.asm -S` compile to asm!

Stack
Heap
Code (in memory)


### Lenghts (for AT&T syntax)

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

|Arithmetic|Logic|Jumps|Stack|
|---|---|---|---|
|add ⟨dest⟩ ⟨src⟩  <br>sub ⟨dest⟩ ⟨src⟩  <br>inc ⟨dest⟩  <br>dec ⟨dest⟩  <br>imul ⟨dest⟩ ⟨src⟩  <br>div ⟨dest⟩|and ⟨dest⟩ ⟨src⟩  <br>or ⟨dest⟩ ⟨src⟩  <br>not ⟨dest⟩  <br>shr ⟨dest⟩, ⟨imm⟩  <br>shr ⟨dest⟩, cl  <br>shl ⟨dest⟩, ⟨imm⟩  <br>shl ⟨dest⟩, cl  <br>sar ⟨dest⟩, ⟨imm⟩  <br>sar ⟨dest⟩, cl|jmp ⟨label⟩  <br>cmp ⟨dest⟩ ⟨src⟩  <br>je ⟨label⟩  <br>jne ⟨label⟩  <br>jg ⟨label⟩  <br>jge ⟨label⟩  <br>jl ⟨label⟩  <br>jle ⟨label⟩|call ⟨label⟩  <br>ret  <br>push ⟨src⟩  <br>pop ⟨dest⟩|
<font size=2>⟨dest⟩ is register or memory, ⟨src⟩ is register or memory or immediate, ⟨imm⟩ is immediate (byte only)</font>

### Program structure in asm

#### Call of function

Call does:
push eip            Saves the old instruction pointer to the stack
jmp function     Hops to the functions address

#### Function Prologue

A function starts with:
push ebp           Save the old base pointer to the stack
mov ebp, esp    Copies the old stack pointer as a new base pointer
push ebx           Push possible regs that will be used in the function
sub esp, 0x404  Make space for the functions variables.. on the stack (in this case a char buffer of 1024 characters)

#### Function Epilogue

A function end with:
leave      = mov esp, ebp   Save the old base pointer as a new stack pointer
         pop ebp            Get the old base pointer from the stack
ret          = pop eip            Get the old instruction pointer from the stack

Meaning leave and ret are really shorthand for these.



### Syscalls list

https://www.chromium.org/chromium-os/developer-library/reference/linux-constants/syscalls/#x86_64-64-bit




![[Images/Pasted image 20230829162650.png|1000]]
![[Images/Pasted image 20230829162741.png]]

#### Assembly

`push var`
- decrement stack pointer `rsp` by 8
- write var to where `rsp` points

`pop var`
- reads the value pointed to by `rsp`
- increment stack pointer `rsp` by 8

Each function has its own stack frame, where each new stack frame is allocated when a function is called, and deallocated when the function is complete (where)

rsp  stack pointer
rbp  frame pointer

Up to 6 arguments can be saved in registers; rdi, rsi, rdx
rcx, r8 and r9.Move can be stored in the stack frame.

Return values will be stored in rax.


