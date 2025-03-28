#!/usr/bin/env python3
# #2025-01-24

from pwn import *
from pprint import pprint

e = ELF('/bin/bash')

# print("\nsymbols")
# pprint(e.symbols)
# print("\nGOT (Global Offset Table)")
# pprint(e.got)
# print("\nPLT (Procedure Linkage Table)")
# pprint(e.plt)
# print("\nfunctions")
# pprint(e.functions)


# Cause a debug break on the 'exit' command
e.asm(e.symbols['exit_builtin'], 'int3') # ads a breakpoint, int3 is an asm instr for this,
                                         # before the function exit_builtin()

# Disable chdir and just print it out instead
e.pack(e.got['chdir'], e.plt['puts'])

# Change the license
p_license = e.symbols['bash_license']
license = e.unpack(p_license)
e.write(license, 'Hello, world!\n\x00')

e.save('./bash-modified')
