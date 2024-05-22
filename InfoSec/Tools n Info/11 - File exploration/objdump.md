
(chatgpt - needs checking)

`objdump` is a command-line tool that comes with GNU Binutils and can provide detailed information about ELF files.

**Installation:**

`sudo apt-get install binutils`

**Usage:**

`objdump -s -j .rodata <your_binary>`

This command shows the contents of the `.rodata` section, which typically contains read-only data, including strings.