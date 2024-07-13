https://github.com/mpgn/CrackMapExec
https://wiki.porchetta.industries/

bruteforce & password spray
enumerating shares
execute commands on some protocols

https://pypa.github.io/pipx/ for virtual installation

![[Pasted image 20230829232517.png]]

![[Pasted image 20230829232748.png]]

smb v1 = try ethernal blue

![[Pasted image 20230829233423.png]]
nullsessions

![[Pasted image 20230829233505.png]]
guest account?

![[Pasted image 20230829233822.png]]
passw file

![[Pasted image 20230829233959.png]]
enum usernames

documentation:
script script.txt
less -r script.txt

![[Pasted image 20230829235355.png]]

-k uses kerberos, this traffic is more common on the network
default is ntlm which is not that common

--use-kcache uses existing kerberos ticket
get ticket by
impacket-getTGT -dc-ip 10.10.10.10 domain.LOCAL/usename
export KRB5CCNAME= user.ccache

then:
![[Pasted image 20230830000447.png]]

mostly useful for golden.. tickets


![[Pasted image 20230830001057.png]]

-x uses cmd
-X uses ps
![[Pasted image 20230830001322.png]]

.cme/obfuscated_scripts
can make your own since fingerprinted - defender finds
custom amsi bypass on cme webbpage

or run ps with cmd lol
![[Pasted image 20230830001734.png]]

dcom, check into this

---
was away n missed stuff

---




![[Pasted image 20230830003039.png]]

---
modules
--

-L to list modules
--list-modules

firefox dump creds!
enum_dns get ad dns


![[Pasted image 20230830003629.png]]
dumps from memory

![[Pasted image 20230830004002.png]]
win11 wont work

![[Pasted image 20230830004237.png]]
can set options



check out masky ad cs




LDAP
--

![[Pasted image 20230830004750.png]]

![[Pasted image 20230830004913.png]]



bloodhound
--

![[Pasted image 20230830005120.png]]


![[Pasted image 20230830005333.png]]
![[Pasted image 20230830005422.png]]

![[Pasted image 20230830005655.png]]

dump --sam & --lsa

copy file
![[Pasted image 20230830010137.png]]
or --get-file

![[Pasted image 20230830010449.png]]


