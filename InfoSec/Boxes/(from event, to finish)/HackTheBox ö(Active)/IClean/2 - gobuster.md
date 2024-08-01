
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.11.12 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,py,html,js
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.12
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              py,html,js,txt
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 274]
/.html                (Status: 403) [Size: 276]
/.html                (Status: 403) [Size: 276]
/server-status        (Status: 403) [Size: 276]
Progress: 1102800 / 1102805 (100.00%)
===============================================================                                                               
Finished                                                                                                                      
===============================================================   
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://capiclean.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64            
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://capiclean.htb
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/about                (Status: 200) [Size: 5267]
/login                (Status: 200) [Size: 2106]
/services             (Status: 200) [Size: 8592]
/team                 (Status: 200) [Size: 8109]
/quote                (Status: 200) [Size: 2237]
/logout               (Status: 200) [Size: 16697]
/dashboard            (Status: 200) [Size: 16697]
/choose               (Status: 200) [Size: 6084]
/server-status        (Status: 403) [Size: 278]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```