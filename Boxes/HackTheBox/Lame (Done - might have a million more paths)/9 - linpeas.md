
```sh
./linpeas.sh


                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
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
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |                        
    |---------------------------------------------------------------------------------|                        
    |         Follow on Twitter         :     @hacktricks_live                        |                        
    |         Respect on HTB            :     SirBroccoli                             |                        
    |---------------------------------------------------------------------------------|                        
    |                                 Thank you!                                      |                        
    \---------------------------------------------------------------------------------/                        
          linpeas-ng by github.com/PEASS-ng                                                                    
                                                                                                               
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                                   
                                                                                                               
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                       
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════                            
                               ╚═══════════════════╝                                                           
OS: Linux version 2.6.24-16-server (buildd@palmer) (gcc version 4.2.3 (Ubuntu 4.2.3-2ubuntu7)) #1 SMP Thu Apr 10 13:58:00 UTC 2008
User & Groups: uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
Hostname: lame
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                           
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                                                                                
                                                                                                               
[+] nmap is available for network discovery & port scanning, you should use it yourself                        
                                                                                                               

Caching directories DONE
                                                                                                               
                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════                             
                              ╚════════════════════╝                                                           
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                             
Linux version 2.6.24-16-server (buildd@palmer) (gcc version 4.2.3 (Ubuntu 4.2.3-2ubuntu7)) #1 SMP Thu Apr 10 13:58:00 UTC 2008
Distributor ID: Ubuntu
Description:    Ubuntu 8.04
Release:        8.04
Codename:       hardy

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                
Sudo version 1.6.9p10                                                                                          


╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                        
/sbin:/bin:/usr/sbin:/usr/bin                                                                                  

╔══════════╣ Date & uptime
Fri May  9 18:43:17 EDT 2025                                                                                   
 18:43:17 up  1:54,  1 user,  load average: 0.26, 0.06, 0.02

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                           
sda
sda1
sda2
sda5

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                      
proc            /proc           proc    defaults        0       0                                              
UUID=59bd36ce-2d78-44fe-843f-a4ca5fcafad1 /               ext3    relatime,errors=remount-ro 0       1
/dev/sda1 /boot           ext3    relatime        0       2
/dev/scd0       /media/cdrom0   udf,iso9660 user,noauto,exec,utf8 0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                        
_DISTCC_SAFEGUARD=1                                                                                            
TERM=linux
HISTSIZE=0
QUIET=
HISTFILESIZE=0
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
runlevel=2
RUNLEVEL=2
UPSTART_EVENT=runlevel
PWD=/tmp
VERBOSE=no
previous=N
PREVLEVEL=N
SHLVL=5
UPSTART_JOB=rc2
UPSTART_JOB_ID=5
HISTFILE=/dev/null
_=/usr/bin/env

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed         
dmesg Not Found                                                                                                
                                                                                                               
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                             
                                                                                                               
╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                        
  [1] american-sign-language                                                                                   
      CVE-2010-4347
      Source: http://www.securityfocus.com/bid/45408
  [2] can_bcm
      CVE-2010-2959
      Source: http://www.exploit-db.com/exploits/14814
  [3] dirty_cow
      CVE-2016-5195
      Source: http://www.exploit-db.com/exploits/40616
  [4] do_pages_move
      Alt: sieve       CVE-2010-0415
      Source: Spenders Enlightenment
  [5] exploit_x
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [6] half_nelson1
      Alt: econet       CVE-2010-3848
      Source: http://www.exploit-db.com/exploits/17787
  [7] half_nelson2
      Alt: econet       CVE-2010-3850
      Source: http://www.exploit-db.com/exploits/17787
  [8] half_nelson3
      Alt: econet       CVE-2010-4073
      Source: http://www.exploit-db.com/exploits/17787
  [9] msr
      CVE-2013-0268
      Source: http://www.exploit-db.com/exploits/27297
  [10] pipe.c_32bit
      CVE-2009-3547
      Source: http://www.securityfocus.com/data/vulnerabilities/exploits/36901-1.c
  [11] pktcdvd
      CVE-2010-3437
      Source: http://www.exploit-db.com/exploits/15150
  [12] reiserfs
      CVE-2010-1146
      Source: http://www.exploit-db.com/exploits/12130
  [13] sock_sendpage
      Alt: wunderbar_emporium       CVE-2009-2692
      Source: http://www.exploit-db.com/exploits/9435
  [14] sock_sendpage2
      Alt: proto_ops       CVE-2009-2692
      Source: http://www.exploit-db.com/exploits/9436
  [15] video4linux
      CVE-2010-3081
      Source: http://www.exploit-db.com/exploits/15024
  [16] vmsplice1
      Alt: jessica biel       CVE-2008-0600
      Source: http://www.exploit-db.com/exploits/5092
  [17] vmsplice2
      Alt: diane_lane       CVE-2008-0600
      Source: http://www.exploit-db.com/exploits/5093


╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.                  
apparmor module is loaded.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found                                                       
═╣ PaX bins present? .............. PaX Not Found                                                              
═╣ Execshield enabled? ............ Execshield Not Found                                                       
═╣ SELinux enabled? ............... sestatus Not Found                                                         
═╣ Seccomp enabled? ............... disabled                                                                   
═╣ User namespace? ................ disabled
═╣ Cgroup2 enabled? ............... disabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... No                                                                         

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                            
                                   ╚═══════════╝                                                               
╔══════════╣ Container related tools present (if any):
╔══════════╣ Am I Containered?                                                                                 
╔══════════╣ Container details                                                                                 
═╣ Is this a container? ........... No                                                                         
═╣ Any running containers? ........ No                                                                         
                                                                                                               

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════                            
                                     ╚═══════╝                                                                 
═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ Aliyun ECS? .......................... No
═╣ Tencent CVM? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No



                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                             
                ╚════════════════════════════════════════════════╝                                             
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                                                                   
root         1  0.0  0.3   2844  1692 ?        Ss   16:49   0:00 /sbin/init                                    
root      2741  0.0  0.1   2240   756 ?        S<s  16:49   0:00 /sbin/udevd --daemon[0m
root      4437  0.0  0.7   6508  3712 ?        S    16:49   0:02 /usr/sbin/vmtoolsd
root      4466  0.0  1.4  13708  7684 ?        S    16:49   0:00 /usr/lib/vmware-vgauth/VGAuthService -s
daemon[0m    4613  0.0  0.1   1836   520 ?        Ss   16:49   0:00 /sbin/portmap
statd     4631  0.0  0.1   1900   724 ?        Ss   16:49   0:00 /sbin/rpc.statd
root      4652  0.0  0.1   3648   564 ?        Ss   16:49   0:00 /usr/sbin/rpc.idmapd
root      4882  0.0  0.0   1716   492 tty4     Ss+  16:49   0:00 /sbin/getty 38400 tty4
root      4883  0.0  0.0   1716   484 tty5     Ss+  16:49   0:00 /sbin/getty 38400 tty5
root      4888  0.0  0.0   1716   488 tty2     Ss+  16:49   0:00 /sbin/getty 38400 tty2
root      4890  0.0  0.0   1716   488 tty3     Ss+  16:49   0:00 /sbin/getty 38400 tty3
root      4893  0.0  0.0   1716   484 tty6     Ss+  16:49   0:00 /sbin/getty 38400 tty6
syslog    4933  0.0  0.1   1936   644 ?        Ss   16:49   0:01 /sbin/syslogd -u syslog
root      4984  0.0  0.1   1872   544 ?        S    16:49   0:00 /bin/dd bs 1 if /proc/kmsg of /var/run/klogd/kmsg
klog      4986  0.0  0.4   3288  2136 ?        Ss   16:49   0:00 /sbin/klogd -P /var/run/klogd/kmsg
bind      5011  0.0  1.4  35408  7684 ?        Ssl  16:49   0:00 /usr/sbin/named -u bind
root      5035  0.0  0.1   5312  1028 ?        Ss   16:49   0:00 /usr/sbin/sshd
root      5116  0.0  0.2   2768  1300 ?        S    16:49   0:00 /bin/sh /usr/bin/mysqld_safe
mysql     5158  0.0  3.3 127560 17024 ?        Sl   16:49   0:00  _ /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --user=mysql --pid-file=/var/run/mysqld/mysqld.pid --skip-external-locking --port=3306 --socket=/var/run/mysqld/mysqld.sock
root      5160  0.0  0.1   1700   560 ?        S    16:49   0:00  _ logger -p daemon[0m.err -t mysqld_safe -i -t mysqld
postgres  5240  0.0  0.9  41340  5076 ?        S    16:49   0:00 /usr/lib/postgresql/8.3/bin/postgres -D /var/lib/postgresql/8.3/main -c config_file=/etc/postgresql/8.3/main/postgresql.conf
postgres  5243  0.0  0.2  41340  1384 ?        Ss   16:49   0:00  _ postgres: writer process
postgres  5244  0.0  0.2  41340  1196 ?        Ss   16:49   0:00  _ postgres: wal writer process
postgres  5245  0.0  0.2  41476  1412 ?        Ss   16:49   0:00  _ postgres: autovacuum launcher process
postgres  5246  0.0  0.2  12660  1160 ?        Ss   16:49   0:00  _ postgres: stats collector process
daemon[0m    5267  0.0  0.0   2316   420 ?        SNs  16:49   0:00 distccd --daemon --user daemon --allow 0.0.0.0/0
daemon[0m    5268  0.0  0.1   2316   560 ?        SN   16:49   0:00  _ distccd --daemon --user daemon --allow 0.0.0.0/0
daemon[0m    5479  0.0  0.1   2316   560 ?        SN   16:49   0:00  _ distccd --daemon --user daemon --allow 0.0.0.0/0
daemon[0m    7055  0.0  0.2   3276  1492 ?        SN   18:03   0:00  |   _ bash
daemon[0m    9828  0.1  0.7   5436  3632 ?        RN   18:43   0:00  |       _ /bin/sh ./linpeas.sh
daemon[0m   11719  0.0  0.5   5436  2792 ?        RN   18:44   0:00  |           _ /bin/sh ./linpeas.sh
daemon[0m   11720  0.0  0.1   2360   944 ?        RN   18:44   0:00  |               _ ps fauxwww
daemon[0m    5480  0.0  0.1   2316   560 ?        SN   16:49   0:00  _ distccd --daemon --user daemon --allow 0.0.0.0/0
root      5335  0.0  0.0   2424   332 ?        Ss   16:49   0:00 /usr/sbin/rpc.mountd
root      5403  0.0  0.3   5412  1732 ?        Ss   16:49   0:00 /usr/lib/postfix/master
postfix   5406  0.0  0.3   5460  1688 ?        S    16:49   0:00  _ qmgr -l -t fifo -u
postfix   9149  0.0  0.3   5420  1648 ?        S    18:29   0:00  _ pickup -l -t fifo -u -c
root      5411  0.0  0.2   5388  1196 ?        Ss   16:49   0:00 /usr/sbin/nmbd -D
root      5413  0.0  0.2   7724  1360 ?        Ss   16:49   0:00 /usr/sbin/smbd -D
root      5417  0.0  0.1   7724   808 ?        S    16:49   0:00  _ /usr/sbin/smbd -D
snmp      5419  0.0  0.7   8488  3764 ?        S    16:49   0:00 /usr/sbin/snmpd -Lsd -Lf /dev/null -u snmp -I -smux -p /var/run/snmpd.pid 127.0.0.1
root      5442  0.0  0.1   2424   856 ?        Ss   16:49   0:00 /usr/sbin/xinetd -pidfile /var/run/xinetd.pid -stayalive -inetd_compat
proftpd   5481  0.0  0.3   9948  1596 ?        Ss   16:49   0:00 proftpd: (accepting connections)
daemon[0m    5497  0.0  0.0   1984   424 ?        Ss   16:49   0:00 /usr/sbin/atd
root      5510  0.0  0.1   2104   892 ?        Ss   16:49   0:00 /usr/sbin/cron
root      5540  0.0  0.0   2052   352 ?        Ss   16:49   0:00 /usr/bin/jsvc -user tomcat55 -cp /usr/share/java/commons-daemon[0m.jar:/usr/share/tomcat5.5/bin/bootstrap.jar -outfile SYSLOG -errfile SYSLOG -pidfile /var/run/tomcat5.5.pid -Djava.awt.headless=true -Xmx128M -Djava.endorsed.dirs=/usr/share/tomcat5.5/common/endorsed -Dcatalina.base=/var/lib/tomcat5.5 -Dcatalina.home=/usr/share/tomcat5.5 -Djava.io.tmpdir=/var/lib/tomcat5.5/temp -Djava.security.manager -Djava.security.policy=/var/lib/tomcat5.5/conf/catalina.policy org.apache.catalina.startup.Bootstrap
root      5541  0.0  0.0   2052   480 ?        S    16:49   0:00  _ /usr/bin/jsvc -user tomcat55 -cp /usr/share/java/commons-daemon[0m.jar:/usr/share/tomcat5.5/bin/bootstrap.jar -outfile SYSLOG -errfile SYSLOG -pidfile /var/run/tomcat5.5.pid -Djava.awt.headless=true -Xmx128M -Djava.endorsed.dirs=/usr/share/tomcat5.5/common/endorsed -Dcatalina.base=/var/lib/tomcat5.5 -Dcatalina.home=/usr/share/tomcat5.5 -Djava.io.tmpdir=/var/lib/tomcat5.5/temp -Djava.security.manager -Djava.security.policy=/var/lib/tomcat5.5/conf/catalina.policy org.apache.catalina.startup.Bootstrap
tomcat55  5543  0.2 17.3 364160 89576 ?        Sl   16:49   0:17  _ /usr/bin/jsvc -user tomcat55 -cp /usr/share/java/commons-daemon[0m.jar:/usr/share/tomcat5.5/bin/bootstrap.jar -outfile SYSLOG -errfile SYSLOG -pidfile /var/run/tomcat5.5.pid -Djava.awt.headless=true -Xmx128M -Djava.endorsed.dirs=/usr/share/tomcat5.5/common/endorsed -Dcatalina.base=/var/lib/tomcat5.5 -Dcatalina.home=/usr/share/tomcat5.5 -Djava.io.tmpdir=/var/lib/tomcat5.5/temp -Djava.security.manager -Djava.security.policy=/var/lib/tomcat5.5/conf/catalina.policy org.apache.catalina.startup.Bootstrap
root      5563  0.0  0.4  10596  2560 ?        Ss   16:49   0:00 /usr/sbin/apache2 -k start
www-data  5564  0.0  0.3  10596  1952 ?        S    16:49   0:00  _ /usr/sbin/apache2 -k start
www-data  5566  0.0  0.3  10596  1952 ?        S    16:49   0:00  _ /usr/sbin/apache2 -k start
www-data  5568  0.0  0.3  10596  1952 ?        S    16:49   0:00  _ /usr/sbin/apache2 -k start
www-data  5572  0.0  0.3  10596  1952 ?        S    16:49   0:00  _ /usr/sbin/apache2 -k start
www-data  5574  0.0  0.3  10596  1952 ?        S    16:49   0:00  _ /usr/sbin/apache2 -k start
root      5584  0.0  5.1  66344 26472 ?        Sl   16:49   0:00 /usr/bin/rmiregistry
root      5588  0.0  0.4  12208  2572 ?        Sl   16:49   0:01 ruby /usr/sbin/druby_timeserver.rb
root      5598  0.0  0.0   1716   488 tty1     Ss+  16:49   0:00 /sbin/getty 38400 tty1
root      5602  0.0  0.4   8540  2364 ?        S    16:49   0:00 /usr/bin/unrealircd
root      5605  0.0  2.3  14036 12016 ?        S    16:49   0:00 Xtightvnc :0 -desktop X -auth /root/.Xauthority -geometry 1024x768 -depth 24 -rfbwait 120000 -rfbauth /root/.vnc/passwd -rfbport 5900 -fp /usr/X11R6/lib/X11/fonts/Type1/,/usr/X11R6/lib/X11/fonts/Speedo/,/usr/X11R6/lib/X11/fonts/misc/,/usr/X11R6/lib/X11/fonts/75dpi/,/usr/X11R6/lib/X11/fonts/100dpi/,/usr/share/fonts/X11/misc/,/usr/share/fonts/X11/Type1/,/usr/share/fonts/X11/75dpi/,/usr/share/fonts/X11/100dpi/ -co /etc/X11/rgb
root      5611  0.0  0.2   2724  1184 ?        S    16:49   0:00 /bin/sh /root/.vnc/xstartup
root      5614  0.0  0.4   5936  2568 ?        S    16:49   0:00  _ xterm -geometry 80x24+10+10 -ls -title X Desktop
root      5649  0.0  0.3   2852  1548 pts/0    Ss+  16:49   0:00  |   _ -bash
root      5616  0.0  0.9   8988  4996 ?        S    16:49   0:01  _ fluxbox

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                   
                                                                                                               
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                      
Proc 4613 with ppid 1 is run by user daemon but the ppid user is root                                          
Proc 4631 with ppid 1 is run by user statd but the ppid user is root
Proc 4933 with ppid 1 is run by user syslog but the ppid user is root
Proc 4986 with ppid 1 is run by user klog but the ppid user is root
Proc 5011 with ppid 1 is run by user bind but the ppid user is root
Proc 5158 with ppid 5116 is run by user mysql but the ppid user is root
Proc 5240 with ppid 1 is run by user postgres but the ppid user is root
Proc 5267 with ppid 1 is run by user daemon but the ppid user is root
Proc 5406 with ppid 5403 is run by user postfix but the ppid user is root
Proc 5419 with ppid 1 is run by user snmp but the ppid user is root
Proc 5481 with ppid 1 is run by user proftpd but the ppid user is root
Proc 5497 with ppid 1 is run by user daemon but the ppid user is root
Proc 5543 with ppid 5540 is run by user tomcat55 but the ppid user is root
Proc 5564 with ppid 5563 is run by user www-data but the ppid user is root
Proc 5566 with ppid 5563 is run by user www-data but the ppid user is root
Proc 5568 with ppid 5563 is run by user www-data but the ppid user is root
Proc 5572 with ppid 5563 is run by user www-data but the ppid user is root
Proc 5574 with ppid 5563 is run by user www-data but the ppid user is root
Proc 9149 with ppid 5403 is run by user postfix but the ppid user is root
Proc 11688 with ppid 11686 is run by user sshd but the ppid user is root
Proc 11689 with ppid 11687 is run by user sshd but the ppid user is root
Proc 11692 with ppid 11690 is run by user sshd but the ppid user is root
Proc 11693 with ppid 11691 is run by user sshd but the ppid user is root
Proc 11696 with ppid 11694 is run by user sshd but the ppid user is root
Proc 11697 with ppid 11695 is run by user sshd but the ppid user is root
Proc 11699 with ppid 11698 is run by user sshd but the ppid user is root
Proc 11702 with ppid 11700 is run by user sshd but the ppid user is root
Proc 11703 with ppid 11701 is run by user sshd but the ppid user is root
Proc 11705 with ppid 11704 is run by user sshd but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information             
COMMAND     PID     USER   FD      TYPE DEVICE    SIZE   NODE NAME                                             

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory             
gdm-password Not Found                                                                                         
gnome-keyring-daemon Not Found                                                                                 
lightdm Not Found                                                                                              
vsftpd Not Found                                                                                               
apache2 process found (dump creds from memory as root)                                                         
sshd: process found (dump creds from memory as root)

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                         
/usr/bin/crontab                                                                                               
incrontab Not Found
-rw-r--r-- 1 root root     724 Apr  8  2008 /etc/crontab                                                       

/etc/cron.d:
total 20
drwxr-xr-x  2 root root 4096 May 14  2012 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..
-rw-r--r--  1 root root  102 Apr  8  2008 .placeholder
-rw-r--r--  1 root root  492 Jan  6  2010 php5
-rw-r--r--  1 root root 1323 Mar 31  2008 postgresql-common

/etc/cron.daily:
total 60
drwxr-xr-x  2 root root 4096 Apr 28  2010 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..
-rw-r--r--  1 root root  102 Apr  8  2008 .placeholder
-rwxr-xr-x  1 root root  633 Feb  1  2008 apache2
-rwxr-xr-x  1 root root 7441 Apr 22  2008 apt
-rwxr-xr-x  1 root root  314 Apr  4  2008 aptitude
-rwxr-xr-x  1 root root  502 Dec 12  2007 bsdmainutils
-rwxr-xr-x  1 root root   89 Jun 19  2006 logrotate
-rwxr-xr-x  1 root root  954 Mar 12  2008 man-db
-rwxr-xr-x  1 root root  183 Mar  8  2008 mlocate
-rwxr-xr-x  1 root root  383 Apr 28  2010 samba
-rwxr-xr-x  1 root root 3295 Apr  8  2008 standard
-rwxr-xr-x  1 root root 1309 Nov 23  2007 sysklogd
-rwxr-xr-x  1 root root  477 Dec  7  2008 tomcat55

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Mar 16  2010 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..
-rw-r--r--  1 root root  102 Apr  8  2008 .placeholder

/etc/cron.monthly:
total 20
drwxr-xr-x  2 root root 4096 Apr 28  2010 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..
-rw-r--r--  1 root root  102 Apr  8  2008 .placeholder
-rwxr-xr-x  1 root root  664 Feb 20  2008 proftpd
-rwxr-xr-x  1 root root  129 Apr  8  2008 standard

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 Mar 16  2010 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..
-rw-r--r--  1 root root  102 Apr  8  2008 .placeholder
-rwxr-xr-x  1 root root  528 Mar 12  2008 man-db
-rwxr-xr-x  1 root root 2522 Jan 28  2008 popularity-contest
-rwxr-xr-x  1 root root 1220 Nov 23  2007 sysklogd

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )


alias
backup
bin
daemon
ftp
games
gnats
guest
irc
lp
mail
man
nobody
operator
proxy
qmaild
qmaill
qmailp
qmailq
qmailr
qmails
sync
sys
www-data

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                 
                                                                                                               
╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                    
You can't write on systemd PATH                                                                                

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                      
                                                                                                               
╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                      
                                                                                                               
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                     
                                                                                                               
╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                     
/anvil                                                                                                         
/bounce
/bsmtp
/cleanup
/defer
/dev/log
  └─(Read Write)
/discard
/error
/flush
/ifmail
/lmtp
/local
/maildrop
/mailman
/proxymap
/proxywrite
/relay
/retry
/rewrite
/scache
/scalemail-backend
/showq
/smtp
/tlsmgr
/tmp/.X11-unix/X0
  └─(Read Write)
/trace
/uucp
/var/run/mysqld/mysqld.sock
  └─(Read Write)
/var/run/postgresql/.s.PGSQL.5432
  └─(Read Write)
/var/run/proftpd/proftpd.sock
  └─(Read Write)
/var/run/vmware/guestServicePipe
  └─(Read Write)
/verify
/virtual

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                       
                                                                                                               
╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                       
busctl Not Found                                                                                               
                                                                                                               

                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                            
                              ╚═════════════════════╝                                                          
╔══════════╣ Hostname, hosts and DNS
lame                                                                                                           
127.0.0.1       localhost
127.0.1.1       lame.hackthebox.gr      lame

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
nameserver 8.8.8.8
hackthebox.gr

╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information                                            
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 00:50:56:94:8d:6e  
          inet addr:10.10.10.3  Bcast:10.10.10.255  Mask:255.255.255.0
          inet6 addr: dead:beef::250:56ff:fe94:8d6e/64 Scope:Global
          inet6 addr: fe80::250:56ff:fe94:8d6e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:46843 errors:0 dropped:0 overruns:0 frame:0
          TX packets:61862 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:9067361 (8.6 MB)  TX bytes:8339425 (7.9 MB)
          Interrupt:19 Base address:0x2024 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:1286 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1286 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:517833 (505.6 KB)  TX bytes:517833 (505.6 KB)


╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                  
tcp        0      0 0.0.0.0:512             0.0.0.0:*               LISTEN      -                              
tcp        0      0 0.0.0.0:513             0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:514             0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:8009            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:6697            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:1099            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:6667            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:50124           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:5900            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:6000            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:8787            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:8180            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:1524            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN      -               
tcp        0      0 10.10.10.3:53           0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:54901           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:23              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:46647           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:37275           0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::2121                 :::*                    LISTEN      -               
tcp6       0      0 :::3632                 :::*                    LISTEN      -               
tcp6       0      0 :::53                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
tcp6       0      0 :::5432                 :::*                    LISTEN      -               
tcp6       0      0 ::1:953                 :::*                    LISTEN      -               

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                             
                                                                                                               


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                            
                               ╚═══════════════════╝                                                           
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                       
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)                                                          

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                   
netpgpkeys Not Found
netpgp Not Found                                                                                               
                                                                                                               
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                               
                                                                                                               
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                         
ptrace protection is enabled ()                                                                                

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2     
                                                                                                               
╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                

╔══════════╣ Users with console
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
makis:x:1003:1003::/home/makis:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
postgres:x:108:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
proxy:x:13:13:proxy:/bin:/bin/sh
root:x:0:0:root:/root:/bin/bash
service:x:1002:1002:,,,:/home/service:/bin/bash
sys:x:3:3:sys:/dev:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                         
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(libuuid) gid=101(libuuid) groups=101(libuuid)
uid=1002(service) gid=1002(service) groups=1002(service)
uid=1003(makis) gid=1003(makis) groups=1003(makis),4(adm),112(admin)
uid=101(dhcp) gid=102(dhcp) groups=102(dhcp)
uid=102(syslog) gid=103(syslog) groups=103(syslog)
uid=103(klog) gid=104(klog) groups=104(klog)
uid=104(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=105(bind) gid=113(bind) groups=113(bind)
uid=106(postfix) gid=115(postfix) groups=115(postfix)
uid=107(ftp) gid=65534(nogroup) groups=65534(nogroup)
uid=108(postgres) gid=117(postgres) groups=117(postgres),114(ssl-cert)
uid=109(mysql) gid=118(mysql) groups=118(mysql)
uid=110(tomcat55) gid=65534(nogroup) groups=65534(nogroup)
uid=111(distccd) gid=65534(nogroup) groups=65534(nogroup)
uid=112(telnetd) gid=120(telnetd) groups=120(telnetd),43(utmp)
uid=113(proftpd) gid=65534(nogroup) groups=65534(nogroup)
uid=114(statd) gid=65534(nogroup) groups=65534(nogroup)
uid=115(snmp) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 18:44:24 up  1:55,  1 user,  load average: 0.09, 0.05, 0.01                                                   
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
root     pts/0    :0.0             16:49    1:54   0.00s  0.00s -bash

╔══════════╣ Last logons
root     tty1                          Sat Oct 31 02:08 - down   (00:31)                                       
root     tty1                          Sat Oct 31 02:08 - 02:08  (00:00)    
root     pts/0        :0.0             Sat Oct 31 02:08 - down   (00:31)    
reboot   system boot  2.6.24-16-server Sat Oct 31 02:07 - 02:39  (00:31)    
root     tty1                          Fri May  5 16:32 - down   (00:00)    
root     tty1                          Fri May  5 16:32 - 16:32  (00:00)    
root     pts/0        :0.0             Fri May  5 16:32 - down   (00:00)    
reboot   system boot  2.6.24-16-server Fri May  5 16:31 - 16:33  (00:01)    

wtmp begins Wed Mar 15 09:37:52 2017

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                              
root             pts/0    :0.0             Fri May  9 16:49:58 -0400 2025
makis            pts/1    192.168.150.100  Tue Mar 14 18:32:04 -0400 2017

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)                                                                       
                                                                                                               
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                               


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                             
                             ╚══════════════════════╝                                                          
╔══════════╣ Useful software
/usr/bin/base64                                                                                                
/usr/bin/curl
/usr/bin/g++
/usr/bin/gcc
/usr/bin/gdb
/usr/bin/make
/bin/nc
/bin/nc.traditional
/bin/netcat
/usr/bin/nmap
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python
/usr/bin/ruby
/usr/bin/socat
/usr/bin/sudo
/usr/bin/wget
/usr/bin/xterm

╔══════════╣ Installed Compilers
ii  distcc                                2.18.3-4.1ubuntu1                       Simple distributed compiler client and serve
ii  g++                                   4:4.2.3-1ubuntu6                        The GNU C++ compiler
ii  g++-4.2                               4.2.4-1ubuntu4                          The GNU C++ compiler
ii  gcc                                   4:4.2.3-1ubuntu6                        The GNU C compiler
ii  gcc-4.2                               4.2.4-1ubuntu4                          The GNU C compiler
ii  gcj-4.2                               4.2.4-1ubuntu3                          The GNU compiler for Java(TM)
/usr/bin/gcc
/usr/bin/g++

╔══════════╣ MySQL version
mysql  Ver 14.12 Distrib 5.0.51a, for debian-linux-gnu (i486) using readline 5.2                               


═╣ MySQL connection using default root/root ........... No
═╣ MySQL connection using root/toor ................... No                                                     
═╣ MySQL connection using root/NOPASS ................. Yes                                                    

╔══════════╣ Searching mysql credentials and exec
Found readable /etc/mysql/my.cnf                                                                               
[client]
port            = 3306
socket          = /var/run/mysqld/mysqld.sock
[mysqld_safe]
socket          = /var/run/mysqld/mysqld.sock
nice            = 0
[mysqld]
user            = mysql
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
port            = 3306
basedir         = /usr
datadir         = /var/lib/mysql
tmpdir          = /tmp
language        = /usr/share/mysql/english
skip-external-locking
bind-address            = 0.0.0.0
key_buffer              = 16M
max_allowed_packet      = 16M
thread_stack            = 128K
thread_cache_size       = 8
query_cache_limit       = 1M
query_cache_size        = 16M
expire_logs_days        = 10
max_binlog_size         = 100M
skip-bdb
ssl-ca=/etc/mysql/cacert.pem
ssl-cert=/etc/mysql/server-cert.pem
ssl-key=/etc/mysql/server-key.pem
[mysqldump]
quick
quote-names
max_allowed_packet      = 16M
[mysql]
[isamchk]
key_buffer              = 16M
!includedir /etc/mysql/conf.d/

╔══════════╣ Analyzing MariaDB Files (limit 70)
                                                                                                               
-rw------- 1 root root 280 May 14  2012 /etc/mysql/debian.cnf

╔══════════╣ Analyzing PostgreSQL Files (limit 70)
Version: psql (PostgreSQL) 8.3.1                                                                               
contains support for command-line editing

-rw-r----- 1 postgres postgres 3619 Mar 30  2010 /etc/postgresql/8.3/main/pg_hba.conf

-rw-r--r-- 1 postgres postgres 16673 Mar 17  2010 /etc/postgresql/8.3/main/postgresql.conf
datestyle = 'iso, mdy'
default_text_search_config = 'pg_catalog.english'



╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.2.8 (Ubuntu)                                                          
Server built:   Mar  9 2010 20:45:36
httpd Not Found
                                                                                                               
Nginx version: nginx Not Found
                                                                                                               
/etc/apache2/mods-available/php5.conf-<IfModule mod_php5.c>
/etc/apache2/mods-available/php5.conf:  AddType application/x-httpd-php .php .phtml .php3
/etc/apache2/mods-available/php5.conf:  AddType application/x-httpd-php-source .phps
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 May 20  2012 /etc/apache2/sites-enabled                                            
drwxr-xr-x 2 root root 4096 May 20  2012 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 36 Apr 28  2010 /etc/apache2/sites-enabled/000-default -> /etc/apache2/sites-available/default                                                                                                         
NameVirtualHost *
<VirtualHost *>
        ServerAdmin webmaster@localhost

        DocumentRoot /var/www/
        <Directory />
                Options FollowSymLinks
                AllowOverride None
        </Directory>
        <Directory /var/www/>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>
        ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
        <Directory "/usr/lib/cgi-bin">
                AllowOverride None
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                Order allow,deny
                Allow from all
        </Directory>
        ScriptAlias /twiki/bin/ "/var/www/twiki/bin/"
        Alias /twiki/ "/var/www/twiki/"
        <Directory "/var/www/twiki/bin">
                Options +ExecCGI
                SetHandler cgi-script
                Allow from all
        </Directory>
        <Directory "/var/www/twiki/pub">
                Options FollowSymLinks +Includes
                AllowOverride None
                Allow from all
        </Directory>
        <Directory "/var/www/twiki/data">
                deny from all
        </Directory>
        <Directory "/var/www/twiki/templates">
                deny from all
        </Directory>

        ErrorLog /var/log/apache2/error.log
        LogLevel warn
        CustomLog /var/log/apache2/access.log combined
        ServerSignature On
    Alias /doc/ "/usr/share/doc/"
    <Directory "/usr/share/doc/">
        Options Indexes MultiViews FollowSymLinks
        AllowOverride None
    </Directory>
    <Directory "/var/www/dav/">
        Options Indexes MultiViews FollowSymLinks
        AllowOverride None
        DAV On
    </Directory>
</VirtualHost>



-rw-r--r-- 1 root root 44587 Jan  6  2010 /etc/php5/apache2/php.ini
allow_call_time_pass_reference = On
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
mysql.allow_persistent = On
msql.allow_persistent = On
pgsql.allow_persistent = On
sybase.allow_persistent = On
sybct.allow_persistent = On
ifx.allow_persistent = On
mssql.allow_persistent = On
-rw-r--r-- 1 root root 44588 May 20  2012 /etc/php5/cgi/php.ini
allow_call_time_pass_reference = On
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
mysql.allow_persistent = On
msql.allow_persistent = On
pgsql.allow_persistent = On
sybase.allow_persistent = On
sybct.allow_persistent = On
ifx.allow_persistent = On
mssql.allow_persistent = On
-rw-r--r-- 1 root root 44588 May 20  2012 /etc/php5/cli/php.ini
allow_call_time_pass_reference = On
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
mysql.allow_persistent = On
msql.allow_persistent = On
pgsql.allow_persistent = On
sybase.allow_persistent = On
sybct.allow_persistent = On
ifx.allow_persistent = On
mssql.allow_persistent = On



╔══════════╣ Analyzing Http conf Files (limit 70)
-rw-r--r-- 1 root root 0 Mar 17  2010 /etc/apache2/httpd.conf                                                  

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 935 Apr 10  2008 /usr/share/doc/rsync/examples/rsyncd.conf                              
pid file=/var/run/rsyncd.pid
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing VNC Files (limit 70)
drwx------ 2 root root 4096 May  9 16:49 /root/.vnc                                                            


-rw-r--r-- 1 root root 1689 Apr  7  2008 /usr/share/doc/tightvncserver/examples/vnc.conf.gz




╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                           
drwxr-xr-x 2 root root 4096 Apr 28  2010 /etc/ldap

drwxr-xr-x 2 root root 4096 Mar 23  2010 /usr/include/c++/4.2/javax/naming/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                    
                                                                                                               

-rw-r--r-- 1 root root 442 May 20  2012 /root/.ssh/known_hosts
|1|gS7DWzAxRvtufzEYnaW40GOvYu0=|5afWvF6s4R5Yaog0mimuOyNfXiI= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAstqnuFMBOZvO3WTEjP4TUdjgWkIVNdTq6kboEDjteOfc65TlI7sRvQBwqAhQjeeyyIk8T55gMDkOD0akSlSXvLDcmcdYfxeIF0ZSuT+nkRhij7XSSA/Oc5QSk3sJ/SInfb78e3anbRHpmkJcVgETJ5WhKObUNf1AKZW++4Xlc63M4KI5cjvMMIPEVOyR3AKmI78Fo3HJjYucg87JjLeC66I7+dlEYX6zT8i1XYwa/L1vZ3qSJISGVu8kRPikMv/cNSvki4j+qDYyZ2E5497W87+Ed46/8P42LNGoOV8OcX/ro6pAcbEPUdUEfkJrqi2YXbhvwIJ0gFMb6wfe5cnQew==


-rw-r--r-- 1 root root 405 May 17  2010 /root/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApmGJFZNl0ibMNALQx7M6sGGoi4KNmj6PVxpbpG70lShHQqldJkcteZZdPFSbW76IUiPR0Oh+WBV0x1c6iPL/0zUYFHyFKAz1e6/5teoweG1jr2qOffdomVhvXXvSjGaSFwwOYB8R0QxsOWWTQTYSeBa66X6e777GVkHCDLYgZSo8wWr5JXln/Tw7XotowHr8FEGvw2zW1krU3Zo9Bzp0e0ac2U+qUGIzIu/WwgztLZs5/D9IyhtRWocyQPE+kcP+Jz2mt4y1uA73KqoXfdw5oGUkxdFo9f1nu2OwkjOc+Wv8Vw7bwkf+1RgiOMgiJ5cCs4WocyVxsXovcNnbALTp3w== msfadmin@metasploitable

-rw-r--r-- 1 root root 609 Apr 28  2010 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 401 Apr 28  2010 /etc/ssh/ssh_host_rsa_key.pub

Port 22
PermitRootLogin yes
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
══╣ Some certificates were found (out limited):
/etc/ssl/certs/ssl-cert-snakeoil.pem                                                                           
9828PSTORAGE_CERTSBIN

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                               


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Nov  3  2020 /etc/pam.d                                                            
-rw-r--r-- 1 root root 1272 Apr  6  2008 /etc/pam.d/sshd
auth       required     pam_env.so # [1]
auth       required     pam_env.so envfile=/etc/default/locale
account    required     pam_nologin.so
session    optional     pam_motd.so # [1]
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so


╔══════════╣ Analyzing NFS Exports Files (limit 70)
Connected NFS Mounts:                                                                                          
rpc_pipefs /var/lib/nfs/rpc_pipefs rpc_pipefs rw,relatime 0 0
nfsd /proc/fs/nfsd nfsd rw,relatime 0 0
-rw-r--r-- 1 root root 367 May 13  2012 /etc/exports
/       *(rw,sync,no_root_squash,no_subtree_check)



╔══════════╣ Searching AD cached hashes
-rw------- 1 root root 16384 May 17  2010 /var/lib/samba/passdb.tdb                                            

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Mar 16  2010 /usr/share/keyrings                                                   
drwxr-xr-x 2 root root 4096 Mar 16  2010 /var/lib/apt/keyrings




╔══════════╣ Analyzing Filezilla Files (limit 70)
-rwxr-xr-x 1 root root 2167728 Jul 25  2008 /usr/bin/filezilla                                                 

lrwxrwxrwx 1 root root 16 May 20  2012 /usr/share/doc/filezilla -> filezilla-common

drwxr-xr-x 3 root root 4096 May 20  2012 /usr/share/filezilla

-rw-r--r-- 1 root root 181 Jul 25  2008 /usr/share/menu/filezilla




╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                 
passwd file: /etc/passwd
passwd file: /usr/share/linda/overrides/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                   
gpg Not Found
netpgpkeys Not Found                                                                                           
netpgp Not Found                                                                                               
                                                                                                               
-rw------- 1 root root 0 Mar 16  2010 /etc/apt/secring.gpg
-rw------- 1 root root 1200 Mar 16  2010 /etc/apt/trustdb.gpg
-rw-r--r-- 1 root root 6713 Mar 16  2010 /etc/apt/trusted.gpg
-rw-r--r-- 1 root root 1724 Apr 22  2008 /usr/share/apt/ubuntu-archive.gpg
-rw-r--r-- 1 root root 6713 Mar  3  2008 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw------- 1 root root 0 Mar 16  2010 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 1227 Mar  3  2008 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 6713 Mar 16  2010 /var/lib/apt/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 198 Apr 26  2012 /var/lib/apt/lists/archive.canonical.com_ubuntu_dists_hardy_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.10 (GNU/Linux)
iEYEABECAAYFAk+Zl5YACgkQQJdur0N9BbUbPwCgqFqD2pm/Mh5NCijYPon78yvg
YS4AoIto2PM3w4lgzbd4ylV+gs5nzof4
=SuAM
-----END PGP SIGNATURE-----
-rw-r--r-- 1 root root 198 Mar 21  2013 /var/lib/apt/lists/old-releases.ubuntu.com_ubuntu_dists_hardy-backports_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.10 (GNU/Linux)
iEYEABECAAYFAlFLWpgACgkQQJdur0N9BbWJMACeJ90sAvdSXdmiAZ/M/QeWk3+b
+k4An0Q5Lfcorpo9Z0oNgdw1woola9cW
=MKXn
-----END PGP SIGNATURE-----
-rw-r--r-- 1 root root 198 May  3  2013 /var/lib/apt/lists/old-releases.ubuntu.com_ubuntu_dists_hardy-security_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.10 (GNU/Linux)
iEYEABECAAYFAlGES2YACgkQQJdur0N9BbUmgACggJXbm8RkGmigRWKWqvvKn/B/
/P4An3e2MopmcPDSInF/U4LgJFj38/4b
=8Xzx
-----END PGP SIGNATURE-----
-rw-r--r-- 1 root root 198 May  3  2013 /var/lib/apt/lists/old-releases.ubuntu.com_ubuntu_dists_hardy-updates_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.10 (GNU/Linux)
iEYEABECAAYFAlGEUS4ACgkQQJdur0N9BbV2RACdGht1LTZ2p7dB4hzOOUCS5A2o
fqwAn3+yIqDjyk3XgHP6xQV5FkEqyHC0
=fxI8
-----END PGP SIGNATURE-----
-rw-r--r-- 1 root root 189 Sep 19  2008 /var/lib/apt/lists/old-releases.ubuntu.com_ubuntu_dists_hardy_Release.gpg                                                                                                             
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.6 (GNU/Linux)
iD8DBQBI1E5SQJdur0N9BbURAoAPAJ0TKt/hCaCxRkbM0D6khuMVQ5XfFgCfVFTj
dpvqNGOkpoBSiUQ9Yd1uw2I=
=tlah
-----END PGP SIGNATURE-----



╔══════════╣ Analyzing SNMP Files (limit 70)
-rw-r--r-- 1 root root 15822 May 20  2012 /etc/snmp/snmpd.conf                                                 
-rw------- 1 snmp root 1066 May  9 16:49 /var/lib/snmp/snmpd.conf

╔══════════╣ Analyzing Postfix Files (limit 70)
-rwxr-xr-x 1 root root 4202 Apr 18  2008 /etc/init.d/postfix                                                   

-rwxr-xr-x 1 root root 803 Apr 18  2008 /etc/network/if-down.d/postfix

-rwxr-xr-x 1 root root 1120 Apr 18  2008 /etc/network/if-up.d/postfix

drwxr-xr-x 3 root root 4096 Apr 28  2010 /etc/postfix
-rw-r--r-- 1 root root 4300 Mar 17  2010 /etc/postfix/master.cf
  flags=DRhu user=vmail argv=/usr/bin/maildrop -d ${recipient}
  flags=Fqhu user=uucp argv=uux -r -n -z -a$sender - $nexthop!rmail ($recipient)
  flags=F user=ftn argv=/usr/lib/ifmail/ifmail -r $nexthop ($recipient)
  flags=Fq. user=bsmtp argv=/usr/lib/bsmtp/bsmtp -t$nexthop -f$sender $recipient
  flags=R user=scalemail argv=/usr/lib/scalemail/bin/scalemail-store ${nexthop} ${user} ${extension}
  flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py

-rwxr-xr-x 1 root root 803 Apr 18  2008 /etc/ppp/ip-down.d/postfix

-rwxr-xr-x 1 root root 1120 Apr 18  2008 /etc/ppp/ip-up.d/postfix

-rwxr-xr-x 1 root root 221 Apr 18  2008 /etc/resolvconf/update-libc.d/postfix

drwxr-xr-x 2 root root 4096 Mar 17  2010 /usr/lib/postfix

-rwxr-xr-x 1 root root 7264 Apr 18  2008 /usr/sbin/postfix

drwxr-xr-x 2 root root 4096 Mar 17  2010 /usr/share/doc/postfix

-rw-r--r-- 1 root root 275 Apr 18  2008 /usr/share/lintian/overrides/postfix

drwxr-xr-x 2 root root 4096 Mar 17  2010 /usr/share/postfix

drwxr-xr-x 2 postfix postfix 4096 Mar 17  2010 /var/lib/postfix

drwxr-xr-x 19 root root 4096 Mar 17  2010 /var/spool/postfix


╔══════════╣ Analyzing FTP Files (limit 70)
-rw-r--r-- 1 root root 4430 May 20  2012 /etc/vsftpd.conf                                                      
anonymous_enable=YES
local_enable=YES
write_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
#chown_uploads=YES
#chown_username=whoever









╔══════════╣ Analyzing X11 Files (limit 70)
-rw------- 1 root root 373 May  9 16:49 /root/.Xauthority                                                      

╔══════════╣ Analyzing Samba Files (limit 70)
                                                                                                               
Samba version 3.0.20-Debian
PID     Username      Group         Machine                        
-------------------------------------------------------------------

Service      pid     machine       Connected at
-------------------------------------------------------

No locked files

-rw-r--r-- 1 root root 7932 May  7  2010 /etc/samba/smb.conf
   
   writable = yes
   create mask = 0700
   directory mask = 0700
;   guest ok = yes
;   
   
   
   browseable = yes
   
   
;   
   read only = no
   guest ok = yes
   
-rw-r--r-- 1 root root 7726 Apr 28  2010 /usr/share/samba/smb.conf
   
   
   create mask = 0700
   directory mask = 0700
;   guest ok = yes
;   
   
   
   browseable = yes
   
   
;   

╔══════════╣ Analyzing DNS Files (limit 70)
drwxr-sr-x 2 root bind 4096 Mar 17  2010 /etc/bind                                                             
drwxr-sr-x 2 root bind 4096 Mar 17  2010 /etc/bind
-rw-r--r-- 1 root root 270 Apr  9  2008 /etc/bind/db.local
-rw-r----- 1 bind bind 77 Mar 17  2010 /etc/bind/rndc.key
-rw-r--r-- 1 root root 2878 Apr  9  2008 /etc/bind/db.root
-rw-r--r-- 1 root bind 165 Apr  9  2008 /etc/bind/named.conf.local
-rw-r--r-- 1 root root 237 Apr  9  2008 /etc/bind/db.0
-rw-r--r-- 1 root bind 907 Apr  9  2008 /etc/bind/named.conf
-rw-r--r-- 1 root root 353 Apr  9  2008 /etc/bind/db.empty
-rw-r--r-- 1 root root 1317 Apr  9  2008 /etc/bind/zones.rfc1918
-rw-r--r-- 1 root root 237 Apr  9  2008 /etc/bind/db.255
-rw-r--r-- 1 root bind 785 Mar 17  2010 /etc/bind/named.conf.options
-rw-r--r-- 1 root root 271 Apr  9  2008 /etc/bind/db.127

-rw-r----- 1 bind bind 77 Mar 17  2010 /etc/bind/rndc.key

-rw-r--r-- 1 root bind 165 Apr  9  2008 /etc/bind/named.conf.local
-rw-r--r-- 1 root bind 907 Apr  9  2008 /etc/bind/named.conf
include "/etc/bind/named.conf.options";
zone "." {
        type hint;
        file "/etc/bind/db.root";
};
zone "localhost" {
        type master;
        file "/etc/bind/db.local";
};
zone "127.in-addr.arpa" {
        type master;
        file "/etc/bind/db.127";
};
zone "0.in-addr.arpa" {
        type master;
        file "/etc/bind/db.0";
};
zone "255.in-addr.arpa" {
        type master;
        file "/etc/bind/db.255";
};
include "/etc/bind/named.conf.local";
-rw-r--r-- 1 root bind 785 Mar 17  2010 /etc/bind/named.conf.options
options {
        directory "/var/cache/bind";
        auth-nxdomain no;    # conform to RFC1035
        listen-on { any; };
        listen-on-v6 { any; };
};

drwxrwxr-x 2 root bind 4096 Apr  9  2008 /var/cache/bind
drwxrwxr-x 2 root bind 4096 Apr  9  2008 /var/cache/bind



drwxrwxr-x 2 root bind 4096 Mar 17  2010 /var/lib/bind
drwxrwxr-x 2 root bind 4096 Mar 17  2010 /var/lib/bind



drwxr-xr-x 3 root root 60 May  9 16:49 /var/run/bind
drwxr-xr-x 3 root root 60 May  9 16:49 /var/run/bind
drwxrwxr-x 2 root bind 60 May  9 16:49 /var/run/bind/run
-rw-r--r-- 1 bind bind 5 May  9 16:49 /var/run/bind/run/named.pid




╔══════════╣ Analyzing Windows Files (limit 70)
                                                                                                               





















-rw-r--r-- 1 root root 3889 Apr 19  2010 /etc/mysql/my.cnf





























╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 2928 Apr 14  2008 /etc/skel/.bashrc                                                     
-rw-r--r-- 1 makis makis 2928 Mar 14  2017 /home/makis/.bashrc
-rw-r--r-- 1 service service 2928 Apr 16  2010 /home/service/.bashrc
-rw-r--r-- 1 1001 1001 2928 Mar 31  2010 /home/user/.bashrc
-rw-r--r-- 1 root root 2227 Oct 20  2007 /root/.bashrc


-rw-r--r-- 1 root root 121 May 20  2012 /etc/hosts.equiv



-rw-r--r-- 1 root root 586 Apr 14  2008 /etc/skel/.profile
-rw-r--r-- 1 makis makis 586 Mar 14  2017 /home/makis/.profile
-rw-r--r-- 1 service service 586 Apr 16  2010 /home/service/.profile
-rw-r--r-- 1 1001 1001 586 Mar 31  2010 /home/user/.profile
-rw-r--r-- 1 root root 141 Oct 20  2007 /root/.profile


-rwx------ 1 root root 4 May 20  2012 /root/.rhosts

-rw-r--r-- 1 makis makis 0 Mar 14  2017 /home/makis/.sudo_as_admin_successful



                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                             
                      ╚════════════════════════════════════╝                                                   
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                               
-rwsr-xr-x 1 root root 63K Apr 14  2008 /bin/umount  --->  BSD/Linux(08-1996)                                  
-rwsr-xr-- 1 root fuse 20K Feb 26  2008 /bin/fusermount
-rwsr-xr-x 1 root root 25K Apr  2  2008 /bin/su
-rwsr-xr-x 1 root root 80K Apr 14  2008 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                       
-rwsr-xr-x 1 root root 31K Dec 10  2007 /bin/ping
-rwsr-xr-x 1 root root 27K Dec 10  2007 /bin/ping6
-rwsr-xr-x 1 root root 64K Dec  2  2008 /sbin/mount.nfs
-rwsr-xr-- 1 root dhcp 2.9K Apr  2  2008 /lib/dhcp3-client/call-dhclient-script (Unknown SUID binary!)
-rwsr-xr-x 2 root root 106K Feb 25  2008 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerableedit
-rwsr-sr-x 1 root root 7.3K Jun 25  2008 /usr/bin/X
-rwsr-xr-x 1 root root 8.4K Nov 22  2007 /usr/bin/netkit-rsh
-rwsr-xr-x 1 root root 37K Apr  2  2008 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 13K Dec 10  2007 /usr/bin/traceroute6.iputils
-rwsr-xr-x 2 root root 106K Feb 25  2008 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 12K Nov 22  2007 /usr/bin/netkit-rlogin
-rwsr-xr-x 1 root root 11K Dec 10  2007 /usr/bin/arping
You own the SUID file: /usr/bin/at
-rwsr-xr-x 1 root root 19K Apr  2  2008 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 28K Apr  2  2008 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 763K Apr  8  2008 /usr/bin/nmap
-rwsr-xr-x 1 root root 24K Apr  2  2008 /usr/bin/chsh
-rwsr-xr-x 1 root root 16K Nov 22  2007 /usr/bin/netkit-rcp
-rwsr-xr-x 1 root root 29K Apr  2  2008 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                        
-rwsr-xr-x 1 root root 46K Mar 31  2008 /usr/bin/mtr
-rwsr-sr-x 1 libuuid libuuid 13K Mar 27  2008 /usr/sbin/uuidd
-rwsr-xr-- 1 root dip 263K Oct  4  2007 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-xr-- 1 root telnetd 5.9K Dec 17  2006 /usr/lib/telnetlogin
-rwsr-xr-- 1 root www-data 11K Mar  9  2010 /usr/lib/apache2/suexec
-rwsr-xr-x 1 root root 4.5K Nov  5  2007 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 162K Apr  6  2008 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 9.4K Aug 17  2009 /usr/lib/pt_chown  --->  GNU_glibc_2.1/2.1.1_-6(08-1999)
-r-sr-xr-x 1 root root 14K Nov  3  2020 /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
-r-sr-xr-x 1 root root 9.4K Nov  3  2020 /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                               
-rwxr-sr-x 1 root shadow 20K Apr  9  2008 /sbin/unix_chkpwd                                                    
-rwxr-sr-x 1 root utmp 3.2K Apr 22  2008 /usr/bin/Eterm (Unknown SGID binary)
-rwsr-sr-x 1 root root 7.3K Jun 25  2008 /usr/bin/X
-rwxr-sr-x 1 root tty 8.0K Dec 12  2007 /usr/bin/bsd-write
-rwxr-sr-x 1 root ssh 75K Apr  6  2008 /usr/bin/ssh-agent
-rwxr-sr-x 1 root mlocate 30K Mar  8  2008 /usr/bin/mlocate
-rwxr-sr-x 1 root crontab 27K Apr  8  2008 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 38K Apr  2  2008 /usr/bin/chage
-rwxr-sr-x 1 root utmp 302K Oct 23  2007 /usr/bin/screen  --->  GNU_Screen_4.5.0
-rwxr-sr-x 1 root shadow 17K Apr  2  2008 /usr/bin/expiry
You own the SGID file: /usr/bin/at
-rwxr-sr-x 1 root utmp 300K Jan  2  2009 /usr/bin/xterm  --->  Solaris_5.5.1_X11R6.3(05-1997)/Debian_xterm_version_222-1etch2(01-2009)                                                                                        
-rwxr-sr-x 1 root tty 9.8K Apr 14  2008 /usr/bin/wall
-rwsr-sr-x 1 libuuid libuuid 13K Mar 27  2008 /usr/sbin/uuidd
-r-xr-sr-x 1 root postdrop 11K Apr 18  2008 /usr/sbin/postqueue
-r-xr-sr-x 1 root postdrop 9.9K Apr 18  2008 /usr/sbin/postdrop

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so                                       
/etc/ld.so.conf                                                                                                
Content of /etc/ld.so.conf:                                                                                    
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/i486-linux-gnu.conf                                                                        
  - /lib/i486-linux-gnu                                                                                        
  - /usr/lib/i486-linux-gnu
  /etc/ld.so.conf.d/libc.conf
  - /usr/local/lib                                                                                             
  /etc/ld.so.conf.d/vmware-tools-libraries.conf
  - /usr/lib/vmware-tools/lib32/libvmGuestLib.so                                                               
  - /usr/lib/vmware-tools/lib64/libvmGuestLib.so
  - /usr/lib/vmware-tools/lib32/libvmGuestLibJava.so
  - /usr/lib/vmware-tools/lib64/libvmGuestLibJava.so
  - /usr/lib/vmware-tools/lib32/libDeployPkg.so
  - /usr/lib/vmware-tools/lib64/libDeployPkg.so

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                      
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                
══╣ Current shell capabilities                                                                                 
CapInh: 0000000000000000                                                                                       
CapPrm: 0000000000000000
CapEff: 0000000000000000

══╣ Parent proc capabilities
CapInh: 0000000000000000                                                                                       
CapPrm: 0000000000000000
CapEff: 0000000000000000


Files with capabilities (limited to 50):

╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root  720 Mar 28  2008 usr.sbin.mysqld                                                       
-rw-r--r-- 1 root root  725 Apr  9  2008 usr.sbin.named

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                        
files with acls in searched folders Not Found                                                                  
                                                                                                               
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                              
total 8                                                                                                        
drwxr-xr-x  2 root root 4096 Apr 15  2008 .
drwxr-xr-x 96 root root 4096 May  9 16:49 ..

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                
                                                                                                               
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                   
═╣ Credentials in fstab/mtab? ........... No                                                                   
═╣ Can I read shadow files? ............. No                                                                   
═╣ Can I read shadow plists? ............ No                                                                   
═╣ Can I write shadow plists? ........... No                                                                   
═╣ Can I read opasswd file? ............. No                                                                   
═╣ Can I write in network-scripts? ...... No                                                                   
═╣ Can I read root folder? .............. total 80                                                             
drwxr-xr-x 13 root root 4096 May  9 16:50 .
drwxr-xr-x 21 root root 4096 Oct 31  2020 ..
-rw-------  1 root root  373 May  9 16:49 .Xauthority
lrwxrwxrwx  1 root root    9 May 14  2012 .bash_history -> /dev/null
-rw-r--r--  1 root root 2227 Oct 20  2007 .bashrc
drwx------  3 root root 4096 May 20  2012 .config
drwx------  2 root root 4096 May 20  2012 .filezilla
drwxr-xr-x  5 root root 4096 May  9 16:49 .fluxbox
drwx------  2 root root 4096 May 20  2012 .gconf
drwx------  2 root root 4096 May 20  2012 .gconfd
drwxr-xr-x  2 root root 4096 May 20  2012 .gstreamer-0.10
drwx------  4 root root 4096 May 20  2012 .mozilla
-rw-r--r--  1 root root  141 Oct 20  2007 .profile
drwx------  5 root root 4096 May 20  2012 .purple
-rwx------  1 root root    4 May 20  2012 .rhosts
drwxr-xr-x  2 root root 4096 May 20  2012 .ssh
drwx------  2 root root 4096 May  9 16:49 .vnc
drwxr-xr-x  2 root root 4096 May 20  2012 Desktop
-rwx------  1 root root  401 May 20  2012 reset_logs.sh
-rw-------  1 root root   33 May  9 16:50 root.txt
-rw-r--r--  1 root root  118 May  9 16:49 vnc.log

╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                         
/home/ftp
/root/
/root/.gstreamer-0.10
/root/.gstreamer-0.10/registry.i486.xml
/root/Desktop
/root/.purple
/root/.vnc
/root/.filezilla
/root/.rhosts
/root/vnc.log
/root/.config
/root/.fluxbox
/root/.fluxbox/windowmenu
/root/.fluxbox/keys
/root/.fluxbox/styles
/root/.fluxbox/apps
/root/.fluxbox/backgrounds
/root/.fluxbox/startup
/root/.fluxbox/init
/root/.fluxbox/lastwallpaper
/root/.fluxbox/overlay
/root/.fluxbox/pixmaps
/root/.fluxbox/menu
/root/.ssh
/root/.ssh/known_hosts
/root/.ssh/authorized_keys
/root/.profile
/root/reset_logs.sh
/root/.bash_history

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
                                                                                                               
╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root daemon 144 Feb 20  2007 /etc/at.deny                                                         

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                              
/dev/shm                                                                                                       
/tmp
/tmp/.ICE-unix
/tmp/.X11-unix
/tmp/distcc_38a77ba8.stderr
/tmp/distcc_3b5b7ba8.stdout
/tmp/distccd_3b147ba8.o
#)You_can_write_even_more_files_inside_last_directory

/usr/bin/at
/var/lib/php5
/var/lock
/var/spool/cron
/var/spool/cron/atjobs
/var/spool/cron/atjobs/.SEQ
/var/spool/cron/atspool
/var/tmp

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                              
  Group daemon:                                                                                                
/var/spool/cron/atjobs                                                                                         
/var/spool/cron/atspool



                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════                            
                            ╚═════════════════════════╝                                                        
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                     
/usr/bin/gettext.sh                                                                                            

╔══════════╣ Executable files potentially added by user (limit 70)
                                                                                                               
╔══════════╣ Unexpected in root
/initrd.img.old                                                                                                
/initrd
/initrd.img
/nohup.out
/vmlinuz
/vmlinuz.old

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/var/log/auth.log                                                                                              
/var/log/syslog
/tmp/distcc_38a77ba8.stderr


╔══════════╣ Files inside /home/daemon (limit 20)
                                                                                                               
╔══════════╣ Files inside others home (limit 20)
/home/service/.profile                                                                                         
/home/service/.bashrc
/home/service/.bash_logout
/home/makis/user.txt
/home/makis/.profile
/home/makis/.sudo_as_admin_successful
/home/makis/.bash_history
/home/makis/.bashrc
/home/makis/.bash_logout
/home/user/.profile
/home/user/.bash_history
/home/user/.bashrc
/home/user/.bash_logout
/root/.gstreamer-0.10/registry.i486.xml
/root/.rhosts
/root/vnc.log
/root/.fluxbox/windowmenu
/root/.fluxbox/keys
/root/.fluxbox/apps
/root/.fluxbox/startup

╔══════════╣ Searching installed mail applications
postfix                                                                                                        
sendmail

╔══════════╣ Mails (limit 50)
 67581    4 -rw-------   1 root     mail         1438 Mar 14  2017 /var/mail/root                              
 67581    4 -rw-------   1 root     mail         1438 Mar 14  2017 /var/spool/mail/root

╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 1725 Mar 28  2008 /usr/share/mysql/mysql-test/t/ndb_backup_print.test                   
-rwxr-xr-x 1 root root 107 Mar 28  2008 /usr/share/mysql/mysql-test/t/backup-master.sh
-rw-r--r-- 1 root root 2050 Mar 28  2008 /usr/share/mysql/mysql-test/t/backup.test
-rw-r--r-- 1 root root 508 Mar 28  2008 /usr/share/mysql/mysql-test/include/ndb_backup_print.inc
-rw-r--r-- 1 root root 955 Mar 28  2008 /usr/share/mysql/mysql-test/include/ndb_backup.inc
-rw-r--r-- 1 root root 1662 Mar 28  2008 /usr/share/mysql/mysql-test/r/ndb_backup_print.result
-rw-r--r-- 1 root root 2040 Mar 28  2008 /usr/share/mysql/mysql-test/r/backup.result
-rw-r--r-- 1 root root 3669 May 20  2012 /usr/share/info/dir.old
-rwxr-xr-x 1 root root 5703 Oct 24  2007 /usr/share/quilt/scripts/backup-files
-rw-r--r-- 1 root root 629 Sep 23  2010 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 1225 Apr 28  2010 /usr/share/man/man8/tdbbackup.8.gz
-rw-r--r-- 1 root root 194838 May 13  2008 /usr/share/doc/x11-common/changelog.Debian.old.gz
-rw-r--r-- 1 root root 317 Mar 28  2008 /usr/share/doc/hdparm/changelog.old.gz
-rw-r--r-- 1 root root 7885 Dec 17  2006 /usr/share/doc/telnet/README.telnet.old.gz
-rwxr-xr-x 1 root root 29888 Nov  3  2020 /usr/lib/vmware-tools/plugins32/vmsvc/libvmbackup.so
-rwxr-xr-x 1 root root 34632 Nov  3  2020 /usr/lib/vmware-tools/plugins64/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 7970844 Oct 31  2020 /boot/initrd.img-2.6.24-16-server.bak
-rw-r--r-- 1 root root 7969070 Oct 31  2020 /boot/initrd.img-2.6.24-32-server.bak
-rw-r--r-- 1 root root 530 Oct 31  2020 /etc/blkid.tab.old
-rw-r--r-- 1 root root 335 Oct 26  2004 /etc/sgml/catalog.old
-rw-r--r-- 1 root root 198 Mar 16  2010 /var/lib/belocs/hashfile.old
-rw-r--r-- 1 root root 2009845 Apr 28  2010 /var/lib/aptitude/pkgstates.old
-rw-r--r-- 1 root root 3731 May 20  2012 /var/backups/infodir.bak

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /etc/aliases.db: Berkeley DB (Hash, version 9, native byte-order)                                        
Found /etc/apparmor/severity.db: ASCII Pascal program text
Found /var/lib/gcj-4.2/classmap.db: data
Found /var/lib/mlocate/mlocate.db: writable, regular file, no read permission
Found /var/lib/postfix/smtp_scache.db: writable, regular file, no read permission
Found /var/lib/postfix/smtpd_scache.db: writable, regular file, no read permission


╔══════════╣ Web files?(output limit)
/var/www/:                                                                                                     
total 8.0K
drwxr-xr-x  2 www-data www-data 4.0K Mar 14  2017 .
drwxr-xr-x 15 root     root     4.0K May 20  2012 ..

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 makis makis 220 Mar 14  2017 /home/makis/.bash_logout                                             
-rw-r--r-- 1 1001 1001 220 Mar 31  2010 /home/user/.bash_logout
-rw-r--r-- 1 root root 5 Dec  5  2007 /usr/share/python-support/antlr/.version
-rw-r--r-- 1 root root 2188 May 20  2012 /usr/share/snmp/mibs/.index
-rw-r--r-- 1 root root 0 May 20  2012 /usr/lib/firefox-3.6.17/.autoreg
-rw-r--r-- 1 root root 1258 Mar 10  2008 /usr/lib/jvm/.java-gcj.jinfo
--w------- 1 root root 0 May  9 16:49 /proc/fs/nfsd/.unexport
--w------- 1 root root 0 May  9 16:49 /proc/fs/nfsd/.export
--w------- 1 root root 0 May  9 16:49 /proc/fs/nfsd/.del
--w------- 1 root root 0 May  9 16:49 /proc/fs/nfsd/.add
--w------- 1 root root 0 May  9 16:49 /proc/fs/nfsd/.svc
-rw-r--r-- 1 root root 220 Apr 14  2008 /etc/skel/.bash_logout
-rw------- 1 root root 0 Mar 16  2010 /etc/.pwd.lock
-rw-r--r-- 1 root root 0 May  9 16:49 /dev/.initramfs-tools
-rw------- 1 postgres postgres 34 May  9 17:47 /var/run/postgresql/.s.PGSQL.5432.lock
-rw-r--r-- 1 root root 34 May 13  2012 /var/lib/python-support/python2.5/.path
-rw------- 1 daemon daemon 2 Mar 16  2010 /var/spool/cron/atjobs/.SEQ
-r--r--r-- 1 root root 11 May  9 16:49 /tmp/.X0-lock

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                                                                         
-rwxr-xr-x 1 daemon daemon 860323 Apr 23  2024 /tmp/linpeas.sh                                                 
-rw------- 1 daemon daemon 3360 May  9 18:44 /tmp/distcc_38a77ba8.stderr
-rw-r--r-- 1 daemon daemon 0 May  9 18:03 /tmp/distcc_3b5b7ba8.stdout
-rw------- 1 daemon daemon 0 May  9 18:03 /tmp/distccd_3b147ba8.o
-rw------- 1 daemon daemon 10 May  9 18:03 /tmp/distccd_3b267ba8.i
-r--r--r-- 1 root root 11 May  9 16:49 /tmp/.X0-lock
-rw-r--r-- 1 root root 1600 May  9 16:49 /tmp/vgauthsvclog.txt.0
-rw-r--r-- 1 root root 2009845 Apr 28  2010 /var/backups/aptitude.pkgstates.0
-rw-r--r-- 1 root root 3731 May 20  2012 /var/backups/infodir.bak

╔══════════╣ Searching passwords in history files
                                                                                                               
╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/etc/bind/rndc.key                                                                                             
/etc/mysql/conf.d/old_passwords.cnf
/etc/pam.d/common-password
/usr/lib/pppd/2.4.4/passwordfd.so
/usr/share/doc/p7zip-full/DOCS/MANUAL/switches/password.htm
/usr/share/man/man3/des_read_2passwords.3ssl.gz
/usr/share/man/man3/des_read_password.3ssl.gz
/usr/share/man/man7/credentials.7.gz
/usr/share/pam/common-password
/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs
                                                                                                               
╔══════════╣ Searching passwords inside logs (limit 70)
Description: Set up users and passwords                                                                        
May  5 16:31:42 lame /etc/mysql/debian-start[5297]: WARNING: mysql.user contains 1 root accounts without password!
May  9 16:49:32 lame /etc/mysql/debian-start[5223]: WARNING: mysql.user contains 1 root accounts without password!
May  9 16:50:10 lame VGAuth[4437]: vmtoolsd: Username and password successfully validated for 'root'.
May  9 16:50:11 lame VGAuth[4437]: vmtoolsd: Username and password successfully validated for 'root'.
May  9 16:50:12 lame VGAuth[4437]: vmtoolsd: Username and password successfully validated for 'root'.
May  9 16:50:13 lame VGAuth[4437]: vmtoolsd: Username and password successfully validated for 'root'.
May  9 17:23:32 lame sshd[5834]: Failed password for invalid user user from 10.10.14.9 port 52304 ssh2
May  9 17:23:38 lame sshd[5834]: Failed password for invalid user user from 10.10.14.9 port 52304 ssh2
May  9 17:23:50 lame sshd[5834]: Failed password for invalid user user from 10.10.14.9 port 52304 ssh2
May  9 17:24:17 lame sshd[5837]: Failed password for invalid user user from 10.10.14.9 port 52206 ssh2
May  9 17:24:24 lame sshd[5837]: Failed password for invalid user user from 10.10.14.9 port 52206 ssh2
May  9 17:24:31 lame sshd[5837]: Failed password for invalid user user from 10.10.14.9 port 52206 ssh2
May  9 17:37:56 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:37:59 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:01 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:03 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:05 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:08 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:10 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:11 lame sshd[5869]: Failed password for invalid user user from 10.10.14.9 port 33478 ssh2
May  9 17:38:24 lame sshd[5872]: Failed password for invalid user user from 10.10.14.9 port 48336 ssh2
May  9 17:38:24 lame sshd[5873]: Failed password for invalid user user from 10.10.14.9 port 48350 ssh2
May  9 17:38:24 lame sshd[5874]: Failed password for invalid user user from 10.10.14.9 port 48356 ssh2
May  9 17:38:24 lame sshd[5875]: Failed password for invalid user user from 10.10.14.9 port 48370 ssh2
May  9 17:38:24 lame sshd[5876]: Failed password for invalid user user from 10.10.14.9 port 48392 ssh2
May  9 17:38:24 lame sshd[5877]: Failed password for invalid user user from 10.10.14.9 port 48380 ssh2
May  9 17:38:24 lame sshd[5878]: Failed password for invalid user user from 10.10.14.9 port 48396 ssh2
May  9 17:38:24 lame sshd[5879]: Failed password for invalid user user from 10.10.14.9 port 48414 ssh2
May  9 17:38:24 lame sshd[5880]: Failed password for invalid user user from 10.10.14.9 port 48400 ssh2
May  9 17:38:24 lame sshd[5881]: Failed password for invalid user user from 10.10.14.9 port 48424 ssh2
May  9 17:38:26 lame sshd[5872]: Failed password for invalid user user from 10.10.14.9 port 48336 ssh2
May  9 17:38:26 lame sshd[5873]: Failed password for invalid user user from 10.10.14.9 port 48350 ssh2
May  9 17:38:26 lame sshd[5874]: Failed password for invalid user user from 10.10.14.9 port 48356 ssh2
May  9 17:38:26 lame sshd[5875]: Failed password for invalid user user from 10.10.14.9 port 48370 ssh2
May  9 17:38:26 lame sshd[5876]: Failed password for invalid user user from 10.10.14.9 port 48392 ssh2
May  9 17:38:26 lame sshd[5877]: Failed password for invalid user user from 10.10.14.9 port 48380 ssh2
May  9 17:38:26 lame sshd[5878]: Failed password for invalid user user from 10.10.14.9 port 48396 ssh2
May  9 17:38:26 lame sshd[5879]: Failed password for invalid user user from 10.10.14.9 port 48414 ssh2
May  9 17:38:26 lame sshd[5880]: Failed password for invalid user user from 10.10.14.9 port 48400 ssh2
May  9 17:38:26 lame sshd[5881]: Failed password for invalid user user from 10.10.14.9 port 48424 ssh2
May  9 17:38:28 lame sshd[5872]: Failed password for invalid user user from 10.10.14.9 port 48336 ssh2
May  9 17:38:28 lame sshd[5873]: Failed password for invalid user user from 10.10.14.9 port 48350 ssh2
May  9 17:38:28 lame sshd[5874]: Failed password for invalid user user from 10.10.14.9 port 48356 ssh2
May  9 17:38:28 lame sshd[5875]: Failed password for invalid user user from 10.10.14.9 port 48370 ssh2
May  9 17:38:28 lame sshd[5876]: Failed password for invalid user user from 10.10.14.9 port 48392 ssh2
May  9 17:38:28 lame sshd[5877]: Failed password for invalid user user from 10.10.14.9 port 48380 ssh2
May  9 17:38:28 lame sshd[5878]: Failed password for invalid user user from 10.10.14.9 port 48396 ssh2
May  9 17:38:28 lame sshd[5879]: Failed password for invalid user user from 10.10.14.9 port 48414 ssh2
May  9 17:38:28 lame sshd[5880]: Failed password for invalid user user from 10.10.14.9 port 48400 ssh2
May  9 17:38:28 lame sshd[5881]: Failed password for invalid user user from 10.10.14.9 port 48424 ssh2
May  9 17:38:30 lame sshd[5872]: Failed password for invalid user user from 10.10.14.9 port 48336 ssh2
May  9 17:38:30 lame sshd[5873]: Failed password for invalid user user from 10.10.14.9 port 48350 ssh2
May  9 17:38:30 lame sshd[5874]: Failed password for invalid user user from 10.10.14.9 port 48356 ssh2
May  9 17:38:30 lame sshd[5875]: Failed password for invalid user user from 10.10.14.9 port 48370 ssh2
May  9 17:38:30 lame sshd[5876]: Failed password for invalid user user from 10.10.14.9 port 48392 ssh2
May  9 17:38:30 lame sshd[5877]: Failed password for invalid user user from 10.10.14.9 port 48380 ssh2
May  9 17:38:30 lame sshd[5878]: Failed password for invalid user user from 10.10.14.9 port 48396 ssh2
May  9 17:38:30 lame sshd[5879]: Failed password for invalid user user from 10.10.14.9 port 48414 ssh2
May  9 17:38:30 lame sshd[5880]: Failed password for invalid user user from 10.10.14.9 port 48400 ssh2
May  9 17:38:30 lame sshd[5881]: Failed password for invalid user user from 10.10.14.9 port 48424 ssh2
May  9 17:38:32 lame sshd[5872]: Failed password for invalid user user from 10.10.14.9 port 48336 ssh2
May  9 17:38:32 lame sshd[5873]: Failed password for invalid user user from 10.10.14.9 port 48350 ssh2
May  9 17:38:32 lame sshd[5874]: Failed password for invalid user user from 10.10.14.9 port 48356 ssh2
May  9 17:38:32 lame sshd[5875]: Failed password for invalid user user from 10.10.14.9 port 48370 ssh2
May  9 17:38:32 lame sshd[5876]: Failed password for invalid user user from 10.10.14.9 port 48392 ssh2
May  9 17:38:32 lame sshd[5877]: Failed password for invalid user user from 10.10.14.9 port 48380 ssh2
May  9 17:38:32 lame sshd[5878]: Failed password for invalid user user from 10.10.14.9 port 48396 ssh2
May  9 17:38:32 lame sshd[5879]: Failed password for invalid user user from 10.10.14.9 port 48414 ssh2
May  9 17:38:32 lame sshd[5880]: Failed password for invalid user user from 10.10.14.9 port 48400 ssh2



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                             
                                ╚════════════════╝                                                             
Regexes to search for API keys aren't activated, use param '-r' 


^C
                                                                                                               
┌──(kali㉿proxli)-[~/exploits]
└─$ 

```

mysql login root ""

╔══════════╣ Analyzing SSH Files (limit 70)                                                                    
                                                                                                               

-rw-r--r-- 1 root root 442 May 20  2012 /root/.ssh/known_hosts
|1|gS7DWzAxRvtufzEYnaW40GOvYu0=|5afWvF6s4R5Yaog0mimuOyNfXiI= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAstqnuFMBOZvO3WTEjP4TUdjgWkIVNdTq6kboEDjteOfc65TlI7sRvQBwqAhQjeeyyIk8T55gMDkOD0akSlSXvLDcmcdYfxeIF0ZSuT+nkRhij7XSSA/Oc5QSk3sJ/SInfb78e3anbRHpmkJcVgETJ5WhKObUNf1AKZW++4Xlc63M4KI5cjvMMIPEVOyR3AKmI78Fo3HJjYucg87JjLeC66I7+dlEYX6zT8i1XYwa/L1vZ3qSJISGVu8kRPikMv/cNSvki4j+qDYyZ2E5497W87+Ed46/8P42LNGoOV8OcX/ro6pAcbEPUdUEfkJrqi2YXbhvwIJ0gFMb6wfe5cnQew==


-rw-r--r-- 1 root root 405 May 17  2010 /root/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApmGJFZNl0ibMNALQx7M6sGGoi4KNmj6PVxpbpG70lShHQqldJkcteZZdPFSbW76IUiPR0Oh+WBV0x1c6iPL/0zUYFHyFKAz1e6/5teoweG1jr2qOffdomVhvXXvSjGaSFwwOYB8R0QxsOWWTQTYSeBa66X6e777GVkHCDLYgZSo8wWr5JXln/Tw7XotowHr8FEGvw2zW1krU3Zo9Bzp0e0ac2U+qUGIzIu/WwgztLZs5/D9IyhtRWocyQPE+kcP+Jz2mt4y1uA73KqoXfdw5oGUkxdFo9f1nu2OwkjOc+Wv8Vw7bwkf+1RgiOMgiJ5cCs4WocyVxsXovcNnbALTp3w== msfadmin@metasploitable

-rw-r--r-- 1 root root 609 Apr 28  2010 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 401 Apr 28  2010 /etc/ssh/ssh_host_rsa_key.pub

Port 22
PermitRootLogin yes
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes


```sh
daemon@lame:/tmp$ ls -la /etc/ssl/certs/
total 12
drwxr-xr-x 2 root root 4096 Mar 17  2010 .
drwxr-xr-x 4 root root 4096 Mar 17  2010 ..
lrwxrwxrwx 1 root root   21 Apr 28  2010 1f4bb285 -> ssl-cert-snakeoil.pem
-rw-r--r-- 1 root root 1224 Mar 17  2010 ssl-cert-snakeoil.pem
daemon@lame:/tmp$ cat ssl-cert-snakeoil.pem
cat: ssl-cert-snakeoil.pem: No such file or directory
daemon@lame:/tmp$ cat /etc/ssl/certs/ssl-cert-snakeoil.pem
-----BEGIN CERTIFICATE-----
MIIDWzCCAsQCCQD6+TpMf7a5zDANBgkqhkiG9w0BAQUFADCB8TELMAkGA1UEBhMC
WFgxKjAoBgNVBAgTIVRoZXJlIGlzIG5vIHN1Y2ggdGhpbmcgb3V0c2lkZSBVUzET
MBEGA1UEBxMKRXZlcnl3aGVyZTEOMAwGA1UEChMFT0NPU0ExPDA6BgNVBAsTM09m
ZmljZSBmb3IgQ29tcGxpY2F0aW9uIG9mIE90aGVyd2lzZSBTaW1wbGUgQWZmYWly
czEjMCEGA1UEAxMadWJ1bnR1ODA0LWJhc2UubG9jYWxkb21haW4xLjAsBgkqhkiG
9w0BCQEWH3Jvb3RAdWJ1bnR1ODA0LWJhc2UubG9jYWxkb21haW4wHhcNMTAwMzE3
MTQwNzQ1WhcNMTAwNDE2MTQwNzQ1WjCB8TELMAkGA1UEBhMCWFgxKjAoBgNVBAgT
IVRoZXJlIGlzIG5vIHN1Y2ggdGhpbmcgb3V0c2lkZSBVUzETMBEGA1UEBxMKRXZl
cnl3aGVyZTEOMAwGA1UEChMFT0NPU0ExPDA6BgNVBAsTM09mZmljZSBmb3IgQ29t
cGxpY2F0aW9uIG9mIE90aGVyd2lzZSBTaW1wbGUgQWZmYWlyczEjMCEGA1UEAxMa
dWJ1bnR1ODA0LWJhc2UubG9jYWxkb21haW4xLjAsBgkqhkiG9w0BCQEWH3Jvb3RA
dWJ1bnR1ODA0LWJhc2UubG9jYWxkb21haW4wgZ8wDQYJKoZIhvcNAQEBBQADgY0A
MIGJAoGBANa0EzYzmpVxexvefIN12nGxPKl//q1kG3fpT66+ytT4y++uu0N5JHP/
POWeO238yLGs+kxNXptMmVQL16hKULqp3h0f9ORrAqP0a0XNTK+NiWIzj2W7NmGf
xCxzwU4uoKgUTphwRmG70bkx34yZ7nVreTxAoK6XAJCd3JkNM6S1AgMBAAEwDQYJ
KoZIhvcNAQEFBQADgYEAkqS0uBRVYyVRSgvDKiLPOvgXagzPZqqnZS9Ibc3jPlyf
d2zURFQfHoRPjtSN3awtiAkhqNpWLKkFPEloNRl1DNpTI4iIGS10JsEiZe4RaINq
U0qcJ8ugtOmNKQyyPBhcZ8xTph4w0Komex6uQLkpAWwuvKIZlHwVbo0wOPbKLnU=
-----END CERTIFICATE-----
daemon@lame:/tmp$ 

```