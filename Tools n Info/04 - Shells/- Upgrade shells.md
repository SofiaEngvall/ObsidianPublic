
`script -qc /bin/bash /dev/null`

`python3 -c 'import pty;pty.spawn("/bin/bash")'`
or `python -c 'import pty;pty.spawn("/bin/bash")'` if ooold python



Ctrl+z
`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
`export TERM=xterm`
