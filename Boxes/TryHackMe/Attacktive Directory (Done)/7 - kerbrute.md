
running [[../../../Tools n Info/10 - AD/kerbrute|kerbrute]] just to test it:

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

much quicker to run through the brute force list!

james@spookysec.local
svc-admin@spookysec.local
robin@spookysec.local
darkstar@spookysec.local
administrator@spookysec.local
backup@spookysec.local
paradox@spookysec.local
ori@spookysec.local
