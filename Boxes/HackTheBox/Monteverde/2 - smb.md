
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111                                      
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u '' -p ''
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\: 
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u '' -p '' --shares
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\: 
SMB         10.129.228.111  445    MONTEVERDE       [-] Error enumerating shares: STATUS_ACCESS_DENIED
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u '' -p '' --users 
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\: 
SMB         10.129.228.111  445    MONTEVERDE       -Username-                    -Last PW Set-       -BadPW- -Description-   
SMB         10.129.228.111  445    MONTEVERDE       Guest                         <never>             0       Built-in account for guest access to the computer/domain
SMB         10.129.228.111  445    MONTEVERDE       AAD_987d7f2f57d2              2020-01-02 22:53:24 0       Service account for the Synchronization Service with installation identifier 05c97990-7587-4a3d-b312-309adfc172d9 running on computer MONTEVERDE.
SMB         10.129.228.111  445    MONTEVERDE       mhope                         2020-01-02 23:40:05 0        
SMB         10.129.228.111  445    MONTEVERDE       SABatchJobs                   2020-01-03 12:48:46 0        
SMB         10.129.228.111  445    MONTEVERDE       svc-ata                       2020-01-03 12:58:31 0        
SMB         10.129.228.111  445    MONTEVERDE       svc-bexec                     2020-01-03 12:59:55 0        
SMB         10.129.228.111  445    MONTEVERDE       svc-netapp                    2020-01-03 13:01:42 0        
SMB         10.129.228.111  445    MONTEVERDE       dgalanos                      2020-01-03 13:06:10 0        
SMB         10.129.228.111  445    MONTEVERDE       roleary                       2020-01-03 13:08:05 0        
SMB         10.129.228.111  445    MONTEVERDE       smorgan                       2020-01-03 13:09:21 0        
SMB         10.129.228.111  445    MONTEVERDE       [*] Enumerated 10 local users: MEGABANK
```

AAD_987d7f2f57d2
mhope
SABatchJobs
svc-ata
svc-bexec
svc-netapp
dgalanos
roleary
smorgan

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u '' -p '' --pass-pol 
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\: 
SMB         10.129.228.111  445    MONTEVERDE       [+] Dumping password info for domain: MEGABANK
SMB         10.129.228.111  445    MONTEVERDE       Minimum password length: 7
SMB         10.129.228.111  445    MONTEVERDE       Password history length: 24
SMB         10.129.228.111  445    MONTEVERDE       Maximum password age: 41 days 23 hours 53 minutes 
SMB         10.129.228.111  445    MONTEVERDE       
SMB         10.129.228.111  445    MONTEVERDE       Password Complexity Flags: 000000
SMB         10.129.228.111  445    MONTEVERDE           Domain Refuse Password Change: 0
SMB         10.129.228.111  445    MONTEVERDE           Domain Password Store Cleartext: 0
SMB         10.129.228.111  445    MONTEVERDE           Domain Password Lockout Admins: 0
SMB         10.129.228.111  445    MONTEVERDE           Domain Password No Clear Change: 0
SMB         10.129.228.111  445    MONTEVERDE           Domain Password No Anon Change: 0
SMB         10.129.228.111  445    MONTEVERDE           Domain Password Complex: 0
SMB         10.129.228.111  445    MONTEVERDE       
SMB         10.129.228.111  445    MONTEVERDE       Minimum password age: 1 day 4 minutes 
SMB         10.129.228.111  445    MONTEVERDE       Reset Account Lockout Counter: 30 minutes 
SMB         10.129.228.111  445    MONTEVERDE       Locked Account Duration: 30 minutes 
SMB         10.129.228.111  445    MONTEVERDE       Account Lockout Threshold: None
SMB         10.129.228.111  445    MONTEVERDE       Forced Log off Time: Not Set
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.228.111 -u '' -p '' --rid-brute
SMB         10.129.228.111  445    MONTEVERDE       [*] Windows 10 / Server 2019 Build 17763 x64 (name:MONTEVERDE) (domain:MEGABANK.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.228.111  445    MONTEVERDE       [+] MEGABANK.LOCAL\: 
SMB         10.129.228.111  445    MONTEVERDE       [-] Error connecting: LSAD SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.
```


