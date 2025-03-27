
https://nmap.org/book/man-port-scanning-techniques.html

### Scanning a network

-n   don't do a reverse DNS lookup

-R   query DNS for offline hosts too (default, only online hosts)

-sn   no port scan, only ping scan
`nmap -sn <targets>`

-PR   arp scan (local network only) sends arp request gets arp reply
`nmap -PR -sn MACHINE_IP/24`

-PE   ICMP echo (ICMP Type 8/Echo/ping request, gets ICMP Type 0/ping reply)
`sudo nmap -PE -sn 10.10.68.220/24

-PP   ICMP timestamp (ICMP Type 13/timestamp request, gets ICMP Type 14/Timestamp reply)
`sudo nmap -PP -sn 10.10.68.220/24`

-PM   ICMP address mask queries (ICMP Type 17) gets address mask reply (ICMP Type 18)
`sudo nmap -PM -sn 10.10.68.220/24`

-PS   TCP SYN  ping, default port 80, can be set by port number (-PS21), range (-PS21-25), list (-PS21, 23) or a combo
`sudo nmap -PS -sn 10.10.68.220/24`

-PA   ACK SYN  requires sudo, ping, default port 80, can be set by port number (-PS21), range (-PS21-25), list (-PS21, 23) or a combo
`sudo nmap -PA -sn 10.10.68.220/24

-PU   UDP packet, open port will not reply but closed port will send ICMP port unreachable packet (ICMP Type 3, Code 3)
`sudo nmap -PU -sn 10.10.68.220/24`


### Scanning ports

-r   scan ports in consecutive order instead of random

-sT   TCP connect scan, Full 3-way handshake
`nmap -sT 10.10.109.38`

-sS   TCP SYN scan, only "SYN", when we get a "SYN, ACK" reply, nmap just sends a "RST" to tear down the connection
`sudo nmap -sS 10.10.109.38`

-sU   UDP scan, we expect no reply from an open port but a closed port will reply with port unreachable packet (ICMP Type 3, Code 3)
`sudo nmap -sU 10.10.251.116`

##### Specifying ports to scan

-p22,80,443
-p1-1023
-p-   all ports
-F   fast mode and just a 100 ports
--top-ports 10
--source-port   set source port

##### Specifying scan speed

-T<0-5>
-T0   slowest
-T3   default
-T5   fastest

`--min-rate <number>`
`--max-rate <number>`
--max-rate 10   max 10 packets per second

`--min-parallelism <numprobes>`
`--max-parallelism <numprobes>`
--max-parallelism=512

`--host-timeout <time>` time to wait for a target
##### Specifying verbosity

--reason   why is a host up, a port open...
-v   high verbosity
-vv   higher
-d   debug mode
-dd   more details

### Service/OS detections and NSE (Nmap Scripting Engine)

-sV   Service detection, uses full 3-way handshake and communicates with the listening service, giving us service and version info
-sV --version-intensity LEVEL   0 to 9 (`-sV --version-light` for intensity 2, `-sV --version-all` for intensity 9)
`sudo nmap -sV 10.10.20.146

-O   OS detection, not always reliable
`sudo nmap -sS -O 10.10.20.146`

--traceroute
`sudo nmap -sS --traceroute 10.10.20.146`

-sC   runs the deault scripts `--script=default`
`sudo nmap -sS -sC 10.10.172.222`

--scripr=...   any of the cathegories:

| Script Category | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| `auth`          | Authentication related scripts                                         |
| `broadcast`     | Discover hosts by sending broadcast messages                           |
| `brute`         | Performs brute-force password auditing against logins                  |
| `default`       | Default scripts, same as `-sC`                                         |
| `discovery`     | Retrieve accessible information, such as database tables and DNS names |
| `dos`           | Detects servers vulnerable to Denial of Service (DoS)                  |
| `exploit`       | Attempts to exploit various vulnerable services                        |
| `external`      | Checks using a third-party service, such as Geoplugin and Virustotal   |
| `fuzzer`        | Launch fuzzing attacks                                                 |
| `intrusive`     | Intrusive scripts such as brute-force attacks and exploitation         |
| `malware`       | Scans for backdoors                                                    |
| `safe`          | Safe scripts that won’t crash the target                               |
| `version`       | Retrieve service versions                                              |
| `vuln`          | Checks for vulnerabilities or exploit vulnerable services              |

--script "script name"
--script "name*"   careful what's included
`sudo nmap -sS -n --script "http-date" 10.10.172.222`

### More Advanced scans (sudo req)

-sN   Null scan, no flags set. Will get no reply from an open port, but a RST/ACK from a closed one. No reply = open/filtered.
`sudo nmap -sN 10.10.217.174`

-sF   FIN scan, FIN flag set. Will get no reply from an open port, but a RST/ACK from a closed one. No reply = open/filtered.
`sudo nmap -sF 10.10.217.174`

-sX   Xmas scan, FIN, PSH and URG falgs set.  Will get no reply from an open port, but a RST/ACK from a closed one. No reply = open/filtered.
`sudo nmap -sX 10.10.217.174`

-sM   Maimon scan. FIN and ACK flags set. Both an open and closed port will send RST back, except for some BSD derived systems, that drops the packet. So usually doesn't work.
`sudo nmap -sM 10.10.252.27`

-sA   TCP ACK scan, ACK flag set. All ports will always respond with RST, meaning we can use this for detecting ports blocked by a firewall.
`sudo nmap -sA 10.10.25.140`

-sW   Window scan, ACK flag set. Same as ACK scan but examines the TCP Window field of the RST packets returned. On some systems, open ports use a positive window size (even for RST packets) while closed ones have a zero window. This is used to distinguish between open anad unfiltered ports.
`sudo nmap -sW 10.10.25.140`

---scanflags   set flags my using their names with no spaces
`sudo nmap --scanflags RSTSYNFIN 10.10.25.140`

#### Spoofing IP and MAC

-e   set network interface
-S   set IP to spoof
`nmap -e NET_INTERFACE -Pn -S SPOOFED_IP 10.10.25.140`

--spoof-mac   set mac to spoof

-D   decoy scan, appearing to have several origins
`nmap -D 10.10.0.1,10.10.0.2,ME 10.10.25.140`
`nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME 10.10.25.140`   ME is our ip, RND is a random ip

#### Fragment packages

-f   8 byte segments
-ff   16 byte fragments
--mtu   set default value, multiple of 8

--data-length NUM

#### Idle/Zombie scan

sI   Idle scan/zombie scan. The zombie ip needs to be a machine that has no network trafic as the packet id number, that is incremented for every packet sent, is used. First our machine sends a SYN/ACK to the zombie and records the ID. Then we send a packet to the target with the zombie ip as the source. Depending on if the target "response" to the zombie (target sending RST makes zombie send nothing, target sending SYN/ACK makes zombie reply with RST) the packet counter will increase or not. Then we send another packet and chack if the conter has been increased or not.
`nmap -sI ZOMBIE_IP 10.10.25.140`

### Output

-oN filename   normal format
-oG filename   grepable format
-oX filename   xml format
-oA filename   all of the above

### Useful commands

nmap -sC -sV -Pn 10.10.10.10
nmap -p- -sC -sV -Pn 10.10.10.10

nmap -sC -sV 10.10.10.10
nmap -sC -sV -p- 10.10.10.10
nmap -sU -sV --top-ports 20 10.10.10.10
nmap --script vuln 10.10.10.10

SYN scan, ports 1-1000, very verbose:
sudo nmap -sS -p1-1000 -vv 10.10.97.172

sudo nmap -sU 10.10.10.10    \#garrs recommended udp scans
sudo nmap -sU -p- 10.10.10.10

slow scan network
nmap -A -p- 10.10.10.0/24 -v

garr:
export target="10.10.10.10"
nmap $target --min-rate=5000 -oA init
sudo nmap $target -p- -oA service -Pn --open -v

"I always start with this scan for open port and then proceed to -sCV"
`nmap -p- --open -sS -min-rate 5000 -n -vvv -Pn <ip>`

-min-rate 5000         speedy!
-n                              don't resolve
-open                        only show open = filters output
-vvv
-sS



###### To use on internal professional test

From Knight on Garrs event

\#discovery
nmap --open --initial-rtt-timeout=250ms --max-rtt-timeout=400ms --host-timeout=20m -sn -PE -PS7,9,13,21-23,25-26,37,53,79-81,88,106,110-111,113,119,135,139,143-144,179,199,389,427,443-445,465,513-515,543-544,548,554,587,631,646,873,990,993,995,1025-1029,1110,1433,1720,1723,1755,1900,2000-2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000-6001,6646,7070,8000,8008-8009,8080-8081,8443,8888,9100,9999-10000,32768,49152-49157 -PU53,67-69,111,123,135,137-139,161-162,445,500,514,520,631,996-999,1434,1701,1900,3283,4500,5353,49152-49154 -iL scope.txt -oA external_disco_customer

\#run on the live hosts fount in the discovery
nmap --version-intensity=0 --min-rate=150 --max-retries=2 --initial-rtt-timeout=50ms --max-rtt-timeout=200ms --max-scan-delay=5s -Pn -sS -sV -sU -p T:1-65535,U:53,67-69,111,123,135,137-139,161-162,445,500,514,520,631,996-999,1434,1701,1900,3283,4500,5353,49152-49154 -iL discovery_scan_hosts -oA external_profile_customer

| Nmap flag     | Description                                                                         |
| ------------- | ----------------------------------------------------------------------------------- |
| -sV           | Attempts to determine the version of the services running                           |
| -p <x> or -p- | Port scan for port <x> or scan all ports                                            |
| -Pn           | Disable host discovery and scan for open ports                                      |
| -A            | Enables OS and version detection, executes in-build scripts for further enumeration |
| -sC           | Scan with the default Nmap scripts                                                  |
| -v            | Verbose mode                                                                        |
| -sU           | UDP port scan                                                                       |
| -sS           | TCP SYN port scan                                                                   |
-iL list.txt
we can list what to scan (space between), use a range like 10.10.0-255.101-125, a subnet like 10.10.12.13/29 or supply a list using -iL.

#### Help

```sh
┌──(kali㉿kali)-[~]
└─$ nmap -h                  
Nmap 7.94 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS´s DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports sequentially - don´t randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --noninteractive: Disable runtime interactions via keyboard
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```



#### Examples

list what will be scanned, will do a reverse dns (use -n not to do the rev dns)
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sL 10.10.12.13/29                                                                                     
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-04 19:53 CEST
Nmap scan report for 10.10.12.8
Nmap scan report for 10.10.12.9
Nmap scan report for 10.10.12.10
Nmap scan report for 10.10.12.11
Nmap scan report for 10.10.12.12
Nmap scan report for 10.10.12.13
Nmap scan report for 10.10.12.14
Nmap scan report for 10.10.12.15
Nmap done: 8 IP addresses (0 hosts up) scanned in 0.00 seconds
```

### How it works

Nmap uses
1. ARP scan: This scan uses ARP requests to discover live hosts (same subnet, not routed)
2. ICMP scan: This scan uses ICMP requests to identify live hosts
3. TCP/UDP ping scan: This scan sends packets to TCP ports and UDP ports to determine live hosts.
![[Images/745e0412b319d324352c7b29863b74f4.png|500]]
