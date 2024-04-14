
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.51.95:12340 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.51.95:12340
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/rms                  (Status: 200) [Size: 5982]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.51.95:12340/rms -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.51.95:12340/rms
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 403) [Size: 213]
/admin                (Status: 200) [Size: 805]
/css                  (Status: 403) [Size: 210]
Progress: 2558 / 220561 (1.16%)[ERROR] Get "http://10.10.51.95:12340/rms/10": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/sitemap": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/09": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/04": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/article": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/faq": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/03": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/archive": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/help": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/events": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/cgi-bin": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/img": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/rss": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/home": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/default": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/2005": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/products": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
[ERROR] Get "http://10.10.51.95:12340/rms/register": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/fonts                (Status: 403) [Size: 212]
/swf                  (Status: 403) [Size: 210]
/connection           (Status: 403) [Size: 217]
/stylesheets          (Status: 403) [Size: 218]
/validation           (Status: 403) [Size: 217]
Progress: 220560 / 220561 (100.00%)
===============================================================                                                               
Finished
===============================================================
```