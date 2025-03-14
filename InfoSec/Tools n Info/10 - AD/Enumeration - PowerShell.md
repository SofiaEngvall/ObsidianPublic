
https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps

Also https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon

If we're not domain joined we can use `-Server`

```powershell
Get-ADUser -Identity gordon.stevens -Server za.tryhackme.com -Properties *
```

```powershell
Get-ADUser -Filter 'Name -like "*stevens"' -Server za.tryhackme.com | Format-Table Name,SamAccountName -A
```

```powershell
Get-ADGroup -Identity Administrators -Server za.tryhackme.com
```

```powersehell
Get-ADGroupMember -Identity Administrators -Server za.tryhackme.com
```

```powershell
$ChangeDate = New-Object DateTime(2022, 02, 28, 12, 00, 00)
Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Server za.tryhackme.com
```

```powershell
Get-ADObject -Filter 'badPwdCount -gt 0' -Server za.tryhackme.com
```

```powershell
Get-ADDomain -Server za.tryhackme.com
```

```powershell
Set-ADAccountPassword -Identity gordon.stevens -Server za.tryhackme.com -OldPassword (ConvertTo-SecureString -AsPlaintext "Old" -force) -NewPassword (ConvertTo-SecureString -AsPlainText "New" -Force)
```

