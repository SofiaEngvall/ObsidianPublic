
```sh
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105                          
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
                                                                                                                              
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u '' -p ''
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [-] Relevant\: STATUS_ACCESS_DENIED 
                                                                                                                              
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'guest' -p ''
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\guest: 
                                                                                                                              
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'guest' -p '' --shares
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\guest: 
SMB         10.10.182.105   445    RELEVANT         [*] Enumerated shares
SMB         10.10.182.105   445    RELEVANT         Share           Permissions     Remark
SMB         10.10.182.105   445    RELEVANT         -----           -----------     ------
SMB         10.10.182.105   445    RELEVANT         ADMIN$                          Remote Admin
SMB         10.10.182.105   445    RELEVANT         C$                              Default share
SMB         10.10.182.105   445    RELEVANT         IPC$                            Remote IPC
SMB         10.10.182.105   445    RELEVANT         nt4wrksv        READ,WRITE   
```

```sh
┌──(kali㉿kali)-[~/thm/relevant]
└─$ smbget --recursive smb://10.10.182.105/nt4wrksv                 
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
Using netbios name KALI.
Using workgroup WORKGROUP.
Password for [WORKGROUP\kali]:
Using domain: WORKGROUP, user: kali
Cannot do GSE to an IP address
Server connect ok: //10.10.182.105/nt4wrksv: 0x561885bcba90
smb://10.10.182.105/nt4wrksv/passwords.txt                                                                                    
Downloaded 98b in 6 seconds
                                                                                                                              
┌──(kali㉿kali)-[~/thm/relevant]
└─$ ls -la
total 12
drwxrwxr-x  2 kali kali 4096 Jul 12 20:26 .
drwxr-xr-x 32 kali kali 4096 Jul 12 20:26 ..
-rwxr-xr-x  1 kali kali   98 Jul 12 20:26 passwords.txt
                                                                                                                              
┌──(kali㉿kali)-[~/thm/relevant]
└─$ cat passwords.txt 
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk                                                                                                                              
┌──(kali㉿kali)-[~/thm/relevant]
└─$ echo Qm9iIC0gIVBAJCRXMHJEITEyMw== | base64 -d
Bob - !P@$$W0rD!123                                                                                                                              
┌──(kali㉿kali)-[~/thm/relevant]
└─$ echo QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk | base64 -d
Bill - Juw4nnaM4n420696969!$$$  
```

```
Bob - !P@$$W0rD!123 
Bill - Juw4nnaM4n420696969!$$$ 
```

Confirming users?
```sh
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Bob' -p 'qwe' --shares
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [-] Relevant\Bob:qwe STATUS_LOGON_FAILURE 

┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Bob' -p '!P@$$W0rD!123' --shares
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
SMB         10.10.182.105   445    RELEVANT         [*] Enumerated shares
SMB         10.10.182.105   445    RELEVANT         Share           Permissions     Remark
SMB         10.10.182.105   445    RELEVANT         -----           -----------     ------
SMB         10.10.182.105   445    RELEVANT         ADMIN$                          Remote Admin
SMB         10.10.182.105   445    RELEVANT         C$                              Default share
SMB         10.10.182.105   445    RELEVANT         IPC$                            Remote IPC
SMB         10.10.182.105   445    RELEVANT         nt4wrksv        READ,WRITE      

┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Bill' -p 'Juw4nnaM4n420696969!$$$' --shares
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\Bill:Juw4nnaM4n420696969!$$$ 
SMB         10.10.182.105   445    RELEVANT         [*] Enumerated shares
SMB         10.10.182.105   445    RELEVANT         Share           Permissions     Remark
SMB         10.10.182.105   445    RELEVANT         -----           -----------     ------
SMB         10.10.182.105   445    RELEVANT         ADMIN$                          Remote Admin
SMB         10.10.182.105   445    RELEVANT         C$                              Default share
SMB         10.10.182.105   445    RELEVANT         IPC$                            Remote IPC
SMB         10.10.182.105   445    RELEVANT         nt4wrksv        READ,WRITE   
```

Nope, it doesn't seem so
```sh
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Bill' -p 'Juw4nnaM4n420696969!$$$' --rid-brute
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\Bill:Juw4nnaM4n420696969!$$$ 
SMB         10.10.182.105   445    RELEVANT         500: RELEVANT\Administrator (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         501: RELEVANT\Guest (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         503: RELEVANT\DefaultAccount (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         513: RELEVANT\None (SidTypeGroup)
SMB         10.10.182.105   445    RELEVANT         1002: RELEVANT\Bob (SidTypeUser)
                                                                                                                              
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Bob' -p '!P@$$W0rD!123' --rid-brute        
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
SMB         10.10.182.105   445    RELEVANT         500: RELEVANT\Administrator (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         501: RELEVANT\Guest (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         503: RELEVANT\DefaultAccount (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         513: RELEVANT\None (SidTypeGroup)
SMB         10.10.182.105   445    RELEVANT         1002: RELEVANT\Bob (SidTypeUser)
                                                                                                                              
┌──(kali㉿kali)-[~/thm/Overpass2]
└─$ nxc smb 10.10.182.105 -u 'Hi' -p '' --rid-brute
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.182.105   445    RELEVANT         [+] Relevant\Hi: 
SMB         10.10.182.105   445    RELEVANT         500: RELEVANT\Administrator (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         501: RELEVANT\Guest (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         503: RELEVANT\DefaultAccount (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         513: RELEVANT\None (SidTypeGroup)
SMB         10.10.182.105   445    RELEVANT         1002: RELEVANT\Bob (SidTypeUser)

```

When we use `nxc smb 10.10.182.105 -u 'Bill' -p 'qwe' --shares` with a an actual username and a wrong password we get a [-] Relevant\Bob:qwe STATUS_LOGON_FAILURE 

When we use another name we still get stuff back (on this server) but it'll be the as no user logged in kinda

