
```sh
┌──(kali㉿proxli)-[~]
└─$ nxc smb 10.10.106.240 -u "svc-admin" -p "management2005" --shares
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [*] Windows 10 / Server 2019 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [+] spookysec.local\svc-admin:management2005 
SMB         10.10.106.240   445    ATTACKTIVEDIREC  [*] Enumerated shares
SMB         10.10.106.240   445    ATTACKTIVEDIREC  Share           Permissions     Remark
SMB         10.10.106.240   445    ATTACKTIVEDIREC  -----           -----------     ------
SMB         10.10.106.240   445    ATTACKTIVEDIREC  ADMIN$                          Remote Admin
SMB         10.10.106.240   445    ATTACKTIVEDIREC  backup          READ            
SMB         10.10.106.240   445    ATTACKTIVEDIREC  C$                              Default share
SMB         10.10.106.240   445    ATTACKTIVEDIREC  IPC$            READ            Remote IPC
SMB         10.10.106.240   445    ATTACKTIVEDIREC  NETLOGON        READ            Logon server share 
SMB         10.10.106.240   445    ATTACKTIVEDIREC  SYSVOL          READ            Logon server share
```
