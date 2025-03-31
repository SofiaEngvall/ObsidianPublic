
```sh
┌──(fixit㉿asusx555b)-[~]
└─$ gobuster dir -r -u http://frizz.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e        
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://frizz.htb
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://frizz.htb/home                 (Status: 200) [Size: 16016]
http://frizz.htb/Home                 (Status: 200) [Size: 16016]
http://frizz.htb/%20                  (Status: 403) [Size: 298]
http://frizz.htb/*checkout*           (Status: 403) [Size: 298]
http://frizz.htb/HOME                 (Status: 200) [Size: 16016]
http://frizz.htb/*docroot*            (Status: 403) [Size: 298]
http://frizz.htb/*                    (Status: 403) [Size: 298]
http://frizz.htb/con                  (Status: 403) [Size: 298]
http://frizz.htb/http%3A              (Status: 403) [Size: 298]
http://frizz.htb/**http%3a            (Status: 403) [Size: 298]
Progress: 36183 / 220561 (16.40%)[ERROR] Get "http://frizz.htb/000075": context deadline excee
```