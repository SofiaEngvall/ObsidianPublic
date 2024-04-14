
```sh
┌──(kali㉿kali)-[~/shells]
└─$ gobuster dir -r -u http://10.10.67.14/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.67.14/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 290]
/login.php            (Status: 200) [Size: 882]
/assets               (Status: 200) [Size: 2190]
/portal.php           (Status: 200) [Size: 882]
/robots.txt           (Status: 200) [Size: 17]
/.php                 (Status: 403) [Size: 290]
/denied.php           (Status: 200) [Size: 882]
/server-status        (Status: 403) [Size: 299]
/clue.txt             (Status: 200) [Size: 54]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================

```
