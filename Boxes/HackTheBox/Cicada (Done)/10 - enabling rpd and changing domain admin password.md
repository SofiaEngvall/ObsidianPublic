

Enable RDP:
`Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0`

Check:
```sh
*Evil-WinRM* PS C:\Users\Administrator\Documents> Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections"


fDenyTSConnections : 0
PSPath             : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server
PSParentPath       : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control
PSChildName        : Terminal Server
PSDrive            : HKLM
PSProvider         : Microsoft.PowerShell.Core\Registry
```

Let rdp through firewall:
`Enable-NetFirewallRule -DisplayGroup "Remote Desktop"`

test with nmap
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nmap -p 3389 -sC -sV -Pn 10.129.169.79                                                                            
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-01 01:10 CEST
Nmap scan report for CICADA-DC.cicada.htb (10.129.169.79)
Host is up (0.025s latency).

PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=CICADA-DC.cicada.htb
| Not valid before: 2025-07-31T06:07:48
|_Not valid after:  2026-01-30T06:07:48
| rdp-ntlm-info: 
|   Target_Name: CICADA
|   NetBIOS_Domain_Name: CICADA
|   NetBIOS_Computer_Name: CICADA-DC
|   DNS_Domain_Name: cicada.htb
|   DNS_Computer_Name: CICADA-DC.cicada.htb
|   DNS_Tree_Name: cicada.htb
|   Product_Version: 10.0.20348
|_  System_Time: 2025-08-01T06:10:55+00:00
|_ssl-date: 2025-08-01T06:11:01+00:00; +7h00m00s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 7h00m00s, deviation: 0s, median: 6h59m59s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.01 seconds
```

try to connect
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ xfreerdp3 /dynamic-resolution /scale-desktop:150 /scale:100 +clipboard /v:10.129.169.79 /u:'cicada\Administrator'      
[01:11:39:793] [1501144:0016e80c] [WARN][com.freerdp.client.x11] - [load_map_from_xkbfile]:     : keycode: 0x08 -> no RDP scancode found
[01:11:39:793] [1501144:0016e80c] [WARN][com.freerdp.client.x11] - [load_map_from_xkbfile]:     : keycode: 0x5D -> no RDP scancode found
[01:11:39:947] [1501144:0016e80c] [WARN][com.freerdp.crypto] - [verify_cb]: Certificate verification failure 'self-signed certificate (18)' at stack position 0
[01:11:39:947] [1501144:0016e80c] [WARN][com.freerdp.crypto] - [verify_cb]: CN = CICADA-DC.cicada.htb
Password:        
[01:11:51:598] [1501144:0016e80c] [ERROR][com.winpr.sspi.Kerberos] - [kerberos_AcquireCredentialsHandleA]: krb5glue_get_init_creds (Cannot find KDC for realm "CICADA" [-1765328230])
[01:11:51:622] [1501144:0016e80c] [ERROR][com.winpr.sspi.Kerberos] - [kerberos_AcquireCredentialsHandleA]: krb5glue_get_init_creds (Cannot find KDC for realm "CICADA" [-1765328230])
[01:11:51:676] [1501144:0016e80c] [ERROR][com.freerdp.core] - [nla_recv_pdu]: ERRCONNECT_LOGON_FAILURE [0x00020014]
[01:11:51:676] [1501144:0016e80c] [ERROR][com.freerdp.core.rdp] - [rdp_recv_callback_int][0x55f90fbc0b70]: CONNECTION_STATE_NLA - nla_recv_pdu() fail
[01:11:51:676] [1501144:0016e80c] [ERROR][com.freerdp.core.rdp] - [rdp_recv_callback_int][0x55f90fbc0b70]: CONNECTION_STATE_NLA status STATE_RUN_FAILED [-1]
[01:11:51:676] [1501144:0016e80c] [ERROR][com.freerdp.core.transport] - [transport_check_fds]: transport_check_fds: transport->ReceiveCallback() - STATE_RUN_FAILED [-1]
```
we need the password


`Set-ADAccountPassword -Identity "Administrator" -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Reset`

`Add-ADGroupMember -Identity "Remote Desktop Users" -Members "Administrator"`
or
`net group "Remote Desktop Users" Administrator /add /domain`

---

```sh
*Evil-WinRM* PS C:\Users\Administrator\Documents> secedit /configure /db secedit.sdb /cfg C:\rdp_policy.inf /overwrite /quiet
```


```sh
*Evil-WinRM* PS C:\Users\Administrator\Documents> secedit /export /cfg C:\rdp.inf

The task has completed successfully.
See log %windir%\security\logs\scesrv.log for detail info.
```



```sh
secedit /export /cfg C:\rdp.inf
```

```sh
whoami /user
```


Look for the line starting with:
`SeRemoteInteractiveLogonRight =`

Replace the whole line with:
`SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-21-917908876-1423158569-3159038727-500`


Dev support already has the permissions - so let's add ourselves - We don't have to do the line replace and 


```
secedit /configure /db C:\secedit.sdb /cfg C:\rdp.inf /overwrite /quiet

gpupdate /force
```


`net group "Dev Support" Administrator /add /domain`


