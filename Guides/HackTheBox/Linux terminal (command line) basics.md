
##### Listing files and directories

`ls` lists files and directories
`ls -la` list all files and directories, including hidden files and all details
`ls -R` list all files recursively

##### Checking and moving between directories

`cd name` moves into directory `name`
`cd ..` moves out of a directory

`pwd` shows your current directory

`mkdir dirname` make a directory called `dirname`

`rm filename` removes the file `filename`
`rm r dirname` removes a directory called `dirname` and it's contents

##### Copying and moving files

`cp file1 file2` makes a copy of `file1` called `file2`
`cp file1 newdir/file1` makes a copy of `file1` in the directory `newdir` (which must exist)
`cp -r mydir .` copy the contents of the directory `mydir` to the current directory

`mv file1 file2` renames `file1` to `file2`
`mv file1 mydir` moves `file1` into `mydir`
`mv /tmp/file1 .` moves `file1` from `/tmp` to the current directory (.)

##### Making and editing files

`touch myfile` creates an empty file `myfile`

`nano myfile` opens the file `myfile` in the text editor `nano`
	save with `Ctrl+S` (if the file doesn't exist it is created when you save)
	exit with `Ctrl+X`

`cat myfile` outputs the file contents in the terminal

##### File permissions

All files in Linux have permissions for the file owner, the file group and everybody else. You can see these in a long file listing like "ls -l". The permission list starts with a `-` for a file, `d` for a directory and `l` for a link. The file permissions are represented by  `r` - read, `w` - write, `x` - execute and `s`/`S` that replaces x for the special permissions suid and sgid. More: [[../../Tools n Info/07 - Linux Exploration/SUID & SGID|SUID & SGID]] There is also `t` which is called the sticky bit. [[../../Tools n Info/07 - Linux Exploration/Sticky Bit|Sticky Bit]]

`chmod +x myfile` makes the file `myfile` executable
`chmod 600 mykeyfile` gives only the file owner permissions to the file

`chown user1 file1` sets the owner of `file1` to `user1`
`chgrp group1 file1` sets the group of `file1` to `group1`

`getcap -r / 2>/dev/null` list all files with capability permissions (errors are ignored)

##### Finding files

`find . -name *txt*` finds all files and directories in the current directory (.) with names containing txt
`find / -type f -name flag* 2> /dev/null` finds all files starting with flag anywhere in the filesystem where you have access (ignoring errors)
`find / -perm -u=s -type f -exec ls -la {} \; 2>/dev/null` finds all files with suid permissions and runs ls on them

Lot's of other useful examples in [[../../Tools n Info/07 - Linux Exploration/- start here (linux)|- start here (linux)]] and in [[../../Tools n Info/07 - Linux Exploration/find|find]]

##### Managing processes

`ps -aux` show all running processes

`kill pid` ask the process with number pid to stop
`kill -9 pid` forcefully kill the process with number pid

##### Filtering output data

`grep [options] "password" file1` is used to search for strings or patterns in data
`cat mysecrets | grep -C 3 "pass"` searches the file mysecrets for the string `pass`, including 3 lines before and after every hit in the output

more info: https://www.geeksforgeeks.org/linux-unix/grep-command-in-unixlinux/

##### Getting information about the user, system and network

`id` shows the current users name, id and group membership
`whoami` shows the current users name

`uname -a` get all system information
`cat /proc/version` also shows gcc info

`ip a` get information about network adapters
`netstat -tulpne` list listening (TCP/UDP) connections (remove l for all)
`ss -tulpne`  modern netstat
`lsof -i -P` list open network sockets (TCP/UDP) and the files/processes using them

##### Scanning and connecting to other computers

`nmap 10.10.10.10` scans the 1000 most common ports of the computer with ip address `10.10.10.10`
`nmap -p- -sV -sC -Pn 10.10.10.10` scan all ports, trying to find what's on the ports and doing some checks

`ssh user1@10.10.10.10` connecting to a remote terminal of the computer with ip `10.10.10.10` using the username `user1`
`scp user1@10.10.10.10:/tmp/myfile .` copy the file myfile from the servers /tmp directory to the current directory on the local machine

`nc 10.10.10.10 1234` connect to the computer with ip `10.10.10.10` on port `1234`
`nc -lvnp 1234` listen for a connection on port 1234

##### Running with elevated permissions

`sudo` put in front of a command to run the command with root permissions
Running as root is a permission you need to have. You will have it on your local virtual machine or Pwnbox

`sudo nano /etc/hosts` opens the hosts file for editing (even though we only have read permissions to it)

`sudo -l` list the sudo permissions of the current user

### Hungry for more?

https://www.geeksforgeeks.org/linux-unix/linux-commands-cheat-sheet/ is a nice list of commands. You can click the command names to get details on a specific command. `ls` for example https://www.geeksforgeeks.org/ls-command-in-linux/.

I also have a lot of information under `/Tools n Info/07 - Linux Exploration` and `/Linux/Commands`.

