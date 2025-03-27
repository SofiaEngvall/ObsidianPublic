
```sh
┌──(kali㉿kali)-[~]
└─$ telnet skynet.thm 110
Trying 10.10.155.35...
Connected to skynet.thm.
Escape character is '^]'.
+OK Dovecot ready.
help
-ERR Unknown command.
user miles
-ERR [AUTH] Plaintext authentication disallowed on non-secure (SSL/TLS) connections.
^C
^]
telnet> exit
?Invalid command
telnet> quit
Connection closed.
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ telnet skynet.thm 143
Trying 10.10.155.35...
Connected to skynet.thm.
Escape character is '^]'.
* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LOGINDISABLED] Dovecot ready.
c1 login miles
c1 BAD Error in IMAP command received by server.
c2 LOGIN miles
c2 BAD Error in IMAP command received by server.
c3 LOGIN Mailes
* BYE Too many invalid IMAP commands.
Connection closed by foreign host.
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ telnet skynet.thm 143
Trying 10.10.155.35...
Connected to skynet.thm.
Escape character is '^]'.
* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LOGINDISABLED] Dovecot ready.
c1 LOGIN Miles
c1 BAD Error in IMAP command received by server.
quit
quit BAD Error in IMAP command received by server.
c2 logout
* BYE Logging out
c2 OK Logout completed.
Connection closed by foreign host.

```

http://skynet.thm/squirrelmail


![[Images/Pasted image 20240614155228.png]]


