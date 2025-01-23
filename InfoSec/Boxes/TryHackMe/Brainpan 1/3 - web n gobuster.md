
Web page:
```sh
<html>
<body bgcolor="ffffff">
<center>
<!-- infographic from http://www.veracode.com/blog/2012/03/safe-coding-and-software-security-infographic/ -->
<img src="soss-infographic-final.png">
</center>
</body>
</html>
```
Not much more, tried some ../../ and googled but mostly found later than 2013 stuff

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://10.10.157.116:10000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -e
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.157.116:10000
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
http://10.10.157.116:10000/bin                  (Status: 200) [Size: 230]
...
```

![[Images/Pasted image 20250122102116.png]]

Downloading brainpan.exe

