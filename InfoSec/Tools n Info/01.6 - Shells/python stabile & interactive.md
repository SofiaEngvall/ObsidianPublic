
Stabilize shell and make it interactive
	`python3 -c 'import pty;pty.spawn("/bin/bash")'`
	Ctrl+z
	`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
	`export TERM=xterm`



