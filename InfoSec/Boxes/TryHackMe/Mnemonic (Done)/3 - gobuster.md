
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.183.107 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64    
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.183.107
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/webmasters           (Status: 301) [Size: 319] [--> http://10.10.183.107/webmasters/]
/server-status        (Status: 403) [Size: 278]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.183.107/webmasters -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt, jpg, zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.183.107/webmasters
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.                    (Status: 200) [Size: 0]
/admin                (Status: 301) [Size: 325] [--> http://10.10.183.107/webmasters/admin/]
/backups              (Status: 301) [Size: 327] [--> http://10.10.183.107/webmasters/backups/]
/.                    (Status: 200) [Size: 0]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt, jpg, zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.183.107/webmasters/backups
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.                    (Status: 200) [Size: 0]
/.                    (Status: 200) [Size: 0]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,jpg,zip  
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.183.107/webmasters/backups
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              jpg,zip,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/backups.zip          (Status: 200) [Size: 409]
Progress: 882240 / 882244 (100.00%)
===============================================================
Finished
===============================================================

```

We have the name of a zip file on http with status 200.

We download it with firefox.
http://10.10.183.107/webmasters/backups/backups.zip
