

make pattern
`ragg2 -P 300 > pattern.txt`

query
`ragg2 -q <EIP>`

```sh
┌──(kali㉿kali)-[~/thm/gatekeeper/Share]
└─$ ragg2 -P 300       
4141414241414341414441414541414641414741414841414941414a41414b41414c41414d41414e41414f41415041415141415241415341415441415541415641415741415841415941415a41416141416241416341416441416541416641416741416841416941416a41416b41416c41416d41416e41416f41417041417141417241417341417441417541417641417741417841417941417a41413141413241413341413441413541413641413741413841413941413041424241424341424441424541424641424741424841424941424a41424b41424c41424d41424e41424f41425041425141425241425341425441425541425641425741425841425941425a41426141426241426341426441426541426641426741426841426941426a41426b41426c41426d4142

┌──(kali㉿kali)-[~/thm/gatekeeper/Share]
└─$ ragg2 -q 0x41426d41
Little endian: 6955
Big endian: 295

┌──(kali㉿kali)-[~/thm/gatekeeper/Share]
└─$ ragg2 -q 0x416d4241
Little endian: 295
Big endian: 6955

```


windows:
```sh
c:\r2w32\bin>ragg2 -help
Usage: ragg2 [-FOLsrxhvz] [-a arch] [-b bits] [-k os] [-o file] [-I path]
             [-i sc] [-E enc] [-B hex] [-c k=v] [-C file] [-p pad] [-q off]
             [-S string] [-f fmt] [-nN dword] [-dDw off:hex] [-e expr] file|f.asm|-
 -a [arch]       select architecture (x86, mips, arm)
 -b [bits]       register size (32, 64, ..)
 -B [hexpairs]   append some hexpair bytes
 -c [k=v]        set configuration options
 -C [file]       append contents of file
 -d [off:dword]  patch dword (4 bytes) at given offset
 -D [off:qword]  patch qword (8 bytes) at given offset
 -e [egg-expr]   take egg program from string instead of file
 -E [encoder]    use specific encoder. see -L
 -f [format]     output format (raw, c, pe, elf, mach0, python, javascript)
 -F              output native format (osx=mach0, linux=elf, ..)
 -h              show this help
 -i [shellcode]  include shellcode plugin, uses options. see -L
 -I [path]       add include path
 -k [os]         operating system´s kernel (linux,bsd,osx,w32)
 -L              list all plugins (shellcodes and encoders)
 -n [dword]      append 32bit number (4 bytes)
 -N [dword]      append 64bit number (8 bytes)
 -o [file]       output file
 -O              use default output file (filename without extension or a.out)
 -p [padding]    add padding after compilation (padding=n10s32)
                 ntas : begin nop, trap, 'a', sequence
                 NTAS : same as above, but at the end
 -P [size]       prepend debruijn pattern
 -q [fragment]   debruijn pattern offset
 -r              show raw bytes instead of hexpairs
 -s              show assembler
 -S [string]     append a string
 -v              show version
 -w [off:hex]    patch hexpairs at given offset
 -x              execute
 -X [hexpairs]   execute rop chain, using the stack provided
 -z              output in C string syntax
R2_NOPLUGINS=1   do not load any plugin
```