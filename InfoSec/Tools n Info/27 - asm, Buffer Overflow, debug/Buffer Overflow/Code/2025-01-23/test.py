from pwn import *

pattern = cyclic(100)
print(pattern)

print(hexdump(read('/dev/urandom', 64)))

