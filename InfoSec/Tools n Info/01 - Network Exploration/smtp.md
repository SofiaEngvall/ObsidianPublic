
https://tryhackme.com/r/room/protocolsandservers

Simple Mail Transfer Protocol

```sh
pentester@TryHackMe$ telnet 10.10.240.43 25
Trying 10.10.240.43...
Connected to 10.10.240.43.
Escape character is '^]'.
220 bento.localdomain ESMTP Postfix (Ubuntu)
helo telnet
250 bento.localdomain
mail from: 
250 2.1.0 Ok
rcpt to: 
250 2.1.5 Ok
data
354 End data with .
subject: Sending email with Telnet
Hello Frank,
I am just writing to say hi!             
.
250 2.0.0 Ok: queued as C3E7F45F06
quit
221 2.0.0 Bye
Connection closed by foreign host.
```

