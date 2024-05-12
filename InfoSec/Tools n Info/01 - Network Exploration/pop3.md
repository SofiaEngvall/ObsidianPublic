
https://tryhackme.com/r/room/protocolsandservers

Post Office Protocol version 3

```sh
pentester@TryHackMe$ telnet 10.10.240.43 110
Trying 10.10.240.43...
Connected to 10.10.240.43.
Escape character is '^]'.
+OK 10.10.240.43 Mail Server POP3 Wed, 15 Sep 2021 11:05:34 +0300 
USER frank
+OK frank
PASS D2xc9CgD
+OK 1 messages (179) octets
STAT
+OK 1 179
LIST
+OK 1 messages (179) octets
1 179
.
RETR 1
+OK
From: Mail Server 
To: Frank 
subject: Sending email with Telnet
Hello Frank,
I am just writing to say hi!
.
QUIT
+OK 10.10.240.43 closing connection
Connection closed by foreign host.
```