
```sh
┌──(fixit㉿asusx555b)-[~]
└─$ gobuster dir -r -u http://titanic.htb -w /usr/share/wordlists/seclists/Discovery/Web-Content/quickhits.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://titanic.htb
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/quickhits.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://titanic.htb/download             (Status: 400) [Size: 41]
http://titanic.htb/server-status/       (Status: 403) [Size: 276]
Progress: 2565 / 2566 (99.96%)
===============================================================
Finished
===============================================================

┌──(fixit㉿asusx555b)-[~]
└─$ gobuster dir -r -u http://titanic.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://titanic.htb
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
http://titanic.htb/download             (Status: 400) [Size: 41]
http://titanic.htb/book                 (Status: 405) [Size: 153]
http://titanic.htb/server-status        (Status: 403) [Size: 276]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================


┌──(fixit㉿asusx555b)-[~/Downloads]
└─$ gobuster dir -k -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -t 20 -u http://titanic.htb
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://titanic.htb
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/download             (Status: 400) [Size: 41]
/book                 (Status: 405) [Size: 153]
/server-status        (Status: 403) [Size: 276]
Progress: 20675 / 26584 (77.77%)[ERROR] parse "http://titanic.htb/error\x1f_log": net/url: invalid control character in URL
Progress: 26583 / 26584 (100.00%)
===============================================================
Finished
===============================================================
```
