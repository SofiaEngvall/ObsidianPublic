#!/usr/bin/env python3
#2025-01-24

from pwn import *

file_name = "/home/kali/bof/validate"
#context.log_level = "debug" # = 10, default is 20
#context.terminal = ['x-terminal-emulator', '-e']

#print("\nELF information:")
#e = ELF(file_name)
#context.binary = e
#print("    Bits:       "+str(context.bits))

#e.asm(e.symbols['validate'], 'int3') # ads a breakpoint

#io = e.process()
#io = process("./"+file_name)

#io = e.debug(["1234567890"], gdbscript='break validate')
io = gdb.debug(exe=file_name, args=["1234567890"], gdbscript='break validate')
io.interactive()
#io = gdb.debug("./"+file_name)

#io.send(cyclic(120))

#print(hexdump(read('/dev/urandom', 64)))

#cyclic_find(0x61616178)
