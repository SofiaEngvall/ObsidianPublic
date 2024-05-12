
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

find users on machine
	`cat /etc/passwd` users and might find info on services through their accounts
	~/ `ls -la ..`
	check permissions on other users directories

File system
	ls -la for files in ~
	interesting files?
	check history files `cat ~/.*history`
	are there config files?
	check `/opt`
	check `/var/backup`
	check logs in /var/logs
	are there email? how to find? /var/mail
	is `/etc/shadow` readable/writeable
	is `/etc/passwd` writeable

Permission info
	`sudo -l`
	Find SUID and SGID binaries
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`
	Find sticky-bit directories
		`find / -perm -1000 -type d 2>/dev/null`
	Find writable files
		`find /etc -writable -ls 2>/dev/null`
	Find write exec perm directories
		`find / ` <- find the actual command to put here

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

if we found a git repo or web dir on the machine
 in dir, do:
 `grep -ri user`
 `grep -ri pass`
 one level?
gre