
make linus password hash (kali)
`mkpasswd -m sha512crypt`

make linux password (some debian box)
`mkpasswd -m sha-512`

### Help (Kali)

```sh
┌──(kali㉿kali)-[~]
└─$ mkpasswd --help 
Usage: mkpasswd [OPTIONS]... [PASSWORD [SALT]]
Crypts the PASSWORD using crypt(3).

      -m, --method=TYPE     select method TYPE
      -5                    like --method=md5crypt
      -S, --salt=SALT       use the specified SALT
      -R, --rounds=NUMBER   use the specified NUMBER of rounds
      -P, --password-fd=NUM read the password from file descriptor NUM
                            instead of /dev/tty
      -s, --stdin           like --password-fd=0
      -h, --help            display this help and exit
      -V, --version         output version information and exit

If PASSWORD is missing then it is asked interactively.
If no SALT is specified, a random one is generated.
If TYPE is 'help', available methods are printed.

Report bugs to <md+whois@linux.it>.
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ mkpasswd -m help
Available methods:
yescrypt        Yescrypt
gost-yescrypt   GOST Yescrypt
scrypt          scrypt
bcrypt          bcrypt
bcrypt-a        bcrypt (obsolete $2a$ version)
sha512crypt     SHA-512
sha256crypt     SHA-256
sunmd5          SunMD5
md5crypt        MD5
bsdicrypt       BSDI extended DES-based crypt(3)
descrypt        standard 56 bit DES-based crypt(3)
nt              NT-Hash
```

### Help (other)

```sh
user@debian:~/tools/mysql-udf$ mkpasswd --help
Usage: mkpasswd [OPTIONS]... [PASSWORD [SALT]]
Crypts the PASSWORD using crypt(3).

      -m, --method=TYPE     select method TYPE
      -5                    like --method=md5
      -S, --salt=SALT       use the specified SALT
      -R, --rounds=NUMBER   use the specified NUMBER of rounds
      -P, --password-fd=NUM read the password from file descriptor NUM
                            instead of /dev/tty
      -s, --stdin           like --password-fd=0
      -h, --help            display this help and exit
      -V, --version         output version information and exit

If PASSWORD is missing then it is asked interactively.
If no SALT is specified, a random one is generated.
If TYPE is 'help', available methods are printed.

Report bugs to <md+whois@linux.it>.
user@debian:~/tools/mysql-udf$ mkpasswd -m help
Available methods:
des     standard 56 bit DES-based crypt(3)
md5     MD5
sha-256 SHA-256
sha-512 SHA-512
```