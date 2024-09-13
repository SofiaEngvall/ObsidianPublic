
Added after Windows XP.

### DEP (Data Execution Prevention)

Regions of memory, for example the stack, are marked Read-Only. This is to prevent users from putting shellcode in memory and running it by setting the instruction pointer. ^should probably be non-exec?

Counter measure: ROP (Return Oriented Programming) allows upload of shellcode to an executable space and then uses existing calls to execute it. Requires knowledge of the memory addresses where things are stored. ASLR tries to prevent this.

#### Stack Smashing Protection (SSP)
A security feature that disallows execution on the stack. Often a part of DEP.


### ASLR (Address Space Layout Randomization)

Randomizes where everything is stored. Makes exploits less reliable.

Counter measures: Possibly leaking memory addresses. Might not be possible.


### Compiling away security features (for testing)

Remove "canaries"/stack cookies that gcc adds to make sure the stack was not tampered with.
`-fno-stack-protector`
`gcc program.c -o program -fno-stack-protector`

Remove PIE (Position Independent Executable) that loads the executable at a different memory address every time it's run.
`-no-pie`
`gcc program.c -o program -fno-stack-protector -no-pie`

 Mark the stack as executable. This allows code execution on the stack.
 `-z execstack`
`gcc program.c -o program -fno-stack-protector -no-pie -z execstack`

Also add `-g` if you want debug symbols.


### Disable security features (for testing)

#### ASLR

Example on my kali box
```
┌──(kali㉿kali)-[~]
└─$ cat /proc/sys/kernel/randomize_va_space 
2

┌──(kali㉿kali)-[~]
└─$ sudo su                                          
[sudo] password for kali: 

┌──(root㉿kali)-[/home/kali]
└─# echo 0 > /proc/sys/kernel/randomize_va_space

┌──(root㉿kali)-[/home/kali]
└─# exit                                        

┌──(kali㉿kali)-[~]
└─$ cat /proc/sys/kernel/randomize_va_space     
0
```
This is reset at reboot.



