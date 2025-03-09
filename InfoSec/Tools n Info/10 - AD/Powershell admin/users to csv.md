
Only for Users OU, remove searchbase option for all
```powershell
Get-ADUser -Filter * -SearchBase "OU=Users,DC=example,DC=com" | Select-Object Name,SamAccountName,UserPrincipalName | Export-Csv -Path "C:\Users\report.csv" -NoTypeInformation
```
