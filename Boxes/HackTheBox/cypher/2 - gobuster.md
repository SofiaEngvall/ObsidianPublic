
```sh
┌──(kali㉿kali)-[~/boxes/htb/cypher]
└─$ gobuster dir -r -u http://cypher.htb -w /usr/share/wordlists/seclists/Discovery/Web-Content/quickhits.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cypher.htb
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/quickhits.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://cypher.htb/demo                 (Status: 200) [Size: 3671]
http://cypher.htb/login                (Status: 200) [Size: 3671]
http://cypher.htb/testing              (Status: 200) [Size: 294]
Progress: 2565 / 2566 (99.96%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~/boxes/htb/cypher]
└─$ gobuster dir -r -u http://cypher.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cypher.htb
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
http://cypher.htb/index                (Status: 200) [Size: 4562]
http://cypher.htb/about                (Status: 200) [Size: 4986]
http://cypher.htb/login                (Status: 200) [Size: 3671]
http://cypher.htb/demo                 (Status: 200) [Size: 3671]
http://cypher.htb/testing              (Status: 200) [Size: 294]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~/boxes/htb/cypher]
└─$ gobuster dir -k -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -t 20 -u http://cypher.htb
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cypher.htb
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 3671]
/api                  (Status: 307) [Size: 0] [--> /api/docs]
/about                (Status: 200) [Size: 4986]
/demo                 (Status: 307) [Size: 0] [--> /login]
/index                (Status: 200) [Size: 4562]
/testing              (Status: 301) [Size: 178] [--> http://cypher.htb/testing/]
Progress: 20528 / 26585 (77.22%)[ERROR] parse "http://cypher.htb/error\x1f_log": net/url: invalid control character in URL
Progress: 26584 / 26585 (100.00%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~/boxes/htb/cypher]
└─$ gobuster vhost -r -u http://10.129.231.244 --domain cypher.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -t 30
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://10.129.231.244
[+] Method:          GET
[+] Threads:         30
[+] Wordlist:        /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Progress: 4989 / 4990 (99.98%)
===============================================================
Finished
===============================================================
```