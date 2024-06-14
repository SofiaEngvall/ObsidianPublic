
```sh
┌──(kali㉿kali)-[~/thm/gamezone]
└─$ ssh agent47@10.10.186.198
The authenticity of host '10.10.186.198 (10.10.186.198)' can't be established.
ED25519 key fingerprint is SHA256:CyJgMM67uFKDbNbKyUM0DexcI+LWun63SGLfBvqQcLA.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.186.198' (ED25519) to the list of known hosts.
agent47@10.10.186.198's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-159-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

109 packages can be updated.
68 updates are security updates.


Last login: Fri Aug 16 17:52:04 2019 from 192.168.1.147
agent47@gamezone:~$ ls -la
total 28
drwxr-xr-x 3 agent47 agent47 4096 Aug 16  2019 .
drwxr-xr-x 3 root    root    4096 Aug 14  2019 ..
lrwxrwxrwx 1 root    root       9 Aug 16  2019 .bash_history -> /dev/null
-rw-r--r-- 1 agent47 agent47  220 Aug 14  2019 .bash_logout
-rw-r--r-- 1 agent47 agent47 3771 Aug 14  2019 .bashrc
drwx------ 2 agent47 agent47 4096 Aug 16  2019 .cache
-rw-r--r-- 1 agent47 agent47  655 Aug 14  2019 .profile
-rw-rw-r-- 1 agent47 agent47   33 Aug 16  2019 user.txt
agent47@gamezone:~$ cat user.txt
649ac17b1480ac13ef1e4fa579dac95c
```

```sh
agent47@gamezone:~$ ss -tulpn
Netid  State      Recv-Q Send-Q               Local Address:Port                              Peer Address:Port              
udp    UNCONN     0      0                                *:10000                                        *:*                  
udp    UNCONN     0      0                                *:68                                           *:*                  
tcp    LISTEN     0      80                       127.0.0.1:3306                                         *:*                  
tcp    LISTEN     0      128                              *:10000                                        *:*                  
tcp    LISTEN     0      128                              *:22                                           *:*                  
tcp    LISTEN     0      128                             :::80                                          :::*                  
tcp    LISTEN     0      128                             :::22                                          :::*                  
agent47@gamezone:~$ 
```
