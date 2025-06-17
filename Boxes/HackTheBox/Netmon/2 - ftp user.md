
```sh
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||50361|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
11-10-23  10:20AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50364|)
125 Data connection already open; Transfer starting.
02-25-19  11:44PM       <DIR>          Administrator
01-15-24  11:03AM       <DIR>          Public
226 Transfer complete.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50372|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd desktop
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50373|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1195 PRTG Enterprise Console.lnk
02-03-19  12:18AM                 1160 PRTG Network Monitor.lnk
05-16-25  08:16AM                   34 user.txt
226 Transfer complete.
ftp> get user.txt
local: user.txt remote: user.txt
229 Entering Extended Passive Mode (|||50374|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|    34        1.43 KiB/s    00:00 ETA
226 Transfer complete.
34 bytes received in 00:00 (1.41 KiB/s)
```

```sh
┌──(kali㉿proxli)-[~]
└─$ cat user.txt
a8097b0439c9c3cf6e32e898c9510088
```

