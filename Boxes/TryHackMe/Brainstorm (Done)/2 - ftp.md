
can connect but no answer on ls, times out

the same with wget but worked with --no-passive

```sh
┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ wget ftp://10.10.32.52/*
--2024-10-11 22:56:57--  ftp://10.10.32.52/*
           => ‘.listing’
Connecting to 10.10.32.52:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD not needed.
==> PASV ... couldn't connect to 10.10.32.52 port 49295: Connection timed out
Retrying.
...
```

```sh
┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ wget -m --no-passive ftp://anonymous:anonymous@10.10.32.52  
--2024-10-11 23:37:59--  ftp://anonymous:*password*@10.10.32.52/
           => ‘10.10.32.52/.listing’
Connecting to 10.10.32.52:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD not needed.
==> PORT ... done.    ==> LIST ... done.

10.10.32.52/.listing                [ <=>                                                  ]      51  --.-KB/s    in 0s      

==> PORT ... done.    ==> LIST ... done.

10.10.32.52/.listing                [ <=>                                                  ]      51  --.-KB/s    in 0s      

2024-10-11 23:38:00 (9.54 MB/s) - ‘10.10.32.52/.listing’ saved [102]

--2024-10-11 23:38:00--  ftp://anonymous:*password*@10.10.32.52/chatserver/
           => ‘10.10.32.52/chatserver/.listing’
==> CWD (1) /chatserver ... done.
==> PORT ... done.    ==> LIST ... done.

10.10.32.52/chatserver/.listing     [ <=>                                                  ]     107  --.-KB/s    in 0s      

2024-10-11 23:38:00 (6.02 MB/s) - ‘10.10.32.52/chatserver/.listing’ saved [107]

--2024-10-11 23:38:00--  ftp://anonymous:*password*@10.10.32.52/chatserver/chatserver.exe
           => ‘10.10.32.52/chatserver/chatserver.exe’
==> CWD not required.
==> PORT ... done.    ==> RETR chatserver.exe ... done.
Length: 43747 (43K)

10.10.32.52/chatserver/chatserv 100%[=====================================================>]  42.72K   183KB/s    in 0.2s    

2024-10-11 23:38:00 (183 KB/s) - ‘10.10.32.52/chatserver/chatserver.exe’ saved [43747]

--2024-10-11 23:38:00--  ftp://anonymous:*password*@10.10.32.52/chatserver/essfunc.dll
           => ‘10.10.32.52/chatserver/essfunc.dll’
==> CWD not required.
==> PORT ... done.    ==> RETR essfunc.dll ... done.
Length: 30761 (30K)

10.10.32.52/chatserver/essfunc. 100%[=====================================================>]  30.04K  --.-KB/s    in 0.1s    

2024-10-11 23:38:01 (256 KB/s) - ‘10.10.32.52/chatserver/essfunc.dll’ saved [30761]

FINISHED --2024-10-11 23:38:01--
Total wall clock time: 1.2s
Downloaded: 4 files, 73K in 0.4s (208 KB/s)
```


```sh
┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ ls -la
total 12
drwxrwxr-x 3 kali kali 4096 Oct 11 23:38 .
drwxrwxr-x 3 kali kali 4096 Oct 11 22:56 ..
drwxrwxr-x 3 kali kali 4096 Oct 11 23:38 10.10.32.52

┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ cd 10.10.32.52 

┌──(kali㉿kali)-[~/thm/brainstorm/ftp/10.10.32.52]
└─$ ls -la
total 16
drwxrwxr-x 3 kali kali 4096 Oct 11 23:38 .
drwxrwxr-x 3 kali kali 4096 Oct 11 23:38 ..
-rw-rw-r-- 1 kali kali   51 Oct 11 23:38 .listing
drwxrwxr-x 2 kali kali 4096 Oct 11 23:38 chatserver

┌──(kali㉿kali)-[~/thm/brainstorm/ftp/10.10.32.52]
└─$ cd chatserver 

┌──(kali㉿kali)-[~/…/brainstorm/ftp/10.10.32.52/chatserver]
└─$ ls -la
total 88
drwxrwxr-x 2 kali kali  4096 Oct 11 23:38 .
drwxrwxr-x 3 kali kali  4096 Oct 11 23:38 ..
-rw-rw-r-- 1 kali kali   107 Oct 11 23:38 .listing
-rw-rw-r-- 1 kali kali 43747 Aug 29  2019 chatserver.exe
-rw-rw-r-- 1 kali kali 30761 Aug 29  2019 essfunc.dll
```

