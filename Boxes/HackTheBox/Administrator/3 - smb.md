
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.203.207                                                                                               
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.203.207 -u '' -p '' --shares
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.207  445    DC               [+] administrator.htb\: 
SMB         10.129.203.207  445    DC               [-] Error enumerating shares: STATUS_ACCESS_DENIED
```

```sh
┌──(fixit42㉿kali)-[/usr/share/wordlists]
└─$ nxc smb 10.129.203.207 -u olivia -p ichliebedich
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.207  445    DC               [+] administrator.htb\olivia:ichliebedich 
```

```sh
┌──(fixit42㉿kali)-[/usr/share/wordlists]
└─$ nxc smb 10.129.203.207 -u olivia -p ichliebedich --shares
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.207  445    DC               [+] administrator.htb\olivia:ichliebedich 
SMB         10.129.203.207  445    DC               [*] Enumerated shares
SMB         10.129.203.207  445    DC               Share           Permissions     Remark
SMB         10.129.203.207  445    DC               -----           -----------     ------
SMB         10.129.203.207  445    DC               ADMIN$                          Remote Admin
SMB         10.129.203.207  445    DC               C$                              Default share
SMB         10.129.203.207  445    DC               IPC$            READ            Remote IPC
SMB         10.129.203.207  445    DC               NETLOGON        READ            Logon server share 
SMB         10.129.203.207  445    DC               SYSVOL          READ            Logon server share 
```

```sh
┌──(fixit42㉿kali)-[/usr/share/wordlists]
└─$ nxc smb 10.129.203.207 -u olivia -p ichliebedich --users 
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.207  445    DC               [+] administrator.htb\olivia:ichliebedich 
SMB         10.129.203.207  445    DC               -Username-                    -Last PW Set-       -BadPW- -Description-   
SMB         10.129.203.207  445    DC               Administrator                 2024-10-22 18:59:36 0       Built-in account for administering the computer/domain                                                                                        
SMB         10.129.203.207  445    DC               Guest                         <never>             0       Built-in account for guest access to the computer/domain                                                                                      
SMB         10.129.203.207  445    DC               krbtgt                        2024-10-04 19:53:28 0       Key Distribution Center Service Account                                                                                                       
SMB         10.129.203.207  445    DC               olivia                        2024-10-06 01:22:48 0        
SMB         10.129.203.207  445    DC               michael                       2024-10-06 01:33:37 0        
SMB         10.129.203.207  445    DC               benjamin                      2024-10-06 01:34:56 0        
SMB         10.129.203.207  445    DC               emily                         2024-10-30 23:40:02 0        
SMB         10.129.203.207  445    DC               ethan                         2024-10-12 20:52:14 0        
SMB         10.129.203.207  445    DC               alexander                     2024-10-31 00:18:04 0        
SMB         10.129.203.207  445    DC               emma                          2024-10-31 00:18:35 0        
SMB         10.129.203.207  445    DC               [*] Enumerated 10 local users: ADMINISTRATOR
```

```sh
┌──(fixit42㉿kali)-[/usr/share/wordlists]
└─$ nxc smb 10.129.203.207 -u olivia -p ichliebedich --rid-brute
SMB         10.129.203.207  445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.207  445    DC               [+] administrator.htb\olivia:ichliebedich 
SMB         10.129.203.207  445    DC               498: ADMINISTRATOR\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.203.207  445    DC               500: ADMINISTRATOR\Administrator (SidTypeUser)
SMB         10.129.203.207  445    DC               501: ADMINISTRATOR\Guest (SidTypeUser)
SMB         10.129.203.207  445    DC               502: ADMINISTRATOR\krbtgt (SidTypeUser)
SMB         10.129.203.207  445    DC               512: ADMINISTRATOR\Domain Admins (SidTypeGroup)
SMB         10.129.203.207  445    DC               513: ADMINISTRATOR\Domain Users (SidTypeGroup)
SMB         10.129.203.207  445    DC               514: ADMINISTRATOR\Domain Guests (SidTypeGroup)
SMB         10.129.203.207  445    DC               515: ADMINISTRATOR\Domain Computers (SidTypeGroup)
SMB         10.129.203.207  445    DC               516: ADMINISTRATOR\Domain Controllers (SidTypeGroup)
SMB         10.129.203.207  445    DC               517: ADMINISTRATOR\Cert Publishers (SidTypeAlias)
SMB         10.129.203.207  445    DC               518: ADMINISTRATOR\Schema Admins (SidTypeGroup)
SMB         10.129.203.207  445    DC               519: ADMINISTRATOR\Enterprise Admins (SidTypeGroup)
SMB         10.129.203.207  445    DC               520: ADMINISTRATOR\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.203.207  445    DC               521: ADMINISTRATOR\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.203.207  445    DC               522: ADMINISTRATOR\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.203.207  445    DC               525: ADMINISTRATOR\Protected Users (SidTypeGroup)
SMB         10.129.203.207  445    DC               526: ADMINISTRATOR\Key Admins (SidTypeGroup)
SMB         10.129.203.207  445    DC               527: ADMINISTRATOR\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.203.207  445    DC               553: ADMINISTRATOR\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.203.207  445    DC               571: ADMINISTRATOR\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.203.207  445    DC               572: ADMINISTRATOR\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.203.207  445    DC               1000: ADMINISTRATOR\DC$ (SidTypeUser)
SMB         10.129.203.207  445    DC               1101: ADMINISTRATOR\DnsAdmins (SidTypeAlias)
SMB         10.129.203.207  445    DC               1102: ADMINISTRATOR\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.203.207  445    DC               1108: ADMINISTRATOR\olivia (SidTypeUser)
SMB         10.129.203.207  445    DC               1109: ADMINISTRATOR\michael (SidTypeUser)
SMB         10.129.203.207  445    DC               1110: ADMINISTRATOR\benjamin (SidTypeUser)
SMB         10.129.203.207  445    DC               1111: ADMINISTRATOR\Share Moderators (SidTypeAlias)
SMB         10.129.203.207  445    DC               1112: ADMINISTRATOR\emily (SidTypeUser)
SMB         10.129.203.207  445    DC               1113: ADMINISTRATOR\ethan (SidTypeUser)
SMB         10.129.203.207  445    DC               3601: ADMINISTRATOR\alexander (SidTypeUser)
SMB         10.129.203.207  445    DC               3602: ADMINISTRATOR\emma (SidTypeUser)
```