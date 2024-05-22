ftp can be secured by used tls = ftps, default port 990
and by using ssh = sftp


### Basic FTP commands

Can be used with telnet/nc

USER username
PASS password
STAT
SYST   get system type info
PASV   switches to passive mode
- Active: In the active mode, the data is sent over a separate channel originating from the FTP server’s port 20.
- Passive: In the passive mode, the data is sent over a separate channel originating from an FTP client’s port above port number 1023.
TYPE A   switches transfer mode to ACSII
TYPE I   switches transfer mode to binary
(we can't transfer files with telnet/nc since a separate connection is created on another port)

```sh
┌──(kali㉿kali)-[~/thm/nmap]
└─$ telnet 10.10.240.43 21
Trying 10.10.240.43...
Connected to 10.10.240.43.
Escape character is '^]'.
220 (vsFTPd 3.0.3)
USER frank
331 Please specify the password.
PASS D2xc9CgD
230 Login successful.
STAT
211-FTP server status:
     Connected to ::ffff:10.18.21.236
     Logged in as frank
     TYPE: ASCII
     No session bandwidth limit
     Session timeout in seconds is 300
     Control connection is plain text
     Data connections will be plain text
     At session startup, client count was 1
     vsFTPd 3.0.3 - secure, fast, stable
211 End of status
SYST
215 UNIX Type: L8
PASV
227 Entering Passive Mode (10,10,240,43,111,47).
HELP
214-The following commands are recognized.
 ABOR ACCT ALLO APPE CDUP CWD  DELE EPRT EPSV FEAT HELP LIST MDTM MKD
 MODE NLST NOOP OPTS PASS PASV PORT PWD  QUIT REIN REST RETR RMD  RNFR
 RNTO SITE SIZE SMNT STAT STOR STOU STRU SYST TYPE USER XCUP XCWD XMKD
 XPWD XRMD
214 Help OK.
ACCT
502 ACCT not implemented.
MODE
504 Bad MODE command.
quit
Connection closed by foreign host.
```

```sh
┌──(kali㉿kali)-[~/thm/nmap]
└─$ ftp 10.10.240.43                         
Connected to 10.10.240.43.
220 (vsFTPd 3.0.3)
Name (10.10.240.43:kali): frank
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||62030|)
150 Here comes the directory listing.
drwx------   10 1001     1001         4096 Sep 15  2021 Maildir
-rw-rw-r--    1 1001     1001         4006 Sep 15  2021 README.txt
-rw-rw-r--    1 1001     1001           39 Sep 15  2021 ftp_flag.thm
226 Directory send OK.
ftp> ascii
200 Switching to ASCII mode.
ftp> ls Maildir
229 Entering Extended Passive Mode (|||11013|)
150 Here comes the directory listing.
drwx------    2 1001     1001         4096 Sep 15  2021 courierimapkeywords
drwx------    2 1001     1001         4096 Sep 15  2021 cur
drwx------    2 1001     1001         4096 Sep 15  2021 new
drwx------    2 1001     1001         4096 Sep 15  2021 tmp
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
ftp> mget *
mget Maildir [anpqy?]? y
229 Entering Extended Passive Mode (|||36977|)
550 Failed to open file.
mget README.txt [anpqy?]? y
229 Entering Extended Passive Mode (|||50916|)
150 Opening BINARY mode data connection for README.txt (4006 bytes).
100% |*********************************************************************************|  4006        1.13 MiB/s    00:00 ETA
226 Transfer complete.
WARNING! 9 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
4006 bytes received in 00:00 (92.63 KiB/s)
mget ftp_flag.thm [anpqy?]? a
Prompting off for duration of mget.
229 Entering Extended Passive Mode (|||45380|)
150 Opening BINARY mode data connection for ftp_flag.thm (39 bytes).
100% |*********************************************************************************|    39      239.53 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 2 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
39 bytes received in 00:00 (0.99 KiB/s)
ftp> help mget
mget            get multiple files
ftp> mget help
ftp> exit
221 Goodbye.
```

