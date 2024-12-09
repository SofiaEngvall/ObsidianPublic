

Check out
https://www.auditscripts.com/subscriptions/audit-toolkit/compliance-audit-tools/
audit tools
take frameworks and optimize - based on actual attacks and things that matter
cross referencing
help develop policies and document.. how implement... review & audit

MITRE ATT&CK
butter knife, not screwdriver
index of common attack

### Application allow listing (white listing)

instead of deny listing - obvious reasons
also allowed traffic
![[Images/Pasted image 20240612003651.png|400]]

example of bypass of deny listing:
![[Images/Pasted image 20240612003823.png|600]]
start with msfvenom exe
make asm
![[Images/Pasted image 20240612004412.png|800]]

![[Images/Pasted image 20240612004543.png]]
![[Images/Pasted image 20240612004627.png]]
make changes to asm
![[Images/Pasted image 20240612004719.png]]

other example, lolbins living of the land

virustotal for testing file against avrs - will probably ruin the usability of that exploit

Unicorn.py - python tool to obfuscate payloads?

How do allowlisting
1. Set directories, only program files
2. hashes of executables to make sure it's really the one
3. digital certs..
4. applocker? built into windows - watch: https://www.youtube.com/watch?v=9qsP5h033Qk
	1.  local securite policy / group policy
	![[Images/Pasted image 20240612095832.png]]
	![[Images/Pasted image 20240612095853.png]]
	![[Images/Pasted image 20240612100854.png]]
Lab: [[Labs/1 - AppLocker|1 - AppLocker]]

### Passwords

we need good passwords
password spraying
2fa might make businesses lacy and only use 8-10 char passwords
use mfa everywhere - what systems can't use it?
use long passphrases - easy to remember

2fa - something you know and something you have - token/sms/apps

attack 2fa - clone sim, ask the user
##### Service accounts
often forgotten
highly prived, maybe domain admins
no lockout, never exp passwd

rubeus, kerbo roasting
responder.py - pretending to be a server, windows will auth
kredking for passwd spraying
evilginx - evil proxy, intercept mfa and hijack ...
##### Password managers
You can use long passwds
What's best
provide solution for end users

PIM Privileged Identity Management
auto rotate service accounts
checking out short lived creds

Lab: [[Labs/2 - Password Cracking|2 - Password Cracking]]



