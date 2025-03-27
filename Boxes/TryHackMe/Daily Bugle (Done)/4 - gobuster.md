
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.11.102 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.102
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
http://10.10.11.102/templates            (Status: 200) [Size: 31]
http://10.10.11.102/media                (Status: 200) [Size: 31]
http://10.10.11.102/modules              (Status: 200) [Size: 31]
http://10.10.11.102/bin                  (Status: 200) [Size: 31]
http://10.10.11.102/plugins              (Status: 200) [Size: 31]
http://10.10.11.102/includes             (Status: 200) [Size: 31]
http://10.10.11.102/language             (Status: 200) [Size: 31]
http://10.10.11.102/components           (Status: 200) [Size: 31]
http://10.10.11.102/cache                (Status: 200) [Size: 31]
http://10.10.11.102/libraries            (Status: 200) [Size: 31]
http://10.10.11.102/images               (Status: 200) [Size: 31]
http://10.10.11.102/tmp                  (Status: 200) [Size: 31]
http://10.10.11.102/layouts              (Status: 200) [Size: 31]
http://10.10.11.102/administrator        (Status: 200) [Size: 4843]
http://10.10.11.102/cli                  (Status: 200) [Size: 31]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================

```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://dailybugle.thm/administrator -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dailybugle.thm/administrator
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
http://dailybugle.thm/administrator/templates            (Status: 200) [Size: 1351]
http://dailybugle.thm/administrator/modules              (Status: 200) [Size: 3944]
http://dailybugle.thm/administrator/includes             (Status: 200) [Size: 1785]
http://dailybugle.thm/administrator/language             (Status: 200) [Size: 1143]
http://dailybugle.thm/administrator/components           (Status: 200) [Size: 7186]
http://dailybugle.thm/administrator/cache                (Status: 200) [Size: 31]
http://dailybugle.thm/administrator/logs                 (Status: 200) [Size: 31]
http://dailybugle.thm/administrator/help                 (Status: 200) [Size: 1136]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```