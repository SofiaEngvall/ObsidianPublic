
ICMP has [many types](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml). ICMP ping uses Type 8 (Echo) and Type 0 (Echo Reply).
If you want to ping a system on the same subnet, an ARP query should precede the ICMP Echo.

ICMP is on the network layer
![[Images/745e0412b319d324352c7b29863b74f4.png|600]]

thm: https://tryhackme.com/r/room/networkingessentials

