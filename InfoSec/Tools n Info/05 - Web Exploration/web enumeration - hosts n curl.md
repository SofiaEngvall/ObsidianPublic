
don't miss virtual hosts
![[../../TO SORT/Pasted image 20240226193023.png]]
try `-H 'Host: localhost'`
try invalid host `skräp.thedomain.com`
try just `thedomain.com`

virtual hosts can be found listed in certificates!

```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ host rust.ctfio.com                                                                                                                 
rust.ctfio.com has address 144.126.192.69

┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ host www.rust.ctfio.com
www.rust.ctfio.com has address 144.126.192.69

┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ curl 144.126.192.69 -H "Host: rust.ctfio.com"
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>

┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ curl 144.126.192.69 -H "Host: localhost"         
{"status":"OK","flag":"FLAG_ONE{95fe9f9e8bf849aec6a8de02fee14d57}"} 

┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ ffuf -H 'Host: FUZZ.rust.ctfio.com' -w ../wordlists/subdomains.txt -u http://144.126.192.69

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://144.126.192.69
 :: Wordlist         : FUZZ: /home/kali/hh/wordlists/subdomains.txt
 :: Header           : Host: FUZZ.rust.ctfio.com
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

10                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 30ms]
...
a.auth-ns               [Status: 200, Size: 670, Words: 111, Lines: 23, Duration: 34ms]
b.auth-ns               [Status: 200, Size: 670, Words: 111, Lines: 23, Duration: 31ms]
c.auth-ns               [Status: 200, Size: 670, Words: 111, Lines: 23, Duration: 32ms]
ipv6.teredo             [Status: 200, Size: 670, Words: 111, Lines: 23, Duration: 32ms]
```
