
```sh
user@debian:~/tools/privesc-scripts$ ./linpeas.sh


                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄▄
      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄
  ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
  ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
  ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
  ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
  ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
  ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
  ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
  ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
  ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
  ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
  ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
  ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄ 
             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    linpeas v2.5.6 by carlospolop
                                                                                                                              
ADVISORY: linpeas should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.                                                                                                      
                                                                                                                              
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                      
  RED/YELLOW: 99% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMangeta: Your username


====================================( Basic information )=====================================
OS: Linux version 2.6.32-5-amd64 (Debian 2.6.32-48squeeze6) (jmm@debian.org) (gcc version 4.3.5 (Debian 4.3.5-4) ) #1 SMP Tue May 13 16:34:35 UTC 2014
User & Groups: uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
Hostname: debian
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h) 
[+] nmap is available for network discover & port scanning, you should use it yourself                                        
                                                                                                                              

Caching directories . . . . . . . . . . . . . . . . . . . . DONE
====================================( System Information )====================================                                
[+] Operative system                                                                                                          
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits                                               
Linux version 2.6.32-5-amd64 (Debian 2.6.32-48squeeze6) (jmm@debian.org) (gcc version 4.3.5 (Debian 4.3.5-4) ) #1 SMP Tue May 13 16:34:35 UTC 2014

[+] Sudo version
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version                                                  
Sudo version 1.7.4p4                                                                                                          

[+] PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#usdpath                                                       
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin                                      
New path exported: /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin

[+] Date
Fri Apr 19 12:26:24 EDT 2024                                                                                                  

[+] System stats
Filesystem            Size  Used Avail Use% Mounted on                                                                        
/dev/xvda1             19G  984M   17G   6% /
tmpfs                 501M     0  501M   0% /lib/init/rw
udev                  496M  100K  496M   1% /dev
tmpfs                 501M     0  501M   0% /dev/shm
             total       used       free     shared    buffers     cached
Mem:       1025296     567264     458032          0     388696      69708
-/+ buffers/cache:     108860     916436
Swap:       901112          0     901112

[+] Environment
[i] Any private information inside environment variables?                                                                     
SHELL=/bin/bash                                                                                                               
TERM=xterm-256color
HISTSIZE=0
SSH_CLIENT=10.18.21.236 35902 22
SSH_TTY=/dev/pts/0
USER=user
HISTFILESIZE=0
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin
MAIL=/var/mail/user
LANG=en_US.UTF-8
HOME=/home/user
SHLVL=2
LOGNAME=user
SSH_CONNECTION=10.18.21.236 35902 10.10.221.227 22
HISTFILE=/dev/null
/usr/sbin/service=() {  /bin/bash -p
}
_=/usr/bin/env

[+] Looking for Signature verification failed in dmseg
 Not Found                                                                                                                    
                                                                                                                              
[+] selinux enabled? .............. sestatus Not Found
[+] Printer? ...................... lpstat Not Found                                                                          
[+] Is this a container? .......... No                                                                                        
[+] Is ASLR enabled? .............. Yes                                                                                       


=========================================( Devices )==========================================
[+] Any sd* disk in /dev? (limit 20)                                                                                          
                                                                                                                              
[+] Unmounted file-system?
[i] Check if you can mount umounted devices                                                                                   
proc    /proc   proc    defaults        0 0                                                                                   
UUID=be5bb36f-7bb4-4900-b459-196278f714b6       /       ext3    errors=remount-ro       0 1
UUID=468658fa-a304-4ed0-981a-d725bf98a790       none    swap    sw      0 0
debugfs /sys/kernel/debug/      debugfs defaults        0 0



====================================( Available Software )====================================
[+] Useful software                                                                                                           
/usr/bin/nmap                                                                                                                 
/bin/nc
/usr/bin/ncat
/bin/netcat
/bin/nc.traditional
/usr/bin/wget
/bin/ping
/usr/bin/gcc
/usr/bin/g++
/usr/bin/make
/usr/bin/gdb
/usr/bin/base64
/usr/bin/python2.6
/usr/bin/perl
/usr/bin/sudo

[+] Installed Compiler
ii  g++                                 4:4.4.5-1                    The GNU C++ compiler                                     
ii  g++-4.4                             4.4.5-8                      The GNU C++ compiler
ii  gcc                                 4:4.4.5-1                    The GNU C compiler
ii  gcc-4.4                             4.4.5-8                      The GNU C compiler
/usr/bin/gcc
/usr/bin/g++


================================( Processes, Cron, Services, Timers & Sockets )================================
[+] Cleaned processes                                                                                                         
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes      
101       2451  0.0  0.0  32716  1024 ?        Ss   07:46   0:00 /usr/sbin/exim4 -bd -q30m                                    
daemon    1278  0.0  0.0   8136   620 ?        Ss   07:46   0:00 /sbin/portmap
root      1248  0.0  0.0   6796  1020 ?        Ss   07:46   0:00 dhclient -v -pf /var/run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases eth0
root      1324  0.0  0.0  27064   592 ?        Ss   07:46   0:00 /usr/sbin/rpc.idmapd
root      1552  0.0  0.1  54336  1688 ?        Sl   07:46   0:00 /usr/sbin/rsyslogd -c4
root      1656  0.0  0.0   3960   644 ?        Ss   07:46   0:00 /usr/sbin/acpid
root      1711  0.0  0.1  18848  1200 ?        Ss   07:46   0:00 /usr/sbin/rpc.mountd --manage-gids
root      1745  0.0  0.2  71424  2888 ?        Ss   07:46   0:00 /usr/sbin/apache2 -k start
root      1874  0.0  0.1  22468  1068 ?        Ss   07:46   0:00 /usr/sbin/cron
root      1897  0.0  0.1  61864  1312 ?        Ss   07:46   0:00 nginx: master process /usr/sbin/nginx
root      1920  0.0  0.1  49224  1164 ?        Ss   07:46   0:00 /usr/sbin/sshd
root      1935  0.0  0.1   9180  1392 ?        S    07:46   0:00 /bin/sh /usr/bin/mysqld_safe
root      2070  0.0  2.3 163420 24124 ?        Sl   07:46   0:02 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --user=root --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306                                
root      2071  0.0  0.0   3896   640 ?        S    07:46   0:00 logger -t mysqld -p daemon.error
root      2491  0.0  0.0   5972   636 tty1     Ss+  07:46   0:00 /sbin/getty 38400 tty1
root      2492  0.0  0.0   5972   632 tty2     Ss+  07:46   0:00 /sbin/getty 38400 tty2
root      2493  0.0  0.0   5972   636 tty3     Ss+  07:46   0:00 /sbin/getty 38400 tty3
root      2494  0.0  0.0   5972   632 tty4     Ss+  07:46   0:00 /sbin/getty 38400 tty4
root      2495  0.0  0.0   5972   632 tty5     Ss+  07:46   0:00 /sbin/getty 38400 tty5
root      2496  0.0  0.0   5972   632 tty6     Ss+  07:46   0:00 /sbin/getty 38400 tty6
root       260  0.0  0.0  16840   824 ?        S<s  07:44   0:00 udevd --daemon
root       944  0.0  0.0  16836   744 ?        S<   07:45   0:00 udevd --daemon
root       945  0.0  0.0  16836   672 ?        S<   07:45   0:00 udevd --daemon
statd     1310  0.0  0.0  14424   892 ?        Ss   07:46   0:00 /sbin/rpc.statd
user      2631  0.0  0.1  70544  1668 ?        S    08:01   0:00 sshd: user@pts/0 
user      2632  0.0  0.2  19288  2112 pts/0    Ss   08:01   0:00 -bash
user     29702  4.0  0.2  11596  2256 pts/0    S+   12:26   0:00 /bin/sh ./linpeas.sh
user     30153  0.0  0.1  16380  1180 pts/0    R+   12:26   0:00 ps aux
user     30155  0.0  0.0  59884   812 pts/0    S+   12:26   0:00 sort
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
www-data  1747  0.0  0.1  71156  1988 ?        S    07:46   0:00 /usr/sbin/apache2 -k start
www-data  1748  0.0  0.3 295124  3388 ?        Sl   07:46   0:00 /usr/sbin/apache2 -k start
www-data  1749  0.0  0.3 295228  3452 ?        Sl   07:46   0:00 /usr/sbin/apache2 -k start
www-data  1899  0.0  0.1  62232  1844 ?        S    07:46   0:00 nginx: worker process
www-data  1900  0.0  0.1  62232  1844 ?        S    07:46   0:00 nginx: worker process
www-data  1901  0.0  0.2  62232  2196 ?        S    07:46   0:00 nginx: worker process
www-data  1902  0.0  0.1  62232  1824 ?        S    07:46   0:00 nginx: worker process

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                                     
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

[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-jobs                                                
-rw-r--r-- 1 root root  804 May 13  2017 /etc/crontab                                                                         

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 May 15  2020 .
drwxr-xr-x 67 root root 4096 Apr 19 12:25 ..
-rw-r--r--  1 root root  607 Oct 17  2009 john
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.daily:
total 72
drwxr-xr-x  2 root root  4096 May 13  2017 .
drwxr-xr-x 67 root root  4096 Apr 19 12:25 ..
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
drwxr-xr-x 67 root root 4096 Apr 19 12:25 ..
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 May 12  2017 .
drwxr-xr-x 67 root root 4096 Apr 19 12:25 ..
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x  2 root root 4096 May 12  2017 .
drwxr-xr-x 67 root root 4096 Apr 19 12:25 ..
-rwxr-xr-x  1 root root  895 Jan  2  2011 man-db
-rw-r--r--  1 root root  102 Dec 18  2010 .placeholder

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh


[+] Services
[i] Search for outdated versions                                                                                              
 [ + ]  acpid                                                                                                                 
 [ + ]  apache2
 [ - ]  bootlogd
 [ - ]  bootlogs
 [ - ]  checkroot.sh
 [ - ]  exim4
 [ - ]  hostname.sh
 [ + ]  nfs-common
 [ + ]  nfs-kernel-server
 [ + ]  nginx
 [ + ]  portmap
 [ - ]  rmnologin
 [ + ]  rsyslog
 [ + ]  ssh
 [ - ]  stop-bootlogd
 [ - ]  stop-bootlogd-single
 [ - ]  urandom

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path                                                  
                                                                                                                              
[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services                                                      
You can't write on systemd PATH so I'm not going to list relative paths executed by services                                  

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers                                                        
                                                                                                                              
[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers                                                        
                                                                                                                              
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets                                                       
                                                                                                                              
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets                                                       
                                                                                                                              
[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus                                                         
                                                                                                                              

===================================( Network Information )====================================
[+] Hostname, hosts and DNS                                                                                                   
debian                                                                                                                        
127.0.0.1       localhost
127.0.1.1       debian.localdomain      debian

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
domain eu-west-1.compute.internal
search eu-west-1.compute.internal
nameserver 10.0.0.2
localdomain

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                                                                     
                                                                                                                              
[+] Networks and neighbours
default         0.0.0.0                                                                                                       
loopback        127.0.0.0
link-local      169.254.0.0

eth0      Link encap:Ethernet  HWaddr 02:1f:49:0e:72:c1  
          inet addr:10.10.221.227  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::1f:49ff:fe0e:72c1/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:5445 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3924 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:387614 (378.5 KiB)  TX bytes:506638 (494.7 KiB)
          Interrupt:20 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:104 errors:0 dropped:0 overruns:0 frame:0
          TX packets:104 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:8756 (8.5 KiB)  TX bytes:8756 (8.5 KiB)

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.10.0.0       *               255.255.0.0     U     0      0        0 eth0
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0

[+] Iptables rules
iptables rules Not Found                                                                                                      
                                                                                                                              
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#internal-open-ports                                           
Active Internet connections (servers and established)                                                                         
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
tcp        0   2896 10.10.221.227:22        10.18.21.236:35902      ESTABLISHED -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
udp        0      0 0.0.0.0:52024           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:50749           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -               
udp        0      0 0.0.0.0:48869           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:111             0.0.0.0:*                           -               
udp        0      0 127.0.0.1:638           0.0.0.0:*                           -               
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           -               

[+] Can I sniff with tcpdump?
No                                                                                                                            
                                                                                                                              

====================================( Users Information )=====================================
[+] My user                                                                                                                   
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#groups                                                        
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)                  

[+] Do I have PGP keys?
                                                                                                                              
[+] Clipboard or highlighted text?
xsel and xclip Not Found                                                                                                      
                                                                                                                              
[+] Testing 'sudo -l' without password & /etc/sudoers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands                          
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

[+] Checking /etc/doas.conf
/etc/doas.conf Not Found                                                                                                      
                                                                                                                              
[+] Checking Pkexec policy
                                                                                                                              
[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                                                                                                           
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!                             
                                                                                                                              
[+] Superusers
root:x:0:0:root:/root:/bin/bash                                                                                               

[+] Users with console
backup:x:34:34:backup:/var/backups:/bin/sh                                                                                    
bin:x:2:2:bin:/bin:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
games:x:5:60:games:/usr/games:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
root:x:0:0:root:/root:/bin/bash
sys:x:3:3:sys:/dev:/bin/sh
user:x:1000:1000:user,,,:/home/user:/bin/bash
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                        
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
uid=100(libuuid) gid=101(libuuid) groups=101(libuuid)
uid=101(Debian-exim) gid=103(Debian-exim) groups=103(Debian-exim)
uid=102(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=103(statd) gid=65534(nogroup) groups=65534(nogroup)
uid=104(mysql) gid=106(mysql) groups=106(mysql)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 12:26:24 up  4:42,  1 user,  load average: 0.08, 0.03, 0.04                                                                  
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
user     pts/0    ip-10-18-21-236. 08:01    1.00s  0.15s  0.00s w

[+] Last logons
user     pts/0        ip-10-18-21-236. Fri Apr 19 08:01   still logged in                                                     
reboot   system boot  2.6.32-5-amd64   Fri Apr 19 07:46 - 12:26  (04:39)    
reboot   system boot  2.6.32-5-amd64   Fri May 15 11:32 - 11:35  (00:03)    
user     pts/0        192.168.1.125    Fri May 15 06:41 - 06:41  (00:00)    
user     pts/0        192.168.1.125    Fri May 15 06:39 - 06:41  (00:01)    
user     pts/0        192.168.1.125    Fri May 15 06:39 - 06:39  (00:00)    

wtmp begins Fri May 15 06:39:11 2020

[+] Last time logon each user
Username         Port     From             Latest                                                                             
root             pts/0    192.168.1.2      Sun Aug 25 14:02:49 -0400 2019
user             pts/0    ip-10-18-21-236. Fri Apr 19 08:01:27 -0400 2024

[+] Password policy
PASS_MAX_DAYS   99999                                                                                                         
PASS_MIN_DAYS   0
PASS_WARN_AGE   7


===================================( Software Information )===================================
[+] MySQL version                                                                                                             
mysql  Ver 14.14 Distrib 5.1.73, for debian-linux-gnu (x86_64) using readline 6.1                                             

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No                                                                   
[+] MySQL connection using root/NOPASS ................. Yes                                                                  
[+] Looking for mysql credentials and exec
From '/etc/mysql/my.cnf' Mysql user: user = root                                                                              
Found readable /etc/mysql/my.cnf
[client]
port            = 3306
socket          = /var/run/mysqld/mysqld.sock
[mysqld_safe]
socket          = /var/run/mysqld/mysqld.sock
nice            = 0
[mysqld]
user = root
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
port            = 3306
basedir         = /usr
datadir         = /var/lib/mysql
tmpdir          = /tmp
language        = /usr/share/mysql/english
skip-external-locking
bind-address            = 127.0.0.1
key_buffer              = 16M
max_allowed_packet      = 16M
thread_stack            = 192K
thread_cache_size       = 8
myisam-recover         = BACKUP
query_cache_limit       = 1M
query_cache_size        = 16M
expire_logs_days        = 10
max_binlog_size         = 100M
[mysqldump]
quick
quote-names
max_allowed_packet      = 16M
[mysql]
[isamchk]
key_buffer              = 16M
!includedir /etc/mysql/conf.d/
From '/usr/share/mysql/debian-start.inc.sh' Mysql user:   ret=$( echo "SELECT count(*) FROM mysql.user WHERE user='root' and password='';" | $MYSQL --skip-column-names )

[+] PostgreSQL version and pgadmin credentials
 Not Found                                                                                                                    
                                                                                                                              
[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No                                                      
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No                                                      
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No                                                      
                                                                                                                              
[+] Apache server info
Version: Server version: Apache/2.2.16 (Debian)                                                                               
Server built:   Jul 28 2015 09:24:24

[+] Looking for PHPCookies
 Not Found                                                                                                                    
                                                                                                                              
[+] Looking for Wordpress wp-config.php files
wp-config.php Not Found                                                                                                       
                                                                                                                              
[+] Looking for Drupal settings.php files
/default/settings.php Not Found                                                                                               
                                                                                                                              
[+] Looking for Tomcat users file
tomcat-users.xml Not Found                                                                                                    
                                                                                                                              
[+] Mongo information
 Not Found                                                                                                                    
                                                                                                                              
[+] Looking for supervisord configuration file
supervisord.conf Not Found                                                                                                    
                                                                                                                              
[+] Looking for cesi configuration file
cesi.conf Not Found                                                                                                           
                                                                                                                              
[+] Looking for Rsyncd config file
rsyncd.conf Not Found                                                                                                         
[+] Looking for Hostapd config file                                                                                           
hostapd.conf Not Found                                                                                                        
                                                                                                                              
[+] Looking for wifi conns file
 Not Found                                                                                                                    
                                                                                                                              
[+] Looking for Anaconda-ks config files
anaconda-ks.cfg Not Found                                                                                                     
                                                                                                                              
[+] Looking for .vnc directories and their passwd files
.vnc Not Found                                                                                                                
                                                                                                                              
[+] Looking for ldap directories and their hashes
/etc/ldap                                                                                                                     
The password hash is from the {SSHA} to 'structural'

[+] Looking for .ovpn files and credentials
/home/user/myvpn.ovpn                                                                                                         
auth-user-pass /etc/openvpn/auth.txt

[+] Looking for ssl/ssh files
Port 22                                                                                                                       
PermitRootLogin yes
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
 --> /etc/hosts.allow file found, read the rules:



Looking inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

[+] Looking for unexpected auth lines in /etc/pam.d/sshd
auth       required     pam_env.so # [1]                                                                                      
auth       required     pam_env.so envfile=/etc/default/locale

[+] Looking for Cloud credentials (AWS, Azure, GC)
                                                                                                                              
[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe                        
                                                                                                                              
/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)



[+] Looking for kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt                                         
krb5.conf Not Found                                                                                                           
tickets kerberos Not Found                                                                                                    
klist Not Found                                                                                                               
                                                                                                                              
[+] Looking for Kibana yaml
kibana.yml Not Found                                                                                                          
                                                                                                                              
[+] Looking for Knock configuration
Knock.config Not Found                                                                                                        
                                                                                                                              
[+] Looking for logstash files
 Not Found                                                                                                                    
                                                                                                                              
[+] Looking for elasticsearch files
 Not Found                                                                                                                    
                                                                                                                              
[+] Looking for Vault-ssh files
vault-ssh-helper.hcl Not Found                                                                                                
                                                                                                                              
[+] Looking for AD cached hashes
cached hashes Not Found                                                                                                       
                                                                                                                              
[+] Looking for screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions                                           
screen Not Found                                                                                                              
                                                                                                                              
[+] Looking for tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions                                           
tmux Not Found                                                                                                                
                                                                                                                              
[+] Looking for Couchdb directory
                                                                                                                              
[+] Looking for redis.conf
                                                                                                                              
[+] Looking for dovecot files
dovecot credentials Not Found                                                                                                 
                                                                                                                              
[+] Looking for mosquitto.conf
                                                                                                                              
[+] Looking for neo4j auth file
                                                                                                                              
[+] Looking Cloud-Init conf file
                                                                                                                              
[+] Looking Erlang cookie file
                                                                                                                              

====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms                                                                       
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands                          
/usr/bin/chsh                                                                                                                 
/usr/bin/sudo           --->    /sudo$
/usr/bin/newgrp         --->    HP-UX_10.20
/usr/bin/sudoedit               --->    Sudo/SudoEdit_1.6.9p21/1.7.2p4/(RHEL_5/6/7/Ubuntu)/Sudo<=1.8.14
/usr/bin/gpasswd
/usr/bin/chfn           --->    SuSE_9.3/10
/usr/local/bin/suid-so
/usr/local/bin/suid-env
/usr/local/bin/suid-env2
/usr/sbin/exim-4.84-3
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/pt_chown               --->    GNU_glibc_2.1/2.1.1_-6(08-1999)
/bin/ping6
/bin/ping
/bin/mount              --->    Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/bin/su
/bin/umount             --->    BSD/Linux(08-1996)
/tmp/shell.elf
/sbin/mount.nfs

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands                          
/usr/bin/expiry                                                                                                               
/usr/bin/ssh-agent
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/chage
/usr/bin/wall
/usr/local/bin/suid-so
/usr/local/bin/suid-env
/usr/local/bin/suid-env2
/tmp/shell.elf
/sbin/unix_chkpwd

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d                                              
/usr/local/lib                                                                                                                
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities                                                  
                                                                                                                              
[+] Users with capabilities
/etc/security/capability.conf Not Found                                                                                       
                                                                                                                              
[+] Files with ACLs
files with acls in searched folders Not Found                                                                                 
                                                                                                                              
[+] .sh files in path
/usr/local/bin/overwrite.sh                                                                                                   
/usr/local/bin/compress.sh
/usr/bin/gettext.sh

[+] Unexpected folders in root
/.ssh                                                                                                                         
/selinux

[+] Files (scripts) in /etc/profile.d/
total 8                                                                                                                       
drwxr-xr-x  2 root root 4096 Jun 11  2014 .
drwxr-xr-x 67 root root 4096 Apr 19 12:25 ..

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No                                                                                 
[+] Credentials in fstab/mtab? ........... No                                                                                 
[+] Can I read shadow files? ............. root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::                                                                                       
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
[+] Can I read root folder? .............. No
                                                                                                                              
[+] Looking for root files in home dirs (limit 20)
/home                                                                                                                         

[+] Looking for others files in folders owned by me
                                                                                                                              
[+] Readable files belonging to root and readable by me but not world readable
                                                                                                                              
[+] Modified interesting files in the last 5mins
/var/log/daemon.log                                                                                                           
/var/log/auth.log
/var/log/syslog
/etc/resolv.conf
/tmp/backup.tar.gz
/tmp/useless
/home/user/.gnupg/pubring.gpg
/home/user/.gnupg/gpg.conf
/home/user/.gnupg/trustdb.gpg

[+] Writable log files (logrotten)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation                                        
                                                                                                                              
[+] Files inside /home/user (limit 20)
total 80                                                                                                                      
drwxr-xr-x 6 user user  4096 Apr 19 12:26 .
drwxr-xr-x 3 root root  4096 May 15  2017 ..
-rw------- 1 user user   210 Apr 19 11:39 .bash_history
-rw-r--r-- 1 user user   220 May 12  2017 .bash_logout
-rw-r--r-- 1 user user  3235 May 14  2017 .bashrc
-rwxr-xr-x 1 user user 10278 Apr 19 12:09 c0w
drwx------ 2 user user  4096 Apr 19 12:26 .gnupg
drwxr-xr-x 2 user user  4096 May 13  2017 .irssi
drwx------ 2 user user  4096 May 15  2020 .john
-rw------- 1 user user   137 May 15  2017 .lesshst
-rw-r--r-- 1 user user   212 May 15  2017 myvpn.ovpn
-rw------- 1 user user    11 May 15  2020 .nano_history
-rw-r--r-- 1 user user   725 May 13  2017 .profile
-rwxr-xr-x 1 user user  6697 Apr 19 08:23 service
drwxr-xr-x 8 user user  4096 May 15  2020 tools
-rw------- 1 user user  6334 May 15  2020 .viminfo

[+] Files inside others home (limit 20)
                                                                                                                              
[+] Looking for installed mail applications
exim.conf                                                                                                                     
exim
exim-4.84-3
sendmail

[+] Mails (limit 50)
                                                                                                                              
[+] Backup files?
-rw-r--r-- 1 root root 154727 May 12  2017 /var/lib/aptitude/pkgstates.old                                                    
-rw-r--r-- 1 root root 673 May 14  2017 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 610 May 14  2017 /etc/xml/catalog.old
-rw-r--r-- 1 root root 335 Jul 18  2010 /etc/sgml/catalog.old
-rw-r--r-- 1 root root 99542 Apr 19 12:26 /tmp/backup.tar.gz

[+] Looking for tables inside readable .db/.sqlite files (limit 100)
                                                                                                                              
[+] Web files?(output limit)
/var/www/:                                                                                                                    
total 16K
drwxr-xr-x  3 root root 4.0K May 14  2017 .
drwxr-xr-x 14 root root 4.0K May 13  2017 ..
drwxr-xr-x  2 root root 4.0K May 14  2017 html
-rw-r--r--  1 root root  177 May 13  2017 index.html

/var/www/html:
total 12K
drwxr-xr-x 2 root root 4.0K May 14  2017 .

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml                                                            
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                           
-rw-r--r-- 1 root root 0 May 13  2017 /etc/apache2/httpd.conf                                                                 
Reading /etc/apache2/httpd.conf
                                                                                                                              
-rw-r--r-- 1 root root 1657 Apr 10  2010 /etc/bash.bashrc
-rw-r--r-- 1 root root 3184 Apr 10  2010 /etc/skel/.bashrc
-rw-r--r-- 1 root root 675 Apr 10  2010 /etc/skel/.profile
lrwxrwxrwx 1 root root 33 May 14  2017 /etc/systemd/system/multi-user.target.wants/nginx.service -> /lib/systemd/system/nginx.service
-rw------- 1 user user 210 Apr 19 11:39 /home/user/.bash_history
Looking for possible passwords inside /home/user/.bash_history
mysql -h somehost.local -uroot -ppassword123                                                                                  

-rw-r--r-- 1 user user 3235 May 14  2017 /home/user/.bashrc
-rw------- 1 user user 11 May 15  2020 /home/user/.nano_history
Looking for possible passwords inside /home/user/.nano_history
                                                                                                                              
-rw-r--r-- 1 user user 725 May 13  2017 /home/user/.profile
-rwxr-xr-x 1 root root 2493 Jul 18  2010 /usr/bin/lft.db
-rw-r--r-- 1 root root 570 Jan 31  2010 /usr/share/base-files/dot.bashrc
-rw-r--r-- 1 root root 870 Nov 21  2010 /usr/share/doc/adduser/examples/adduser.local.conf.examples/bash.bashrc
-rw-r--r-- 1 root root 1865 Nov 21  2010 /usr/share/doc/adduser/examples/adduser.local.conf.examples/skel/dot.bashrc

[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw------- 1 root root 0 Apr 19 07:46 /var/lib/nfs/.xtab.lock                                                                 
-rw------- 1 root root 0 May 15  2020 /var/lib/nfs/.etab.lock
-rw------- 1 root root 0 Apr 19 11:33 /var/lib/nfs/.rmtab.lock
-rw-r--r-- 1 root root 220 Apr 10  2010 /etc/skel/.bash_logout
-rw------- 1 root root 0 May 12  2017 /etc/.pwd.lock
-rw-r--r-- 1 root root 0 Apr 19 07:43 /lib/init/rw/.ramfs
-rw------- 1 user user 137 May 15  2017 /home/user/.lesshst
-rw------- 1 user user 6334 May 15  2020 /home/user/.viminfo
-rw-r--r-- 1 user user 220 May 12  2017 /home/user/.bash_logout
-rw-r--r-- 1 root root 0 Apr 19 07:43 /dev/.initramfs-tools
-rw------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.getfs
-rw------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.getfd
--w------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.unexport
--w------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.export
--w------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.del
--w------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.add
--w------- 1 root root 0 Apr 19 07:46 /proc/fs/nfsd/.svc

[+] Readable files inside /tmp, /var/tmp, /var/backups(limit 70)
-rw-r--r-- 1 root root 99542 Apr 19 12:26 /tmp/backup.tar.gz                                                                  
-rw-r--r-- 1 root root 29 Apr 19 12:26 /tmp/useless
-rwsr-sr-x 1 root root 132 Apr 19 11:37 /tmp/shell.elf
-rw-r--r-- 1 root root 243 May 12  2017 /var/backups/apt.extended_states.3.gz
-rw-r--r-- 1 root root 254113 May 15  2020 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 154661 May 12  2017 /var/backups/aptitude.pkgstates.0
-rw-r--r-- 1 root root 627 May 15  2017 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 48531 May 12  2017 /var/backups/dpkg.status.3.gz
-rw-r--r-- 1 root root 74780 May 15  2017 /var/backups/dpkg.status.1.gz
-rw-r--r-- 1 root root 5266 May 15  2020 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 558 May 13  2017 /var/backups/apt.extended_states.2.gz
-rw-r--r-- 1 root root 68660 May 13  2017 /var/backups/dpkg.status.2.gz

[+] Interesting writable files owned by me or writable by everyone (not in Home)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files                                                
/dev/shm                                                                                                                      
/etc/exports
/etc/init.d/rc.local
/etc/passwd
/etc/shadow
/home/user
/tmp
/usr/bin/passwd
/usr/local/bin/overwrite.sh
/var/lock
/var/tmp

[+] Interesting GROUP writable files (not in Home)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files                                                
  Group user:                                                                                                                 
  Group cdrom:                                                                                                                
  Group floppy:                                                                                                               
  Group audio:                                                                                                                
  Group dip:                                                                                                                  
  Group video:                                                                                                                
  Group plugdev:                                                                                                              
                                                                                                                              
[+] Searching passwords in config PHP files
                                                                                                                              
[+] Finding IPs inside logs (limit 70)
     77 /var/log/dpkg.log.1:1.7.3.1                                                                                           
     37 /var/log/dpkg.log.1:1.5.36.1
     29 /var/log/dpkg.log.1:4.1.4.2
     19 /var/log/dpkg.log.1:1.2.3.4
      9 /var/log/dpkg.log.1:2.2.4.2
      8 /var/log/wtmp.1:192.168.1.2
      3 /var/log/wtmp:192.168.1.125
      3 /var/log/wtmp.1:172.16.51.1
      2 /var/log/installer/status:1.2.3.3
      1 /var/log/wtmp.1:192.168.1.125
      1 /var/log/wtmp.1:172.16.70.1
      1 /var/log/lastlog:192.168.1.2
      1 /var/log/installer/status:1.2.3.4

[+] Finding passwords inside logs (limit 70)
/var/log/dpkg.log.1:2017-05-12 07:02:29 configure base-passwd 3.5.22 3.5.22                                                   
/var/log/dpkg.log.1:2017-05-12 07:02:29 install base-passwd <none> 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:29 status half-configured base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:29 status half-installed base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:29 status installed base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:29 status unpacked base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:32 install passwd <none> 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:32 status half-configured base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:32 status half-installed base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:32 status half-installed passwd 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:32 status unpacked base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:32 status unpacked passwd 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:32 upgrade base-passwd 3.5.22 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:34 configure base-passwd 3.5.22 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:34 status half-configured base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:34 status installed base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:34 status unpacked base-passwd 3.5.22
/var/log/dpkg.log.1:2017-05-12 07:02:35 configure passwd 1:4.1.4.2+svn3283-2+squeeze1 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:35 status half-configured passwd 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:35 status installed passwd 1:4.1.4.2+svn3283-2+squeeze1
/var/log/dpkg.log.1:2017-05-12 07:02:35 status unpacked passwd 1:4.1.4.2+svn3283-2+squeeze1
/var/log/installer/status:Description: Set up users and passwords

[+] Finding emails inside logs (limit 70)
     62 /var/log/installer/status:debian-boot@lists.debian.org                                                                
      2 /var/log/installer/status:pkg-lvm-maintainers@lists.alioth.debian.org
      1 /var/log/installer/status:xfs@oss.sgi.com
      1 /var/log/installer/status:tytso@mit.edu
      1 /var/log/installer/status:racke@linuxia.de
      1 /var/log/installer/status:pkg-mdadm-devel@lists.alioth.debian.org
      1 /var/log/installer/status:pkg-gnupg-maint@lists.alioth.debian.org
      1 /var/log/installer/status:parted-maintainers@lists.alioth.debian.org
      1 /var/log/installer/status:packages@release.debian.org
      1 /var/log/installer/status:lamont@debian.org
      1 /var/log/installer/status:guus@debian.org
      1 /var/log/installer/status:ender@debian.org
      1 /var/log/installer/status:djpig@debian.org
      1 /var/log/installer/status:debian-glibc@lists.debian.org
      1 /var/log/installer/status:debian-bsd@lists.debian.org
      1 /var/log/installer/status:daniel@lists.debian-maintainers.org
      1 /var/log/installer/status:anibal@debian.org

[+] Finding *password* or *credential* files in home (limit 70)
                                                                                                                              
[+] Finding 'pwd' or 'passw' variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/exim4/conf.d/auth/30_exim4-config_examples:PASSWDLINE=${sg{\                                                             
/etc/exim4/conf.d/auth/30_exim4-config_examples:                    ^${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}"
/etc/exim4/conf.d/auth/30_exim4-config_examples:                     ^${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}\
/etc/exim4/conf.d/auth/30_exim4-config_examples:                 ; ${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}"
/etc/exim4/exim4.conf.template:PASSWDLINE=${sg{\
/etc/exim4/exim4.conf.template:             ^${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}"
/etc/exim4/exim4.conf.template:              ^${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}\
/etc/exim4/exim4.conf.template:          ; ${sg{PASSWDLINE}{\\N([^:]+:)(.*)\\N}{\\$2}}"
/etc/nsswitch.conf:passwd:         compat
/etc/pam.d/common-password:password     [success=1 default=ignore]      pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword          = A challenge password
/etc/ssl/openssl.cnf:challengePassword_max              = 20
/etc/ssl/openssl.cnf:challengePassword_min              = 4
/home/user/tools/mysql-udf/raptor_udf2.c: * Enter password:
/home/user/tools/privesc-scripts/LinEnum.sh:  echo -e "\e[00;31m[-] Contents of /etc/passwd:\e[00m\n$readpasswd" 
/home/user/tools/privesc-scripts/LinEnum.sh:  echo -e "\e[00;31m[-] Password and storage information:\e[00m\n$logindefs" 
/home/user/tools/privesc-scripts/LinEnum.sh:    echo -e "\e[00;33m[-] htpasswd found - could contain passwords:\e[00m\n$htpasswd"                                                                                                                           
/home/user/tools/privesc-scripts/LinEnum.sh:hashesinpasswd=`grep -v '^[^:]*:[x]' /etc/passwd 2>/dev/null`
/home/user/tools/privesc-scripts/LinEnum.sh:htpasswd=`find / -name .htpasswd -print -exec cat {} \; 2>/dev/null`
/home/user/tools/privesc-scripts/LinEnum.sh:readmasterpasswd=`cat /etc/master.passwd 2>/dev/null`
/home/user/tools/privesc-scripts/LinEnum.sh:readpasswd=`cat /etc/passwd 2>/dev/null`
/home/user/tools/privesc-scripts/linpeas.sh:    echo "  You can login as $USER using password: $PASSWORDTRY" | sed "s,.*,${C}[1;31;103m&${C}[0m,"
/home/user/tools/privesc-scripts/linpeas.sh:  FIND_PASSWORD_RELEVANT_NAMES=$(prep_to_find "$PASSWORD_RELEVANT_NAMES")
/home/user/tools/privesc-scripts/linpeas.sh:  PASSWORD_RELEVANT_NAMES="*password* *credential* creds*"
/home/user/tools/privesc-scripts/linpeas.sh:  PASSWORDTRY=$2
/home/user/tools/privesc-scripts/linpeas.sh:      SHELLUSERS=`cat /etc/passwd 2>/dev/null | grep -i "sh$" | cut -d ":" -f 1`
/home/user/tools/privesc-scripts/lse.sh:  cecho "${lblue}    Password:${reset} "
/home/user/tools/privesc-scripts/lse.sh:    'for u in $(cut -d: -f1 /etc/passwd); do [ $(id -u $u) = 0 ] && echo $u; done | grep -v root'
/home/user/tools/privesc-scripts/lse.sh:    'for u in $(cut -d: -f 1 /etc/passwd); do [ "$u" != "$lse_user" ] && crontab -l -u "$u"; done'
/home/user/tools/privesc-scripts/lse.sh:    'grep -E "(user|username|login|pass|password|pw|credentials)[=:]" /etc/fstab /etc/mtab'
/home/user/tools/privesc-scripts/lse.sh:[ -z "$lse_home" ] && lse_home="`(grep -E "^$lse_user:" /etc/passwd | cut -d: -f6)2>/dev/null`"
/var/backups/dpkg.status.0:Depends: libc6 (>= 2.3), libpopt0 (>= 1.15), libselinux1 (>= 1.32), cron | anacron | fcron, base-passwd (>= 2.0.3.4)                                                                                                             
/var/backups/dpkg.status.0:Depends: passwd, libc6 (>= 2.3)
/var/backups/dpkg.status.0:Depends: perl-base (>= 5.6.0), passwd (>= 1:4.0.12), debconf | debconf-2.0

[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/exim4/conf.d/auth/30_exim4-config_examples:  client_secret = ${extract{2}{:}{${lookup{$host}nwildlsearch{CONFDIR/passwd.client}{$value}fail}}}
/etc/exim4/exim4.conf.template:  client_secret = ${extract{2}{:}{${lookup{$host}nwildlsearch{CONFDIR/passwd.client}{$value}fail}}}

[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/home/user/tools/privesc-scripts/lse.sh:    'grep -E "(user|username|login|pass|password|pw|credentials)[=:]" /etc/fstab /etc/mtab'

[+] Looking for specific hashes inside files - less false positives (limit 70)

```

