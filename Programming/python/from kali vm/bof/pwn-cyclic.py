#!/usr/bin/env python3

from pwn import cyclic

pattern = cyclic(120)
print(pattern)
