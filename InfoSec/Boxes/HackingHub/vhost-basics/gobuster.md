
Should have used https, not http. That's why it's not redirecting.
```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ gobuster vhost -u http://144.126.192.69/ -w hosts.txt                                                              
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://144.126.192.69/
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        hosts.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: localhost Status: 200 [Size: 67]
Found: zeus.rust.ctfio.com Status: 301 [Size: 178] [--> https://zeus.rust.ctfio.com/]
Found: app-api.rust.ctfio.com Status: 301 [Size: 178] [--> https://app-api.rust.ctfio.com/]
Found: app-admin.rust.ctfio.com Status: 301 [Size: 178] [--> https://app-admin.rust.ctfio.com/]
Found: store.rust.ctfio.com Status: 301 [Size: 178] [--> https://store.rust.ctfio.com/]
Found: stores.rust.ctfio.com Status: 301 [Size: 178] [--> https://stores.rust.ctfio.com/]
Found: admin.rust.ctfio.com Status: 301 [Size: 178] [--> https://admin.rust.ctfio.com/]
Found: app-dev.rust.ctfio.com Status: 301 [Size: 178] [--> https://app-dev.rust.ctfio.com/]
Progress: 8 / 9 (88.89%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ gobuster vhost -u http://144.126.192.69/ -w hosts.txt -r
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://144.126.192.69/
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        hosts.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: localhost Status: 200 [Size: 67]
[ERROR] Get "https://app-api.rust.ctfio.com/": dial tcp: lookup app-api.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://zeus.rust.ctfio.com/": dial tcp: lookup zeus.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://stores.rust.ctfio.com/": dial tcp: lookup stores.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://admin.rust.ctfio.com/": dial tcp: lookup admin.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://app-dev.rust.ctfio.com/": dial tcp: lookup app-dev.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://store.rust.ctfio.com/": dial tcp: lookup store.rust.ctfio.com on 192.168.233.2:53: no such host
[ERROR] Get "https://app-admin.rust.ctfio.com/": dial tcp: lookup app-admin.rust.ctfio.com on 192.168.233.2:53: no such host
Progress: 8 / 9 (88.89%)
===============================================================
Finished
===============================================================
```
