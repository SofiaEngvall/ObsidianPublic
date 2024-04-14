
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.11.251 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.251
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 147] [--> http://10.10.11.251/img/]
/css                  (Status: 301) [Size: 147] [--> http://10.10.11.251/css/]
/js                   (Status: 301) [Size: 146] [--> http://10.10.11.251/js/]
/IMG                  (Status: 301) [Size: 147] [--> http://10.10.11.251/IMG/]
/*checkout*           (Status: 400) [Size: 3420]
/CSS                  (Status: 301) [Size: 147] [--> http://10.10.11.251/CSS/]
/Img                  (Status: 301) [Size: 147] [--> http://10.10.11.251/Img/]
/JS                   (Status: 301) [Size: 146] [--> http://10.10.11.251/JS/]
/*docroot*            (Status: 400) [Size: 3420]
/*                    (Status: 400) [Size: 3420]
/http%3A%2F%2Fwww     (Status: 400) [Size: 3420]
/http%3A              (Status: 400) [Size: 3420]
/q%26a                (Status: 400) [Size: 3420]
/**http%3a            (Status: 400) [Size: 3420]
/*http%3A             (Status: 400) [Size: 3420]
/**http%3A            (Status: 400) [Size: 3420]
/http%3A%2F%2Fyoutube (Status: 400) [Size: 3420]
/http%3A%2F%2Fblogs   (Status: 400) [Size: 3420]
/http%3A%2F%2Fblog    (Status: 400) [Size: 3420]
/**http%3A%2F%2Fwww   (Status: 400) [Size: 3420]
/s%26p                (Status: 400) [Size: 3420]
/%3FRID%3D2671        (Status: 400) [Size: 3420]
/devinmoore*          (Status: 400) [Size: 3420]
/200109*              (Status: 400) [Size: 3420]
/*sa_                 (Status: 400) [Size: 3420]
/*dc_                 (Status: 400) [Size: 3420]
/http%3A%2F%2Fcommunity (Status: 400) [Size: 3420]
/Clinton%20Sparks%20%26%20Diddy%20-%20Dont%20Call%20It%20A%20Comeback%28RuZtY%29 (Status: 400) [Size: 3420]
/Chamillionaire%20%26%20Paul%20Wall-%20Get%20Ya%20Mind%20Correct (Status: 400) [Size: 3420]
/DJ%20Haze%20%26%20The%20Game%20-%20New%20Blood%20Series%20Pt (Status: 400) [Size: 3420]
/http%3A%2F%2Fradar   (Status: 400) [Size: 3420]
/q%26a2               (Status: 400) [Size: 3420]
/login%3f             (Status: 400) [Size: 3420]
/Shakira%20Oral%20Fixation%201%20%26%202 (Status: 400) [Size: 3420]
/http%3A%2F%2Fjeremiahgrossman (Status: 400) [Size: 3420]
/http%3A%2F%2Fweblog  (Status: 400) [Size: 3420]
/http%3A%2F%2Fswik    (Status: 400) [Size: 3420]
Progress: 661680 / 661683 (100.00%)
===============================================================
Finished
===============================================================
```