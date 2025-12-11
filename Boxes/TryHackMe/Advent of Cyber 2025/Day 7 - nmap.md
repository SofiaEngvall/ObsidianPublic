
`tbfc-devqa01`
`10.82.165.44`
find: `KEYNAME:KEY`

```sh
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ ftp 10.81.166.95 21212
Connected to 10.81.166.95.
220 (vsFTPd 3.0.5)
Name (10.81.166.95:fixit42): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||18291|)
ftp: Can't connect to `10.81.166.95:18291': Connection timed out
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            13 Oct 22 16:27 tbfc_qa_key1
226 Directory send OK.
ftp> get tbfc_qa_key1
local: tbfc_qa_key1 remote: tbfc_qa_key1
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for tbfc_qa_key1 (13 bytes).
100% |*********************************************************************************|    13       13.18 KiB/s    00:00 ETA
226 Transfer complete.
13 bytes received in 00:00 (0.32 KiB/s)
ftp> quit
221 Goodbye.
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ cat tbfc_qa_key1 
KEY1:3aster_
```

KEY1:3aster_

```sh
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ nc 10.82.165.44 25251
TBFC maintd v0.2
Type HELP for commands.
HELP
Commands: HELP, STATUS, GET KEY, QUIT
STATUS
status: armed_for=50s, port=25251
GET KEY
KEY2:15_th3_
QUIT
bye
```

KEY2:15_th3_

```sh
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ nmap -sU 10.81.166.95
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-09 21:36 CET
Nmap scan report for 10.81.166.95
Host is up (0.042s latency).
Not shown: 999 open|filtered udp ports (no-response)
PORT   STATE SERVICE
53/udp open  domain

Nmap done: 1 IP address (1 host up) scanned in 16.44 seconds
```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ dig @10.81.166.95 TXT key3.tbfc.local +short
"KEY3:n3w_xm45"
```

KEY3:n3w_xm45


Full key: 3aster_15_th3_n3w_xm45

![[Images/Pasted image 20251209214837.png]]
![[Images/Pasted image 20251209215609.png]]

```sh
tbfcapp@tbfc-devqa01:~$ ss -tunlp                                                                                              
Netid        State         Recv-Q        Send-Q                   Local Address:Port                  Peer Address:Port        Process           
udp          UNCONN        0             0                              0.0.0.0:53                         0.0.0.0:*           
udp          UNCONN        0             0                    10.80.188.12%ens5:68                         0.0.0.0:*           
tcp          LISTEN        0             2048                         127.0.0.1:8000                       0.0.0.0:*           
 users:(("gunicorn",pid=940,fd=5),("gunicorn",pid=935,fd=5),("gunicorn",pid=673,fd=5))                                         
tcp          LISTEN        0             32                             0.0.0.0:53                         0.0.0.0:*           
tcp          LISTEN        0             4096                           0.0.0.0:22                         0.0.0.0:*           
tcp          LISTEN        0             4096                         127.0.0.1:7681                       0.0.0.0:*           
tcp          LISTEN        0             511                            0.0.0.0:80                         0.0.0.0:*           
tcp          LISTEN        0             151                          127.0.0.1:3306                       0.0.0.0:*           
tcp          LISTEN        0             50                             0.0.0.0:25251                      0.0.0.0:*           
tcp          LISTEN        0             32                             0.0.0.0:21212                      0.0.0.0:*           
tcp          LISTEN        0             4096                              [::]:22                            [::]:*           
```

```sh
tbfcapp@tbfc-devqa01:~$ mysql                                                                                              Welcome to the MySQL monitor.  Commands end with ; or \g.                                                                  Your MySQL connection id is 8                                                                                                                                  
Server version: 8.0.43-0ubuntu0.24.04.2 (Ubuntu)                                                                                                               
                                                                                                                                                               
Copyright (c) 2000, 2025, Oracle and/or its affiliates.                                                                                                        
                                                                                                                                                               
Oracle is a registered trademark of Oracle Corporation and/or its                                                                                              
affiliates. Other names may be trademarks of their respective                                                                                                  
owners.                                                                                                                                                        
                                                                                                                                                               
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.                                                                                 
                                                                                                                                                               
mysql> help                                                                                                                                                    
                                                                                                                                                               
For information about MySQL products and services, visit:                                                                                                      
   http://www.mysql.com/                                                                                                                                       
For developer information, including the MySQL Reference Manual, visit:                                                                                        
   http://dev.mysql.com/                                                                                                                                       
To buy MySQL Enterprise support, training, or other products, visit:                                                                                           
   https://shop.mysql.com/                                                                                                                                     
                                                                                                                                                               
List of all MySQL commands:                                                                                                                                    
Note that all text commands must be first on line and end with ';'                                                                                             
?         (\?) Synonym for `help'.                                                                                                                             
clear     (\c) Clear the current input statement.                                                                                                              
connect   (\r) Reconnect to the server. Optional arguments are db and host.                                                                                    
delimiter (\d) Set statement delimiter.                                                                                                                        
edit      (\e) Edit command with $EDITOR.                                                                                                                      
ego       (\G) Send command to mysql server, display result vertically.                                                                                        
exit      (\q) Exit mysql. Same as quit.                                                                                                                       
go        (\g) Send command to mysql server.                                                                                                                   
help      (\h) Display this help.                                                                                                                              
nopager   (\n) Disable pager, print to stdout.                                                                                                                 
notee     (\t) Don't write into outfile.                                                                                                                       
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.                                                                                        
print     (\p) Print current command.                                                                                                                          
prompt    (\R) Change your mysql prompt.                                                                                                                       
quit      (\q) Quit mysql.                                                                                                                                     
rehash    (\#) Rebuild completion hash.                                                                                                                        
source    (\.) Execute an SQL script file. Takes a file name as an argument.                                                                                   
status    (\s) Get status information from the server.                                                                                                         
system    (\!) Execute a system shell command, if enabled                                                                                                      
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.                                                                                 
use       (\u) Use another database. Takes database name as argument.                                                                                          
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.                                                      
warnings  (\W) Show warnings after every statement.                                                                                                            
nowarning (\w) Don't show warnings after every statement.                                                                                                      
resetconnection(\x) Clean session context.                                                                                                                     
query_attributes Sets string parameters (name1 value1 name2 value2 ...) for the next query to pick up.                                                         
ssl_session_data_print Serializes the current SSL session data to stdout or file                                                                               
                                                                                                                                                               
For server side help, type 'help contents'                                                                                                                     
                                                                                                                                                               
mysql> status                                                                                                                                                  
--------------                                                                                                                                                 
mysql  Ver 8.0.43-0ubuntu0.24.04.2 for Linux on x86_64 ((Ubuntu))                                                                                              
                                                                                                                                                               
Connection id:          8                                                                                                                                      
Current database:                                                                                                                                              
Current user:           tbfcapp@localhost                                                                                                                      
SSL:                    Not in use                                                                                                                             
Current pager:          stdout                                                                                                                                 
Using outfile:          ''                                                                                                                                     
Using delimiter:        ;                                                                                                                                      
Server version:         8.0.43-0ubuntu0.24.04.2 (Ubuntu)                                                                                                       
Protocol version:       10                                                                                                                                     
Connection:             Localhost via UNIX socket                                                                                                              
Server characterset:    utf8mb4                                                                                                                                
Db     characterset:    utf8mb4                                                                                                                                
Client characterset:    latin1                                                                                                                                 
Conn.  characterset:    latin1                                                                                                                                 
UNIX socket:            /var/run/mysqld/mysqld.sock                                                                                                            
Binary data as:         Hexadecimal                                                                                                                            
Uptime:                 24 min 25 sec                                                                                                                          
                                                                                                                                                               
Threads: 2  Questions: 5  Slow queries: 0  Opens: 119  Flush tables: 3  Open tables: 38  Queries per second avg: 0.003                                         
--------------                                                                                                                                                 
                                                                                                                                                               
mysql> use                                                                                                                                                     
ERROR:                                                                                                                                                         
USE must be followed by a database name                                                                                                                        
mysql> show databases;                                                                                                                                         
+--------------------+                                                                                                                                         
| Database           |                                                                                                                                         
+--------------------+                                                                                                                                         
| information_schema |                                                                                                                                         
| performance_schema |                                                                                                                                         
| tbfcqa01           |                                                                                                                                         
+--------------------+                                                                                                                                         
3 rows in set (0.02 sec)                                                                                                                                       
                                                                                                                                                               
mysql> use tbfcqa01                                                                                                                                            
Reading table information for completion of table and column names                                                                                             
You can turn off this feature to get a quicker startup with -A                                                                                                 
                                                                                                                                                               
Database changed                                                                                                                                               
mysql> show tables;                                                                                                                                            
+--------------------+                                                                                                                                         
| Tables_in_tbfcqa01 |                                                                                                                                         
+--------------------+                                                                                                                                         
| flags              |                                                                                                                                         
+--------------------+                                                                                                                                         
1 row in set (0.00 sec)                                                                                                                                        
                                                                                                                                                               
mysql> select * from flags;                                                                                                                                    
+----+------------------------------+                                                                                                                          
| id | flag                         |                                                                                                                          
+----+------------------------------+                                                                                                                          
|  1 | THM{4ll_s3rvice5_d1sc0vered} |                                                                                                                          
+----+------------------------------+                                                                                                                          
1 row in set (0.01 sec)                                                                                                                                        
                                                                                                                                                               
mysql>                                                                                                                                                         
```

THM{4ll_s3rvice5_d1sc0vered}

### nmap scans

```
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ nmap -p- -sC -sV -Pn 10.82.165.44  
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-09 20:56 CET
Nmap scan report for 10.82.165.44
Host is up (0.041s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|_  256 1e:6e:b0:8a:88:a5:d5:f5:fa:bc:c3:71:b5:a7:5b:53 (ECDSA)
80/tcp    open  http    nginx
|_http-title: TBFC QA \xE2\x80\x94 EAST-mas
21212/tcp open  ftp     vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.171.66
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
25251/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, LDAPBindReq, NULL, RPCCheck, SMBProgNeg, X11Probe: 
|     TBFC maintd v0.2
|     Type HELP for commands.
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, LDAPSearchReq, RTSPRequest: 
|     TBFC maintd v0.2
|     Type HELP for commands.
|     unknown command
|     unknown command
|   Help: 
|     TBFC maintd v0.2
|     Type HELP for commands.
|     Commands: HELP, STATUS, GET KEY, QUIT
|   Kerberos, LPDString, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     TBFC maintd v0.2
|     Type HELP for commands.
|     unknown command
|   SIPOptions: 
|     TBFC maintd v0.2
|     Type HELP for commands.
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|     unknown command
|_    unknown command
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25251-TCP:V=7.95%I=7%D=12/9%Time=69387F98%P=x86_64-pc-linux-gnu%r(N
SF:ULL,29,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20commands\.\n")%
SF:r(GenericLines,49,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20comm
SF:ands\.\nunknown\x20command\nunknown\x20command\n")%r(GetRequest,49,"TBF
SF:C\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20commands\.\nunknown\x20com
SF:mand\nunknown\x20command\n")%r(HTTPOptions,49,"TBFC\x20maintd\x20v0\.2\
SF:nType\x20HELP\x20for\x20commands\.\nunknown\x20command\nunknown\x20comm
SF:and\n")%r(RTSPRequest,49,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\
SF:x20commands\.\nunknown\x20command\nunknown\x20command\n")%r(RPCCheck,29
SF:,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20commands\.\n")%r(DNSV
SF:ersionBindReqTCP,29,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20co
SF:mmands\.\n")%r(DNSStatusRequestTCP,29,"TBFC\x20maintd\x20v0\.2\nType\x2
SF:0HELP\x20for\x20commands\.\n")%r(Help,4F,"TBFC\x20maintd\x20v0\.2\nType
SF:\x20HELP\x20for\x20commands\.\nCommands:\x20HELP,\x20STATUS,\x20GET\x20
SF:KEY,\x20QUIT\n")%r(SSLSessionReq,39,"TBFC\x20maintd\x20v0\.2\nType\x20H
SF:ELP\x20for\x20commands\.\nunknown\x20command\n")%r(TerminalServerCookie
SF:,39,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20commands\.\nunknow
SF:n\x20command\n")%r(TLSSessionReq,39,"TBFC\x20maintd\x20v0\.2\nType\x20H
SF:ELP\x20for\x20commands\.\nunknown\x20command\n")%r(Kerberos,39,"TBFC\x2
SF:0maintd\x20v0\.2\nType\x20HELP\x20for\x20commands\.\nunknown\x20command
SF:\n")%r(SMBProgNeg,29,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20c
SF:ommands\.\n")%r(X11Probe,29,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20f
SF:or\x20commands\.\n")%r(FourOhFourRequest,49,"TBFC\x20maintd\x20v0\.2\nT
SF:ype\x20HELP\x20for\x20commands\.\nunknown\x20command\nunknown\x20comman
SF:d\n")%r(LPDString,39,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\x20for\x20c
SF:ommands\.\nunknown\x20command\n")%r(LDAPSearchReq,49,"TBFC\x20maintd\x2
SF:0v0\.2\nType\x20HELP\x20for\x20commands\.\nunknown\x20command\nunknown\
SF:x20command\n")%r(LDAPBindReq,29,"TBFC\x20maintd\x20v0\.2\nType\x20HELP\
SF:x20for\x20commands\.\n")%r(SIPOptions,D9,"TBFC\x20maintd\x20v0\.2\nType
SF:\x20HELP\x20for\x20commands\.\nunknown\x20command\nunknown\x20command\n
SF:unknown\x20command\nunknown\x20command\nunknown\x20command\nunknown\x20
SF:command\nunknown\x20command\nunknown\x20command\nunknown\x20command\nun
SF:known\x20command\nunknown\x20command\n");
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 324.29 seconds
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/thm]
└─$ nmap -p- --script=banner 10.82.165.44
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-09 21:06 CET
Nmap scan report for 10.82.165.44
Host is up (0.043s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
21212/tcp open  trinket-agent
|_banner: 220 (vsFTPd 3.0.5)
25251/tcp open  unknown
|_banner: TBFC maintd v0.2\x0AType HELP for commands.

Nmap done: 1 IP address (1 host up) scanned in 122.81 seconds

```