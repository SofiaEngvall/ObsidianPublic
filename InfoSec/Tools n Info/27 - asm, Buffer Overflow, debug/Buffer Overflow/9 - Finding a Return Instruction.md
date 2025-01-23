

Sometimes we can just put the address to the shellcode in EIP but the below method is a safer bet.

#### Finding a Return Instruction

In some cases we want to put the shellcode after the eip/address so that it will be located at the stack pointer position. In this case we can use another method to jump to the shell code:

We can set eip to point to a `jmp esp`, `call esp` or `push esp; ret` instruction/s in the actual program - not to the stack.

### Using r2

`/a` is search assembly
`/a jmp esp`
`/a call esp`
`/a push esp; ret`

### Using x64dbg

To find there instructions in the program using x64dbg we can:

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

### Using Immunity Debugger and mona

```sh
!mona jmp -r esp -cpb "\x00<more bad chars here>"
```

Ex `!mona jmp -r esp -cpb "\x00\x0a"`

In the Log data output, we see:
```sh
0BADF00D  [+] Command used:
0BADF00D  !mona jmp -r esp -cpb "\x00\x0a"
          
          ---------- Mona command started on 2025-01-17 12:34:14 (v2.0, rev 636) ----------
0BADF00D  [+] Processing arguments and criteria
0BADF00D      - Pointer access level : X
0BADF00D      - Bad char filter will be applied to pointers : "\x00\x0a" 
0BADF00D  [+] Generating module info table, hang on...
0BADF00D      - Processing modules
0BADF00D      - Done. Let's rock 'n roll.
0BADF00D  [+] Querying 1 modules
0BADF00D      - Querying module gatekeeper.exe
0BADF00D      - Search complete, processing results
0BADF00D  [+] Preparing output file 'jmp.txt'
0BADF00D      - (Re)setting logfile c:\mona\gatekeeper\jmp.txt
0BADF00D  [+] Writing results to c:\mona\gatekeeper\jmp.txt
0BADF00D      - Number of pointers of type 'jmp esp' : 2 
0BADF00D  [+] Results : 
080414C3    0x080414c3 : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, CFG: False, OS: True, v-1.0- (C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper\gatekeeper.exe), 0x8000
080416BF    0x080416bf : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, CFG: False, OS: True, v-1.0- (C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper\gatekeeper.exe), 0x8000
0BADF00D      Found a total of 2 pointers
0BADF00D  
0BADF00D  [+] This mona.py action took 0:00:05.578000
```

mona also saves a file called jmp.txt in the configured output directory containing more info.

