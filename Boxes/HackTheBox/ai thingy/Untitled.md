

```sh
┌──(kali㉿proxli)-[~/shells]
└─$ gobuster dir -r -u http://http://83.136.249.46:41241 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://http://83.136.249.46:41241
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

Error: error on running gobuster: unable to connect to http://http://83.136.249.46:41241/: Get "http://http//83.136.249.46:41241/": dial tcp: lookup http on 8.8.8.8:53: no such host
                                                                                                               
┌──(kali㉿proxli)-[~/shells]
└─$ gobuster dir -r -u http://https://83.136.249.46:41241 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://https://83.136.249.46:41241
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

Error: error on running gobuster: unable to connect to http://https://83.136.249.46:41241/: Get "http://https//83.136.249.46:41241/": dial tcp: lookup https on 8.8.8.8:53: no such host
                                                                                                               
┌──(kali㉿proxli)-[~/shells]
└─$ gobuster dir -r -u https://83.136.249.46:41241 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://83.136.249.46:41241
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

Error: error on running gobuster: unable to connect to https://83.136.249.46:41241/: Get "https://83.136.249.46:41241/": http: server gave HTTP response to HTTPS client
                                                                                                               
┌──(kali㉿proxli)-[~/shells]
└─$ gobuster dir -r -u http://83.136.249.46:41241 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://83.136.249.46:41241
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
http://83.136.249.46:41241/login                (Status: 200) [Size: 1472]
http://83.136.249.46:41241/register             (Status: 200) [Size: 3432]
http://83.136.249.46:41241/chat                 (Status: 200) [Size: 1472]
http://83.136.249.46:41241/dashboard            (Status: 200) [Size: 1472]
http://83.136.249.46:41241/like                 (Status: 405) [Size: 153]
http://83.136.249.46:41241/matches              (Status: 500) [Size: 265]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```