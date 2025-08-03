
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.10.111.19 -u '' -p '' --shares
SMB         10.10.111.19    445    ROUTERPANEL      [*] Unix - Samba (name:ROUTERPANEL) (domain:ROUTERPANEL) (signing:False) (SMBv1:False)
SMB         10.10.111.19    445    ROUTERPANEL      [+] ROUTERPANEL\: 
SMB         10.10.111.19    445    ROUTERPANEL      [*] Enumerated shares
SMB         10.10.111.19    445    ROUTERPANEL      Share           Permissions     Remark
SMB         10.10.111.19    445    ROUTERPANEL      -----           -----------     ------
SMB         10.10.111.19    445    ROUTERPANEL      public          READ            
SMB         10.10.111.19    445    ROUTERPANEL      IPC$                            IPC Service (Samba 4.15.13-Ubuntu)
```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/athena]
└─$ cat msg_for_administrator.txt 

Dear Administrator,

I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel

Yours sincerely,

Athena
Intern
```
