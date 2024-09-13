
C code:
```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int bowfunc(char *string) {

        char buffer[1024];
        strcpy(buffer, string);
        return 1;
}

int main(int argc, char *argv[]) {

        bowfunc(argv[1]);
        printf("Done.\n");
        return 1;
}
```

Compile:
```sh
gcc bow.c -o bow32 -fno-stack-protector -z execstack -m32 
```
For info on options check [[../../../Tools n Info/27 - asm, Buffer Overflow, debug/Modern security features|Modern security features]]
`-m64` for a 64-bit program

Exploring with gdb:
```sh
┌──(kali㉿kali)-[~/htb-a/stack-bof-linux]
└─$ gdb -q bow32
Reading symbols from bow32...
(No debugging symbols found in bow32)
(gdb) disassemble main
Dump of assembler code for function main:
   0x000011d2 <+0>:     lea    ecx,[esp+0x4]
   0x000011d6 <+4>:     and    esp,0xfffffff0
   0x000011d9 <+7>:     push   DWORD PTR [ecx-0x4]
   0x000011dc <+10>:    push   ebp
   0x000011dd <+11>:    mov    ebp,esp
   0x000011df <+13>:    push   ebx
   0x000011e0 <+14>:    push   ecx
   0x000011e1 <+15>:    call   0x10a0 <__x86.get_pc_thunk.bx>
   0x000011e6 <+20>:    add    ebx,0x2e0e
   0x000011ec <+26>:    mov    eax,ecx
   0x000011ee <+28>:    mov    eax,DWORD PTR [eax+0x4]
   0x000011f1 <+31>:    add    eax,0x4
   0x000011f4 <+34>:    mov    eax,DWORD PTR [eax]
   0x000011f6 <+36>:    sub    esp,0xc
   0x000011f9 <+39>:    push   eax
   0x000011fa <+40>:    call   0x119d <bowfunc>
   0x000011ff <+45>:    add    esp,0x10
   0x00001202 <+48>:    sub    esp,0xc
   0x00001205 <+51>:    lea    eax,[ebx-0x1fec]
   0x0000120b <+57>:    push   eax
   0x0000120c <+58>:    call   0x1050 <puts@plt>
   0x00001211 <+63>:    add    esp,0x10
   0x00001214 <+66>:    mov    eax,0x1
   0x00001219 <+71>:    lea    esp,[ebp-0x8]
   0x0000121c <+74>:    pop    ecx
   0x0000121d <+75>:    pop    ebx
   0x0000121e <+76>:    pop    ebp
   0x0000121f <+77>:    lea    esp,[ecx-0x4]
   0x00001222 <+80>:    ret
End of assembler dump.
(gdb) disas bowfunc
Dump of assembler code for function bowfunc:
   0x0000119d <+0>:     push   ebp
   0x0000119e <+1>:     mov    ebp,esp
   0x000011a0 <+3>:     push   ebx
   0x000011a1 <+4>:     sub    esp,0x404
   0x000011a7 <+10>:    call   0x1223 <__x86.get_pc_thunk.ax>
   0x000011ac <+15>:    add    eax,0x2e48
   0x000011b1 <+20>:    sub    esp,0x8
   0x000011b4 <+23>:    push   DWORD PTR [ebp+0x8]
   0x000011b7 <+26>:    lea    edx,[ebp-0x408]
   0x000011bd <+32>:    push   edx
   0x000011be <+33>:    mov    ebx,eax
   0x000011c0 <+35>:    call   0x1040 <strcpy@plt>
   0x000011c5 <+40>:    add    esp,0x10
   0x000011c8 <+43>:    mov    eax,0x1
   0x000011cd <+48>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x000011d0 <+51>:    leave
   0x000011d1 <+52>:    ret
End of assembler dump.
(gdb) 
```
