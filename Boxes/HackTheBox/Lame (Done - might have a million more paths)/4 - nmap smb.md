
```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.10.3
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-09 21:23 CEST
Nmap scan report for 10.10.10.3
Host is up (0.025s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-users: 
|   LAME\backup (RID: 1068)
|     Full name:   backup
|     Flags:       Account disabled, Normal user account
|   LAME\bin (RID: 1004)
|     Full name:   bin
|     Flags:       Account disabled, Normal user account
|   LAME\bind (RID: 1210)
|     Flags:       Account disabled, Normal user account
|   LAME\daemon (RID: 1002)
|     Full name:   daemon
|     Flags:       Account disabled, Normal user account
|   LAME\dhcp (RID: 1202)
|     Flags:       Account disabled, Normal user account
|   LAME\distccd (RID: 1222)
|     Flags:       Account disabled, Normal user account
|   LAME\ftp (RID: 1214)
|     Flags:       Account disabled, Normal user account
|   LAME\games (RID: 1010)
|     Full name:   games
|     Flags:       Account disabled, Normal user account
|   LAME\gnats (RID: 1082)
|     Full name:   Gnats Bug-Reporting System (admin)
|     Flags:       Account disabled, Normal user account
|   LAME\irc (RID: 1078)
|     Full name:   ircd
|     Flags:       Account disabled, Normal user account
|   LAME\klog (RID: 1206)
|     Flags:       Account disabled, Normal user account
|   LAME\libuuid (RID: 1200)
|     Flags:       Account disabled, Normal user account
|   LAME\list (RID: 1076)
|     Full name:   Mailing List Manager
|     Flags:       Account disabled, Normal user account
|   LAME\lp (RID: 1014)
|     Full name:   lp
|     Flags:       Account disabled, Normal user account
|   LAME\mail (RID: 1016)
|     Full name:   mail
|     Flags:       Account disabled, Normal user account
|   LAME\man (RID: 1012)
|     Full name:   man
|     Flags:       Account disabled, Normal user account
|   LAME\msfadmin (RID: 3000)
|     Full name:   msfadmin,,,
|     Flags:       Normal user account
|   LAME\mysql (RID: 1218)
|     Full name:   MySQL Server,,,
|     Flags:       Account disabled, Normal user account
|   LAME\news (RID: 1018)
|     Full name:   news
|     Flags:       Account disabled, Normal user account
|   LAME\nobody (RID: 501)
|     Full name:   nobody
|     Flags:       Account disabled, Normal user account
|   LAME\postfix (RID: 1212)
|     Flags:       Account disabled, Normal user account
|   LAME\postgres (RID: 1216)
|     Full name:   PostgreSQL administrator,,,
|     Flags:       Account disabled, Normal user account
|   LAME\proftpd (RID: 1226)
|     Flags:       Account disabled, Normal user account
|   LAME\proxy (RID: 1026)
|     Full name:   proxy
|     Flags:       Account disabled, Normal user account
|   LAME\root (RID: 1000)
|     Full name:   root
|     Flags:       Account disabled, Normal user account
|   LAME\service (RID: 3004)
|     Full name:   ,,,
|     Flags:       Account disabled, Normal user account
|   LAME\sshd (RID: 1208)
|     Flags:       Account disabled, Normal user account
|   LAME\sync (RID: 1008)
|     Full name:   sync
|     Flags:       Account disabled, Normal user account
|   LAME\sys (RID: 1006)
|     Full name:   sys
|     Flags:       Account disabled, Normal user account
|   LAME\syslog (RID: 1204)
|     Flags:       Account disabled, Normal user account
|   LAME\telnetd (RID: 1224)
|     Flags:       Account disabled, Normal user account
|   LAME\tomcat55 (RID: 1220)
|     Flags:       Account disabled, Normal user account
|   LAME\user (RID: 3002)
|     Full name:   just a user,111,,
|     Flags:       Normal user account
|   LAME\uucp (RID: 1020)
|     Full name:   uucp
|     Flags:       Account disabled, Normal user account
|   LAME\www-data (RID: 1066)
|     Full name:   www-data
|_    Flags:       Account disabled, Normal user account
| smb-enum-shares: 
|   account_used: <blank>
|   \\10.10.10.3\ADMIN$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: <none>
|   \\10.10.10.3\IPC$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|   \\10.10.10.3\opt: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: <none>
|   \\10.10.10.3\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|   \\10.10.10.3\tmp: 
|     Type: STYPE_DISKTREE
|     Comment: oh noes!
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE

Nmap done: 1 IP address (1 host up) scanned in 39.43 seconds
```

| smb-enum-users: 

|   LAME\distccd (RID: 1222)
|     Flags:       Account disabled, Normal user account

|   LAME\msfadmin (RID: 3000)
|     Full name:   msfadmin,,,
|     Flags:       Normal user account

|   LAME\user (RID: 3002)
|     Full name:   just a user,111,,
|     Flags:       Normal user account

The account we found out should exist is disabled
But we have two other users

| smb-enum-shares: 

|   account_used: `<blank>`

|   \\10.10.10.3\IPC$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Path: C:\tmp
|     Anonymous access: READ/WRITE

|   \\10.10.10.3\tmp: 
|     Type: STYPE_DISKTREE
|     Comment: oh noes!
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE

Let's check out `\\10.10.10.3\tmp`
