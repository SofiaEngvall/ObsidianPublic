
/etc/passwd file, which stores all users registered on the system.

File System Hierarchy
The Linux operating system is structured in a tree-like hierarchy and is documented in the Filesystem Hierarchy Standard (FHS). Linux is structured with the following standard top-level directories:

Path
Description
/
The top-level directory is the root filesystem and contains all of the files required to boot the operating system before other filesystems are mounted as well as the files required to boot the other filesystems. After boot, all of the other filesystems are mounted at standard mount points as subdirectories of the root.
/bin
Contains essential command binaries.
/boot
Consists of the static bootloader, kernel executable, and files required to boot the Linux OS.
/dev
Contains device files to facilitate access to every hardware device attached to the system.
/etc
Local system configuration files. Configuration files for installed applications may be saved here as well.
/home
Each user on the system has a subdirectory here for storage.
/lib
Shared library files that are required for system boot.
/media
External removable media devices such as USB drives are mounted here.
/mnt
Temporary mount point for regular filesystems.
/opt
Optional files such as third-party tools can be saved here.
/root
The home directory for the root user.
/sbin
This directory contains executables used for system administration (binary system files).
/tmp
The operating system and many programs use this directory to store temporary files. This directory is generally cleared upon system boot and may be deleted at other times without any warning.
/usr
Contains executables, libraries, man files, etc.
/var
This directory contains variable data files such as log files, email in-boxes, web application related files, cron files, and more.




### Useful commands

`man <tool>`
`<tool>  --help`
`<tool> -h`
`apropos <keyword>`

Command     Description
whoami	Displays current username.
id	Returns users identity
hostname	Sets or prints the name of current host system.
uname	Prints basic information about the operating system name and system hardware.
pwd	Returns working directory name.
ifconfig	The ifconfig utility is used to assign or to view an address to a network interface
	and/or configure network interface parameters.
ip	Ip is a utility to show or manipulate routing, network devices, interfaces and tunnels.
netstat	Shows network status.
ss	Another utility to investigate sockets.
ps	Shows process status.
who	Displays who is logged in.
env	Prints environment or sets and executes command.
lsblk	Lists block devices.
lsusb	Lists USB devices
lsof	Lists opened files.
lspci	Lists PCI devices.

`ssh [username]@[IP address]`


### Linux basics by OTW

pwd
whoami

… --help
… -h
… -?
man …

locate …
whereis …
which …
find directory options expression

ps aux
ps aux | grep apache2
cat > mytextfile		write to textfile, end typing with ctrl+D
cat mytextfile		


apt update
apt upgrade
apt  dist-upgrade


### Kali Linux

echo hello > hello.txt (overwrite)
echo hi again >> hello.txt (append)

/tmp/ has full rwx so can be used for dling files and executing them

locate
updatedb (if locate doesn’t work or not updated)

adduser
usermod -a -G mygroup myuser
usermod -a -G sudo sofia

chmod 777
cat /etc/passwd
cat /etc/shadow
cat /etc/group
cat /etc/sudoers

ifconfig
iwconfig (wireless)
ip a

ifconfig eth0 192.168.0.23
ifconfig eth0 192.168.0.23 netmask 255.255.255.0 broadcast 192.168.0.255

arp -a
ip n (neighbor)

route  (check for more than one network/way out)
ip r

netstat -ano

apt update && apt upgrade (does both)

