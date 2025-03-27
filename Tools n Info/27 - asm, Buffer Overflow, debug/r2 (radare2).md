aflood
Preinstalled in kali full
https://github.com/radareorg/radare2
https://book.rada.re - manual

r2 exists for windows too

Cheatsheet: https://r2wiki.readthedocs.io/en/latest/home/misc/cheatsheet/
Docs: https://r2wiki.readthedocs.io/en/latest/

To list strings:
	`r2 -A <executableFilename>`   (same as aaa at r2 prompt)
		`iz` list strings

To debug a file or running process:
	`r2 -d A ./file1 [arguments for file1]`
		`afl` functions list
		`pdf @main` print disassembly function

At r2 prompt:
`i`  show file info
`e asm.syntax=att` set AT&T syntax
`e asm.syntax=intel` set Intel syntax (default)

`aaa` analyze
`ia` show all info
`ie` entry point
`im` memory
`is` symbols (including functions)
`afl` list functions
`afl | grep main`
`pdf @main` disassemble function
`iz`  list strings

`db` list brakepoints
`db sym.main` add breakpoint
`db <addr>` add breakpoint
`db- <addr>` remove breakpoint
`db-*` remove all breakpoints

`dc` continue execution
`ds` step one instruction
`dsb` step back one instruction
`dsl` step one source line
`dsp` Step into program (skip libs)

`dr` list registers contents

`px <@memory-address>` list memory contents
`px @rbp-0xc` adress example using rbp
`pxr @rsp`  show hexword references (reverses the order of the bytes compared to normal string order and px or pxa..)
`pxa @rsp`  show annotated hexdump <--- I'm using this
`pxw @rsp`  show hexadecimal words dump (32bit) (also reverses ^)
`pxq @rsp`  show hexadecimal quad-words dump (64bit)
`ad@r:SP`  to analyze the stack data

`ood` reload the program
`ood <arguments>` reloads and adds arguments to the program we debug

`/a` is search assembly
`/a jmp esp`  searches asm code for jmp esp instructions (does not search libraries)
`/a call esp`
`/a push esp; ret`

## Examples

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

[0x7ffff7dd9ef0]> iz
[Strings]
nth paddr      vaddr      len size section type  string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
0   0x00000630 0x00400630 43  44   .rodata ascii Here's a program that echo's out your input

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



```

```sh
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


```



## Help

```sh
$ radare2 -h
Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-i file]
          [-s addr] [-B baddr] [-m maddr] [-c cmd] [-e k=v] file|pid|-|--|=
 --           run radare2 without opening any file
 -            same as 'r2 malloc://512'
 =            read file from stdin (use -i and -c to run cmds)
 -=           perform !=! command to run all commands remotely
 -0           print \x00 after init and every command
 -2           close stderr file descriptor (silent warning messages)
 -a [arch]    set asm.arch
 -A           kailenced code
 -b [bits]    set asm.bits
 -B [baddr]   set base address for PIE binaries
 -c 'cmd..'   execute radare command
 -C           file is host:port (alias for -c+=http://%s/cmd/)
 -d           debug the executable 'file' or running process 'pid'
 -D [backend] enable debug mode (e cfg.debug=true)
 -e k=v       evaluate config var
 -f           block size = file size
 -F [binplug] force to use that rbin plugin
 -h, -hh      show help message, -hh for long
 -H ([var])   display variable
 -i [file]    run script file
 -I [file]    run script file before the file is opened
 -j           use json for -v, -L and maybe others
 -k [OS/kern] set asm.os (linux, macos, w32, netbsd, ...)
 -l [lib]     load plugin file
 -L           list supported IO plugins
 -m [addr]    map file at given address (loadaddr)
 -M           do not demangle symbol names
 -n, -nn      do not load RBin info (-nn only load bin structures)
 -N           do not load user settings and scripts
 -NN          do not load any script or plugin
 -q           quiet mode (no prompt) and quit after -i
 -qq          quit after running all -c and -i
 -Q           quiet mode (no prompt) and quit faster (quickLeak=true)
 -p [prj]     use project, list if no arg, load if no file
 -P [file]    apply rapatch file and quit
 -r [rarun2]  specify rarun2 profile to load (same as -e dbg.profile=X)
 -R [rr2rule] specify custom rarun2 directive
 -s [addr]    initial seek
 -S           start r2 in sandbox mode
 -T           do not compute file hashes
 -u           set bin.filter=false to get raw sym/sec/cls names
 -v, -V       show radare2 version (-V show lib versions)
 -w           open file in write mode
 -x           open without exec-flag (asm.emu will not work), See io.exec
 -X           same as -e bin.usextr=false (useful for dyldcache)
 -z, -zz      do not load strings or load them even in raw
```

```sh
[0x7ffff7dd9ef0]> ?
Usage: [.][times][cmd][~grep][@[@iter]addr!size][|>pipe] ; ...   
Append '?' to any char command to get detailed help
Prefix with number to repeat command N times (f.ex: 3x)
| %var=value              alias for 'env' command
| *[?] off[=[0x]value]    pointer read/write data/values (see ?v, wx, wv)
| (macro arg0 arg1)       manage scripting macros
| .[?] [-|(m)|f|!sh|cmd]  Define macro or load r2, cparse or rlang file
| _[?]                    Print last output
| =[?] [cmd]              send/listen for remote commands (rap://, raps://, udp://, http://, <fd>)
| <[...]                  push escaped string into the RCons.readChar buffer
| /[?]                    search for bytes, regexps, patterns, ..
| ![?] [cmd]              run given command as in system(3)
| #[?] !lang [..]         Hashbang to run an rlang script
| a[?]                    analysis commands
| b[?]                    display or change the block size
| c[?] [arg]              compare block with given data
| C[?]                    code metadata (comments, format, hints, ..)
| d[?]                    debugger commands
| e[?] [a[=b]]            list/get/set config evaluable vars
| f[?] [name][sz][at]     add flag at current address
| g[?] [arg]              generate shellcodes with r_egg
| i[?] [file]             get info about opened file from r_bin
| k[?] [sdb-query]        run sdb-query. see k? for help, 'k *', 'k **' ...
| l [filepattern]         list files and directories
| L[?] [-] [plugin]       list, unload load r2 plugins
| m[?]                    mountpoints commands
| o[?] [file] ([offset])  open file at optional address
| p[?] [len]              print current block with format and length
| P[?]                    project management utilities
| q[?] [ret]              quit program with a return value
| r[?] [len]              resize file
| s[?] [addr]             seek to address (also for '0x', '0x1' == 's 0x1')
| t[?]                    types, noreturn, signatures, C parser and more
| T[?] [-] [num|msg]      Text log utility (used to chat, sync, log, ...)
| u[?]                    uname/undo seek/write
| v                       visual mode (v! = panels, vv = fcnview, vV = fcngraph, vVV = callgraph)
| w[?] [str]              multiple write operations
| x[?] [len]              alias for 'px' (print hexadecimal)
| y[?] [len] [[[@]addr    Yank/paste bytes from/to memory
| z[?]                    zignatures management
| ?[??][expr]             Help or evaluate math expression
| ?$?                     show available '$' variables and aliases
| ?@?                     misc help for '@' (seek), '~' (grep) (see ~??)
| ?>?                     output redirection
| ?|?                     help for '|' (pipe)
```

```sh
[0x7ffff7dd9ef0]> a?
Usage: a  [abdefFghoprxstc] [...]
| a                  alias for aai - analysis information
| a*                 same as afl*;ah*;ax*
| aa[?]              analyze all (fcns + bbs) (aa0 to avoid sub renaming)
| a8 [hexpairs]      analyze bytes
| ab[b] [addr]       analyze block at given address
| abb [len]          analyze N basic blocks in [len] (section.size by default)
| ac[?]              manage classes
| aC[?]              analyze function call
| aCe[?]             same as aC, but uses esil with abte to emulate the function
| ad[?]              analyze data trampoline (wip)
| ad [from] [to]     analyze data pointers to (from-to)
| ae[?] [expr]       analyze opcode eval expression (see ao)
| afaf?             analyze Functions
| aF                 same as above, but using anal.depth=1
| ag[?] [options]    draw graphs in various formats
| ah[?]              analysis hints (force opcode size, ...)
| ai [addr]          address information (show perms, stack, heap, ...)
| aj                 same as a* but in json (aflj)
| aL                 list all asm/anal plugins (e asm.arch=?)
| an [name] [@addr]  show/rename/create whatever flag/function is used at addr
| ao[?] [len]        analyze Opcodes (or emulate it)
| aO[?] [len]        Analyze N instructions in M bytes
| ap                 find prelude for current offset
| ar[?]              like 'dr' but for the esil vm. (registers)
| as[?] [num]        analyze syscall using dbg.reg
| av[?] [.]          show vtables
| ax[?]              manage refs/xrefs (see also afx?)
```

```sh
[0x7ffff7dd9ef0]> af?
Usage: af  
| af ([name]) ([addr])                  analyze functions (start at addr or $$)
| afr ([name]) ([addr])                 analyze functions recursively
| af+ addr name [type] [diff]           hand craft a function (requires afb+)
| af- [addr]                            clean all function analysis data (or function at addr)
| afa                                   analyze function arguments in a call (afal honors dbg.funcarg)
| afb+ fcnA bbA sz [j] [f] ([t]( [d]))  add bb to function @ fcnaddr
| afb[?] [addr]                         List basic blocks of given function
| afbF([0|1])                           Toggle the basic-block 'folded' attribute
| afB 16                                set current function as thumb (change asm.bits)
| afC[lc] ([addr])@[addr]               calculate the Cycles (afC) or Cyclomatic Complexity (afCc)
| afc[?] type @[addr]                   set calling convention for function
| afd[addr]                             show function + delta for given offset
| aff                                   re-adjust function boundaries to fit
| afF[1|0|]                             fold/unfold/toggle
| afi [addr|fcn.name]                   show function(s) information (verbose afl)
| afj [tableaddr] [count]               analyze function jumptable
| afl[?] [ls*] [fcn name]               list functions (addr, size, bbs, name) (see afll)
| afm name                              merge two functions
| afM name                              print functions map
| afn[?] name [addr]                    rename name for function at address (change flag too)
| afna                                  suggest automatic name for current offset
| afo[?j] [fcn.name]                    show address for the function name or current offset
| afs[!] ([fcnsign])                    get/set function signature at current address (afs! uses cfg.editor)
| afS[stack_size]                       set stack frame size for function at current address
| afsr [function_name] [new_type]       change type for given function
| aft[?]                                type matching, type propagation
| afu addr                              resize and analyze function from current address until addr
| afv[bsra]?                            manipulate args, registers and variables in function
| afx                                   list function references
```

```sh
[0x7ffff7dd9ef0]> d?
Usage: d   # Debug commands
| db[?]                    Breakpoints commands
| dbt[?]                   Display backtrace based on dbg.btdepth and dbg.btalgo
| dc[?]                    Continue execution
| dd[?]                    File descriptors (!fd in r1)
| de[-sc] [perm] [rm] [e]  Debug with ESIL (see de?)
| dg <file>                Generate a core-file (WIP)
| dH [handler]             Transplant process to a new handler
| di[?]                    Show debugger backend information (See dh)
| dk[?]                    List, send, get, set, signal handlers of child
| dL[?]                    List or set debugger handler
| dm[?]                    Show memory maps
| do[?]                    Open process (reload, alias for 'oo')
| doo[args]                Reopen in debugger mode with args (alias for 'ood')
| dp[?]                    List, attach to process or thread id
| dr[?]                    Cpu registers
| ds[?]                    Step, over, source line
| dt[?]                    Display instruction traces
| dw <pid>                 Block prompt until pid dies
| dx[?]                    Inject and run code on target process (See gs)
```

```sh
[0x7ffff7dd9ef0]> db?
Usage: db    # Breakpoints commands
| db                        List breakpoints
| db*                       List breakpoints in r commands
| db sym.main               Add breakpoint into sym.main
| db <addr>                 Add breakpoint
| db- <addr>                Remove breakpoint
| db-*                      Remove all the breakpoints
| db.                       Show breakpoint info in current offset
| dbj                       List breakpoints in JSON format
| dbc <addr> <cmd>          Run command when breakpoint is hit
| dbC <addr> <cmd>          Run command but continue until <cmd> returns zero
| dbd <addr>                Disable breakpoint
| dbe <addr>                Enable breakpoint
| dbs <addr>                Toggle breakpoint
| dbf                       Put a breakpoint into every no-return function
| dbm <module> <offset>     Add a breakpoint at an offset from a module´s base
| dbn [<name>]              Show or set name for current breakpoint
| dbi                       List breakpoint indexes
| dbi <addr>                Show breakpoint index in givengiven  offset
| dbi.                      Show breakpoint index in current offset
| dbix <idx> [expr]         Set expression for bp at given index
| dbic <idx> <cmd>          Run command at breakpoint index
| dbie <idx>                Enable breakpoint by index
| dbid <idx>                Disable breakpoint by index
| dbis <idx>                Swap Nth breakpoint
| dbite <idx>               Enable breakpoint Trace by index
| dbitd <idx>               Disable breakpoint Trace by index
| dbits <idx>               Swap Nth breakpoint trace
| dbh x86                   Set/list breakpoint plugin handlers
| dbh- <name>               Remove breakpoint plugin handler
| dbt[?]                    Show backtrace. See dbt? for more details
| dbx [expr]                Set expression for bp in current offset
| dbw <addr> <r/w/rw>       Add watchpoint
| drx number addr len perm  Modify hardware breakpoint
| drx-number                Clear hardware breakpoint
```

```sh
[0x7ffff7dd9ef0]> ds?
Usage: ds   Step commands
| ds                Step one instruction
| ds <num>          Step <num> instructions
| dsb               Step back one instruction
| dsf               Step until end of frame
| dsi <cond>        Continue until condition matches
| dsl               Step one source line
| dsl <num>         Step <num> source lines
| dso <num>         Step over <num> instructions
| dsp               Step into program (skip libs)
| dss <num>         Skip <num> step instructions
| dsu[?] <address>  Step until <address>. See 'dsu?' for other step until cmds.
```

```sh
[0x7ffff7dd9ef0]> p?
Usage: p[=68abcdDfiImrstuxz] [arg|len] [@addr]  
| p[b|B|xb] [len] ([S])   bindump N bits skipping S bytes
| p[iI][df] [len]         print N ops/bytes (f=func) (see pi? and pdi)
| p[kK] [len]             print key in randomart (K is for mosaic)
| p-[?][jh] [mode]        bar|json|histogram blocks (mode: e?search.in)
| p2 [len]                8x8 2bpp-tiles
| p3 [file]               print stereogram (3D)
| p6[de] [len]            base64 decode/encode
| p8[?][j] [len]          8bit hexpair list of bytes
| p=[?][bep] [N] [L] [b]  show entropy/printable chars/chars bars
| pa[edD] [arg]           pa:assemble  pa[dD]:disasm or pae: esil from hex
| pA[n_ops]               show n_ops address and type
| pb[?] [n]               bitstream of N bits
| pB[?] [n]               bitstream of N bytes
| pc[?][p] [len]          output C (or python) format
| pC[aAcdDxw] [rows]      print disassembly in columns (see hex.cols and pdi)
| pd[?] [sz] [a] [b]      disassemble N opcodes (pd) or N bytes (pD)
| pf[?][.nam] [fmt]       print formatted data (pf.name, pf.name $<expr>)
| pF[?][apx]              print asn1, pkcs7 or x509
| pg[?][x y w h] [cmd]    create new visual gadget or print it (see pg? for details)
| ph[?][=|hash] ([len])   calculate hash for a block
| pj[?] [len]             print as indented JSON
| pm[?] [magic]           print libmagic data (see pm? and /m?)
| po[?] hex               print operation applied to block (see po?)
| pp[?][sz] [len]         print patterns, see pp? for more help
| pq[?][is] [len]         print QR code with the first Nbytes
| pr[?][glx] [len]        print N raw bytes (in lines or hexblocks, 'g'unzip)
| ps[?][pwz] [len]        print pascal/wide/zero-terminated strings
| pt[?][dn] [len]         print different timestamps
| pu[?][w] [len]          print N url encoded bytes (w=wide)
| pv[?][jh] [mode]        show variable/pointer/value in memory
| pwd                     display current working directory
| px[?][owq] [len]        hexdump of N bytes (o=octal, w=32bit, q=64bit)
| pz[?] [len]             print zoom view (see pz? for help)
```

```sh
[0x7ffff7dd9ef0]> pd?
Usage: p[dD][ajbrfils] [len]   # Print Disassembly
| NOTE: len        parameter can be negative
| NOTE:            Pressing ENTER on empty command will repeat last print command in next page
| pD N             disassemble N bytes
| pd -N            disassemble N instructions backward
| pd N             disassemble N instructions
| pd--[n]          context disassembly of N instructions
| pda              disassemble all possible opcodes (byte per byte)
| pdb              disassemble basic block
| pdc              pseudo disassembler output in C-like syntax
| pdC              show comments found in N instructions
| pdf              disassemble function
| pdi              like 'pi', with offset and bytes
| pdj              disassemble to json
| pdJ              formatted disassembly like pd as json
| pdk              disassemble all methods of a class
| pdl              show instruction sizes
| pdp              disassemble by following pointers to read ropchains
| pdr              recursive disassemble across the function graph
| pdR              recursive disassemble block size bytes without analyzing functions
| pdr.             recursive disassemble across the function graph (from current basic block)
| pds[?]           disassemble summary (strings, calls, jumps, refs) (see pdsf and pdfs)
| pdt [n] [query]  disassemble N instructions in a table (see dtd for debug traces)
| pdx [hex]        alias for pad or pix
```

```sh
[0x7ffff7dd9ef0]> i?
Usage: i   Get info from opened file (see rabin2´s manpage)
Output mode:
| '*'                Output in radare commands
| 'j'                Output in json
| 'q'                Simple quiet output
Actions:
| i|ij               Show info of current file (in JSON)
| iA                 List archs
| ia                 Show all info (imports, exports, sections..)
| ib                 Reload the current buffer for setting of the bin (use once only)
| ic                 List classes, methods and fields
| icc                List classes, methods and fields in Header Format
| icg                List classes as agn/age commands to create class hirearchy graphs
| icq                List classes, in quiet mode (just the classname)
| icqq               List classes, in quieter mode (only show non-system classnames)
| iC                 Show signature info (entitlements, ...)
| id[?]              Debug information (source lines)
| idp                Load pdb file information
| iD lang sym        demangle symbolname for given language
| ie                 Entrypoint
| iee                Show Entry and Exit (preinit, init and fini)
| iE                 Exports (global symbols)
| iE.                Current export
| ih                 Headers (alias for iH)
| iHH                Verbose Headers in raw text
| ii                 Imports
| iI                 Binary info
| ik [query]         Key-value database from RBinObject
| il                 Libraries
| iL [plugin]        List all RBin plugins loaded or plugin details
| im                 Show info about predefined memory allocation
| iM                 Show main address
| io [file]          Load info from file (or last opened) use bin.baddr
| iO[?]              Perform binary operation (dump, resize, change sections, ...)
| ir                 List the Relocations
| iR                 List the Resources
| is                 List the Symbols
| is.                Current symbol
| iS [entropy,sha1]  Sections (choose which hash algorithm to use)
| iS.                Current section
| iS=                Show ascii-art color bars with the section ranges
| iSS                List memory segments (maps with om)
| it                 File hashes
| iT                 File signature
| iV                 Display file version info
| iw                 try/catch blocks
| iX                 Display source files used (via dwarf)
| iz|izj             Strings in data sections (in JSON/Base64)
| izz                Search for Strings in the whole binary
| izzz               Dump Strings from whole binary to r2 shell (for huge files)
| iz- [addr]         Purge string via bin.str.purge
| iZ                 Guess size of binary program

```
