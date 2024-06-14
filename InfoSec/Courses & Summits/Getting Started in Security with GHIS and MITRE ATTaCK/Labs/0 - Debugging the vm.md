
https://github.com/krooth/Antisyphon_lab_scripts/tree/main/WinADHD

PROBLEM: 
VM works but Unbuntu shell fails (error message regarding needing Virtualization enabled, etc)

SOLUTION (for me - YMMV):
Turning ON "Virtualize Intel VT-X..." in the VM processor settings.



Just as an FYI - this is the my current state:

HOST BIOS
Virtualisation in BIOS: Enabled


HOST Windows settings:
Settings:
Update & Security
Windows Security-Device Security-Core isolation
Memory integrity: off


HOST Optional features
Windows Subsystem for Linux: Unchecked
Windows Machine Platform: Unchecked
Windows Sandbox: Unchecked
Windows Hypervisor Platform: Unchecked
Hyper-V: Unchecked


HOST VMWare Workstation 17 PRO VM Settings:

Hardware tab:
Processors
Virtualization engine:
Virtualize Intel VT-x/EPT or AMD-V/RVI: checked
NOTE THIS is opposite to what most people need, but this was what fixed it for me.


Options tab:
Advanced
Settings:
Enable VBS (Virtualized Based Security) support: unchecked


HOST command prompt:
bcdedit /set hypervisorlaunchtype off


HOST powershell prompt:
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
bcdedit /set hypervisorlaunchtype off
bcdedit /set vsmlaunchtype off
