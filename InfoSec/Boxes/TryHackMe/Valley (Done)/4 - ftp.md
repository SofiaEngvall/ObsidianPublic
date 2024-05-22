
```sh
──(kali㉿kali)-[~]
└─$ ftp 10.10.171.184 37370
Connected to 10.10.171.184.
220 (vsFTPd 3.0.3)
Name (10.10.171.184:kali): 
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> 
ftp> exit
421 Timeout.
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ ftp 10.10.171.184 37370
Connected to 10.10.171.184.
220 (vsFTPd 3.0.3)
Name (10.10.171.184:kali): anonymous
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed

```

```sh
┌──(kali㉿kali)-[/usr/share/nmap]
└─$ sudo nmap -v -sS -n -p37370 --script "ftp*" 10.10.171.184
[sudo] password for kali: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-16 19:41 CEST
NSE: Loaded 8 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:41
Completed NSE at 19:41, 0.00s elapsed
Initiating Ping Scan at 19:41
Scanning 10.10.171.184 [4 ports]
Completed Ping Scan at 19:41, 0.06s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 19:41
Scanning 10.10.171.184 [1 port]
Discovered open port 37370/tcp on 10.10.171.184
Completed SYN Stealth Scan at 19:41, 0.06s elapsed (1 total ports)
NSE: Script scanning 10.10.171.184.
Initiating NSE at 19:41
Completed NSE at 19:41, 0.00s elapsed
Nmap scan report for 10.10.171.184
Host is up (0.040s latency).

PORT      STATE SERVICE
37370/tcp open  unknown

NSE: Script Post-scanning.
Initiating NSE at 19:41
Completed NSE at 19:41, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.32 seconds
           Raw packets sent: 5 (196B) | Rcvd: 2 (84B)
```