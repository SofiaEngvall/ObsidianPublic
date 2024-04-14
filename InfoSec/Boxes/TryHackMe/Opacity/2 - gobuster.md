
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.206.202 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.206.202
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/login.php            (Status: 200) [Size: 848]
/.php                 (Status: 403) [Size: 278]
/index.php            (Status: 200) [Size: 848]
/logout.php           (Status: 200) [Size: 848]
/cloud                (Status: 200) [Size: 639]
/.php                 (Status: 403) [Size: 278]
/server-status        (Status: 403) [Size: 278]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```

/login.php            (Status: 200) [Size: 848]
/cloud                (Status: 200) [Size: 639]


```sh
┌──(kali㉿kali)-[~]
└─$ feroxbuster -u http://10.10.66.65/ -E  

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.66.65/
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💰  Collect Extensions    │ true
 💸  Ignored Extensions    │ [Images, Movies, Audio, etc...]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
302      GET        0l        0w        0c http://10.10.66.65/ => login.php
301      GET        9l       28w      308c http://10.10.66.65/css => http://10.10.66.65/css/
301      GET        9l       28w      310c http://10.10.66.65/cloud => http://10.10.66.65/cloud/
301      GET        9l       28w      317c http://10.10.66.65/cloud/images => http://10.10.66.65/cloud/images/
[####################] - 56s   120007/120007  0s      found:4       errors:91     
[####################] - 52s    30000/30000   577/s   http://10.10.66.65/ 
[####################] - 53s    30000/30000   569/s   http://10.10.66.65/css/ 
[####################] - 38s    30000/30000   796/s   http://10.10.66.65/cloud/ 
[####################] - 39s    30000/30000   768/s   http://10.10.66.65/cloud/images/                                      
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.66.65/cloud/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.66.65/cloud/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 276]
/index.php            (Status: 200) [Size: 648]
/storage.php          (Status: 200) [Size: 757]
/.php                 (Status: 403) [Size: 276]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.66.65/cloud/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.66.65/cloud/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.php            (Status: 200) [Size: 648]
/.php                 (Status: 403) [Size: 276]
/storage.php          (Status: 200) [Size: 757]
/.php                 (Status: 403) [Size: 276]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```
