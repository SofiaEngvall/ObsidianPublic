
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://watcher.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://watcher.thm
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
http://watcher.thm/css                  (Status: 200) [Size: 1166]
http://watcher.thm/images               (Status: 200) [Size: 1358]
http://watcher.thm/server-status        (Status: 403) [Size: 276]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```