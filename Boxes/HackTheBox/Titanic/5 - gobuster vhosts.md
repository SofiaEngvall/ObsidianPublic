
```sh
┌──(fixit㉿asusx555b)-[~/Downloads]
└─$ gobuster vhost -r -u http://10.10.11.55 --domain titanic.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -t 30
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://10.10.11.55
[+] Method:          GET
[+] Threads:         30
[+] Wordlist:        /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: dev.titanic.htb Status: 200 [Size: 13982]
Progress: 4989 / 4990 (99.98%)
===============================================================
Finished
===============================================================
```
