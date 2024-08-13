
```sh
┌──(kali㉿kali)-[~]
└─$ ssh user1@10.10.131.13
The authenticity of host '10.10.131.13 (10.10.131.13)' can't be established.
ED25519 key fingerprint is SHA256:AsF56RWYwwHAw06LwzfQZsBY9+GuN1jrYmQRK3FP5dU.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:3: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.131.13' (ED25519) to the list of known hosts.
user1@10.10.131.13's password: 
Last login: Wed Nov 27 21:42:30 2019 from 82.34.52.37

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
ls -l[user1@ip-10-10-131-13 ~]$ ls -la
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
[user1@ip-10-10-131-13 ~]$ cd overflow-3
[user1@ip-10-10-131-13 overflow-3]$ ls -la
total 20
drwxrwxr-x 2 user1 user1   72 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwsrwxr-x 1 user2 user2 8264 Sep  2  2019 buffer-overflow
-rw-rw-r-- 1 user1 user1  285 Sep  2  2019 buffer-overflow.c
-rw------- 1 user2 user2   22 Sep  2  2019 secret.txt
[user1@ip-10-10-131-13 overflow-3]$
```

```c
#include <stdio.h>
#include <stdlib.h>

void copy_arg(char *string)
{
    char buffer[140];
    strcpy(buffer, string);
    printf("%s\n", buffer);
    return 0;
}

int main(int argc, char **argv)
{
    printf("Here's a program that echo's out your input\n");
    copy_arg(argv[1]);
}
```

shell code - code to open a basic shell
```
\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3
```

the shell code disassembled (r2, aaa, pdf)
![[Images/Pasted image 20240809204245.png]]

Opening the c program with gdb
```sh
[user1@ip-10-10-15-3 overflow-3]$ gdb buffer-overflow
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
Reading symbols from buffer-overflow...(no debugging symbols found)...done.

(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000400400  _init
0x0000000000400430  strcpy@plt
0x0000000000400440  puts@plt
0x0000000000400450  _start
0x0000000000400480  deregister_tm_clones
0x00000000004004b0  register_tm_clones
0x00000000004004f0  __do_global_dtors_aux
0x0000000000400520  frame_dummy
0x0000000000400527  copy_arg
0x0000000000400564  main
0x00000000004005a0  __libc_csu_init
0x0000000000400610  __libc_csu_fini
0x0000000000400614  _fini

(gdb) info registers
The program has no registers now.

(gdb) start
Temporary breakpoint 1 at 0x400568
Starting program: /home/user1/overflow-3/buffer-overflow 
Missing separate debuginfos, use: debuginfo-install glibc-2.26-64.amzn2.0.2.x86_64

Temporary breakpoint 1, 0x0000000000400568 in main ()

(gdb) info registers
rax            0x400564 4195684
rbx            0x0      0
rcx            0x0      0
rdx            0x7fffffffe4a8   140737488348328
rsi            0x7fffffffe498   140737488348312
rdi            0x1      1
rbp            0x7fffffffe3b0   0x7fffffffe3b0
rsp            0x7fffffffe3b0   0x7fffffffe3b0
r8             0x400610 4195856
r9             0x7ffff7de8370   140737351943024
r10            0x0      0
r11            0x0      0
r12            0x400450 4195408
r13            0x7fffffffe490   140737488348304
r14            0x0      0
r15            0x0      0
rip            0x400568 0x400568 <main+4>
eflags         0x246    [ PF ZF IF ]
cs             0x33     51
ss             0x2b     43
ds             0x0      0
es             0x0      0
fs             0x0      0
gs             0x0      0

(gdb) q
A debugging session is active.

        Inferior 1 [process 13343] will be killed.

Quit anyway? (y or n) y
[user1@ip-10-10-15-3 overflow-3]$
```

time for r2
```sh
[user1@ip-10-10-54-231 overflow-3]$ r2 -d ./buffer-overflow
Process with PID 13282 started...
= attach 13282 13282
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Select your architecture with: 'e asm.arch=<arch>' or r2 -a from the shell
 
[0x7ffff7dd9ef0]> aaa
[Cannot analyze at 0x00600ff0g with sym. and entry0 (aa)
Invalid address from 0x004005e9
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can´t run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.

[0x7ffff7dd9ef0]> ia
arch     x86
baddr    0x400000
binsz    6403
bintype  elf
bits     64
canary   false
class    ELF64
compiler GCC: (GNU) 7.3.1 20180303 (Red Hat 7.3.1-5)
crypto   false
endian   little
havecode true
intrp    /lib64/ld-linux-x86-64.so.2
laddr    0x0
lang     c
linenum  true
lsyms    true
machine  AMD x86-64 architecture
maxopsz  16
minopsz  1
nx       false
os       linux
pcalign  0
pic      false
relocs   true
relro    partial
rpath    NONE
sanitiz  false
static   false
stripped false
subsys   linux
va       true

[Imports]
nth vaddr      bind   type   name
―――――――――――――――――――――――――――――――――
1   0x00400430 GLOBAL FUNC   strcpy
2   0x00400440 GLOBAL FUNC   puts
3   0x00000000 GLOBAL FUNC   __libc_start_main
4   0x00000000 WEAK   NOTYPE __gmon_start__

[Exports]

nth paddr       vaddr      bind   type   size name
――――――――――――――――――――――――――――――――――――――――――――――――――
43   0x00000610 0x00400610 GLOBAL FUNC   2    __libc_csu_fini
47   0x00000527 0x00400527 GLOBAL FUNC   61   copy_arg
48   ---------- 0x0060102c GLOBAL NOTYPE 0    _edata
49   0x00000614 0x00400614 GLOBAL FUNC   0    _fini
51   0x00001028 0x00601028 GLOBAL NOTYPE 0    __data_start
53   0x00000628 0x00400628 GLOBAL OBJ    0    __dso_handle
54   0x00000620 0x00400620 GLOBAL OBJ    4    _IO_stdin_used
55   0x000005a0 0x004005a0 GLOBAL FUNC   101  __libc_csu_init
56   ---------- 0x00601030 GLOBAL NOTYPE 0    _end
57   0x00000450 0x00400450 GLOBAL FUNC   43   _start
58   ---------- 0x0060102c GLOBAL NOTYPE 0    __bss_start
59   0x00000564 0x00400564 GLOBAL FUNC   51   main
60   ---------- 0x00601030 GLOBAL OBJ    0    __TMC_END__
61   0x00000400 0x00400400 GLOBAL FUNC   0    _init

[0x7ffff7dd9ef0]> is
[Symbols]

nth paddr       vaddr      bind   type   size name
――――――――――――――――――――――――――――――――――――――――――――――――――
1    0x00000238 0x00400238 LOCAL  SECT   0    .interp
2    0x00000254 0x00400254 LOCAL  SECT   0    .note.ABI-tag
3    0x00000274 0x00400274 LOCAL  SECT   0    .note.gnu.build-id
4    0x00000298 0x00400298 LOCAL  SECT   0    .gnu.hash
5    0x000002b8 0x004002b8 LOCAL  SECT   0    .dynsym
6    0x00000330 0x00400330 LOCAL  SECT   0    .dynstr
7    0x00000374 0x00400374 LOCAL  SECT   0    .gnu.version
8    0x00000380 0x00400380 LOCAL  SECT   0    .gnu.version_r
9    0x000003a0 0x004003a0 LOCAL  SECT   0    .rela.dyn
10   0x000003d0 0x004003d0 LOCAL  SECT   0    .rela.plt
11   0x00000400 0x00400400 LOCAL  SECT   0    .init
12   0x00000420 0x00400420 LOCAL  SECT   0    .plt
13   0x00000450 0x00400450 LOCAL  SECT   0    .text
14   0x00000614 0x00400614 LOCAL  SECT   0    .fini
15   0x00000620 0x00400620 LOCAL  SECT   0    .rodata
16   0x0000065c 0x0040065c LOCAL  SECT   0    .eh_frame_hdr
17   0x00000698 0x00400698 LOCAL  SECT   0    .eh_frame
18   0x00000e10 0x00600e10 LOCAL  SECT   0    .init_array
19   0x00000e18 0x00600e18 LOCAL  SECT   0    .fini_array
20   0x00000e20 0x00600e20 LOCAL  SECT   0    .dynamic
21   0x00000ff0 0x00600ff0 LOCAL  SECT   0    .got
22   0x00001000 0x00601000 LOCAL  SECT   0    .got.plt
23   0x00001028 0x00601028 LOCAL  SECT   0    .data
24   ---------- 0x0060102c LOCAL  SECT   0    .bss
25   ---------- 0x00000000 LOCAL  SECT   0    .comment
26   ---------- 0x00000000 LOCAL  FILE   0    crtstuff.c
27   0x00000480 0x00400480 LOCAL  FUNC   0    deregister_tm_clones
28   0x000004b0 0x004004b0 LOCAL  FUNC   0    register_tm_clones
29   0x000004f0 0x004004f0 LOCAL  FUNC   0    __do_global_dtors_aux
30   ---------- 0x0060102c LOCAL  OBJ    1    completed.6984
31   0x00000e18 0x00600e18 LOCAL  OBJ    0    __do_global_dtors_aux_fini_array_entry
32   0x00000520 0x00400520 LOCAL  FUNC   0    frame_dummy
33   0x00000e10 0x00600e10 LOCAL  OBJ    0    __frame_dummy_init_array_entry
34   ---------- 0x00000000 LOCAL  FILE   0    buffer-overflow.c
35   ---------- 0x00000000 LOCAL  FILE   0    crtstuff.c
36   0x000007a4 0x004007a4 LOCAL  OBJ    0    __FRAME_END__
37   ---------- 0x00000000 LOCAL  FILE   0    
38   0x00000e18 0x00600e18 LOCAL  NOTYPE 0    __init_array_end
39   0x00000e20 0x00600e20 LOCAL  OBJ    0    _DYNAMIC
40   0x00000e10 0x00600e10 LOCAL  NOTYPE 0    __init_array_start
41   0x0000065c 0x0040065c LOCAL  NOTYPE 0    __GNU_EH_FRAME_HDR
42   0x00001000 0x00601000 LOCAL  OBJ    0    _GLOBAL_OFFSET_TABLE_
43   0x00000610 0x00400610 GLOBAL FUNC   2    __libc_csu_fini
44   0x00001028 0x00601028 WEAK   NOTYPE 0    data_start
47   0x00000527 0x00400527 GLOBAL FUNC   61   copy_arg
48   ---------- 0x0060102c GLOBAL NOTYPE 0    _edata
49   0x00000614 0x00400614 GLOBAL FUNC   0    _fini
51   0x00001028 0x00601028 GLOBAL NOTYPE 0    __data_start
53   0x00000628 0x00400628 GLOBAL OBJ    0    __dso_handle
54   0x00000620 0x00400620 GLOBAL OBJ    4    _IO_stdin_used
55   0x000005a0 0x004005a0 GLOBAL FUNC   101  __libc_csu_init
56   ---------- 0x00601030 GLOBAL NOTYPE 0    _end
57   0x00000450 0x00400450 GLOBAL FUNC   43   _start
58   ---------- 0x0060102c GLOBAL NOTYPE 0    __bss_start
59   0x00000564 0x00400564 GLOBAL FUNC   51   main
60   ---------- 0x00601030 GLOBAL OBJ    0    __TMC_END__
61   0x00000400 0x00400400 GLOBAL FUNC   0    _init
1    0x00000430 0x00400430 GLOBAL FUNC   16   imp.strcpy
2    0x00000440 0x00400440 GLOBAL FUNC   16   imp.puts
3    ---------- 0x00000000 GLOBAL FUNC   16   imp.__libc_start_main
4    ---------- 0x00000000 WEAK   NOTYPE 16   imp.__gmon_start__

[0x7ffff7dd9ef0]> afl
0x00400450    1 42           entry0
0x00400480    4 42   -> 37   sym.deregister_tm_clones
0x004004b0    4 58   -> 55   sym.register_tm_clones
0x004004f0    3 34   -> 29   entry.fini0
0x00400520    1 7            entry.init0
0x00400610    1 2            sym.__libc_csu_fini
0x00400527    1 61           sym.copy_arg
0x00400430    1 6            sym.imp.strcpy
0x00400440    1 6            sym.imp.puts
0x00400614    1 9            sym._fini
0x004005a0    3 101  -> 92   sym.__libc_csu_init
0x00400400    3 23           sym._init
0x00400564    1 51           main
0x7ffff7dd9ef0    1 71           fcn.7ffff7dd9ef0
0x7ffff7ddaab0  111 -136357633 -> 1549 fcn.7ffff7ddaab0
0x7ffff7de7f70   18 305  -> 288  fcn.7ffff7de7f70

[0x7ffff7dd9ef0]> afl | grep main
0x00400564    1 51           main
```

![[Images/Pasted image 20240808152921.png]]

![[Images/Pasted image 20240808153023.png]]

