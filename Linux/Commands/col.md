
outputs a man page like normal text
`man whatever | col -b`

### Help

```sh
┌──(kali㉿kali)-[~/exploits]
└─$ col --help          

Usage:
 col [options]

Filter out reverse line feeds from standard input.

Options:
 -b, --no-backspaces    do not output backspaces
 -f, --fine             permit forward half line feeds
 -p, --pass             pass unknown control sequences
 -h, --tabs             convert spaces to tabs
 -x, --spaces           convert tabs to spaces
 -l, --lines NUM        buffer at least NUM lines
 -H, --help             display this help
 -V, --version          display version

For more details see col(1).
```

 