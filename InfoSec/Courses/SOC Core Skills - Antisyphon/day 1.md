
![[Images/Pasted image 20250127194750.png]]

![[Images/Pasted image 20250127194837.png]]

sip = voip

5900 vnc


### tcpdmp

`tcpdump -n -r magnitude_1hr.pcap host 192.168.99.52`
not resolve hostnames **(-n)** and read in the data from a file (-r)

`tcpdump -n -r magnitude_1hr.pcap host 192.168.99.52 and port 80`

`tcpdump -n -r magnitude_1hr.pcap host 192.168.99.52 and port 80 -A`
-A acsii

`tcpdump -n -r magnitude_1hr.pcap host 192.168.99.52 and port 80 -AX`
- A acsii
- X hex

`tcpdump -n -r magnitude_1hr.pcap ip6`
ipv6 traffic

`tcpdump -n -r magnitude_1hr.pcap net 192.168.99.0/24`

`tcpdump -n -r magnitude_1hr.pcap host 192.168.99.52 and port 80 -A > blah.txt` `less blah.txt` in less hit `/15:14:32.638976` anyone got an easier way or this is the best option?


### Wireshark

![[Images/Pasted image 20250127211013.png]]

Also check out Statistics, Conversations - Who's talking to whom?
If we sort on packets we can see if there's some intense traffic going on!

Then we can:
![[Images/Pasted image 20250127212013.png]]
Updates the main window

https://github.com/KAISERaustin/IntroLabsRemastered/blob/master/IntroClassFiles/Tools/IntroClass/Wireshark/Wireshark.md

![[Images/Pasted image 20250127212649.png]]


### Job searching

builtwith.com on company website
get "security best practises" on systems they use, ex cloudflare - get familiar with their tech
cisecurity.com/cis-benchmarks for best practises
add to cv/profile "I am familiar with cloudflare security technologies"

### pcaps to check out:

Please check out, "Malware of the Day" from **Active Countermeasures**!

`https://www.activecountermeasures.com/category/malware-of-the-day/`

Below are the commands to download some of the capture files. Try and run through the basic level analysis we just did with them.

`https://www.dropbox.com/s/zyqn3nn5ygfki59/teamviewer_1hr.pcap`

`https://www.activecountermeasures.com/pcap/apt1virtuallythere_1hr.pcap`

`https://www.dropbox.com/s/51uzphl1f3ca691/lateral_backup_c2_1hr.pcap`

`https://www.dropbox.com/s/bhgvpablx11u8yb/taidoor_1hr.pcap`

Here is a great resource to try some more options in **TCPDump**:

`https://danielmiessler.com/study/tcpdump/`