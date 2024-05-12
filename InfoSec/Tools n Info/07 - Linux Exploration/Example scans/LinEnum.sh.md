
```sh
user@debian:~/tools/privesc-scripts$ ./LinEnum.sh

#########################################################
# Local Linux Enumeration & Privilege Escalation Script #
#########################################################
# www.rebootuser.com
# version 0.982

[-] Debug Info
[+] Thorough tests = Disabled


Scan started at:
Fri Apr 19 12:24:58 EDT 2024                                                                                                  
                                                                                                                              

### SYSTEM ##############################################
[-] Kernel information:
Linux debian 2.6.32-5-amd64 #1 SMP Tue May 13 16:34:35 UTC 2014 x86_64 GNU/Linux


[-] Kernel information (continued):
Linux version 2.6.32-5-amd64 (Debian 2.6.32-48squeeze6) (jmm@debian.org) (gcc version 4.3.5 (Debian 4.3.5-4) ) #1 SMP Tue May 13 16:34:35 UTC 2014


[-] Hostname:
debian


### USER/GROUP ##########################################
[-] Current user/group info:
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)


[-] Users that have previously logged onto the system:
Username         Port     From             Latest
root             pts/0    192.168.1.2      Sun Aug 25 14:02:49 -0400 2019
user             pts/0    ip-10-18-21-236. Fri Apr 19 08:01:27 -0400 2024


[-] Who else is logged on:
 12:24:58 up  4:41,  1 user,  load average: 0.00, 0.02, 0.04
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
user     pts/0    ip-10-18-21-236. 08:01    2.00s  0.08s  0.00s /bin/bash ./Lin


[-] Group memberships:
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=100(libuuid) gid=101(libuuid) groups=101(libuuid)
uid=101(Debian-exim) gid=103(Debian-exim) groups=103(Debian-exim)
uid=102(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
uid=103(statd) gid=65534(nogroup) groups=65534(nogroup)
uid=104(mysql) gid=106(mysql) groups=106(mysql)


[-] Contents of /etc/passwd:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
sshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin
user:x:1000:1000:user,,,:/home/user:/bin/bash
statd:x:103:65534::/var/lib/nfs:/bin/false
mysql:x:104:106:MySQL Server,,,:/var/lib/mysql:/bin/false


[+] We can read the shadow file!
root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::
daemon:*:17298:0:99999:7:::
bin:*:17298:0:99999:7:::
sys:*:17298:0:99999:7:::
sync:*:17298:0:99999:7:::
games:*:17298:0:99999:7:::
man:*:17298:0:99999:7:::
lp:*:17298:0:99999:7:::
mail:*:17298:0:99999:7:::
news:*:17298:0:99999:7:::
uucp:*:17298:0:99999:7:::
proxy:*:17298:0:99999:7:::
www-data:*:17298:0:99999:7:::
backup:*:17298:0:99999:7:::
list:*:17298:0:99999:7:::
irc:*:17298:0:99999:7:::
gnats:*:17298:0:99999:7:::
nobody:*:17298:0:99999:7:::
libuuid:!:17298:0:99999:7:::
Debian-exim:!:17298:0:99999:7:::
sshd:*:17298:0:99999:7:::
user:$6$M1tQjkeb$M1A/ArH4JeyF1zBJPLQ.TZQR1locUlz0wIZsoY6aDOZRFrYirKDW5IJy32FBGjwYpT2O1zrR2xTROv7wRIkF8.:17298:0:99999:7:::
statd:*:17299:0:99999:7:::
mysql:!:18133:0:99999:7:::


[-] Super user account(s):
root


[+] We can sudo without supplying a password!
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH

User user may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more


[+] Possible sudo pwnage!
/usr/sbin/iftop
/usr/bin/find
/usr/bin/nano
/usr/bin/vim
/usr/bin/man
/usr/bin/awk
/usr/bin/less
/usr/bin/ftp
/usr/bin/nmap
/bin/more


[-] Are permissions on /home directories lax:
total 12K
drwxr-xr-x  3 root root 4.0K May 15  2017 .
drwxr-xr-x 22 root root 4.0K Aug 25  2019 ..
drwxr-xr-x  5 user user 4.0K Apr 19 12:09 user


[-] Root is allowed to login via SSH:
PermitRootLogin yes


### ENVIRONMENTAL #######################################
[-] Environment information:
SHELL=/bin/bash
TERM=xterm-256color
HISTSIZE=1000000
SSH_CLIENT=10.18.21.236 35902 22
SSH_TTY=/dev/pts/0
USER=user
HISTFILESIZE=1000000
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin
MAIL=/var/mail/user
PWD=/home/user/tools/privesc-scripts
LANG=en_US.UTF-8
HOME=/home/user
SHLVL=2
LOGNAME=user
SSH_CONNECTION=10.18.21.236 35902 10.10.221.227 22
/usr/sbin/service=() {  /bin/bash -p
}
_=/usr/bin/env


[-] Path information:
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin
drwxr-xr-x 2 root root   4096 Aug 25  2019 /bin
drwxr-xr-x 2 root root   4096 May 13  2017 /sbin
drwxr-xr-x 2 root root  20480 Apr 19 12:14 /usr/bin
drwxr-xr-x 2 root root   4096 Jun 11  2014 /usr/games
drwxrwsr-x 2 root staff  4096 May 14  2017 /usr/local/bin
drwxrwsr-x 2 root staff  4096 May 12  2017 /usr/local/games
drwxrwsr-x 2 root staff  4096 May 12  2017 /usr/local/sbin
drwxr-xr-x 2 root root   4096 May 15  2020 /usr/sbin


[-] Available shells:
# /etc/shells: valid login shells
/bin/csh
/bin/sh
/usr/bin/es
/usr/bin/ksh
/bin/ksh
/usr/bin/rc
/usr/bin/tcsh
/bin/tcsh
/usr/bin/esh
/bin/dash
/bin/bash
/bin/rbash


[-] Current umask value:
0022
u=rwx,g=rx,o=rx


[-] umask value as specified in /etc/login.defs:
UMASK           022


[-] Password and storage information:
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_WARN_AGE   7


### JOBS/TASKS ##########################################
[-] Cron jobs:
-rw-r--r-- 1 root root  804 May 13  2017 /etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 May 15  2020 .
drwxr-xr-x 67 root root 4096 Apr 19 12:00 ..
-rw-r--r--  1 root root  607 Oct 17  2009 john
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.daily:
total 72
drwxr-xr-x  2 root root  4096 May 13  2017 .
drwxr-xr-x 67 root root  4096 Apr 19 12:00 ..
-rwxr-xr-x  1 root root   633 Jul 28  2015 apache2
-rwxr-xr-x  1 root root 14799 Apr 15  2011 apt
-rwxr-xr-x  1 root root   314 Aug 10  2011 aptitude
-rwxr-xr-x  1 root root   502 Jun 17  2010 bsdmainutils
-rwxr-xr-x  1 root root   256 Jun  5  2014 dpkg
-rwxr-xr-x  1 root root  4109 Oct 25  2012 exim4-base
-rwxr-xr-x  1 root root  2211 Oct 26  2010 locate
-rwxr-xr-x  1 root root    89 Apr 17  2010 logrotate
-rwxr-xr-x  1 root root  1335 Jan  2  2011 man-db
-rwxr-xr-x  1 root root   249 Feb 15  2011 passwd
-rw-r--r--  1 root root   102 Dec 18  2010 .placeholder
-rwxr-xr-x  1 root root  3594 Dec 18  2010 standard

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 May 12  2017 .
drwxr-xr-x 67 root root 4096 Apr 19 12:00 ..
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 May 12  2017 .
drwxr-xr-x 67 root root 4096 Apr 19 12:00 ..
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x  2 root root 4096 May 12  2017 .
drwxr-xr-x 67 root root 4096 Apr 19 12:00 ..
-rwxr-xr-x  1 root root  895 Jan  2  2011 man-db
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder


[-] Crontab contents:
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh


### NETWORKING  ##########################################
[-] Network and IP info:
eth0      Link encap:Ethernet  HWaddr 02:1f:49:0e:72:c1  
          inet addr:10.10.221.227  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::1f:49ff:fe0e:72c1/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:5279 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3779 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:377408 (368.5 KiB)  TX bytes:420008 (410.1 KiB)
          Interrupt:20 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:104 errors:0 dropped:0 overruns:0 frame:0
          TX packets:104 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:8756 (8.5 KiB)  TX bytes:8756 (8.5 KiB)


[-] ARP history:
ip-10-10-0-1.eu-west-1.compute.internal (10.10.0.1) at 02:c8:85:b5:5a:aa [ether] on eth0


[-] Nameserver(s):
nameserver 10.0.0.2


[-] Default route:
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0


[-] Listening TCP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:44301           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:42321           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:45661           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               


[-] Listening UDP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
udp        0      0 0.0.0.0:52024           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:50749           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -               
udp        0      0 0.0.0.0:48869           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:111             0.0.0.0:*                           -               
udp        0      0 127.0.0.1:638           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           -               


### SERVICES #############################################
[-] Running processes:
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   8396   816 ?        Ss   07:43   0:00 init [2]  
root         2  0.0  0.0      0     0 ?        S    07:43   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    07:43   0:00 [migration/0]
root         4  0.0  0.0      0     0 ?        S    07:43   0:00 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S    07:43   0:00 [watchdog/0]
root         6  0.0  0.0      0     0 ?        S    07:43   0:00 [events/0]
root         7  0.0  0.0      0     0 ?        S    07:43   0:00 [cpuset]
root         8  0.0  0.0      0     0 ?        S    07:43   0:00 [khelper]
root         9  0.0  0.0      0     0 ?        S    07:43   0:00 [netns]
root        10  0.0  0.0      0     0 ?        S    07:43   0:00 [async/mgr]
root        11  0.0  0.0      0     0 ?        S    07:43   0:00 [pm]
root        12  0.0  0.0      0     0 ?        S    07:43   0:00 [xenwatch]
root        13  0.0  0.0      0     0 ?        S    07:43   0:00 [xenbus]
root        14  0.0  0.0      0     0 ?        S    07:43   0:00 [sync_supers]
root        15  0.0  0.0      0     0 ?        S    07:43   0:00 [bdi-default]
root        16  0.0  0.0      0     0 ?        S    07:43   0:00 [kintegrityd/0]
root        17  0.0  0.0      0     0 ?        S    07:43   0:00 [kblockd/0]
root        18  0.0  0.0      0     0 ?        S    07:43   0:00 [kacpid]
root        19  0.0  0.0      0     0 ?        S    07:43   0:00 [kacpi_notify]
root        20  0.0  0.0      0     0 ?        S    07:43   0:00 [kacpi_hotplug]
root        21  0.0  0.0      0     0 ?        S    07:43   0:00 [kseriod]
root        23  0.0  0.0      0     0 ?        S    07:43   0:00 [kondemand/0]
root        24  0.0  0.0      0     0 ?        S    07:43   0:00 [khungtaskd]
root        25  0.0  0.0      0     0 ?        S    07:43   0:00 [kswapd0]
root        26  0.0  0.0      0     0 ?        SN   07:43   0:00 [ksmd]
root        27  0.0  0.0      0     0 ?        S    07:43   0:00 [aio/0]
root        28  0.0  0.0      0     0 ?        S    07:43   0:00 [crypto/0]
root       157  0.0  0.0      0     0 ?        S    07:43   0:00 [ata/0]
root       158  0.0  0.0      0     0 ?        S    07:43   0:00 [ata_aux]
root       159  0.0  0.0      0     0 ?        S    07:43   0:00 [scsi_eh_0]
root       160  0.0  0.0      0     0 ?        S    07:43   0:00 [scsi_eh_1]
root       190  0.0  0.0      0     0 ?        S    07:43   0:00 [kjournald]
root       258  0.0  0.0      0     0 ?        S    07:44   0:00 [flush-202:0]
root       260  0.0  0.0  16840   824 ?        S<s  07:44   0:00 udevd --daemon
root       395  0.0  0.0      0     0 ?        S    07:44   0:00 [kpsmoused]
root       944  0.0  0.0  16836   744 ?        S<   07:45   0:00 udevd --daemon
root       945  0.0  0.0  16836   672 ?        S<   07:45   0:00 udevd --daemon
root      1248  0.0  0.0   6796  1020 ?        Ss   07:46   0:00 dhclient -v -pf /var/run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases eth0
daemon    1278  0.0  0.0   8136   620 ?        Ss   07:46   0:00 /sbin/portmap
statd     1310  0.0  0.0  14424   892 ?        Ss   07:46   0:00 /sbin/rpc.statd
root      1313  0.0  0.0      0     0 ?        S    07:46   0:00 [rpciod/0]
root      1315  0.0  0.0      0     0 ?        S<   07:46   0:00 [kslowd000]
root      1316  0.0  0.0      0     0 ?        S<   07:46   0:00 [kslowd001]
root      1317  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsiod]
root      1324  0.0  0.0  27064   592 ?        Ss   07:46   0:00 /usr/sbin/rpc.idmapd
root      1552  0.0  0.1  54336  1688 ?        Sl   07:46   0:00 /usr/sbin/rsyslogd -c4
root      1656  0.0  0.0   3960   644 ?        Ss   07:46   0:00 /usr/sbin/acpid
root      1697  0.0  0.0      0     0 ?        S    07:46   0:00 [lockd]
root      1698  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd4]
root      1699  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1700  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1701  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1702  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1703  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1704  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1705  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1706  0.0  0.0      0     0 ?        S    07:46   0:00 [nfsd]
root      1711  0.0  0.1  18848  1200 ?        Ss   07:46   0:00 /usr/sbin/rpc.mountd --manage-gids
root      1745  0.0  0.2  71424  2888 ?        Ss   07:46   0:00 /usr/sbin/apache2 -k start
www-data  1747  0.0  0.1  71156  1988 ?        S    07:46   0:00 /usr/sbin/apache2 -k start
www-data  1748  0.0  0.3 295124  3388 ?        Sl   07:46   0:00 /usr/sbin/apache2 -k start
www-data  1749  0.0  0.3 295228  3452 ?        Sl   07:46   0:00 /usr/sbin/apache2 -k start
root      1874  0.0  0.1  22468  1068 ?        Ss   07:46   0:00 /usr/sbin/cron
root      1897  0.0  0.1  61864  1312 ?        Ss   07:46   0:00 nginx: master process /usr/sbin/nginx
www-data  1899  0.0  0.1  62232  1844 ?        S    07:46   0:00 nginx: worker process
www-data  1900  0.0  0.1  62232  1844 ?        S    07:46   0:00 nginx: worker process
www-data  1901  0.0  0.2  62232  2196 ?        S    07:46   0:00 nginx: worker process
www-data  1902  0.0  0.1  62232  1824 ?        S    07:46   0:00 nginx: worker process
root      1920  0.0  0.1  49224  1164 ?        Ss   07:46   0:00 /usr/sbin/sshd
root      1935  0.0  0.1   9180  1392 ?        S    07:46   0:00 /bin/sh /usr/bin/mysqld_safe
root      2070  0.0  2.3 163420 24124 ?        Sl   07:46   0:02 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --user=root --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306
root      2071  0.0  0.0   3896   640 ?        S    07:46   0:00 logger -t mysqld -p daemon.error
101       2451  0.0  0.0  32716  1024 ?        Ss   07:46   0:00 /usr/sbin/exim4 -bd -q30m
root      2491  0.0  0.0   5972   636 tty1     Ss+  07:46   0:00 /sbin/getty 38400 tty1
root      2492  0.0  0.0   5972   632 tty2     Ss+  07:46   0:00 /sbin/getty 38400 tty2
root      2493  0.0  0.0   5972   636 tty3     Ss+  07:46   0:00 /sbin/getty 38400 tty3
root      2494  0.0  0.0   5972   632 tty4     Ss+  07:46   0:00 /sbin/getty 38400 tty4
root      2495  0.0  0.0   5972   632 tty5     Ss+  07:46   0:00 /sbin/getty 38400 tty5
root      2496  0.0  0.0   5972   632 tty6     Ss+  07:46   0:00 /sbin/getty 38400 tty6
root      2629  0.0  0.3  70544  3296 ?        Ss   08:01   0:00 sshd: user [priv]
user      2631  0.0  0.1  70544  1656 ?        S    08:01   0:00 sshd: user@pts/0 
user      2632  0.0  0.2  19288  2112 pts/0    Ss   08:01   0:00 -bash
user     29181  0.0  0.1  11224  1944 pts/0    S+   12:24   0:00 /bin/bash ./LinEnum.sh
user     29182  0.5  0.1  11252  1504 pts/0    S+   12:24   0:00 /bin/bash ./LinEnum.sh
user     29183  0.0  0.0   5408   640 pts/0    S+   12:24   0:00 tee -a
user     29408  0.0  0.1  11244  1208 pts/0    S+   12:24   0:00 /bin/bash ./LinEnum.sh
user     29409  0.0  0.1  16380  1184 pts/0    R+   12:24   0:00 ps aux


[-] Process binaries and associated permissions (from above list):
912K -rwxr-xr-x 1 root root 905K Apr 10  2010 /bin/bash
   0 lrwxrwxrwx 1 root root    4 May 14  2017 /bin/sh -> bash
 20K -rwxr-xr-x 2 root root  20K Jan 25  2011 /sbin/getty
 24K -rwxr-xr-x 1 root root  21K Feb 24  2010 /sbin/portmap
 72K -rwxr-xr-x 1 root root  65K Dec 13  2014 /sbin/rpc.statd
 44K -rwxr-xr-x 1 root root  41K May  1  2012 /usr/sbin/acpid
   0 lrwxrwxrwx 1 root root   33 May 13  2017 /usr/sbin/apache2 -> ../lib/apache2/mpm-worker/apache2
 44K -rwxr-xr-x 1 root root  41K Dec 18  2010 /usr/sbin/cron
   0 lrwxrwxrwx 1 root root    4 May 13  2017 /usr/sbin/exim4 -> exim
9.7M -rwxr-xr-x 1 root root 9.7M Oct 21  2014 /usr/sbin/mysqld
 32K -rwxr-xr-x 1 root root  32K Dec 13  2014 /usr/sbin/rpc.idmapd
 92K -rwxr-xr-x 1 root root  88K Dec 13  2014 /usr/sbin/rpc.mountd
328K -rwxr-xr-x 1 root root 321K Nov 30  2010 /usr/sbin/rsyslogd
472K -rwxr-xr-x 1 root root 465K Apr  2  2014 /usr/sbin/sshd


[-] /etc/init.d/ binary permissions:
total 300
drwxr-xr-x  2 root root  4096 Aug 25  2019 .
drwxr-xr-x 67 root root  4096 Apr 19 12:00 ..
-rwxr-xr-x  1 root root  2233 May  1  2012 acpid
-rwxr-xr-x  1 root root  7621 Jul 28  2015 apache2
-rwxr-xr-x  1 root root  2444 Mar 24  2012 bootlogd
-rwxr-xr-x  1 root root  1579 Mar 24  2012 bootlogs
-rwxr-xr-x  1 root root  1381 Mar 24  2012 bootmisc.sh
-rwxr-xr-x  1 root root  3978 Mar 24  2012 checkfs.sh
-rwxr-xr-x  1 root root 10822 Mar 24  2012 checkroot.sh
-rwxr-xr-x  1 root root  1279 Jun 26  2010 console-setup
-rwxr-xr-x  1 root root  3753 Dec 18  2010 cron
-rw-r--r--  1 root root  2067 Aug 25  2019 .depend.boot
-rw-r--r--  1 root root   693 Aug 25  2019 .depend.start
-rw-r--r--  1 root root   796 Aug 25  2019 .depend.stop
-rwxr-xr-x  1 root root  6479 May 15  2017 exim4
-rwxr-xr-x  1 root root  1329 Mar 24  2012 halt
-rwxr-xr-x  1 root root  1423 Mar 24  2012 hostname.sh
-rwxr-xr-x  1 root root  5079 Jan 25  2011 hwclockfirst.sh
-rwxr-xr-x  1 root root  5061 Jan 25  2011 hwclock.sh
-rwxr-xr-x  1 root root  2518 Sep 15  2006 ifupdown
-rwxr-xr-x  1 root root  1047 Sep  6  2009 ifupdown-clean
-rwxr-xr-x  1 root root  7743 Oct 13  2010 kbd
-rwxr-xr-x  1 root root  1486 Jun 26  2010 keyboard-setup
-rwxr-xr-x  1 root root  1293 Mar 24  2012 killprocs
-rwxr-xr-x  1 root root  1334 Oct 30  2011 module-init-tools
-rwxr-xr-x  1 root root   620 Mar 24  2012 mountall-bootclean.sh
-rwxr-xr-x  1 root root  1668 Mar 24  2012 mountall.sh
-rwxr-xr-x  1 root root  1560 Mar 24  2012 mountdevsubfs.sh
-rwxr-xr-x  1 root root  1924 Mar 24  2012 mountkernfs.sh
-rwxr-xr-x  1 root root   628 Mar 24  2012 mountnfs-bootclean.sh
-rwxr-xr-x  1 root root  2330 Mar 24  2012 mountnfs.sh
-rwxr-xr-x  1 root root  1315 Mar 24  2012 mountoverflowtmp
-rwxr-xr-x  1 root root  3649 Mar 24  2012 mtab.sh
-rwxr-xr-x  1 root root  5437 Oct 21  2014 mysql
-rwxr-xr-x  1 root root  2451 Apr 18  2010 networking
-rwxr-xr-x  1 root root  6013 Dec 13  2014 nfs-common
-rwxr-xr-x  1 root root  4526 Dec 13  2014 nfs-kernel-server
-rwxr-xr-x  1 root root  4766 Jun  7  2016 nginx
-rwxr-xr-x  1 root root  2192 Feb 24  2010 portmap
-rwxr-xr-x  1 root root  1298 Jan 31  2010 procps
-rwxr-xr-x  1 root root  8635 Mar 24  2012 rc
-rwxr-xrwx  1 root root   801 May 14  2017 rc.local
-rwxr-xr-x  1 root root   117 Mar 24  2012 rcS
-rw-r--r--  1 root root  2427 Mar 24  2012 README
-rwxr-xr-x  1 root root   639 Mar 24  2012 reboot
-rwxr-xr-x  1 root root  1074 Mar 24  2012 rmnologin
-rwxr-xr-x  1 root root  3080 Nov 30  2010 rsyslog
-rwxr-xr-x  1 root root  3286 Mar 24  2012 sendsigs
-rwxr-xr-x  1 root root   590 Mar 24  2012 single
-rw-r--r--  1 root root  4304 Mar 24  2012 skeleton
-rwxr-xr-x  1 root root  3704 Apr  2  2014 ssh
-rwxr-xr-x  1 root root   567 Mar 24  2012 stop-bootlogd
-rwxr-xr-x  1 root root  1143 Mar 24  2012 stop-bootlogd-single
-rwxr-xr-x  1 root root   551 Jan  5  2016 sudo
-rwxr-xr-x  1 root root  7578 Dec 12  2010 udev
-rwxr-xr-x  1 root root  1153 Dec 12  2010 udev-mtab
-rwxr-xr-x  1 root root  2869 Mar 24  2012 umountfs
-rwxr-xr-x  1 root root  2143 Mar 24  2012 umountnfs.sh
-rwxr-xr-x  1 root root  1456 Mar 24  2012 umountroot
-rwxr-xr-x  1 root root  1985 Mar 24  2012 urandom


[-] /lib/systemd/* config file permissions:
/lib/systemd/:
total 4.0K
drwxr-xr-x 2 root root 4.0K May 14  2017 system

/lib/systemd/system:
total 4.0K
-rw-r--r-- 1 root root 986 Jun  7  2016 nginx.service


### SOFTWARE #############################################
[-] Sudo version:
Sudo version 1.7.4p4


[-] MYSQL version:
mysql  Ver 14.14 Distrib 5.1.73, for debian-linux-gnu (x86_64) using readline 6.1


[+] We can connect to the local MYSQL service as 'root' and without a password!
mysqladmin  Ver 8.42 Distrib 5.1.73, for debian-linux-gnu on x86_64
Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version          5.1.73-1+deb6u1
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 4 hours 38 min 27 sec

Threads: 1  Questions: 100  Slow queries: 0  Opens: 99  Flush tables: 1  Open tables: 23  Queries per second avg: 0.5


[-] Apache version:
Server version: Apache/2.2.16 (Debian)
Server built:   Jul 28 2015 09:24:24


[-] Apache user configuration:
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data


[-] Installed Apache modules:
Loaded Modules:
 core_module (static)
 log_config_module (static)
 logio_module (static)
 mpm_worker_module (static)
 http_module (static)
 so_module (static)
 alias_module (shared)
 auth_basic_module (shared)
 authn_file_module (shared)
 authz_default_module (shared)
 authz_groupfile_module (shared)
 authz_host_module (shared)
 authz_user_module (shared)
 autoindex_module (shared)
 cgid_module (shared)
 deflate_module (shared)
 dir_module (shared)
 env_module (shared)
 mime_module (shared)
 negotiation_module (shared)
 reqtimeout_module (shared)
 setenvif_module (shared)
 status_module (shared)


### INTERESTING FILES ####################################
[-] Useful file locations:
/bin/nc
/bin/netcat
/usr/bin/wget
/usr/bin/nmap
/usr/bin/gcc


[-] Installed compilers:
ii  g++                                 4:4.4.5-1                    The GNU C++ compiler
ii  g++-4.4                             4.4.5-8                      The GNU C++ compiler
ii  gcc                                 4:4.4.5-1                    The GNU C compiler
ii  gcc-4.4                             4.4.5-8                      The GNU C compiler


[-] Can we read/write sensitive files:
-rw-r--rw- 1 root root 1009 Aug 25  2019 /etc/passwd
-rw-r--r-- 1 root root 572 Aug 25  2019 /etc/group
-rw-r--r-- 1 root root 823 Aug  6  2010 /etc/profile
-rw-r--rw- 1 root shadow 837 Aug 25  2019 /etc/shadow


[-] SUID files:
-rwsr-xr-x 1 root root 37552 Feb 15  2011 /usr/bin/chsh
-rwsr-xr-x 2 root root 168136 Jan  5  2016 /usr/bin/sudo
-rwsr-xr-x 1 root root 32808 Feb 15  2011 /usr/bin/newgrp
-rwsr-xr-x 2 root root 168136 Jan  5  2016 /usr/bin/sudoedit
-rwsr-xr-x 1 root root 60208 Feb 15  2011 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 39856 Feb 15  2011 /usr/bin/chfn
-rwsr-sr-x 1 root staff 9861 May 14  2017 /usr/local/bin/suid-so
-rwsr-sr-x 1 root staff 6883 May 14  2017 /usr/local/bin/suid-env
-rwsr-sr-x 1 root staff 6899 May 14  2017 /usr/local/bin/suid-env2
-rwsr-xr-x 1 root root 963691 May 13  2017 /usr/sbin/exim-4.84-3
-rwsr-xr-x 1 root root 6776 Dec 19  2010 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 212128 Apr  2  2014 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10592 Feb 15  2016 /usr/lib/pt_chown
-rwsr-xr-x 1 root root 36640 Oct 14  2010 /bin/ping6
-rwsr-xr-x 1 root root 34248 Oct 14  2010 /bin/ping
-rwsr-xr-x 1 root root 78616 Jan 25  2011 /bin/mount
-rwsr-xr-x 1 root root 34024 Feb 15  2011 /bin/su
-rwsr-xr-x 1 root root 53648 Jan 25  2011 /bin/umount
-rwsr-sr-x 1 root root 132 Apr 19 11:37 /tmp/shell.elf
-rwsr-xr-x 1 root root 94992 Dec 13  2014 /sbin/mount.nfs


[+] Possibly interesting SUID files:
-rwsr-sr-x 1 root staff 6883 May 14  2017 /usr/local/bin/suid-env


[-] SGID files:
-rwxr-sr-x 1 root shadow 19528 Feb 15  2011 /usr/bin/expiry
-rwxr-sr-x 1 root ssh 108600 Apr  2  2014 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 11000 Jun 17  2010 /usr/bin/bsd-write
-rwxr-sr-x 1 root crontab 35040 Dec 18  2010 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 56976 Feb 15  2011 /usr/bin/chage
-rwxr-sr-x 1 root tty 12000 Jan 25  2011 /usr/bin/wall
-rwsr-sr-x 1 root staff 9861 May 14  2017 /usr/local/bin/suid-so
-rwsr-sr-x 1 root staff 6883 May 14  2017 /usr/local/bin/suid-env
-rwsr-sr-x 1 root staff 6899 May 14  2017 /usr/local/bin/suid-env2
-rwsr-sr-x 1 root root 132 Apr 19 11:37 /tmp/shell.elf
-rwxr-sr-x 1 root shadow 31864 Oct 17  2011 /sbin/unix_chkpwd


[+] Possibly interesting SGID files:
-rwsr-sr-x 1 root staff 6883 May 14  2017 /usr/local/bin/suid-env


[-] NFS config details: 
-rw-r--rw- 1 root root 492 May 14  2017 /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#

/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)

#/tmp *(rw,sync,insecure,no_subtree_check)


[-] Can't search *.conf files as no keyword was entered

[-] Can't search *.php files as no keyword was entered

[-] Can't search *.log files as no keyword was entered

[-] Can't search *.ini files as no keyword was entered

[-] All *.conf files in /etc (recursive 1 level):
-rw-r--r-- 1 root root 88 Apr 19 12:00 /etc/resolv.conf
-rw-r--r-- 1 root root 1260 May 30  2008 /etc/ucf.conf
-rw-r--r-- 1 root root 9 Aug  7  2006 /etc/host.conf
-rw-r--r-- 1 root root 2940 Jun  6  2012 /etc/gai.conf
-rw-r--r-- 1 root root 2969 Jan 30  2011 /etc/debconf.conf
-rw-r--r-- 1 root root 599 Feb 19  2009 /etc/logrotate.conf
-rw-r--r-- 1 root root 475 Aug 28  2006 /etc/nsswitch.conf
-rw-r--r-- 1 root root 899 Aug 31  2009 /etc/gssapi_mech.conf
-rw-r--r-- 1 root root 882 May  7  2010 /etc/insserv.conf
-rw-r--r-- 1 root root 2981 May 12  2017 /etc/adduser.conf
-rw-r--r-- 1 root root 2572 Nov 30  2010 /etc/rsyslog.conf
-rw-r--r-- 1 root root 34 May 12  2017 /etc/ld.so.conf
-rw-r--r-- 1 root root 36870 May 15  2017 /etc/exim.conf
-rw-r--r-- 1 root root 145 Aug 25  2010 /etc/idmapd.conf
-rw-r--r-- 1 root root 600 Nov 21  2010 /etc/deluser.conf
-rw-r--r-- 1 root root 2082 Feb 24  2010 /etc/sysctl.conf
-rw-r--r-- 1 root root 801 Jun 19  2011 /etc/mke2fs.conf
-rw-r--r-- 1 root root 144 May 12  2017 /etc/kernel-img.conf
-rw-r--r-- 1 root root 552 Oct 17  2011 /etc/pam.conf
-rw-r--r-- 1 root root 15752 Jul 25  2009 /etc/ltrace.conf


[-] Current user's history files:
-rw------- 1 user user 210 Apr 19 11:39 /home/user/.bash_history
-rw------- 1 user user  11 May 15  2020 /home/user/.nano_history


[-] Location and contents (if accessible) of .bash_history file(s):
/home/user/.bash_history
ls -al
cat .bash_history 
ls -al
mysql -h somehost.local -uroot -ppassword123
exit
cd /tmp
clear
ifconfig
netstat -antp
nano myvpn.ovpn 
ls
exit
whoami
exit
ext
exit
whoami
exit
rm /tmp/mybash
exit
whoami
exit


[-] Location and Permissions (if accessible) of .bak file(s):
-rw------- 1 root root 1009 Aug 25  2019 /var/backups/passwd.bak
-rw------- 1 root shadow 478 Aug 25  2019 /var/backups/gshadow.bak
-rw------- 1 root shadow 837 Aug 25  2019 /var/backups/shadow.bak
-rw------- 1 root root 572 Aug 25  2019 /var/backups/group.bak


[-] Any interesting mail in /var/mail:
total 8
drwxrwsr-x  2 root mail 4096 May 12  2017 .
drwxr-xr-x 14 root root 4096 May 13  2017 ..


### SCAN COMPLETE ####################################

```
