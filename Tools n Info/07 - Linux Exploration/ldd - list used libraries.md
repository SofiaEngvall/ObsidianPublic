
See which shared libraries are used by a program

`ldd [program]`

`ldd /usr/sbin/apache2`
```sh
┌──(kali㉿kali)-[~]
└─$ ldd /usr/sbin/apache2
        linux-vdso.so.1 (0x00007ffef8922000)
        libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007fc6f7a65000)
        libaprutil-1.so.0 => /lib/x86_64-linux-gnu/libaprutil-1.so.0 (0x00007fc6f7a36000)
        libapr-1.so.0 => /lib/x86_64-linux-gnu/libapr-1.so.0 (0x00007fc6f79f8000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc6f7816000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007fc6f77eb000)
        libcrypt.so.1 => /lib/x86_64-linux-gnu/libcrypt.so.1 (0x00007fc6f77ad000)
        libuuid.so.1 => /lib/x86_64-linux-gnu/libuuid.so.1 (0x00007fc6f77a3000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fc6f7bd0000)
```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ ldd --help           
Usage: ldd [OPTION]... FILE...
      --help              print this help and exit
      --version           print version information and exit
  -d, --data-relocs       process data relocations
  -r, --function-relocs   process data and function relocations
  -u, --unused            print unused direct dependencies
  -v, --verbose           print all information

For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

