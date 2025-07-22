
### Taskmanager

In details tab, add columns `Image path name` and `Command line`

### tasklist
(also remote)

tasklist /?
tasklist /svc

### Get-Process

alias ps

### Process hacker

![[Images/Pasted image 20250411220443.png]]

### Process explorer
https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer

![[Images/Pasted image 20250411220552.png]]


The System process always has the ID 4
Runs in kernel mode

In windows, the processor has two modes, kernel mode for the system/core OS components and user mode for the apps. This affects which address space is uses. A user mode process can't access virtual addresses reserved for the OS.

All code running in kernel mode shares a single virtual address space.


#### smss.exe - Session Manager Subsystem/Windows Session Manager
*parent: System (4)*

first user-mode process started by the kernel
starts the kernel and user modes, includes:
- win32k.sys (kernel mode)
- winsrv.dll (user mode)
- csrss.exe (user mode)

###### Sessions (User mode?)

Session 0
- an isolated Windows session for the operating system
- csrss.exe (Client Server Runtime Process - Windows subsystem) and wininit.exe (Windows Start-Up Application)

Session 1
- the user session
- csrss.exe (as above) and winlogon.exe (Windows Logon Process)

Also starts subsystems in `HKLM\System\CurrentControlSet\Control\Session Manager\Subsystems` set as `Required`.

Normal smss.exe:
![[Images/smss.png|1000]]
#### csrss.exe (Client Server Runtime Process/Subsystem)
*parent: smss.exe (auto-terminates so Non-existent later)*
	started twice, once for session 0 and once for session 1§

the user-mode side of windows

responsible for:
- Win32 console window
- process thread creation and deletion
- making the Windows API available to other processes
- mapping drive letters
- handling the Windows shutdown process

each instance loads:
- csrsrv.dll
- basesrv.dll
- winsrv.dll
- ...

Normal csrss.exe, Session 0 & Session 1 (random pids):
![[Images/csrss-session0.png|1000]]

additional instances for new sessions

#### wininit.exe (Windows Initialization Process)
*parent: smss.exe (auto-terminates so Non-existent later)*

loads:
- services.exe (Service Control Manager)
- lsass.exe (Local Security Authority Subsystem)
- lsaiso.exe (associated with Credential Guard and KeyGuard)

Normal wininit.exe:
![[Images/wininit.png|1000]]

#### services.exe (Service Control Manager)
*parent: wininit.exe*

- manages services
	- service info at `HKLM\System\CurrentControlSet\Services`
- also loads device drivers marked as auto-start into memory
- sets `HKLM\System\Select\LastKnownGood` to the CurrentControlSet at successful user logon

loads:
- svchost.exe
- spoolsv.exe
- msmpeng.exe
- dllhost.exe
- ...

Normal services.exe:
![[Images/services.png|1000]]

#### svchost.exe (Host Process for Windows Services)
`parent: services.exe`

- hosting and managing Windows services in DLL format
	- `ServiceDLL` found in `HKLM\SYSTEM\CurrentControlSet\Services\SERVICE NAME\Parameters`

Normal svchost.exe
![[Images/svchost.png|1000]]

Run with varying accounts; SYSTEM, Network Service, Local Service, logged-in user

#### lsass.exe (Local Security Authority Subsystem Service)
*parent: wininit.exe*

responsible for:
- enforcing the security policy on the system
- verifies users logging in
- password changes
- creating access tokens
- writing to the Windows Security Log
- creates security tokens for SAM (Security Account Manager), AD (Active Directory), and NETLOGON
	-  uses authentication packages specified in `HKLM\System\CurrentControlSet\Control\Lsa`

Normal lsass.exe:
![[Images/lsass.png|1000]]

#### winlogon.exe (Windows Logon)
*parent: smss.exe (auto-terminates so Non-existent later)*

responsible for:
- handling the Secure Attention Sequence (SAS), ALT+CTRL+DELETE
- loading the user profile
	- loads the user's NTUSER.DAT into HKCU
	- userinit.exe loads the user's shell
- locking the screen and running the user's screensaver
- ...

Normal winlogon.exe:
![[Images/winlogon1.png|1000]]
![[Images/winlogon2.png|700]]

#### explorer.exe (Windows Explorer)
`parent: userinit.exe (terminates after loading explorer so Non-existent later)`
<font size=3>Winlogon runs userinit.exe, which launches "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell"</font>

![[Images/explorer.png|1000]]






