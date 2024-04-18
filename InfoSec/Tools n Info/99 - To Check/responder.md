
https://www.kali.org/tools/responder/

Responder is a sniffing tool used to gain vulnerable credentials from network traffic, including those sent over SMB, HTTP, and other protocols. Responder is also an LLMNR, NBT-NS, and MDNS poisoner.

In a Windows environment, protocols such as LLMNR and NBT-NS can often be easily exploitable. LLMNR (Linked-Local Multicast Name Resolution) is a Windows component that acts as a host discovery method in Windows systems. LLMNR is used very often in Active Directory environments. Local networks have many things on them that we, as penetration testers, can exploit. Windows stores passwords in the Security Accounts Manager (SAM) Database or the Active Directory database in domains, and they are hashed.

![[mceclip0.png]]
##### Stages
1. A Windows server makes an LLMNR request looking for a specific resource.
2. The attacker using the Responder tool provides the Windows server with the IP of the attacker’s machine.
3. The Windows server supplies its domain credentials to the attacker in an attempt to access the specified resource.

### Examples

`responder -I eth0`

