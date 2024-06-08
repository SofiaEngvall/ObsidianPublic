WMI command line utility

OS Arch
	`vmic OS get OSArchitecture`

Get user account SIDs
	`wmic useraccount get name,sid`

Installed/unpatched software
	`wmic product get name,version,vendor` enum programs - also check desktop shortcuts, start menu, available services...

HotFixes
	`wmic qfe get Caption,Description,HotFixID,InstalledOn`

List drive letters
	`(wmic logicaldisk get caption 2>nul | more) || (fsutil fsinfo drives 2>nul)`


