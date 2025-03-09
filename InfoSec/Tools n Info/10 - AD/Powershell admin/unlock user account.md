
```powershell
#unlock user account
Unlock-ADAccount -Identity "Username"

#reset a user’s password
Set-ADAccountPassword -Identity “Username” -Reset -NewPassword (ConvertTo-SecureString -AsPlainText “new_password” -Force)
```

