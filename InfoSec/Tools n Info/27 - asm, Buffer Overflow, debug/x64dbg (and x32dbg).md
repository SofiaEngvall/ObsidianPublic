
 [x64dbg](https://github.com/x64dbg/x64dbg) with the plugin [ERC.Xdbg](https://github.com/Andy53/ERC.Xdbg)

Install the latest release of x64dbg.
Get the ERC 32-bit and put it in `x64dbg\x32\plugins`. (& the same for 64-bit)

Set the working dir..
```sh
ERC --config SetWorkingDirectory C:\Users\htb-student\Desktop\
```

x64dbg docs: https://help.x64dbg.com/en/latest/
ERC docs: https://evilrobots.club/ERC.net/api/index.html


F3  Open file
Alt+A  Attach to running process (opens dialog - if you can't see the process, run x64dbg as admin)


We can use ERC to create non-repetitive patterns in x64dbg
Pattern create: `ERC --pattern <create | c> <length>`
Pattern offset: `ERC --pattern <offset | o> <search string>`

Run ERC on the Log tab at the Command: line.
`erc`

