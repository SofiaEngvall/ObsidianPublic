
Stabilize shell and make it interactive
	`python3 -c 'import pty;pty.spawn("/bin/bash")'`
	Ctrl+z
	`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
	`export TERM=xterm`

User info
	`id`
	`whoami`

Machine
	`cat /etc/os-release`
	`uname -a`

File system
	ls -la for files in ~
	interesting files?
	check history file
	check /opt
	check logs in /var/logs
	are there email? how to find?
	is `/etc/shadow` readable/writeable
	is `/etc/passwd` writeable

Permission info
	`sudo -l`
	Find SUID binaries
		`find / -perm -u=s -type f 2>/dev/null`
	Find SGID binaries
		`find / -perm -g=s -type f 2>/dev/null`
	Both - test this one more
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`
	Find sticky-bit binaries
		`find / -perm -1000 -type d 2>/dev/null`
	Find writable files
	`find /etc -writable -ls 2>/dev/null`
	Find write exec perm directories
		`find / ` <- find the actual command to put here


find users on machine
	~/ `ls -la ..`
	check permissions on other users directories
	`cat /etc/passwd`

check for ssh keys
	`/home/<user>/.ssh`
	Can we add a user
		[Dirty C0w](https://dirtycow.ninja/) 
		writeable /etc/shadow or /etc/passwd

what processes are running
	`ps aux`
	are we in a docker container? tiny number of processes
	[[pspy]]

What's scheduled
	[[cron - crontab]]
	...

Open ports
	`ss -tlupn`
	`netstat -antplue`
	`netstat -ano`

Use tools
	[[enum4linux|enum4linux]]
	[[linpeas]]

---

Found git repo or web dir on machine
 in dir, do:
 `grep -ri user`
 `grep -ri pass`
 one level?
gre