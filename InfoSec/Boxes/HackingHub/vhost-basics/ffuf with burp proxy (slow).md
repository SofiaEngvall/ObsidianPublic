
```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ ffuf -H 'Host: FUZZ' -w hosts.txt -u https://143.110.162.23 -x http://127.0.0.1:8080

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://143.110.162.23
 :: Wordlist         : FUZZ: /home/kali/hh/vhost-basics/hosts.txt
 :: Header           : Host: FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Proxy            : http://127.0.0.1:8080
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

app-api.earth.ctfio.com [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 189ms]
localhost               [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 291ms]
stores.earth.ctfio.com  [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 325ms]
admin.earth.ctfio.com   [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 385ms]
store.earth.ctfio.com   [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 421ms]
app-dev.earth.ctfio.com [Status: 200, Size: 705, Words: 98, Lines: 25, Duration: 484ms]
zeus.earth.ctfio.com    [Status: 200, Size: 69, Words: 7, Lines: 2, Duration: 556ms]
app-admin.earth.ctfio.com [Status: 200, Size: 2273, Words: 521, Lines: 55, Duration: 621ms]
:: Progress: [8/8] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::

```