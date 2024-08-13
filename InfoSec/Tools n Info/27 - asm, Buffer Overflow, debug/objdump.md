
`objdump` is a command-line tool that comes with GNU Binutils and can provide detailed information about ELF files.

`objdump -s -j .rodata <your_binary>` shows contents of `.rodata` section, typically read-only data, including strings.

`objdump -D -M intel file.bin | grep main.: -A20` disassemble file.bin

https://en.wikipedia.org/wiki/Objdump
https://man7.org/linux/man-pages/man1/objdump.1.html
