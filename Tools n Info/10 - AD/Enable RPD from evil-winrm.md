
Requirements:
- RDP needs to be 
- User neemds to ba a member of the group Remote Desktop Users (or of a group that's a member)
- On domain controllers only - Explicit SeRemoteInteractiveLogonRight

### Enable RDP

Set:
`Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0`

Check with:
`Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections"`

Make sure it doesn't get stuck in the firewall
`Enable-NetFirewallRule -DisplayGroup "Remote Desktop"`

No restart required!


Test using nmap:
`nmap -p 3389 -sC -sV -Pn 10.10.10.10`

### NLA - Network Level Authentication

Might need changing - TODO! add more info

`Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "UserAuthentication" -Value 0`

`Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "UserAuthentication"`


### Hash to password

in evil-winrm:
`Set-ADAccountPassword -Identity "Administrator" -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Reset`

### Become a member of Remote Desktop users

First check if any groups are members - If so, add yourself there

`Add-ADGroupMember -Identity "Remote Desktop Users" -Members "Administrator"`
or
`net group "Remote Desktop Users" Administrator /add /domain`


### Check the Group Policy

find your users sid:
`whoami /user`

`secedit /configure /db secedit.sdb /cfg C:\rdp_policy.inf /overwrite /quiet`
(-quiet makes it not ask for confirmation - great for non interactive shells)


Look for the line starting with:
`SeRemoteInteractiveLogonRight =`

Replace the whole line with:
`SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-21-917908876-1423158569-3159038727-500`

If a group is listed, just join the group
`net group "my rdp groupDev Support" myuser /add /domain`

saving it back to the dc
```
secedit /configure /db C:\secedit.sdb /cfg C:\rdp.inf /overwrite /quiet

gpupdate /force
```


### Domain controllers vs "normal" computers

Normal servers/workstations:
Adding a user to the "Remote Desktop Users" group usually grants this logon right automatically.

Domain Controllers:
Local groups don't function normally. So even if a user is in "Remote Desktop Users", they won’t get RDP access unless explicitly granted the SeRemoteInteractiveLogonRight via Group Policy or secedit.

