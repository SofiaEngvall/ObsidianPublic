

```sh
┌──(fixit㉿asusx555b)-[~]
└─$ gobuster dir -r -u http://dev.titanic.htb -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.titanic.htb
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://dev.titanic.htb/administrator        (Status: 200) [Size: 19997]
http://dev.titanic.htb/admin                (Status: 200) [Size: 11306]
http://dev.titanic.htb/a                    (Status: 200) [Size: 19793]
http://dev.titanic.htb/v2                   (Status: 401) [Size: 50]
http://dev.titanic.htb/issues               (Status: 200) [Size: 11307]
http://dev.titanic.htb/developer            (Status: 200) [Size: 25150]
http://dev.titanic.htb/explore              (Status: 200) [Size: 20925]
http://dev.titanic.htb/notifications        (Status: 200) [Size: 11306]
http://dev.titanic.htb/milestones           (Status: 200) [Size: 11306]
Progress: 20502 / 26584 (77.12%)[ERROR] parse "http://dev.titanic.htb/error\x1f_log": net/url: invalid control character in URL
Progress: 26583 / 26584 (100.00%)
===============================================================
Finished
===============================================================

```

http://dev.titanic.htb/administrator        (Status: 200) [Size: 19997] -> user page!! - seems to be a username
http://dev.titanic.htb/admin                (Status: 200) [Size: 11306] ->user login
http://dev.titanic.htb/a                    (Status: 200) [Size: 19793] -> 404
http://dev.titanic.htb/v2                   (Status: 401) [Size: 50] -> unauth
http://dev.titanic.htb/issues               (Status: 200) [Size: 11307] -> login
http://dev.titanic.htb/developer            (Status: 200) [Size: 25150] -> user page!! - seems to be a username
http://dev.titanic.htb/explore              (Status: 200) [Size: 20925] -> http://dev.titanic.htb/explore/repos repo list
http://dev.titanic.htb/notifications        (Status: 200) [Size: 11306]
http://dev.titanic.htb/milestones           (Status: 200) [Size: 11306]

