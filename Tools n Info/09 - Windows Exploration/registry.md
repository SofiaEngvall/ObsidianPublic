
`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\userinit`
Names of executable files (no extension req)
Specifies the programs that Winlogon runs when a user logs on
"By default, Winlogon runs Userinit.exe, which runs logon scripts, reestablishes network connections, and then starts Explorer.exe, the Windows user interface.
You can change the value of this entry to add or remove programs. For example, to have a program run before the Windows Explorer user interface starts, substitute the name of that program for Userinit.exe in the value of this entry, then include instructions in that program to start Userinit.exe. You might also want to substitute Explorer.exe for Userinit.exe if you are working offline and are not using logon scripts."





