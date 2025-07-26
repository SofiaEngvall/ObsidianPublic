
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2 -u 'return\svc-printer' -p '1edFg43012!!' --shares
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)
SMB         10.129.176.2    445    PRINTER          [+] return\svc-printer:1edFg43012!! 
SMB         10.129.176.2    445    PRINTER          [*] Enumerated shares
SMB         10.129.176.2    445    PRINTER          Share           Permissions     Remark
SMB         10.129.176.2    445    PRINTER          -----           -----------     ------
SMB         10.129.176.2    445    PRINTER          ADMIN$          READ            Remote Admin
SMB         10.129.176.2    445    PRINTER          C$              READ,WRITE      Default share
SMB         10.129.176.2    445    PRINTER          IPC$            READ            Remote IPC
SMB         10.129.176.2    445    PRINTER          NETLOGON        READ            Logon server share 
SMB         10.129.176.2    445    PRINTER          SYSVOL          READ            Logon server share
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2 -u 'return\svc-printer' -p '1edFg43012!!' --rid-brute
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)
SMB         10.129.176.2    445    PRINTER          [+] return\svc-printer:1edFg43012!! 
SMB         10.129.176.2    445    PRINTER          498: RETURN\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          500: RETURN\Administrator (SidTypeUser)
SMB         10.129.176.2    445    PRINTER          501: RETURN\Guest (SidTypeUser)
SMB         10.129.176.2    445    PRINTER          502: RETURN\krbtgt (SidTypeUser)
SMB         10.129.176.2    445    PRINTER          512: RETURN\Domain Admins (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          513: RETURN\Domain Users (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          514: RETURN\Domain Guests (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          515: RETURN\Domain Computers (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          516: RETURN\Domain Controllers (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          517: RETURN\Cert Publishers (SidTypeAlias)
SMB         10.129.176.2    445    PRINTER          518: RETURN\Schema Admins (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          519: RETURN\Enterprise Admins (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          520: RETURN\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          521: RETURN\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          522: RETURN\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          525: RETURN\Protected Users (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          526: RETURN\Key Admins (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          527: RETURN\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          553: RETURN\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.176.2    445    PRINTER          571: RETURN\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.176.2    445    PRINTER          572: RETURN\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.176.2    445    PRINTER          1000: RETURN\PRINTER$ (SidTypeUser)
SMB         10.129.176.2    445    PRINTER          1101: RETURN\DnsAdmins (SidTypeAlias)
SMB         10.129.176.2    445    PRINTER          1102: RETURN\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.176.2    445    PRINTER          1103: RETURN\svc-printer (SidTypeUser)
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2 -u 'return\svc-printer' -p '1edFg43012!!' --pass-pol
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)
SMB         10.129.176.2    445    PRINTER          [+] return\svc-printer:1edFg43012!! 
SMB         10.129.176.2    445    PRINTER          [+] Dumping password info for domain: RETURN
SMB         10.129.176.2    445    PRINTER          Minimum password length: 7
SMB         10.129.176.2    445    PRINTER          Password history length: 24
SMB         10.129.176.2    445    PRINTER          Maximum password age: 41 days 23 hours 53 minutes 
SMB         10.129.176.2    445    PRINTER          
SMB         10.129.176.2    445    PRINTER          Password Complexity Flags: 000001
SMB         10.129.176.2    445    PRINTER              Domain Refuse Password Change: 0
SMB         10.129.176.2    445    PRINTER              Domain Password Store Cleartext: 0
SMB         10.129.176.2    445    PRINTER              Domain Password Lockout Admins: 0
SMB         10.129.176.2    445    PRINTER              Domain Password No Clear Change: 0
SMB         10.129.176.2    445    PRINTER              Domain Password No Anon Change: 0
SMB         10.129.176.2    445    PRINTER              Domain Password Complex: 1
SMB         10.129.176.2    445    PRINTER          
SMB         10.129.176.2    445    PRINTER          Minimum password age: 1 day 4 minutes 
SMB         10.129.176.2    445    PRINTER          Reset Account Lockout Counter: 30 minutes 
SMB         10.129.176.2    445    PRINTER          Locked Account Duration: 30 minutes 
SMB         10.129.176.2    445    PRINTER          Account Lockout Threshold: None
SMB         10.129.176.2    445    PRINTER          Forced Log off Time: Not Set
```

