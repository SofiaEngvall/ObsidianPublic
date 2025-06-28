
### wevtutil.exe (Windows Events Commandline Utility)
`wevtutil.exe /?`
`wevtutil COMMAND /?`
`wevtutil enum-log`  list logs

### Get-WinEvent
`Get-WinEvent -ListLog *`
`Get-WinEvent -ListProvider *`
`Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' }`


### XPath Queries (XPath = XML Path)
Just the filtering with xml in event viewer but in ps/cmd
PS: `Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=100'`
cmd: `wevtutil.exe qe Application /q:*/System[EventID=100] /f:text /c:1`








