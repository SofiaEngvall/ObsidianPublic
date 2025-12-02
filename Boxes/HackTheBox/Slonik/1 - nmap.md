
```sh
┌──(fixit42㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.129.234.160
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-19 23:03 CEST
Nmap scan report for 10.129.234.160
Host is up (0.025s latency).
Not shown: 65527 closed tcp ports (reset)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 2d:8d:0a:43:a7:58:20:73:6b:8c:fc:b0:d1:2f:45:07 (ECDSA)
|_  256 82:fb:90:b0:eb:ac:20:a2:53:5e:3c:7c:d3:3c:34:79 (ED25519)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      34009/udp   mountd
|   100005  1,2,3      34695/udp6  mountd
|   100005  1,2,3      38009/tcp6  mountd
|   100005  1,2,3      52987/tcp   mountd
|   100021  1,3,4      39145/tcp   nlockmgr
|   100021  1,3,4      42539/tcp6  nlockmgr
|   100021  1,3,4      43117/udp   nlockmgr
|   100021  1,3,4      59454/udp6  nlockmgr
|   100024  1          33686/udp   status
|   100024  1          45693/tcp6  status
|   100024  1          56673/tcp   status
|   100024  1          59056/udp6  status
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/tcp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
39129/tcp open  mountd   1-3 (RPC #100005)
39145/tcp open  nlockmgr 1-4 (RPC #100021)
42385/tcp open  mountd   1-3 (RPC #100005)
52987/tcp open  mountd   1-3 (RPC #100005)
56673/tcp open  status   1 (RPC #100024)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.46 seconds
```

ports 22, 111 rpc, nfs ...

nfs
```sh
┌──(fixit42㉿kali)-[~]
└─$ nmap -p111 --script=nfs* 10.129.234.160
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-19 23:05 CEST
Nmap scan report for 10.129.234.160
Host is up (0.025s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-ls: Volume /var/backups
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE     TIME                 FILENAME
| rwxr-xr-x   0    0    4096     2025-10-19T21:04:04  .
| ??????????  ?    ?    ?        ?                    ..
| rw-r--r--   0    0    4666455  2025-10-19T21:03:04  archive-2025-10-19T2103.zip
| rw-r--r--   0    0    4666456  2025-10-19T21:04:04  archive-2025-10-19T2104.zip
| 
| 
| Volume /home
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID   GID   SIZE  TIME                 FILENAME
| ??????????  ?     ?     ?     ?                    .
| ??????????  ?     ?     ?     ?                    ..
| rwxr-x---   1337  1337  4096  2025-09-22T12:46:40  service
|_
| nfs-statfs: 
|   Filesystem    1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|   /var/backups  6915100.0  2960152.0  3866404.0  44%   16.0T        32000
|_  /home         6915100.0  2960160.0  3866396.0  44%   16.0T        32000
| nfs-showmount: 
|   /var/backups *
|_  /home *

Nmap done: 1 IP address (1 host up) scanned in 1.43 seconds
```
