
2011
aka Lockheed Martin Cyber Kill Chain

attack phases
- Reconnaissance
- Weaponization
- Delivery
- Exploitation
- Installation
- Command & Control
- Actions on Objectives


### Reconnaissance

osint
phishing
social media

https://github.com/laramies/theHarvester
https://hunter.io/
https://osintframework.com/


 ### Weaponization
 
 generate payload using common tools
 buy malware
 create custom malware

examples:
office doc with macro
payload/worm on usb
c2 techniques
backdoor implants

### Delivery

phishing email
infected usb
watering hole attack - replace common website


### Exploitation

examples:
- The victim triggers the exploit by opening the email attachment or clicking on a malicious link
- Using a zero-day exploit
- Exploit software, hardware, or even human vulnerabilities
- An attacker triggers the exploit for server-based vulnerabilities

### Installation

getting persistance

examples:
web shell
backdoor on victim machine
new/modified windows service
add an autostart app through registry or startup folder (or scheduled task)


### Command & Control - C2

beaconing - the infected host will communicate with a C2 server consistently

the attacker can send commands back

historically IRC was used for the communication but now http/s and dns is most common


### Actions on Objectives - Exfiltration

For example:
- Collect the credentials from users.
- Perform privilege escalation (gaining elevated access like domain administrator access from a workstation by exploiting the misconfiguration).
- Internal reconnaissance (for example, an attacker gets to interact with internal software to find its vulnerabilities).
- Lateral movement through the company's environment.
- Collect and exfiltrate sensitive data.
- Deleting the backups and shadow copies. Shadow Copy is a Microsoft technology that can create backup copies, snapshots of computer files, or volumes. 
- Overwrite or corrupt data.

