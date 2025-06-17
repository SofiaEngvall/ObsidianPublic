
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ ssh user@10.10.10.3                                                   
Unable to negotiate with 10.10.10.3 port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss

┌──(kali㉿proxli)-[~/exploits]
└─$ ssh -oHostKeyAlgorithms=+ssh-rsa user@10.10.10.3
The authenticity of host '10.10.10.3 (10.10.10.3)' can't be established.
RSA key fingerprint is SHA256:BQHm5EoHX9GCiOLuVscegPXLQOsuPs+E9d/rrJB84rk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.10.3' (RSA) to the list of known hosts.
user@10.10.10.3's password: 
Permission denied, please try again.
user@10.10.10.3's password: 
Permission denied, please try again.
user@10.10.10.3's password: 
user@10.10.10.3: Permission denied (publickey,password).
```
