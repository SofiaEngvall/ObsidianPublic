
```powershell
# Define variables
$DomainName = "fixit42.com"
$NetBIOSName = "FIXIT42"
$SafeModeAdministratorPassword = Read-Host -AsSecureString -Prompt 'Set Safe Mode Administrator Password'

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
