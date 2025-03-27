
#### Exploring memory (stack and heap)

When we find a buffer overflow vulnerability we need more information. We can use different tools to explore memory and to debug and step through program execution. Hopefully we can run the program in a debugger or attach to a process with a GUI debugger like like edb (Linux) or Immunity debugger (Windows).

There are lots of tools available to debug and explore applications in different ways. For Linux we have for example [[../r2 (radare2)]], [[../gdb]], lldb, [[../objdump]], readelf and edb (graphical). For Windows there are WinDbg, OllyDbg, Immunity Debugger, (IDA)... A modern choice is [[../x64dbg (and x32dbg)]].

The simplest for basic info might be objdump:
`objdump -d <program>` disassemble program to get function adress..

More complex with almost infinite possibilities tools like are gdb and r2...

Examples gdb:

```sh
(gdb) info functions
0x0000000000400527  copy_arg
0x0000000000400564  main
...
```

```sh
(gdb) info registers
rax            0x400564 4195684
rbx            0x0      0
rbp            0x7fffffffe3b0   0x7fffffffe3b0
rsp            0x7fffffffe3b0   0x7fffffffe3b0
rip            0x400568 0x400568 <main+4>
...
```

```sh
(gdb) disassemble main
Dump of assembler code for function main:
   0x000011d2 <+0>:     lea    ecx,[esp+0x4]
   0x000011d6 <+4>:     and    esp,0xfffffff0
   0x000011d9 <+7>:     push   DWORD PTR [ecx-0x4]
   0x000011dc <+10>:    push   ebp
   0x000011dd <+11>:    mov    ebp,esp
```

```sh
(gdb) x/40x $sp
0x7fffffffdd30: 0x00000000      0x00000000      0xf7fe6c40      0x00007fff
0x7fffffffdd40: 0x00000000      0x00000000      0xf7ffdab0      0x00007fff
0x7fffffffdd50: 0x00000001      0x00000000      0xf7decc8a      0x00007fff
0x7fffffffdd60: 0xffffde50      0x00007fff      0x55555159      0x00005555
...
```


Examples r2:

```sh
[0x7ffff7dd9ef0]> afl
0x00400527    1 61           sym.copy_arg
0x00400564    1 51           main
...
```

```sh
[0x0040052b]> dr
rax = 0x7fffffffe623
rbx = 0x00000000
rsp = 0x7fffffffe2d0
rbp = 0x7fffffffe2d0
rip = 0x0040052b
...
```

```sh
[0x7ffff7dd9ef0]> pdf @main
┌ 51: int main (int argc, char **argv, char **envp);
│           0x00400564      55             push rbp
│           0x00400565      4889e5         mov rbp, rsp
│           0x00400568      4883ec10       sub rsp, 0x10
│           0x0040056c      897dfc         mov dword [var_4h], edi     ; argc
│           0x0040056f      488975f0       mov qword [var_10h], rsi    ; argv
...
```

```sh
[0x00400532]> pxa @rsp
    - offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
                 /rsp                                                   
0x7fffffffe230  c0f8 dcf7 ff7f 0000 23e6 ffff ff7f 0000  ........#.......
0x7fffffffe240  2b00 0000 0000 0000 2c00 0000 0000 0000  +.......,.......
0x7fffffffe250  0a00 0000 0000 0000 3006 4000 0000 0000  ........0.@.....
0x7fffffffe260  0004 ddf7 ff7f 0000 0000 0000 0000 0000  ................
...
```
