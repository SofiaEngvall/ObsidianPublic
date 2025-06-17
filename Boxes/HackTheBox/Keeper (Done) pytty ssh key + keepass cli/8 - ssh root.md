
```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ ssh -i id_rsa root@10.129.229.41 
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-78-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

You have new mail.
Last login: Tue Aug  8 19:00:06 2023 from 10.10.14.41

root@keeper:~# ls -la
total 85384
drwx------  5 root root     4096 Jun 16 15:38 .
drwxr-xr-x 18 root root     4096 Jul 27  2023 ..
lrwxrwxrwx  1 root root        9 May 24  2023 .bash_history -> /dev/null
-rw-r--r--  1 root root     3106 Dec  5  2019 .bashrc
drwx------  2 root root     4096 May 24  2023 .cache
-rw-------  1 root root       20 Jul 27  2023 .lesshst
lrwxrwxrwx  1 root root        9 May 24  2023 .mysql_history -> /dev/null
-rw-r--r--  1 root root      161 Dec  5  2019 .profile
-rw-r-----  1 root root       33 Jun 16 15:38 root.txt
-rw-r--r--  1 root root 87391651 Jul 25  2023 RT30000.zip
drwxr-xr-x  2 root root     4096 Jul 25  2023 SQL
drwxr-xr-x  2 root root     4096 May 24  2023 .ssh
-rw-r--r--  1 root root       39 Jul 20  2023 .vimrc

root@keeper:~# cat root.txt
ffc5130059ae5ff0f8e2bb59b9fb18e8
```
