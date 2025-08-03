
```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2                                                 
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)

┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2 -u '' -p ''
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)
SMB         10.129.176.2    445    PRINTER          [+] return.local\: 

┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.176.2 -u '' -p '' --shares
SMB         10.129.176.2    445    PRINTER          [*] Windows 10 / Server 2019 Build 17763 x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)
SMB         10.129.176.2    445    PRINTER          [+] return.local\: 
SMB         10.129.176.2    445    PRINTER          [-] Error enumerating shares: STATUS_ACCESS_DENIED
```