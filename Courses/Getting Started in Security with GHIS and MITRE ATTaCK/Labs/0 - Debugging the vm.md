
https://github.com/krooth/Antisyphon_lab_scripts/tree/main/WinADHD









---

PROBLEM: 
VM works but Unbuntu shell fails (error message regarding needing Virtualization enabled, etc)

SOLUTION (for me - YMMV):
Turning ON "Virtualize Intel VT-X..." in the VM processor settings.



Just as an FYI - this is the my current state:

HOST BIOS
Virtualisation in BIOS: Enabled
(of course)

HOST Windows settings:
Settings:
Update & Security
Windows Security-Device Security-Core isolation
Memory integrity: off
(Already had this)

HOST Optional features
Windows Subsystem for Linux: Unchecked
Windows Machine Platform: Unchecked
Windows Sandbox: Unchecked
Windows Hypervisor Platform: Unchecked
Hyper-V: Unchecked
(Turned windows subsystem and hyper-v off)

HOST VMWare Workstation 17 PRO VM Settings:

Hardware tab:
Processors
Virtualization engine:
Virtualize Intel VT-x/EPT or AMD-V/RVI: checked
NOTE THIS is opposite to what most people need, but this was what fixed it for me.
(When I check it it failed, but not doing the above too)
(Now turned it off again to test as it won't start)

Options tab:
Advanced
Settings:
Enable VBS (Virtualized Based Security) support: unchecked
(already off)

HOST command prompt:
bcdedit /set hypervisorlaunchtype off
(ran this
```sh
C:\WINDOWS\system32>bcdedit /get hypervisorlaunchtype
An unknown command was specified.
Run "bcdedit /?" for command line assistance.

C:\WINDOWS\system32>bcdedit /set hypervisorlaunchtype off
The operation completed successfully.

C:\WINDOWS\system32>
```
)

HOST powershell prompt:
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
bcdedit /set hypervisorlaunchtype off
bcdedit /set vsmlaunchtype off
(Ran this:
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
                                                                                                               Try the new cross-platform PowerShell https://aka.ms/pscore6                                                                                                                                                                  PS C:\WINDOWS\system32> Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All              

Path          :
Online        : True
RestartNeeded : False



PS C:\WINDOWS\system32> bcdedit /set hypervisorlaunchtype off
The operation completed successfully.
PS C:\WINDOWS\system32> bcdedit /set vsmlaunchtype off
The operation completed successfully.
PS C:\WINDOWS\system32>
```
)
