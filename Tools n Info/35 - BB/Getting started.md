
How to Crush Bug Bounties in the first 12 Months
https://www.youtube.com/watch?v=AbebbJ3cRLI

Bugcrowd youtube has lots of videos

### Education

The Bug Hunter's Metodology v4, Jason Haddix - Recon + Application Hacking (2 vids)
Recon: https://youtu.be/gIz_yn0Uvb8?si=VJSnh5DN33Nuk4WT (v4.02)
App analysis: 
#### Books

OWASP Testing Guide
The Web Application Hacker's Handbook
### Tools

Burp/Zap - web proxies
FireFox/Chrome - Browser with extensions
- Proxy switcher - Foxy Proxy
- Wappalyser/BuiltWith - web page info
- Open multiple URS - open pasted urls
- Copy Tab URLs - copy all tab urls
- Snap Links Plus - drag a box over the oage and copy all links passed over
- Link Gopher - parses all liknks on a page
VMware/Virtualbox
Kali/Ubuntu machine
Tools to make notes
### Labs

OWASP Vulnerable Web Applications Directory Project - Vuln apps

### Sites

HackerOne
BugCrowd

### Submitting

- Write so a developer can understand, not just a security researcher
- Think from the customers angle
	- What can you actually do with this bug?
	- How hard will it be to fix?
- Select the right category - Go for top level if you can't find a suitable one
- Use Markdown to make it easy to read
- Include as much information as possible
- Good screenshots
- Videos are great as is also proves the bug was there in case it's fixed later

Make templates for common bug reports


### Note taking
(Haddix uses Xmind mindmap)
(Color code the status of parts of notes, ex green = done, orange = working on this)
Keep track on where you are, so you can come back later

Recon
	ASNs
		123
		456
	Acquisitions
		qwe
		asd
	Linked Discovery
	Reverse WHOIS
Roots
	abc.com
	qwerty.com
		123.qwert.com
		all subdomains
	
Site drilldown notes for one domain: all the questions you ask yourself when hacking a site
123.qwerty.com
	Notes
		Drupal (php), akamai
	interesting endpoints
		`/asdfgh`
	narrow recon
		service identification
			port scanning
		stack identification
			technology profiles
			version or cvss investigation
		content discovery
			javascript analysis
			file/folder bruteforce
		Application feature analysis
			business logic flows
		Dynamic inputs
			file uploads
				PDF (XML), Doc ++
				image
			Interesting
				multi-part forms
				APIs
				parameters referencing a path ot URL
				Errors!
			other dynamic parameters
			++
		Questions to ask
			How does the framework handle `"'!´-*&^%_+` (special) characters?
			How does the site reference a user?
			Are there multiple user roles?

What he said:
multiple user roles?
how does it reference users
how does it handle special characters
what are the dynamic parameters
does it have an api component
what kind of errors am I seeing
does it have file uploads
have I done javascript analysis for path
have I done content discovery


### Recon

Wide Recon - find as many assets related to the target as possible (make sure they are within scope)

Scope domains
- From bb site
- wide scope = `*.tesla.com`, "Any host verified to be owned by Tesla..."
	examples, tesla.com, verizon media
Acqusitions
	- is there stuff that has not been taken down
	- search site: Chrunchbase
ASN Enumeration (Autonomous System Number)
- given to big networks - shows known ip ranges
- search site: hurricane electric (https://bap.he.net)
- cmd tools: mstebigor, asnlookup
Reverse WHOIS
Subdomain Enumeration
Port Analysis

Vulnerability scanning (during recon)
- Subdomain Takeover
- Buckets
- Github leaks

Automation/Helpers
- Interlace
- - Screenshotting
- Frameworks

