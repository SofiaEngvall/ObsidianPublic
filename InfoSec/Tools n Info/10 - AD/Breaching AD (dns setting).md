
- NTLM Authenticated Services
- LDAP Bind Credentials
- Authentication Relays
- Microsoft Deployment Toolkit
- Configuration Files


Get specific .ovpn-file from https://tryhackme.com/access, click Network to see "breachingad" and update DNS settings in Kali
### DNS settings Kali

Settings - Settings Manager - Advanced Network Configuration - your network connection - IPv4 Settings
![[Images/Pasted image 20250221161352.png]]

### DNS in AD

AD is totally dependent on working DNS since Kerberos can't use IPs.

##### Debugging DNS

1. Make sure the DC IP is in your list of DNS servers. Add with `nmcli connection modify "Wired connection 1" ipv4.dns "10.200.80.101"` and `sudo systemctl restart NetworkManager`. 
2. Ping the IP of the DC server (the DNS) to make sure you're on the network (VPN...) `ping 10.200.80.101`.
3. Run `nslookup za.tryhackme.com 10.200.80.101` and `nslookup za.tryhackme.com`. The result should be the same as 10.200.80.101 should be your main DNS.

IPs:
THMDC 10.200.80.101
THM-IIS 10.200.80.201
ntlmauth.za.tryhackme.com

