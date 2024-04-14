port 88
kerberos-sec

key distribution server

look up pdc record in dns

ldap ports  389 & 3268?
ad = ldap databade with special structure
636 encrypted ldap

often on dc but not on all
only the global catalog on a few dcs

domin name by 389 port info from nmap

dc usually also a dns server

adidnsdump tool dirkjanm github
enum ad dns stuff

rid every entity has one = sids

rid is the end of the sid
domain admins 512

crackmapexec smb <IP> -u '' -p '' --rid-brute
to bruteforce

zip2john 

