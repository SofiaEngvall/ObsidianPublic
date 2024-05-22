
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://valley.thm/static/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e -x txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://valley.thm/static/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://valley.thm/static/3                    (Status: 200) [Size: 421858]
http://valley.thm/static/00                   (Status: 200) [Size: 127]
http://valley.thm/static/11                   (Status: 200) [Size: 627909]
http://valley.thm/static/9                    (Status: 200) [Size: 1190575]
http://valley.thm/static/5                    (Status: 200) [Size: 1426557]
http://valley.thm/static/12                   (Status: 200) [Size: 2203486]
http://valley.thm/static/10                   (Status: 200) [Size: 2275927]
http://valley.thm/static/1                    (Status: 200) [Size: 2473315]
Progress: 6407 / 441122 (1.45%)[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
[ERROR] context deadline exceeded (Client.Timeout or context cancellation while reading body)
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
```

http://valley.thm/static/00                   (Status: 200) [Size: 127]

