
short:
id
sudo -l
ls -la /opt
cat /etc/crontab


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
	ls -la for files in `~`
	interesting files?
	check history files `cat ~/.*history`
	are there config files?
	`ls -la /opt`
	`ls -la /var/backup`
	check logs in `/var/log`
	are there email? how to find? `/var/mail`
	is `/etc/shadow` readable/writeable
	is `/etc/passwd` writeable

Permission info
	`sudo -l`
	Find SUID and SGID binaries
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`
	Find sticky-bit directories, missing on tmp? (restricted deletion flag - other users can't overwrite/delete files in the dir)
		`find / -perm -1000 -type d 2>/dev/null`
	Find writable files
		`find /etc -writable -ls 2>/dev/null`
	Find files with permissions for your group (if user has extra groups)
		`find / -type f -group `mygroup` 2>/dev/null`
	Find write exec perm directories
		`find / -type` <- find the actual command to put here

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
	`crontab -l` lists jobs for active user
	`cat /etc/crontab` list system wide jobs
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

search in logfiles and binaries for usernames and passwords
- `strings filename | grep -i -E "user|name|pass" -C5`
- `grep -i -E "user|name|pass" -C5 file1 file2` for text files and logs..

Recursively strings + grep
- `find dirname -type f -exec sh -c 'strings "$1" | grep -i -E "user|name|pass" -C5' sh {} \;`

Recursively strings +/ grep only using strings for binaries
- `find dirname -type f -exec sh -c 'file "{}" | grep -q "text" && grep -i -E "user|name|pass" -C5 "{}" || strings "{}" | grep -i -E "user|name|pass" -C5' \;`

if we found a git repo or web dir on the machine
 in dir, do:
 `grep -ri user`
 `grep -ri pass`
 one level?
gre