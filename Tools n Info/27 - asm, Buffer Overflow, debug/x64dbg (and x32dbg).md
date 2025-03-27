
 [x64dbg](https://github.com/x64dbg/x64dbg) with the plugin [ERC.Xdbg](https://github.com/Andy53/ERC.Xdbg)

Install the latest release of x64dbg.
Get the ERC 32-bit and put it in `x64dbg\x32\plugins`. (& the same for 64-bit)

Set the working dir..
```sh
ERC --config SetWorkingDirectory C:\Users\htb-student\Desktop\
```

x64dbg docs: https://help.x64dbg.com/en/latest/
ERC docs: https://evilrobots.club/ERC.net/api/index.html


F3  Open file
Alt+A  Attach to running process (opens dialog - if you can't see the process, run x64dbg as admin)


We can use ERC to create non-repetitive patterns in x64dbg
Pattern create: `ERC --pattern <create | c> <length>`
Pattern offset: `ERC --pattern <offset | o> <search string>`

Run ERC on the Log tab at the Command: line.
`erc`


### Searching for instructions in the program

Logs tab:
- `erc --moduleinfo`  list all the processes modules
- Find the ones with no protection, all false.
- The programs own files are more likely to be running on another machine, especially the main executable.

Symbols tab (Alt+E):
- Double click the module name to jump to it in the CPU tab.
- Ctrl+F to search for an instruction in the module. For example `jmp esp`.
	If we need to search for more than one instruction we use Ctrl+B and enter the hex machine code for the instructions.
	https://defuse.ca/online-x86-assembler.htm can be used to convert instructions to machine code.
- The searches will hop us to the References tab. Mouse over or double click for more into.



### Shortcuts

| **x32dbg**                                                                                        |                                                  |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `F3`                                                                                              | Open file                                        |
| `alt+A`                                                                                           | Attach to a process                              |
| `alt+L`                                                                                           | Go to Logs Tab                                   |
| `alt+E`                                                                                           | Go to Symbols Tab                                |
| `ctrl+f`                                                                                          | Search for instruction                           |
| `ctrl+b`                                                                                          | Search for pattern                               |
| `Search For>All Modules>Command`                                                                  | Search all loaded modules for instruction        |
| `Search For>All Modules>Pattern`                                                                  | Search all loaded modules for pattern            |
| **ERC**                                                                                           |                                                  |
| `ERC --config SetWorkingDirectory C:\Users\htb-student\Desktop\`                                  | Configure Working Directory                      |
| `ERC --pattern c 5000`                                                                            | Create Pattern                                   |
| `ERC --pattern o 1hF0`                                                                            | Find Pattern Offset                              |
| `ERC --bytearray`                                                                                 | Generate All Characters Byte Array               |
| `ERC --bytearray -bytes 0x00`                                                                     | Generate Byte Array excluding certain bytes      |
| `ERC --compare 0014F974 C:\Users\htb-student\Desktop\ByteArray_1.bin`                             | Compare bytes in memory to a Byte Array file     |
| `ERC --ModuleInfo`                                                                                | List loaded modules and their memory protections |