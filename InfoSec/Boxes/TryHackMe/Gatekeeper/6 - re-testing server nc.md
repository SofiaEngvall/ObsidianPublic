
```
┌──(kali㉿kali)-[~]
└─$ nc 10.10.26.181 31337
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
Hello 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890!!!
12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
Hello 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890!!!
123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
Hello 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890!!�qwe
Hello qwe!!!
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
Hello 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012�]�!!!
��▒�YL���qwe
Hello qwe!!!
12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
Hello 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012�]�1234��90!!

┌──(kali㉿kali)-[~]
└─$ nc 10.10.26.181 31337
qwe
Hello qwe!!!
```

As this does crash let's rewrite our script to just connect once and send several test strings during the same one.
The 120 char one was the last to get a reply.

Observe that we can reconnect though