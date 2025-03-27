
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://pilgrimage.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                 http://pilgrimage.htb
[+] Method:              GET
[+] Threads:             64
[+] Wordlist:            /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:          gobuster/3.6
[+] Extensions:          php
[+] Timeout:             10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.php        (Status: 200) [Size: 7621]
/login.php        (Status: 200) [Size: 6166]
/register.php     (Status: 200) [Size: 6173]
/assets           (Status: 301) [Size: 169] [--> http://pilgrimage.htb/assets/]
/logout.php       (Status: 302) [Size: 0] [--> /]
/vendor           (Status: 301) [Size: 169] [--> http://pilgrimage.htb/vendor/]
/dashboard.php    (Status: 302) [Size: 0] [--> /login.php]
/tmp              (Status: 301) [Size: 169] [--> http://pilgrimage.htb/tmp/]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://pilgrimage.htb/assets -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x js                                
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                 http://pilgrimage.htb/assets
[+] Method:              GET
[+] Threads:             64
[+] Wordlist:            /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:          gobuster/3.6
[+] Extensions:          js
[+] Timeout:             10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images           (Status: 301) [Size: 169] [--> http://pilgrimage.htb/assets/images/]
/css              (Status: 301) [Size: 169] [--> http://pilgrimage.htb/assets/css/]
/js               (Status: 301) [Size: 169] [--> http://pilgrimage.htb/assets/js/]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
  
 
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://pilgrimage.htb/assets/js/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x js
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                 http://pilgrimage.htb/assets/js/
[+] Method:              GET
[+] Threads:             64
[+] Wordlist:            /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:          gobuster/3.6
[+] Extensions:          js
[+] Timeout:             10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/custom.js        (Status: 200) [Size: 5292]
/tabs.js          (Status: 200) [Size: 485937]
/popup.js         (Status: 200) [Size: 1031]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
```

