
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://internal.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://internal.thm
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
http://internal.thm/blog                 (Status: 200) [Size: 53892]
http://internal.thm/javascript           (Status: 403) [Size: 277]
http://internal.thm/phpmyadmin           (Status: 200) [Size: 10531]
http://internal.thm/server-status        (Status: 403) [Size: 277]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://internal.thm/blog -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://internal.thm/blog
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
http://internal.thm/blog/wp-content           (Status: 200) [Size: 0]
http://internal.thm/blog/wp-includes          (Status: 403) [Size: 277]
http://internal.thm/blog/wp-admin             (Status: 200) [Size: 4530]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://internal.thm/blog/wp-content -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://internal.thm/blog/wp-content
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
http://internal.thm/blog/wp-content/themes               (Status: 200) [Size: 0]
http://internal.thm/blog/wp-content/plugins              (Status: 200) [Size: 0]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```
