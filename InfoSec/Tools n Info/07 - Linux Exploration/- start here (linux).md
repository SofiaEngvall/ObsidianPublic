
short:
id
sudo -l
ls -la /opt
cat /etc/crontab


Start
	`pwd`
	`ls -la`
	`ls -la *` for files in `~`
	check history files `cat ~/.*history`

Stabilize shell and make it interactive
	`python3 -c 'import pty;pty.spawn("/bin/bash")'`
	Ctrl+z
	`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
	`export TERM=xterm`

User info
	`id` privilege level and group memberships
	`whoami`

Machine
	`hostname`
	`cat /etc/os-release`
	`uname -a`
	`cat /proc/version` also gcc info
	`cat /etc/issue`

Other
	`env` show environment variables
	`history`

find users on machine
	`cat /etc/passwd` users and might find info on services through their accounts
	~/ `ls -la ..`
	check permissions on other users directories

File system - interesting files?
	`ls -la /opt`
	`ls -la /var/backup`
	check logs in `/var/log`
	are there email? how to find? `/var/mail` `/var/spool/mail`
	is `/etc/shadow` readable/writeable
	is `/etc/passwd` writeable


Check config files
	`cat /etc/exports` nfs config file

Permission info
	`sudo -l` list all commands your user can run using `sudo`
	Find SUID and SGID binaries
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} + 2> /dev/null|cat`
	Find sticky-bit directories, missing on tmp? (restricted deletion flag - other users can't overwrite/delete files in the dir)
		`find / -perm -1000 -type d 2>/dev/null`
	Find writable files
		`find /etc -writable -ls 2>/dev/null`
	Find files with permissions for your group (if user has extra groups)
		`find / -type f -group `mygroup` 2>/dev/null`
	Find write exec perm directories
		`find / -perm -o x -type d 2>/dev/null`
	Find files with capability "permissions"
		`getcap -r / 2>/dev/null`

check for ssh keys
	`/home/<user>/.ssh`
	Can we add a user
		[Dirty C0w](https://dirtycow.ninja/) 
		writeable /etc/shadow or /etc/passwd

what processes are running
	`ps aux` show processes for all users (a), display user that launched the process (u), show processes not attached to a terminal (x)
	`ps ax` can see long commands
	`ps auxf|cat` can see all the things!!! thanks stderr_dk
	`ps axjf` tree style (f)
	`ps axf`
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

finding files, like flags:
	`find / -type f -name flag2.txt 2> /dev/null

---

search in logfiles and binaries for usernames and passwords
- `strings filename | grep -i -E "user|name|pass" -C5`
- `grep -i -E "user|name|pass" -C5 file1 file2` for text files and logs..

Recursively strings + grep
- `find [dirname] -type f -exec sh -c 'strings "$1" | grep -i -E "user|name|pass" -C5' sh {} \;`

Recursively strings +/ grep only using strings for binaries
- `find [dirname] -type f -exec sh -c 'file "{}" | grep -q "text" && grep -i -E "user|name|pass" -C5 "{}" || strings "{}" | grep -i -E "user|name|pass" -C5' \;`

if we found a git repo or web dir on the machine
 in dir, do:
 `grep -ri user`
 `grep -ri pass`
 one level?

---

network
	`ifconfig` what interfaces exist..
	`ip route` check this with route table


---

Use tools
	[[enum4linux|enum4linux]]
	[[linpeas]] [LinPeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
	[LinEnum](https://github.com/rebootuser/LinEnum)
	[LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
	[Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
	[Linux Priv Checker](https://github.com/linted/linuxprivchecker)

