
Runs commands on local and remote computers.

`Invoke-Command -FilePath c:\scripts\localscript.ps1 -ComputerName remotecomputername`

`Invoke-Command -ComputerName remotecomputername -Credential Domain01\User01 -ScriptBlock { Get-Culture }`
powershell will ask for password and auth method

