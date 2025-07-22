
### wevtutil.exe (Windows Events Commandline Utility)
`wevtutil.exe /?`
`wevtutil COMMAND /?`
`wevtutil enum-log`  list logs

### Get-WinEvent
`Get-WinEvent -ListLog *`
`Get-WinEvent -ListProvider *`
`Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' }`

##### XPath Queries (XPath = XML Path)
Just the filtering with xml in event viewer but in ps/cmd
PS: `Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=100'`
cmd: `wevtutil.exe qe Application /q:*/System[EventID=100] /f:text /c:1`

#### Examples

`Get-WinEvent -Path <Path to Log> -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=4444'`

`Get-WinEvent -Path <Path to Log> -FilterXPath '*/System/EventID=10 and */EventData/Data[@Name="TargetImage"] and */EventData/Data="C:\Windows\system32\lsass.exe"'`

More: https://medium.com/@jcm3/sysmon-tryhackme-walkthrough-7ef41688827f








