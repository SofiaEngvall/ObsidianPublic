
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://skynet.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm/
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
http://skynet.thm/admin                (Status: 403) [Size: 275]
http://skynet.thm/css                  (Status: 403) [Size: 275]
http://skynet.thm/js                   (Status: 403) [Size: 275]
http://skynet.thm/config               (Status: 403) [Size: 275]
http://skynet.thm/ai                   (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail         (Status: 200) [Size: 2912]
http://skynet.thm/server-status        (Status: 403) [Size: 275]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://skynet.thm/squirrelmail/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm/squirrelmail/
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
http://skynet.thm/squirrelmail/images               (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/themes               (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/plugins              (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/src                  (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/include              (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/config               (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/help                 (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/class                (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/functions            (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/po                   (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/locale               (Status: 403) [Size: 275]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://skynet.thm/squirrelmail/src/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm/squirrelmail/src/
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
http://skynet.thm/squirrelmail/src/login.php            (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/src/help.php             (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/image.php            (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/redirect.php         (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/download.php         (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/.php                 (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/src/index.php            (Status: 200) [Size: 2912]
http://skynet.thm/squirrelmail/src/search.php           (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/options.php          (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/webmail.php          (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/mailto.php           (Status: 200) [Size: 2969]
http://skynet.thm/squirrelmail/src/folders.php          (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/compose.php          (Status: 200) [Size: 1857]
http://skynet.thm/squirrelmail/src/addressbook.php      (Status: 200) [Size: 1803]
http://skynet.thm/squirrelmail/src/.php                 (Status: 403) [Size: 275]
http://skynet.thm/squirrelmail/src/vcard.php            (Status: 200) [Size: 1803]
Progress: 441120 / 441122 (100.00%)
===============================================================
Finished
===============================================================
    
```