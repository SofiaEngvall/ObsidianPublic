
Goal - Identify vulnerabilities/anticipate attacks and mitigate before they can be exploited

https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
Details: https://owasp.org/www-community/Threat_Modeling_Process
History + more: https://en.wikipedia.org/wiki/Threat_model
company page, but lots of info: https://threat-modeling.com/

Draw up your IT environment, an application or whatever you are protecting/attacking

For example using:
- OWASP Threat Dragon (saves in json) https://github.com/OWASP/threat-dragon/releases
- Microsoft Threat Modeling Tool https://www.microsoft.com/en-us/download/details.aspx?id=49168
- draw.io https://app.diagrams.net/

Threat dragon DTD symbols:
![[Images/Pasted image 20250622231832.png|200]]

Data flow diagram examples
![[Images/Pasted image 20250622235237.png]]
![[Images/Pasted image 20250622235421.png]]
from: https://www.youtube.com/watch?v=rEnJYNkUde0

### Threat Enumeration

Go through possible vulnerabilities

Threat modeling frameworks
CIA (the classic)
[[STRIDE]] (Microsoft 1999) Spoofing, Tampering, Repudiation, Information disclosure, DOS, Elevation of privilege
[[DREAD]] (Microsoft, newer but discontinued) Damage Potential, Reproducibility, Exploitability, Affected Users, Discoverability
PASTA Process for Attack Simulation and Threat Analysis, 7 steps
OCTAVE Operationally Critical Threat Asset & Vulnerability Evaluation
NIST 800-154 docs for Guide to Data-Centric System Threat Modeling
[[LINDDUN]]

there's also the attack libraries/trees, MITRE, CAPEC

Make a spreadsheet, list or integrate into an app like OWASP Dragon
for every security boundary(/flowline) (put one wherever auth happens or vulns can exist in other words)
Check what applies to your system (per boundary(/flowline)... choose amount of detail)

![[Images/Pasted image 20250622231905.png|700]]
https://en.wikipedia.org/wiki/STRIDE_model
![[Images/Pasted image 20250622232058.png]]
images from: https://www.youtube.com/watch?v=X5pXetz52zI

example spreadsheet use:
![[Images/Pasted image 20250623001055.png]]
from: https://www.youtube.com/watch?v=rEnJYNkUde0


Communicate back n forth with different teams making sure the information in the threat model is correct

Have all threats been documented (and mitigations found?)

