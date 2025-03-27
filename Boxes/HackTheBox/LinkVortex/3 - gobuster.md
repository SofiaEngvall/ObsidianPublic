
```sh
┌──(kali㉿kali)-[~/exploits]
└─$ gobuster vhost -r -u http://10.10.11.47 --domain linkvortex.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -t 30   
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://10.10.11.47
[+] Method:          GET
[+] Threads:         30
[+] Wordlist:        /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: dev.linkvortex.htb Status: 200 [Size: 2538]
Progress: 4989 / 4990 (99.98%)
===============================================================
Finished
===============================================================
```

```sh
┌──(kali㉿kali)-[~/exploits]
└─$ gobuster dir -r -u http://dev.linkvortex.htb -w /usr/share/wordlists/seclists/Discovery/Web-Content/quickhits.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.linkvortex.htb
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
http://dev.linkvortex.htb/.git/config          (Status: 200) [Size: 201]
http://dev.linkvortex.htb/.git/HEAD            (Status: 200) [Size: 41]
http://dev.linkvortex.htb/.git/logs/HEAD       (Status: 200) [Size: 175]
http://dev.linkvortex.htb/.git/                (Status: 200) [Size: 2796]
http://dev.linkvortex.htb/.git/logs/           (Status: 200) [Size: 868]
http://dev.linkvortex.htb/.git                 (Status: 200) [Size: 2796]
http://dev.linkvortex.htb/.htaccess-dev        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess            (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.ht_wsr.txt          (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.hta                 (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess-marco      (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.txt        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.orig       (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.save       (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.old        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.bak1       (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.bak        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.sample     (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess.BAK        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess-local      (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccessBAK         (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccessOLD         (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htgroup             (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccessOLD2        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess_extra      (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess_sc         (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htpasswd            (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htpasswd-old        (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess~           (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htpasswds           (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htpasswd_test       (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htusers             (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.htaccess_orig       (Status: 403) [Size: 199]
http://dev.linkvortex.htb/.git/index           (Status: 200) [Size: 707577]
http://dev.linkvortex.htb/server-status/       (Status: 403) [Size: 199]
Progress: 2565 / 2566 (99.96%)
===============================================================
Finished
===============================================================
```

We found a dev. and a .git!

