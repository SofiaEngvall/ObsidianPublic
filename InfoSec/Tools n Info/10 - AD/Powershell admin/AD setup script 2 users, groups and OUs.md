
```powershell
New-ADOrganizationalUnit -Name "Sales" -Path "DC=fixit42,DC=com"

Import-Csv .\users.csv | New-ADUser

#crerate group
New-ADGroup -Name "AdminGroup" -GroupScope Global -Path "CN=Users,DC=fixit42,DC=com"

#Add user to group
Add-ADGroupMember -Identity "AdminGroup" -Members "sofia"


Get-ADUser -Filter *
Get-ADGroup -Filter *
Get-ADGroupMember -Identity "AdminGroup"
```

csv file:
```sh
Name, GivenName, Surname, SamAccountName, UserPrincipalName, Path, AccountPassword, Enabled
"John Doe", "John", "Doe", "johndoe", "johndoe@fixit42.com", "OU=Sales,DC=fixit42,DC=com", "P@ssw0rd!", $true
"Sofia Engvall", "Sofia", "Engvall", "sofia", "sofia@fixit42.com", "CN=Users,DC=fixit42,DC=com", ""qweRTY123¤%&"", $true
```

cleanup/undo
```powershell
$ConfirmPreference = 'None'
$oldErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"

#delete user in group
Remove-ADGroupMember -Identity "AdminGroup" -Members "sofia" -Confirm:$false
#if ((Get-ADGroupMember -Identity "AdminGroup").SamAccountName -contains "sofia"){#output stuff TODO!}

#delete group
Remove-ADGroup -Identity "AdminGroup" -Confirm:$false -WhatIf:$false
if (Get-ADGroup -Identity "AdminGroup" -ErrorAction SilentlyContinue) {
}

#Import-Csv .\users.csv | New-ADUser

$user = Get-ADUser -Identity "jdoe" -ErrorAction SilentlyContinue
if ($user) { Remove-ADUser -Identity "jdoe" -Confirm:$false }

Remove-ADUser -Identity "sofia" -Confirm:$false
if (Get-ADUser -Identity "sofia" -ErrorAction SilentlyContinue) {
}

$sales = "OU=Sales,DC=test,DC=local"
Set-ADOrganizationalUnit -Identity $sales -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity $sales -Confirm:$false
if (Get-ADOrganizationalUnit -Identity $sales -ErrorAction SilentlyContinue) {
}

Get-ADUser -Filter *
Get-ADGroup -Filter *
Get-ADGroupMember -Identity "AdminGroup"

$ConfirmPreference = 'High'
$ErrorActionPreference = $oldErrorActionPreference
```

