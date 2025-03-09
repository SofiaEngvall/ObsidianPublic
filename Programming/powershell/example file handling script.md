
```powershell
$mailfolder = "C:\Users\Administrator\Desktop\emails"
foreach($mailbox in (Get-ChildItem -Path $mailfolder)){
    Write-Host "Processing mailbox: "+$($mailbox)
    foreach($mail in (Get-ChildItem -Path $mailfolder\$mailbox)){
        Write-Host "Processing mail: "+$($mail)

        foreach($line in (Get-Content $mailfolder\$mailbox\$mail) ){
#            Write-Host test $line

            if($line.contains("https")){
                Write-Host "HTTPS found in: $mail"
            }
            if($line.contains("password")){
                Write-Host Password found in file: $mailfolder\$mailbox\$mail `n $line
            }
        }
    }
}
```
