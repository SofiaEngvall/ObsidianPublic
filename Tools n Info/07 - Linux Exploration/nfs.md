
NFS (Network File Sharing)

[[nfs - no_root_squash]]
Configuration file `/etc/exports`

`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.212.230`


enum by nmap
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.212.230
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-20 03:37 CEST
Nmap scan report for 10.10.212.230
Host is up (0.040s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *

Nmap done: 1 IP address (1 host up) scanned in 0.83 seconds
```

enum by showmount
```sh
┌──(kali㉿kali)-[~]
└─$ showmount -e 10.10.103.212
Export list for 10.10.103.212:
/home/ubuntu/sharedfolder *
/tmp                      *
/home/backup              *
  
```

