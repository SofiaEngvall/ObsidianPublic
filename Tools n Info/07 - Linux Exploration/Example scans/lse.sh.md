
```sh
user@debian:~/tools/privesc-scripts$ ./lse.sh
---
If you know the current user password, write it here to check sudo privileges: password321                                    
---
                                                                                                                              
 LSE Version: 2.1                                                                                                             

        User: user
     User ID: 1000
    Password: ******
        Home: /home/user
        Path: /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin
       umask: 0022

    Hostname: debian
       Linux: 2.6.32-5-amd64
Architecture: x86_64

==================================================================( users )=====
[i] usr000 Current user groups............................................. yes!
[*] usr010 Is current user in an administrative group?..................... nope
[*] usr020 Are there other users in an administrative groups?.............. nope
[*] usr030 Other users with shell.......................................... yes!
[i] usr040 Environment information......................................... skip
[i] usr050 Groups for other users.......................................... skip                                              
[i] usr060 Other users..................................................... skip                                              
[*] usr070 PATH variables defined inside /etc.............................. yes!                                              
[!] usr080 Is '.' in a PATH variable defined inside /etc?.................. nope
===================================================================( sudo )=====
[!] sud000 Can we sudo without a password?................................. nope
[!] sud010 Can we list sudo commands without a password?................... yes!
---
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
---
[!] sud020 Can we sudo with a password?.................................... nope
[*] sud040 Can we read /etc/sudoers?....................................... nope
[*] sud050 Do we know if any other users used sudo?........................ nope
============================================================( file system )=====
[*] fst000 Writable files outside user's home.............................. yes!
[*] fst010 Binaries with setuid bit........................................ yes!
[!] fst020 Uncommon setuid binaries........................................ yes!
---
/usr/sbin/exim-4.84-3
/tmp/shell.elf
---
[!] fst030 Can we write to any setuid binary?.............................. nope
[*] fst040 Binaries with setgid bit........................................ skip
[!] fst050 Uncommon setgid binaries........................................ skip                                              
[!] fst060 Can we write to any setgid binary?.............................. skip                                              
[*] fst070 Can we read /root?.............................................. nope                                              
[*] fst080 Can we read subdirectories under /home?......................... nope
[*] fst090 SSH files in home directories................................... nope
[*] fst100 Useful binaries................................................. yes!
[*] fst110 Other interesting files in home directories..................... nope
[!] fst120 Are there any credentials in fstab/mtab?........................ nope
[*] fst130 Does 'user' have mail?.......................................... nope
[!] fst140 Can we access other users mail?................................. nope
[*] fst150 Looking for GIT/SVN repositories................................ nope
[!] fst160 Can we write to critical files?................................. yes!
---
-rw-r--rw- 1 root root 1009 Aug 25  2019 /etc/passwd
-rw-r--rw- 1 root shadow 837 Aug 25  2019 /etc/shadow
---
[!] fst170 Can we write to critical directories?........................... nope
[!] fst180 Can we write to directories from PATH defined in /etc?.......... yes!
---
drwxr-xr-x 5 user user 4096 Apr 19 12:09 /home/user
---
[!] fst190 Can we read any backup?......................................... yes!
---
-rw-r--r-- 1 root root 99542 Apr 19 12:16 /tmp/backup.tar.gz
---
[i] fst500 Files owned by user 'user'...................................... skip
[i] fst510 SSH files anywhere.............................................. skip                                              
[i] fst520 Check hosts.equiv file and its contents......................... skip                                              
[i] fst530 List NFS server shares.......................................... skip                                              
[i] fst540 Dump fstab file................................................. skip                                              
=================================================================( system )=====                                              
[i] sys000 Who is logged in................................................ skip
[i] sys010 Last logged in users............................................ skip                                              
[!] sys020 Does the /etc/passwd have hashes?............................... nope                                              
[!] sys022 Does the /etc/group have hashes?................................ nope
[!] sys030 Can we read /etc/shadow file?................................... yes!
---
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
---
[!] sys030 Can we read /etc/shadow- file?.................................. nope
[!] sys030 Can we read /etc/shadow~ file?.................................. nope
[!] sys030 Can we read /etc/gshadow file?.................................. nope
[!] sys030 Can we read /etc/gshadow- file?................................. nope
[!] sys030 Can we read /etc/master.passwd file?............................ nope
[*] sys040 Check for other superuser accounts.............................. nope
[*] sys050 Can root user log in via SSH?................................... yes!
[i] sys060 List available shells........................................... skip
[i] sys070 System umask in /etc/login.defs................................. skip                                              
[i] sys080 System password policies in /etc/login.defs..................... skip                                              
===============================================================( security )=====                                              
[*] sec000 Is SELinux present?............................................. nope
[*] sec010 List files with capabilities.................................... nope
[!] sec020 Can we write to a binary with caps?............................. nope
[!] sec030 Do we have all caps in any binary?.............................. nope
[*] sec040 Users with associated capabilities.............................. nope
[!] sec050 Does current user have capabilities?............................ skip
========================================================( recurrent tasks )=====                                              
[*] ret000 User crontab.................................................... nope
[!] ret010 Cron tasks writable by user..................................... nope
[*] ret020 Cron jobs....................................................... yes!
[*] ret030 Can we read user crontabs....................................... nope
[*] ret040 Can we list other user cron tasks?.............................. nope
[*] ret050 Can we write to any paths present in cron jobs.................. yes!
[!] ret060 Can we write to executable paths present in cron jobs........... yes!
---
/etc/crontab:PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
---
[i] ret400 Cron files...................................................... skip
[*] ret500 User systemd timers............................................. nope                                              
[!] ret510 Can we write in any system timer?............................... nope
[i] ret900 Systemd timers.................................................. skip
================================================================( network )=====                                              
[*] net000 Services listening only on localhost............................ yes!
[!] net010 Can we sniff traffic with tcpdump?.............................. nope
[i] net500 NIC and IP information.......................................... skip
[i] net510 Routing table................................................... skip                                              
[i] net520 ARP table....................................................... skip                                              
[i] net530 Namerservers.................................................... skip                                              
[i] net540 Systemd Nameservers............................................. skip                                              
[i] net550 Listening TCP................................................... skip                                              
[i] net560 Listening UDP................................................... skip                                              
===============================================================( services )=====                                              
[!] srv000 Can we write in service files?.................................. yes!
---
/etc/init.d/rc.local
---
[!] srv010 Can we write in binaries executed by services?.................. nope
[*] srv020 Files in /etc/init.d/ not belonging to root..................... nope
[*] srv030 Files in /etc/rc.d/init.d not belonging to root................. nope
[*] srv040 Upstart files not belonging to root............................. nope
[*] srv050 Files in /usr/local/etc/rc.d not belonging to root.............. nope
[i] srv400 Contents of /etc/inetd.conf..................................... skip
[i] srv410 Contents of /etc/xinetd.conf.................................... skip                                              
[i] srv420 List /etc/xinetd.d if used...................................... skip                                              
[i] srv430 List /etc/init.d/ permissions................................... skip                                              
[i] srv440 List /etc/rc.d/init.d permissions............................... skip                                              
[i] srv450 List /usr/local/etc/rc.d permissions............................ skip                                              
[i] srv460 List /etc/init/ permissions..................................... skip                                              
[!] srv500 Can we write in systemd service files?.......................... nope                                              
[!] srv510 Can we write in binaries executed by systemd services?.......... nope
[*] srv520 Systemd files not belonging to root............................. nope
[i] srv900 Systemd config files permissions................................ skip
===============================================================( software )=====                                              
[!] sof000 Can we connect to MySQL with root/root credentials?............. nope
[!] sof010 Can we connect to MySQL as root without password?............... yes!
---
mysqladmin  Ver 8.42 Distrib 5.1.73, for debian-linux-gnu on x86_64
Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version          5.1.73-1+deb6u1
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 4 hours 29 min 48 sec

Threads: 1  Questions: 99  Slow queries: 0  Opens: 99  Flush tables: 1  Open tables: 23  Queries per second avg: 0.6
---
[!] sof020 Can we connect to PostgreSQL template0 as postgres and no pass?. nope
[!] sof020 Can we connect to PostgreSQL template1 as postgres and no pass?. nope
[!] sof020 Can we connect to PostgreSQL template0 as psql and no pass?..... nope
[!] sof020 Can we connect to PostgreSQL template1 as psql and no pass?..... nope
[*] sof030 Installed apache modules........................................ yes!
[!] sof040 Found any .htpasswd files?...................................... nope
[i] sof500 Sudo version.................................................... skip
[i] sof510 MySQL version................................................... skip                                              
[i] sof520 Postgres version................................................ skip                                              
[i] sof530 Apache version.................................................. skip                                              
=============================================================( containers )=====                                              
[*] ctn000 Are we in a docker container?................................... nope
[*] ctn010 Is docker available?............................................ nope
[!] ctn020 Is the user a member of the 'docker' group?..................... nope
[*] ctn200 Are we in a lxc container?...................................... nope
[!] ctn210 Is the user a member of any lxc/lxd group?...................... nope
==============================================================( processes )=====
[i] pro000 Waiting for the process monitor to finish....................... yes!
[i] pro001 Retrieving process binaries..................................... yes!
[i] pro002 Retrieving process users........................................ yes!
[!] pro010 Can we write in any process binary?............................. nope
[*] pro020 Processes running with root permissions......................... yes!
[*] pro030 Processes running by non-root users with shell.................. yes!
[i] pro500 Running processes............................................... skip
[i] pro510 Running process binaries and permissions........................ skip                                              
                                                                                                                              
==================================( FINISHED )================================== 
```


