
Added after Windows XP.

### DEP (Data Execution Prevention)

Regions of memory, for example the stack, are marked non-executable (NX). This is to prevent users from putting shellcode in memory and running it by setting the instruction pointer.

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

If you want a permanent disable, add this to `/etc/sysctl.conf`:
```
kernel.randomize_va_space=0
```


### Check binary

`readelf -s /path/to/your/binary` to see more data
`__stack_chk_fail` means stack canaries are enabled (remove with `-fstack-protector`)

### Check system

NX protection is a hardware feature that prevents execution of code on the stack. While this is usually controlled by the system, you can check the status with:

`cat /proc/sys/vm/legacy_va_layout`

If it returns `1`, NX is disabled. If it returns `0`, you may need to disable it in the BIOS/UEFI settings or at the kernel level (although this is uncommon in most systems).


### Disabling security in windows (for testing)

TODO Add stuff here


### Advanced bypass methods

To add:
Return Oriented Programming (`ROP`)
Windows-specific exploitation methods like Egg Hunting or Structured Exception Handling (`SEH`) exploitation.