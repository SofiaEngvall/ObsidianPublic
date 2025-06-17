
```sh
┌──(kali㉿proxli)-[~]
└─$ gobuster dir -r -u http://10.10.10.95:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.95:8080
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
http://10.10.10.95:8080/docs                 (Status: 200) [Size: 19677]
http://10.10.10.95:8080/examples             (Status: 200) [Size: 1285]
http://10.10.10.95:8080/manager              (Status: 401) [Size: 2536]
http://10.10.10.95:8080/http%3A%2F%2Fwww     (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fyoutube (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fblogs   (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fblog    (Status: 400) [Size: 0]
http://10.10.10.95:8080/**http%3A%2F%2Fwww   (Status: 400) [Size: 0]
http://10.10.10.95:8080/External%5CX-News    (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fcommunity (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fradar   (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fjeremiahgrossman (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fweblog  (Status: 400) [Size: 0]
http://10.10.10.95:8080/http%3A%2F%2Fswik    (Status: 400) [Size: 0]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================

┌──(kali㉿proxli)-[~]
└─$ gobuster dir -k -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -t 20 -u http://10.10.10.95:8080
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.95:8080
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/con                  (Status: 200) [Size: 0]
/plain]               (Status: 400) [Size: 0]
/[                    (Status: 400) [Size: 0]
/]                    (Status: 400) [Size: 0]
/aux                  (Status: 200) [Size: 0]
/quote]               (Status: 400) [Size: 0]
Progress: 20398 / 26584 (76.73%)[ERROR] parse "http://10.10.10.95:8080/error\x1f_log": net/url: invalid control character in URL
/extension]           (Status: 400) [Size: 0]
/prn                  (Status: 200) [Size: 0]
/[0-9]                (Status: 400) [Size: 0]
Progress: 26583 / 26584 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ gobuster vhost -r -u http://10.10.10.95:8080 --domain jerry.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -t 30
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://10.10.10.95:8080
[+] Method:          GET
[+] Threads:         30
[+] Wordlist:        /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: gc._msdcs.jerry.htb Status: 400 [Size: 0]
Progress: 4989 / 4990 (99.98%)
===============================================================
Finished
===============================================================
```