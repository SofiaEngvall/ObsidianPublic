
if smb v1 - try eternal blue

nmap smb scripts:
`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.10.10`
`nmap -p 445 --script=smb* 10.10.10.10`

[[../9.5 - netexec -/nxc smb|nxc smb]] checks



