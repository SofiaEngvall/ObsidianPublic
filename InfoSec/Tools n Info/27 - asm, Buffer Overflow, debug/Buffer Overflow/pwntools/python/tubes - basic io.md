https://github.com/Gallopsled/pwntools-tutorial/blob/master/tubes.md

```python
from pwn import *

io = process('sh')

io.sendline('echo Hello, world')
io.recvline()
# 'Hello, world\n'
```
### Receiving data

- `recv(n)` - Receive any number of available bytes
- `recvline()` - Receive data until a newline is encountered
- `recvuntil(delim)` - Receive data until a delimiter is found
- `recvregex(pattern)` - Receive data until a regex pattern is satisfied
- `recvrepeat(timeout)` - Keep receiving data until a timeout occurs
- `clean()` - Discard all buffered data

### Sending data

- `send(data)` - Sends data
- `sendline(line)` - Sends data plus a newline

### Manipulating integers

- `pack(int)` - Sends a word-size packed integer
- `unpack()` - Receives and unpacks a word-size integer