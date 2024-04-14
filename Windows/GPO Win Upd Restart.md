
Run `gpedit.msc` to edit your Local Group Policy
Go to `Computer Configuration\Administrative Templates\Windows Components\Windows Update\`
Change `No auto-restart with logged in users for scheduled automatic updates installations` to Enabled!

![[Pasted image 20231115083931.png]]

`Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU`
`DWORD` `NoAutoRebootWithLoggedOnUsers` = 1
should have been set

Also `Task Scheduler\Task Scheduler Library\Microsoft\Windows\UpdateOrchestrator`
Reboot_AC should have been disabled. (Here you can see the last time it was run.)

![[Pasted image 20231115090523.png]]
