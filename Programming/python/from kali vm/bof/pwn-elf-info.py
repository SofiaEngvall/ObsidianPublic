#!/usr/bin/env python3
#2025-01-24

from pwn import *

file_name = "validate"
#context.log_level = "debug" # = 10, default is 20

print("\nELF information:")
e = ELF(file_name)

print()
#context.arch = 'amd64'
#context.bits = 32
context.binary = e
print("OS:           "+context.os)
print("Architecture: "+context.arch)
print("Bits:         "+str(context.bits))
print("Endianess:    "+context.endian)
print("Log level:    "+str(context.log_level))

#e.address = 0x400000 #sets the base address of the elf file
print("\nBase address: %#x" % e.address)

print("\nThe first 32 bytes of data in the ELF",end="")
print("\n"+hexdump(e.read(e.address, 32)))

print("\nFunctions:")
for function in e.functions.values():
  if(not function.name[:1] == "_"):
    print("\nDisassembling function %s at %#x" % (function.name, function.address))
    print(e.disasm(e.symbols[function.name], function.size))
