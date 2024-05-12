
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://mafialive.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://mafialive.thm
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://mafialive.thm/test.php             (Status: 200) [Size: 286]
http://mafialive.thm/.php                 (Status: 403) [Size: 278]
http://mafialive.thm/.php                 (Status: 403) [Size: 278]
http://mafialive.thm/server-status        (Status: 403) [Size: 278]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ feroxbuster -u http://mafialive.thm -E                                     

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://mafialive.thm
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
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET       15l       21w      286c http://mafialive.thm/test.php
403      GET        9l       28w      278c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        3l        3w       59c http://mafialive.thm/
[####################] - 55s    60002/60002   0s      found:2       errors:0      
[##########>---------] - 54s    30000/60000   552/s   http://mafialive.thm/   
```

found test.php
