#!/usr/bin/env python3
# #2025-01-24

from pwn import *

context.binary = './validate'
#pprint(context)
print()
print("OS:           "+context.os)
print("Architecture: "+context.arch)
print("Bits:         "+str(context.bits))
print("Endianess:    "+context.endian)
