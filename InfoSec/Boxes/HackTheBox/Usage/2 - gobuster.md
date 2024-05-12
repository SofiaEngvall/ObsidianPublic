
no info gotten, just a lot of crap. might it be that it's so slow? odd stuff

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.11.18 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.18
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
http://10.10.11.18/3                    (Status: 503) [Size: 206]
http://10.10.11.18/archives             (Status: 503) [Size: 206]
http://10.10.11.18/keygen               (Status: 503) [Size: 206]
http://10.10.11.18/help                 (Status: 503) [Size: 206]
http://10.10.11.18/rss                  (Status: 503) [Size: 206]
...
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://usage.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e       
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://usage.htb
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
http://usage.htb/2006                 (Status: 503) [Size: 206]
http://usage.htb/keygen               (Status: 503) [Size: 206]
http://usage.htb/articles             (Status: 503) [Size: 206]
http://usage.htb/archive              (Status: 503) [Size: 206]
http://usage.htb/09                   (Status: 503) [Size: 206]
...
http://usage.htb/icom_foot            (Status: 503) [Size: 206]
http://usage.htb/grcom_foot           (Status: 503) [Size: 206]
http://usage.htb/team                 (Status: 503) [Size: 206]
http://usage.htb/u                    (Status: 503) [Size: 206]
http://usage.htb/earthweb_foot2       (Status: 503) [Size: 206]
http://usage.htb/out                  (Status: 503) [Size: 206]
http://usage.htb/ruledivide_foot      (Status: 503) [Size: 206]
Progress: 622 / 220561 (0.28%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 622 / 220561 (0.28%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://usage.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e -b 503
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://usage.htb
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   503
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================

Error: the server returns a status code that matches the provided options for non existing urls. http://usage.htb/50f0cb1c-5746-4134-9b43-8cb1a83dd4eb => 404 (Length: 6603). To continue please exclude the status code or the length
```