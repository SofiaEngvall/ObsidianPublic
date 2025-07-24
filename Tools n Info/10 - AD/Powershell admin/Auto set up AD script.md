
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

