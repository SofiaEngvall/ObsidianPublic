
General info on AD commands: https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2025-ps

```powershell
# Define variables
$DomainName = "test.local"
$NetBIOSName = "TEST"
$SafeModeAdministratorPassword = ConvertTo-SecureString "YourSecurePassword123" -AsPlainText -Force

# Install AD DS role and management tools
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote the server to a domain controller
#Import-Module ADDSDeployment
Install-ADDSForest `
    -DomainName $DomainName `
    -DomainNetbiosName $DomainNetbiosName `
    -SafeModeAdministratorPassword $SafeModeAdministratorPassword `
    -InstallDns:$true `
    -Force:$true
```

Run with: `powershell -ExecutionPolicy Bypass -File Setup-AD.ps1`

```powershell
# Verify installation
Get-Service ntds, adws, kdc, netlogon, dns
```

```powershell
Get-ADDomain
#Get-ADUser -Filter * -SearchBase "OU=UserAccounts,DC=TEST,DC=local"
Get-ADComputer
Get-ADUser -Filter *
Get-ADGroup -Filter *
Get-ADGroupMember -Filter *
```

Create OU and user
```powershell
# Import the Active Directory module
Import-Module ActiveDirectory

# Create a new OU
New-ADOrganizationalUnit -Name "Sales" -Path "DC=test,DC=local"
New-ADOrganizationalUnit -Name "Users" -Path "DC=test,DC=local" -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "Computers" -Path "DC=test,DC=local" -ProtectedFromAccidentalDeletion $false

# Create a new user
New-ADUser `
    -Name "JohnDoe" `
    -GivenName "John" `
    -Surname "Doe" `
    -SamAccountName "johndoe" `
	-UserPrincipalName "johndoe@example.com" `
#    -Path "CN=Users,DC=YourDomainName,DC=com" `
    -Path "OU=Sales,DC=example,DC=com" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) `
    -Enabled $true

#crerate group
New-ADGroup -Name "AdminGroup" -GroupScope Global -Path "CN=Users,DC=test,DC=local"

#Add user to group
Add-ADGroupMember -Identity "AdminGroup" -Members "jdoe"

```


```powershell
# Create and link a basic GPO
New-GPO -Name "Baseline Security" | New-GPLink -Target "OU=Users,DC=test,DC=local"



```

https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps

Use the `Import-Csv` cmdlet with the `New-ADUser` cmdlet to create multiple Active Directory user objects.
```powershell
Import-Csv usersToAdd.csv | New-ADUser
```

Example data ($true might not work?)
```sh
Name, GivenName, Surname, SamAccountName, UserPrincipalName, Path, AccountPassword, Enabled
"JohnDoe", "John", "Doe", "johndoe", "johndoe@example.com", "OU=Sales,DC=example,DC=com", "P@ssw0rd!", $true
```

```powershell
#Create computer object
New-ADComputer -Name "ComputerName" -SamAccountName "ComputerName" -Path "OU=Computers,DC=Domain,DC=com"

#Add computer object to domain
Add-Computer -DomainName "domain.com" -Credential Domain\Username -Restart –Force
```
### **Security Hardening**

- **Enforce strong passwords** (`Minimum password length: 12, Complexity: Enabled`)
- **Account lockout policy** (`Lock after 5 failed attempts, unlock after 15 min`)
- **Disable LM/NTLMv1** (Force NTLMv2 or Kerberos only)
- **Enable Windows Defender and real-time protection**

### **Access Control**

- **Disable RDP for all users except admins**
- **Restrict anonymous enumeration** (`No anonymous access to SAM or shares`)
- **Limit local admin access** (`Deny network logon for local admins`)

### **Logging & Auditing**

- **Enable advanced security auditing** (Log logins, privilege changes, process creation)
- **Increase log sizes** (`Security log: 128MB, Application/System: 64MB`)

### **Performance & Usability**

- **Disable OneDrive auto-setup**
- **Set a custom login message**
- **Redirect user folders to a network share** (if needed)



```powershell
PS C:\Users\Administrator\Desktop\AD> C:\Users\Administrator\Desktop\AD\ad-setup-2.ps1


DistinguishedName : CN=Administrator,CN=Users,DC=fixit42,DC=com
Enabled           : True
GivenName         : 
Name              : Administrator
ObjectClass       : user
ObjectGUID        : c3a14b6c-9784-4b88-8e5b-ef1221194f1b
SamAccountName    : Administrator
SID               : S-1-5-21-1965777406-2460568277-2501755671-500
Surname           : 
UserPrincipalName : 

DistinguishedName : CN=Guest,CN=Users,DC=fixit42,DC=com
Enabled           : False
GivenName         : 
Name              : Guest
ObjectClass       : user
ObjectGUID        : 282ad3b7-2ad5-4f4f-b251-fd69c037ed68
SamAccountName    : Guest
SID               : S-1-5-21-1965777406-2460568277-2501755671-501
Surname           : 
UserPrincipalName : 

DistinguishedName : CN=krbtgt,CN=Users,DC=fixit42,DC=com
Enabled           : False
GivenName         : 
Name              : krbtgt
ObjectClass       : user
ObjectGUID        : 516e0c7c-1955-43ed-abf9-d20bc1f8b514
SamAccountName    : krbtgt
SID               : S-1-5-21-1965777406-2460568277-2501755671-502
Surname           : 
UserPrincipalName : 

DistinguishedName : CN=John Doe,OU=Sales,DC=fixit42,DC=com
Enabled           : False
GivenName         : John
Name              : John Doe
ObjectClass       : user
ObjectGUID        : 6148e958-d668-4cc0-9593-12c5f025bc5b
SamAccountName    : johndoe
SID               : S-1-5-21-1965777406-2460568277-2501755671-1601
Surname           : Doe
UserPrincipalName : johndoe@fixit42.com

DistinguishedName : CN=Sofia Engvall,CN=Users,DC=fixit42,DC=com
Enabled           : False
GivenName         : Sofia
Name              : Sofia Engvall
ObjectClass       : user
ObjectGUID        : e0ccfa32-30a3-4c47-ad06-0704a2038309
SamAccountName    : sofia
SID               : S-1-5-21-1965777406-2460568277-2501755671-1602
Surname           : Engvall
UserPrincipalName : sofia@fixit42.com

DistinguishedName : CN=Administrators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Administrators
ObjectClass       : group
ObjectGUID        : 7e5b2dbe-a4bc-41d1-a7a6-ff3571349884
SamAccountName    : Administrators
SID               : S-1-5-32-544

DistinguishedName : CN=Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Users
ObjectClass       : group
ObjectGUID        : 94aceba5-7cc1-45c1-95ce-e28c5bb4f4cf
SamAccountName    : Users
SID               : S-1-5-32-545

DistinguishedName : CN=Guests,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Guests
ObjectClass       : group
ObjectGUID        : 7a1be9a0-522a-4e72-9db1-a308dbcfc646
SamAccountName    : Guests
SID               : S-1-5-32-546

DistinguishedName : CN=Print Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Print Operators
ObjectClass       : group
ObjectGUID        : f610d71a-2516-4730-9c06-508f0e3b6c02
SamAccountName    : Print Operators
SID               : S-1-5-32-550

DistinguishedName : CN=Backup Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Backup Operators
ObjectClass       : group
ObjectGUID        : 56e32a6d-35e6-42e0-8d36-b8eea66b79d0
SamAccountName    : Backup Operators
SID               : S-1-5-32-551

DistinguishedName : CN=Replicator,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Replicator
ObjectClass       : group
ObjectGUID        : 873be843-2871-4ba5-885a-b6ba9c4e7138
SamAccountName    : Replicator
SID               : S-1-5-32-552

DistinguishedName : CN=Remote Desktop Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Remote Desktop Users
ObjectClass       : group
ObjectGUID        : 206a7511-2d28-4775-b276-9bb4210d6209
SamAccountName    : Remote Desktop Users
SID               : S-1-5-32-555

DistinguishedName : CN=Network Configuration Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Network Configuration Operators
ObjectClass       : group
ObjectGUID        : 1e0d3825-bf6d-4d6a-bca2-c5add622ce89
SamAccountName    : Network Configuration Operators
SID               : S-1-5-32-556

DistinguishedName : CN=Performance Monitor Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Performance Monitor Users
ObjectClass       : group
ObjectGUID        : f7bf6888-25b9-4e18-8d35-9b4f5962c16e
SamAccountName    : Performance Monitor Users
SID               : S-1-5-32-558

DistinguishedName : CN=Performance Log Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Performance Log Users
ObjectClass       : group
ObjectGUID        : 49df4416-0450-442b-af47-07e98bebbce9
SamAccountName    : Performance Log Users
SID               : S-1-5-32-559

DistinguishedName : CN=Distributed COM Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Distributed COM Users
ObjectClass       : group
ObjectGUID        : b529154d-779b-4fc0-96bb-ae41bc922bfb
SamAccountName    : Distributed COM Users
SID               : S-1-5-32-562

DistinguishedName : CN=IIS_IUSRS,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : IIS_IUSRS
ObjectClass       : group
ObjectGUID        : ab7f768b-b829-42dc-a4ea-78070727e8df
SamAccountName    : IIS_IUSRS
SID               : S-1-5-32-568

DistinguishedName : CN=Cryptographic Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Cryptographic Operators
ObjectClass       : group
ObjectGUID        : 05c26290-82b5-4144-b1d5-e6d5b5a2e73b
SamAccountName    : Cryptographic Operators
SID               : S-1-5-32-569

DistinguishedName : CN=Event Log Readers,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Event Log Readers
ObjectClass       : group
ObjectGUID        : faebccee-ae0d-48d8-897a-c8689af645fa
SamAccountName    : Event Log Readers
SID               : S-1-5-32-573

DistinguishedName : CN=Certificate Service DCOM Access,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Certificate Service DCOM Access
ObjectClass       : group
ObjectGUID        : 103a4f41-282d-41f4-88d8-fc4631a51c60
SamAccountName    : Certificate Service DCOM Access
SID               : S-1-5-32-574

DistinguishedName : CN=RDS Remote Access Servers,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : RDS Remote Access Servers
ObjectClass       : group
ObjectGUID        : 82b443b2-1fd5-4b39-b521-ae42964abd14
SamAccountName    : RDS Remote Access Servers
SID               : S-1-5-32-575

DistinguishedName : CN=RDS Endpoint Servers,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : RDS Endpoint Servers
ObjectClass       : group
ObjectGUID        : 6194a3f3-6d33-45c4-8171-65e7c32a8ac0
SamAccountName    : RDS Endpoint Servers
SID               : S-1-5-32-576

DistinguishedName : CN=RDS Management Servers,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : RDS Management Servers
ObjectClass       : group
ObjectGUID        : 917079f0-429a-46a9-a03c-b754b5ff5335
SamAccountName    : RDS Management Servers
SID               : S-1-5-32-577

DistinguishedName : CN=Hyper-V Administrators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Hyper-V Administrators
ObjectClass       : group
ObjectGUID        : 5b2eedd9-6b75-4bed-aee6-0da61c93afda
SamAccountName    : Hyper-V Administrators
SID               : S-1-5-32-578

DistinguishedName : CN=Access Control Assistance Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Access Control Assistance Operators
ObjectClass       : group
ObjectGUID        : 217d9a5c-ae8c-4e2d-b09f-1288bf02c1f7
SamAccountName    : Access Control Assistance Operators
SID               : S-1-5-32-579

DistinguishedName : CN=Remote Management Users,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Remote Management Users
ObjectClass       : group
ObjectGUID        : b100b8c2-afc7-4231-a0cf-de91ba79be0a
SamAccountName    : Remote Management Users
SID               : S-1-5-32-580

DistinguishedName : CN=Storage Replica Administrators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Storage Replica Administrators
ObjectClass       : group
ObjectGUID        : 609fba36-1289-4e8e-adcd-c2e86aebe115
SamAccountName    : Storage Replica Administrators
SID               : S-1-5-32-582

DistinguishedName : CN=Domain Computers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Domain Computers
ObjectClass       : group
ObjectGUID        : 14b635e3-95fe-445d-91b0-496789494d26
SamAccountName    : Domain Computers
SID               : S-1-5-21-1965777406-2460568277-2501755671-515

DistinguishedName : CN=Domain Controllers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Domain Controllers
ObjectClass       : group
ObjectGUID        : 7fcaca3e-6021-408c-8e0f-5815b5619252
SamAccountName    : Domain Controllers
SID               : S-1-5-21-1965777406-2460568277-2501755671-516

DistinguishedName : CN=Schema Admins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Universal
Name              : Schema Admins
ObjectClass       : group
ObjectGUID        : a2751331-aba5-4877-bf6b-3c51c571d051
SamAccountName    : Schema Admins
SID               : S-1-5-21-1965777406-2460568277-2501755671-518

DistinguishedName : CN=Enterprise Admins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Universal
Name              : Enterprise Admins
ObjectClass       : group
ObjectGUID        : 5fdb0729-a22a-4668-b97f-b41216e06e16
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-1965777406-2460568277-2501755671-519

DistinguishedName : CN=Cert Publishers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Cert Publishers
ObjectClass       : group
ObjectGUID        : bd28148c-e529-4980-b9be-8b63286dafa4
SamAccountName    : Cert Publishers
SID               : S-1-5-21-1965777406-2460568277-2501755671-517

DistinguishedName : CN=Domain Admins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Domain Admins
ObjectClass       : group
ObjectGUID        : 1fd3b05c-f7af-46c0-878a-1c87df270f59
SamAccountName    : Domain Admins
SID               : S-1-5-21-1965777406-2460568277-2501755671-512

DistinguishedName : CN=Domain Users,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Domain Users
ObjectClass       : group
ObjectGUID        : 3863bcc7-3452-4d1a-a62d-684a60ff782a
SamAccountName    : Domain Users
SID               : S-1-5-21-1965777406-2460568277-2501755671-513

DistinguishedName : CN=Domain Guests,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Domain Guests
ObjectClass       : group
ObjectGUID        : 4a4a32bb-22ea-4a9a-9fa5-118d912f4395
SamAccountName    : Domain Guests
SID               : S-1-5-21-1965777406-2460568277-2501755671-514

DistinguishedName : CN=Group Policy Creator Owners,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Group Policy Creator Owners
ObjectClass       : group
ObjectGUID        : 07a5e8dd-6fea-4ac6-8d74-c3dcc4288462
SamAccountName    : Group Policy Creator Owners
SID               : S-1-5-21-1965777406-2460568277-2501755671-520

DistinguishedName : CN=RAS and IAS Servers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : RAS and IAS Servers
ObjectClass       : group
ObjectGUID        : 745465a4-08f8-44cf-ade7-ec5ac571aae4
SamAccountName    : RAS and IAS Servers
SID               : S-1-5-21-1965777406-2460568277-2501755671-553

DistinguishedName : CN=Server Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Server Operators
ObjectClass       : group
ObjectGUID        : 62f36131-4b42-483a-b22a-636534440783
SamAccountName    : Server Operators
SID               : S-1-5-32-549

DistinguishedName : CN=Account Operators,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Account Operators
ObjectClass       : group
ObjectGUID        : 9906e561-93f2-4bec-9ee4-da56c3c4d1d8
SamAccountName    : Account Operators
SID               : S-1-5-32-548

DistinguishedName : CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Pre-Windows 2000 Compatible Access
ObjectClass       : group
ObjectGUID        : 5aaa21ab-da10-474e-a476-518e5f5069c4
SamAccountName    : Pre-Windows 2000 Compatible Access
SID               : S-1-5-32-554

DistinguishedName : CN=Incoming Forest Trust Builders,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Incoming Forest Trust Builders
ObjectClass       : group
ObjectGUID        : ad8b4134-f991-4c6e-ac70-f25be8a517f5
SamAccountName    : Incoming Forest Trust Builders
SID               : S-1-5-32-557

DistinguishedName : CN=Windows Authorization Access Group,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Windows Authorization Access Group
ObjectClass       : group
ObjectGUID        : f8e96bf2-b841-454e-b81c-ed519a810a0e
SamAccountName    : Windows Authorization Access Group
SID               : S-1-5-32-560

DistinguishedName : CN=Terminal Server License Servers,CN=Builtin,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Terminal Server License Servers
ObjectClass       : group
ObjectGUID        : 754627ca-c437-4906-a17c-11617a1ff8a9
SamAccountName    : Terminal Server License Servers
SID               : S-1-5-32-561

DistinguishedName : CN=Allowed RODC Password Replication Group,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Allowed RODC Password Replication Group
ObjectClass       : group
ObjectGUID        : 849b40e0-6c45-4426-98a8-093aaeb51e46
SamAccountName    : Allowed RODC Password Replication Group
SID               : S-1-5-21-1965777406-2460568277-2501755671-571

DistinguishedName : CN=Denied RODC Password Replication Group,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Denied RODC Password Replication Group
ObjectClass       : group
ObjectGUID        : 6d662118-efc3-4891-9155-3ea2b4b10921
SamAccountName    : Denied RODC Password Replication Group
SID               : S-1-5-21-1965777406-2460568277-2501755671-572

DistinguishedName : CN=Read-only Domain Controllers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Read-only Domain Controllers
ObjectClass       : group
ObjectGUID        : dbfb3afe-b837-466b-a174-5cda432f3bd2
SamAccountName    : Read-only Domain Controllers
SID               : S-1-5-21-1965777406-2460568277-2501755671-521

DistinguishedName : CN=Enterprise Read-only Domain Controllers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Universal
Name              : Enterprise Read-only Domain Controllers
ObjectClass       : group
ObjectGUID        : 960dde77-08fa-4c9a-b075-d407230465b0
SamAccountName    : Enterprise Read-only Domain Controllers
SID               : S-1-5-21-1965777406-2460568277-2501755671-498

DistinguishedName : CN=Cloneable Domain Controllers,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Cloneable Domain Controllers
ObjectClass       : group
ObjectGUID        : cb0431d3-ee16-46c6-8f55-24b56525d538
SamAccountName    : Cloneable Domain Controllers
SID               : S-1-5-21-1965777406-2460568277-2501755671-522

DistinguishedName : CN=Protected Users,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Protected Users
ObjectClass       : group
ObjectGUID        : 89bbc338-04ec-434d-bccc-cf7dde5159ff
SamAccountName    : Protected Users
SID               : S-1-5-21-1965777406-2460568277-2501755671-525

DistinguishedName : CN=Key Admins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Key Admins
ObjectClass       : group
ObjectGUID        : d0f0401b-4185-49e1-9815-2d3657d73463
SamAccountName    : Key Admins
SID               : S-1-5-21-1965777406-2460568277-2501755671-526

DistinguishedName : CN=Enterprise Key Admins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Universal
Name              : Enterprise Key Admins
ObjectClass       : group
ObjectGUID        : 27ba7186-de16-4959-9b5e-526d1225fd41
SamAccountName    : Enterprise Key Admins
SID               : S-1-5-21-1965777406-2460568277-2501755671-527

DistinguishedName : CN=DnsAdmins,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : DnsAdmins
ObjectClass       : group
ObjectGUID        : 1e3cd246-f994-418a-8728-4a4c2217d8d5
SamAccountName    : DnsAdmins
SID               : S-1-5-21-1965777406-2460568277-2501755671-1101

DistinguishedName : CN=DnsUpdateProxy,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : DnsUpdateProxy
ObjectClass       : group
ObjectGUID        : 5c4f6609-e961-4852-b97e-5a27f9c35734
SamAccountName    : DnsUpdateProxy
SID               : S-1-5-21-1965777406-2460568277-2501755671-1102

DistinguishedName : CN=AdminGroup,CN=Users,DC=fixit42,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : AdminGroup
ObjectClass       : group
ObjectGUID        : f89db12f-9c0c-46bf-abf3-7e1ddc45424a
SamAccountName    : AdminGroup
SID               : S-1-5-21-1965777406-2460568277-2501755671-1603

distinguishedName : CN=Sofia Engvall,CN=Users,DC=fixit42,DC=com
name              : Sofia Engvall
objectClass       : user
objectGUID        : e0ccfa32-30a3-4c47-ad06-0704a2038309
SamAccountName    : sofia
SID               : S-1-5-21-1965777406-2460568277-2501755671-1602

```