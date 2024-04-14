
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.11.229 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.229
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 314] [--> http://10.10.11.229/uploads/]
/shop                 (Status: 301) [Size: 311] [--> http://10.10.11.229/shop/]
/assets               (Status: 301) [Size: 313] [--> http://10.10.11.229/assets/]
/upload.php           (Status: 200) [Size: 5322]
/index.php            (Status: 200) [Size: 16738]
/.php                 (Status: 403) [Size: 277]
/.php                 (Status: 403) [Size: 277]
/server-status        (Status: 403) [Size: 277]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
```

```sh

```