
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.224.11                                               
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-16 10:21 CEST
Nmap scan report for 10.10.224.11
Host is up (0.039s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.224.11\ADMIN$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.224.11\C$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.224.11\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: READ
|     Current user access: READ/WRITE
|   \\10.10.224.11\Users: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|_    Current user access: READ

Nmap done: 1 IP address (1 host up) scanned in 7.95 seconds
```

```sh
┌──(kali㉿kali)-[~/thm/gatekeeper]
└─$ smbget --recursive smb://10.10.224.11/Users 
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
Using netbios name KALI.
Using workgroup WORKGROUP.
Password for [WORKGROUP\kali]:
Using domain: WORKGROUP, user: kali
Server connect ok: //10.10.224.11/Users: 0x556924993d50
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/desktop.ini                         
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/Shows Desktop.lnk                   
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/Window Switcher.lnk                 
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/SendTo/Compressed (zipped) Folder.ZFSendToTarget           
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/SendTo/Desktop (create shortcut).DeskLink                  
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/SendTo/Desktop.ini                                         
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/SendTo/Fax Recipient.lnk                                   
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/SendTo/Mail Recipient.MAPIMail                             
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility/Desktop.ini  
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility/Ease of Access.lnk
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility/Magnify.lnk  
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility/Narrator.lnk 
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility/On-Screen Keyboard.lnk
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Command Prompt.lnk         
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Desktop.ini                
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad.lnk                
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Run.lnk                    
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/System Tools/computer.lnk  
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/System Tools/Control Panel.lnk
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/System Tools/Desktop.ini   
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/System Tools/Private Character Editor.lnk
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Windows Explorer.lnk       
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Maintenance/Desktop.ini                
smb://10.10.224.11/Users/Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Maintenance/Help.lnk                   
smb://10.10.224.11/Users/Default/NTUSER.DAT                                                                                   
smb://10.10.224.11/Users/Default/NTUSER.DAT.LOG                                                                               
smb://10.10.224.11/Users/Default/NTUSER.DAT.LOG1                                                                              
smb://10.10.224.11/Users/Default/NTUSER.DAT.LOG2                                                                              
smb://10.10.224.11/Users/Default/NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf                                      
smb://10.10.224.11/Users/Default/NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms 
smb://10.10.224.11/Users/Default/NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms 
smb://10.10.224.11/Users/desktop.ini                                                                                          
smb://10.10.224.11/Users/Share/gatekeeper.exe                                                                                 
Downloaded 1.52MB in 16 seconds
```
