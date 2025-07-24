
create share for upload to our machine
`sudo impacket-smbserver -smb2support -username <user> -password <password> myshare <../dirname>`

`sudo impacket-smbserver -smb2support -username user -password password share share`
where the subdirectory `share` is shared under the share name `share`


Can easily be user to access files from both Windows and Linux:

#### Linux
[[smbclient]]
`smbclient //10.10.10.10/share -U user`

#### Windows
[[net use - connect from windows]]
`net use v: \\192.168.220.129\share /USER:user password`
or `net use \\10.10.10.10\share /USER:user password` and connect in gui

`dir` to list files
`get <filename>` to get a file
