
```sh
┌──(kali㉿proxli)-[~]
└─$ ssh lnorgaard@10.129.229.41
lnorgaard@10.129.229.41´s password: 
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-78-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
You have mail.
Last login: Tue Aug  8 11:31:22 2023 from 10.10.14.23

lnorgaard@keeper:~$ ls -la
total 85384
drwxr-xr-x 4 lnorgaard lnorgaard     4096 Jul 25  2023 .
drwxr-xr-x 3 root      root          4096 May 24  2023 ..
lrwxrwxrwx 1 root      root             9 May 24  2023 .bash_history -> /dev/null
-rw-r--r-- 1 lnorgaard lnorgaard      220 May 23  2023 .bash_logout
-rw-r--r-- 1 lnorgaard lnorgaard     3771 May 23  2023 .bashrc
drwx------ 2 lnorgaard lnorgaard     4096 May 24  2023 .cache
-rw------- 1 lnorgaard lnorgaard      807 May 23  2023 .profile
-rw-r--r-- 1 root      root      87391651 Jun 16 17:42 RT30000.zip
drwx------ 2 lnorgaard lnorgaard     4096 Jul 24  2023 .ssh
-rw-r----- 1 root      lnorgaard       33 Jun 16 15:38 user.txt
-rw-r--r-- 1 root      root            39 Jul 20  2023 .vimrc

lnorgaard@keeper:~$ cat user.txt
6bee33b74fde77d48fcb8392e76e0a11
```

Interesting file RT30000.zip, let's download

```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ scp lnorgaard@10.129.229.41:/home/lnorgaard/RT30000.zip .
lnorgaard@10.129.229.41´s password: 
RT30000.zip                                                                  100%   83MB   6.4MB/s   00:13
```


