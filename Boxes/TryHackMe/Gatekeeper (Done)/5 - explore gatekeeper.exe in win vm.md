
We started x32dbg and opened gatekeeper.exe.

Confirming the port it's running on:
```sh
C:\Windows\system32>netstat -ab

Active Connections

  Proto  Local Address          Foreign Address        State
...
  TCP    0.0.0.0:31337          DESKTOP-S2GUNPV:0      LISTENING
 [gatekeeper.exe]
...
```

gatekeeper is running on port 31337 as expected

Let's make a fuzzer script to explore buffer overflow

When fuzzing it doesn't work if we recv data, why?

Also, there doesn't seem to be a buffer overflow possibility as we get this when going hiiiigh:

```sh
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
```

oh, it did crash:

server log:
```sh
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 56000
Client disconnected.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 57000
Client disconnected.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58000
Client disconnected.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623
[!] recvbuf exhausted. Giving up.
Received connection from remote host.
Connection handed off to handler thread.
Bytes received: 58623                               at 105000 here :O
[!] recvbuf exhausted. Giving up.
```
count the number of results after 58000
this was the crach point

data
![[Images/Pasted image 20241016120212.png]]

