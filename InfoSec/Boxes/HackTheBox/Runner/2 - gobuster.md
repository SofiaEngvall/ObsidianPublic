
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://runner.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e       
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://runner.htb
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
http://runner.htb/assets               (Status: 403) [Size: 162]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://runner.htb:8000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://runner.htb:8000
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
http://runner.htb:8000/version              (Status: 200) [Size: 9]
http://runner.htb:8000/health               (Status: 200) [Size: 3]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://runner.htb/version:8000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://runner.htb/version:8000
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
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://runner.htb/health:8000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://runner.htb/health:8000
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
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================

```