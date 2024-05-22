
Enumerate all the things
- all ports, tcp and udp
- what services are running
	- what version is the service
	- are there known vulns for this version
	- what tools could we use to access the service, try several tools for the same thing
	- what information can I find using these


nmap -sC -sV -Pn 10.10.10.10
nmap -p- -sC -sV -Pn 10.10.10.10
sudo nmap -p- -sN 10.10.10.10      sneakier

--script "name*"   careful what's included
`sudo nmap -sS -n --script "http*" 10.10.171.184`
`sudo nmap -v -sS -n -p80 --script "http*" 10.10.171.184` (30 min)
`sudo nmap -v -sS -n -p80 --script "http-sitemap-generator" 10.10.32.33`

check nmap service versions - exploints?

Always try usernames you find as passwords
look up default creds

#### http
* gobuster on main http dirs
	* on subdirectories
	* check for virtual hosts (make wordlist from webpage to use their terminology)

#### ftp
- anonymous login

#### smb
- anon login

#### ssh



