
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.171.184 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.171.184
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.171.184/gallery              (Status: 200) [Size: 946]
http://10.10.171.184/static               (Status: 200) [Size: 567]
http://10.10.171.184/pricing              (Status: 200) [Size: 1140]
http://10.10.171.184/server-status        (Status: 403) [Size: 278]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ feroxbuster -u http://valley.thm -E   
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://valley.thm
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
403      GET        9l       28w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      272c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      140l      394w     3940c http://valley.thm/gallery/gallery.html
200      GET       38l      129w     1163c http://valley.thm/index.html
200      GET       32l       61w      924c http://valley.thm/pricing/pricing.html
200      GET       52l      106w      945c http://valley.thm/styles.css
200      GET       38l      129w     1163c http://valley.thm/
301      GET        9l       28w      310c http://valley.thm/gallery => http://valley.thm/gallery/
301      GET        9l       28w      309c http://valley.thm/static => http://valley.thm/static/
200      GET        3l       10w       57c http://valley.thm/pricing/note.txt
301      GET        9l       28w      310c http://valley.thm/pricing => http://valley.thm/pricing/
[####################] - 2m    209756/209756  0s      found:9       errors:40     
[####################] - 2m    119741/119741  1269/s  http://valley.thm/ 
[####################] - 0s     30000/30000   152284/s http://valley.thm/pricing/ => Directory listing
[####################] - 0s     30000/30000   500000/s http://valley.thm/gallery/ => Directory listing
[####################] - 0s     60000/60000   566038/s http://valley.thm/static/ => Directory listing  
```

