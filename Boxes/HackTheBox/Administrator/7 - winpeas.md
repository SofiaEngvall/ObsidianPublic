
Autorun Applications
È Check if you can modify other users AutoRuns binaries (Note that is normal that you can modify HKCU registry and binaries indicated there) https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries 
```sh

    Folder: C:\windows\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]
   =================================================================================================


    Folder: C:\windows\system32\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]

```

Current UDP Listening Ports
È Check for services restricted from the outside 
  Enumerating IPv4 connections
```
    UDP        127.0.0.1             50202         *:*                            3020              ismserv
  UDP        127.0.0.1             51933         *:*                            2044              svchost
  UDP        127.0.0.1             52708         *:*                            2916              Microsoft.ActiveDirectory.WebServices
  UDP        127.0.0.1             52710         *:*                            1380              svchost
  UDP        127.0.0.1             55378         *:*                            3720              WmiPrvSE
  UDP        127.0.0.1             56038         *:*                            1424              svchost
  UDP        127.0.0.1             58311         *:*                            2996              dfsrs

```


