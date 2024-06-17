
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://skynet.thm/45kra24zxs28v3yd/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm/45kra24zxs28v3yd/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://skynet.thm/45kra24zxs28v3yd/.php                 (Status: 403) [Size: 275]
http://skynet.thm/45kra24zxs28v3yd/administrator        (Status: 200) [Size: 4945]
http://skynet.thm/45kra24zxs28v3yd/.php                 (Status: 403) [Size: 275]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================

```
