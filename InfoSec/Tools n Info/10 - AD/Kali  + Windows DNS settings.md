
Get specific .ovpn-file from https://tryhackme.com/access, click Network to see "breachingad" and update DNS settings in Kali
### DNS settings Kali

Settings - Settings Manager - Advanced Network Configuration - your network connection - IPv4 Settings
![[Images/Pasted image 20250221161352.png]]

### DNS in AD

AD is totally dependent on working DNS since Kerberos can't use IPs.

##### Debugging DNS in Kali

1. Make sure the DC IP is in your list of DNS servers. Add with `nmcli connection modify "Wired connection 1" ipv4.dns "10.200.78.101"` and `sudo systemctl restart NetworkManager`. 
2. Ping the IP of the DC server (the DNS) to make sure you're on the network (VPN...) `ping 10.200.80.101`.
3. Run `nslookup za.tryhackme.com 10.200.80.101` and `nslookup za.tryhackme.com`. The result should be the same as 10.200.80.101 should be your main DNS.

IPs:
THMDC 10.200.80.101
THM-IIS 10.200.80.201
ntlmauth.za.tryhackme.com

#### On Windown

```powershell
$dnsip = "<DC IP>"
$index = Get-NetAdapter -Name 'Ethernet' | Select-Object -ExpandProperty 'ifIndex'
Set-DnsClientServerAddress -InterfaceIndex $index -ServerAddresses $dnsip
```

Test with `dir \\za.tryhackme.com\SYSVOL\` (in cmd for better view)

##### Explanation

```powershell
PS C:\Users\leslie.young> Get-netAdapter

Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
----                      --------------------                    ------- ------       ----------             ---------
Ethernet 4                Amazon Elastic Network Adapter                6 Up           02-F4-FC-C9-E3-CF        25 Gbps
```

```powershell
PS C:\Users\leslie.young> Get-NetAdapter -Name 'Ethernet 4' | Select-Object -ExpandProperty 'ifIndex'
6
```

```powershell
PS C:\Users\leslie.young> Get-DnsClientServerAddress

InterfaceAlias               Interface Address ServerAddresses
                             Index     Family
--------------               --------- ------- ---------------
Ethernet 4                           6 IPv4    {10.200.56.101}
Ethernet 4                           6 IPv6    {}
Loopback Pseudo-Interface 1          1 IPv4    {}
Loopback Pseudo-Interface 1          1 IPv6    {fec0:0:0:ffff::1, fec0:0:0:ffff::2, fec0:0:0:ffff::3}
```

