```sh
┌──(kali㉿kali)-[/opt/enum4linux-ng]
└─$ python3 enum4linux-ng.py 10.10.11.222                              
ENUM4LINUX - next generation (v1.3.2)

 ==========================
|    Target Information    |
 ==========================
[*] Target ........... 10.10.11.222
[*] Username ......... ''
[*] Random Username .. 'voaavttp'
[*] Password ......... ''
[*] Timeout .......... 5 second(s)

 =====================================
|    Listener Scan on 10.10.11.222    |
 =====================================
[*] Checking LDAP
[+] LDAP is accessible on 389/tcp
[*] Checking LDAPS
[+] LDAPS is accessible on 636/tcp
[*] Checking SMB
[+] SMB is accessible on 445/tcp
[*] Checking SMB over NetBIOS
[+] SMB over NetBIOS is accessible on 139/tcp

 ====================================================
|    Domain Information via LDAP for 10.10.11.222    |
 ====================================================
[*] Trying LDAP
[+] Appears to be root/parent DC
[+] Long domain name is: authority.htb

 ===========================================================
|    NetBIOS Names and Workgroup/Domain for 10.10.11.222    |
 ===========================================================
[-] Could not get NetBIOS names information via 'nmblookup': timed out

 =========================================
|    SMB Dialect Check on 10.10.11.222    |
 =========================================
[*] Trying on 445/tcp
[+] Supported dialects and settings:
Supported dialects:                                                                                                          
  SMB 1.0: false                                                                                                             
  SMB 2.02: true                                                                                                             
  SMB 2.1: true                                                                                                              
  SMB 3.0: true                                                                                                              
  SMB 3.1.1: true                                                                                                            
Preferred dialect: SMB 3.0                                                                                                   
SMB1 only: false                                                                                                             
SMB signing required: true                                                                                                   

 ===========================================================
|    Domain Information via SMB session for 10.10.11.222    |
 ===========================================================
[*] Enumerating via unauthenticated SMB session on 445/tcp
[+] Found domain information via SMB
NetBIOS computer name: AUTHORITY                                                                                             
NetBIOS domain name: HTB                                                                                                     
DNS domain: authority.htb                                                                                                    
FQDN: authority.authority.htb                                                                                                
Derived membership: domain member                                                                                            
Derived domain: HTB                                                                                                          

 =========================================
|    RPC Session Check on 10.10.11.222    |
 =========================================
[*] Check for null session
[+] Server allows session using username '', password ''
[*] Check for random user
[+] Server allows session using username 'voaavttp', password ''
[H] Rerunning enumeration with user 'voaavttp' might give more results

 ===================================================
|    Domain Information via RPC for 10.10.11.222    |
 ===================================================
[-] Could not get domain information via 'lsaquery': STATUS_ACCESS_DENIED

 ===============================================
|    OS Information via RPC for 10.10.11.222    |
 ===============================================
[*] Enumerating via unauthenticated SMB session on 445/tcp
[+] Found OS information via SMB
[*] Enumerating via 'srvinfo'
[-] Could not get OS info via 'srvinfo': STATUS_ACCESS_DENIED
[+] After merging OS information we have the following result:
OS: Windows 10, Windows Server 2019, Windows Server 2016                                                                     
OS version: '10.0'                                                                                                           
OS release: '1809'                                                                                                           
OS build: '17763'                                                                                                            
Native OS: not supported                                                                                                     
Native LAN manager: not supported                                                                                            
Platform id: null                                                                                                            
Server type: null                                                                                                            
Server type string: null                                                                                                     

 =====================================
|    Users via RPC on 10.10.11.222    |
 =====================================
[*] Enumerating users via 'querydispinfo'
[-] Could not find users via 'querydispinfo': STATUS_ACCESS_DENIED
[*] Enumerating users via 'enumdomusers'
[-] Could not find users via 'enumdomusers': STATUS_ACCESS_DENIED

 ======================================
|    Groups via RPC on 10.10.11.222    |
 ======================================
[*] Enumerating local groups
[-] Could not get groups via 'enumalsgroups domain': STATUS_ACCESS_DENIED
[*] Enumerating builtin groups
[-] Could not get groups via 'enumalsgroups builtin': STATUS_ACCESS_DENIED
[*] Enumerating domain groups
[-] Could not get groups via 'enumdomgroups': STATUS_ACCESS_DENIED

 ======================================
|    Shares via RPC on 10.10.11.222    |
 ======================================
[*] Enumerating shares
[+] Found 0 share(s) for user '' with password '', try a different user

 =========================================
|    Policies via RPC for 10.10.11.222    |
 =========================================
[*] Trying port 445/tcp
[-] SMB connection error on port 445/tcp: STATUS_ACCESS_DENIED
[*] Trying port 139/tcp
[-] SMB connection error on port 139/tcp: session failed

 =========================================
|    Printers via RPC for 10.10.11.222    |
 =========================================
[-] Could not get printer info via 'enumprinters': STATUS_ACCESS_DENIED

Completed after 10.20 seconds
```