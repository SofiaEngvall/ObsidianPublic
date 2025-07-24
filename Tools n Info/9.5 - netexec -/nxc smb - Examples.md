

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101                
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
```
smb answers and gives us the os and some info on smb

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u '' -p ''
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [+] za.tryhackme.com\: 
```
null sessions works! `[+]`

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u 'guest' -p ''
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [-] za.tryhackme.com\guest: STATUS_ACCOUNT_DISABLED
```
guest account is disabled

---
### Confirming an existing account

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u '123' -p ''
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [-] za.tryhackme.com\123: STATUS_LOGON_FAILURE 
```
this is how a fail looks

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u 'barbara.taylor' -p 'Knockers2015?'
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [+] za.tryhackme.com\barbara.taylor:Knockers2015?
```
this is how the confirmation of a correct account looks like

---
### Shares

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u '' -p '' --shares                  
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [+] za.tryhackme.com\: 
SMB         10.200.78.101   445    THMDC            [-] Error enumerating shares: STATUS_ACCESS_DENIED
```
a null session can't read shares on this server - it might have been able to though

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.200.78.101 -u 'barbara.taylor' -p 'Knockers2015?' --shares
SMB         10.200.78.101   445    THMDC            [*] Windows 10 / Server 2019 Build 17763 x64 (name:THMDC) (domain:za.tryhackme.com) (signing:True) (SMBv1:False)
SMB         10.200.78.101   445    THMDC            [+] za.tryhackme.com\barbara.taylor:Knockers2015? 
SMB         10.200.78.101   445    THMDC            [*] Enumerated shares
SMB         10.200.78.101   445    THMDC            Share           Permissions     Remark
SMB         10.200.78.101   445    THMDC            -----           -----------     ------
SMB         10.200.78.101   445    THMDC            ADMIN$                          Remote Admin
SMB         10.200.78.101   445    THMDC            C$                              Default share
SMB         10.200.78.101   445    THMDC            IPC$            READ            Remote IPC
SMB         10.200.78.101   445    THMDC            NETLOGON        READ            Logon server share 
SMB         10.200.78.101   445    THMDC            SYSVOL          READ            Logon server share 
```
lists shares the user has access to

---



