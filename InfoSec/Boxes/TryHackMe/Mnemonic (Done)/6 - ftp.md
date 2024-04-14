
```sh
250 Directory successfully changed.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10092|)
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> get *
```

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ftp ftpuser@10.10.183.107
Connected to 10.10.183.107.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||10048|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> help
Commands may be abbreviated.  Commands are:

!               delete          hash            mlsd            pdir            remopts         struct
$               dir             help            mlst            pls             rename          sunique
account         disconnect      idle            mode            pmlsd           reset           system
append          edit            image           modtime         preserve        restart         tenex
ascii           epsv            lcd             more            progress        rhelp           throttle
bell            epsv4           less            mput            prompt          rmdir           trace
binary          epsv6           lpage           mreget          proxy           rstatus         type
bye             exit            lpwd            msend           put             runique         umask
case            features        ls              newer           pwd             send            unset
cd              fget            macdef          nlist           quit            sendport        usage
cdup            form            mdelete         nmap            quote           set             user
chmod           ftp             mdir            ntrans          rate            site            verbose
close           gate            mget            open            rcvbuf          size            xferbuf
cr              get             mkdir           page            recv            sndbuf          ?
debug           glob            mls             passive         reget           status
ftp> help get
get             receive file
ftp> get *
local: backups remote: *
229 Entering Extended Passive Mode (|||10100|)
550 Failed to open file.
ftp> get data-1
local: data-1 remote: data-1
229 Entering Extended Passive Mode (|||10088|)
550 Failed to open file.
ftp> get data-1/
local: data-1 remote: data-1/
229 Entering Extended Passive Mode (|||10100|)
550 Failed to open file.
ftp> cd data-1
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||10087|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -la
229 Entering Extended Passive Mode (|||10050|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-2
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10034|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-3
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10057|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10092|)
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> get *
local: backups remote: *
229 Entering Extended Passive Mode (|||10091|)
550 Failed to open file.
ftp> get .
local: . remote: .
229 Entering Extended Passive Mode (|||10049|)
550 Failed to open file.
ftp> cd ..
250 Directory successfully changed.
ftp> ls -R
229 Entering Extended Passive Mode (|||10055|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> ls -r
229 Entering Extended Passive Mode (|||10035|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
226 Directory send OK.
ftp> cd data-5
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10099|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-6
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10040|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-7
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10057|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-8
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10047|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-9
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10021|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-10
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10051|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-5
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10059|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10055|)
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||10051|)
150 Opening BINARY mode data connection for id_rsa (1766 bytes).
100% |*********************************************************************************|  1766       19.87 KiB/s    00:00 ETA
226 Transfer complete.
1766 bytes received in 00:00 (13.71 KiB/s)
ftp> get not.txt
local: not.txt remote: not.txt
229 Entering Extended Passive Mode (|||10006|)
150 Opening BINARY mode data connection for not.txt (31 bytes).
100% |*********************************************************************************|    31      137.60 KiB/s    00:00 ETA
226 Transfer complete.
31 bytes received in 00:00 (0.75 KiB/s)
ftp> cd 3
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10096|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 14  2020 .
drwxr-xr-x    4 0        0            4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd 4
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||10059|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 14  2020 .
drwxr-xr-x    4 0        0            4096 Jul 14  2020 ..
226 Directory send OK.
ftp> 

```