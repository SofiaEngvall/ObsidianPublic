
### Low level program execution - Assembler

#### Registers

There are a number of registers, tiny bits of memory inside the processor, with special purposes.

The most important ones are:
- The Instruction pointer, ip, that keeps track of where in memory we are currently reading and executing instructions.
- The Stack pointer, sp, that keeps track of the memory address of the top of the stack.
- The Base pointer, bp, that keeps track of the memory address of current stack frame's start (aka Stack base pointer or Frame pointer)

There are also other registers, for example ax and bx, that have different specific functions in the execution of a program. Also the names of the registers are added to depending on the number of bits the program can handle.

More about registers here: [[Registers x86]]

#### Memory layout

When a program is executed two main areas of the computers memory are used, the stack and the heap.

##### The heap

The heap is mostly used for dynamically assigned memory.

##### The stack

A thing you need to remember about the stack is that it grows downwards - This means that for example when space for a new variable is declared the adress of this will be lower than the last one declared.

The stack is mainly used for saving smaller amounts of data. The most important being the next instruction to run and other registers after a function is called, local variables...

The assembler instructions push and pop can be used to quickly add/remove something to/from the stack, like a plate on a stack of plates (the reason for the name stack).

###### What push and pop actually does

push value:
`sub esp, 4`              Decrease the stack pointer by the size of the data (4 bytes)
`mov [esp], value`   Store the value at the address now pointed to by ESP

pop destination:
`mov destination, [esp]`  Load the value at ESP into the destination
`add esp, 4`                        Increase the stack pointer by the size of the data (4 bytes)

##### Stack Frames

For every function that is run a new bit of the stack is used. The old top of the stack (esp) will now be the base of the new Stack Frame (ebp). The stack frame will contain:
- the old instruction pointer (eip)
- the old base pointer (ebp)
- other registers saved by the code (compiler/programmer)
- local variables
The new top of the stack (esp) will be the stack frames top.

As you can see in the images a buffer is addressed from the "bottom" as the stack is growing to lower memory addresses.

![[Images/KmWsaIs.png|250]]    ![[Images/lqE6o0S.png|275]]

And when we put to much data into the buffer and get a buffer overflow it will overwrite what was previously put on the stack. First other variables, then other saved registers and then the saved base pointer (ebp) and instruction pointer (eip).

![[Images/buffer_overflow_2.webp|700]]

When we later leave the function, this will all reverse. The saved base pointer and instruction pointer are read back into the registers we will get a segmentation fault if they don't contain usable values. We need to get the right values into the right places.

#### Program flow in assembler

##### Call of function

Call does:
push eip            Saves the old instruction pointer to the stack
jmp function     Sets the instruction pointer to the functions memory address

##### At the start of a function

A function starts with:
push ebp           Save the old base pointer to the stack
mov ebp, esp    Copies the old stack pointer as a new base pointer
push ebx           Push possible regs that will be used in the function
sub esp, 0x404  Make space for the functions variables.. on the stack (in this case a char buffer of 1024 characters)

##### At the end of a function

A function end with:
leave      = mov esp, ebp   Save the old base pointer as a new stack pointer
         pop ebp            Get the old base pointer from the stack
ret          = pop eip            Get the old instruction pointer from the stack

Meaning leave and ret are really shorthand for these.



