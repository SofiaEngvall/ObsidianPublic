
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse skynet.thm  
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-14 14:13 CEST
Nmap scan report for skynet.thm (10.10.155.35)
Host is up (0.041s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.155.35\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (skynet server (Samba, Ubuntu))
|     Users: 2
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.155.35\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: Skynet Anonymous Share
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\srv\samba
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.155.35\milesdyson: 
|     Type: STYPE_DISKTREE
|     Comment: Miles Dyson Personal Share
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\milesdyson\share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.155.35\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
| smb-enum-users: 
|   SKYNET\milesdyson (RID: 1000)
|     Full name:   
|     Description: 
|_    Flags:       Normal user account

Nmap done: 1 IP address (1 host up) scanned in 8.03 seconds
```

```sh
┌──(kali㉿kali)-[~/thm/skynet]
└─$ smbget --recursive smb://skynet.thm/anonymous
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
Using netbios name KALI.
Using workgroup WORKGROUP.
Password for [WORKGROUP\kali]:
Using domain: WORKGROUP, user: kali
Server connect ok: //skynet.thm/anonymous: 0x55d52e4ee240
smb://skynet.thm/anonymous/attention.txt                                                                                     
smb://skynet.thm/anonymous/logs/log2.txt                                                                                      
smb://skynet.thm/anonymous/logs/log1.txt                                                                                      
smb://skynet.thm/anonymous/logs/log3.txt                                                                                      
Downloaded 634b in 14 seconds
```

```sh
┌──(kali㉿kali)-[~/thm/skynet]
└─$ cat attention.txt 
A recent system malfunction has caused various passwords to be changed. All skynet employees are required to change their password after seeing this.
-Miles Dyson
```

```sh
┌──(kali㉿kali)-[~/thm/skynet/logs]
└─$ cat log1.txt     
cyborg007haloterminator
terminator22596
terminator219
terminator20
terminator1989
terminator1988
terminator168
terminator16
terminator143
terminator13
terminator123!@#
terminator1056
terminator101
terminator10
terminator02
terminator00
roboterminator
pongterminator
manasturcaluterminator
exterminator95
exterminator200
dterminator
djxterminator
dexterminator
determinator
cyborg007haloterminator
avsterminator
alonsoterminator
Walterminator
79terminator6
1996terminator
```


