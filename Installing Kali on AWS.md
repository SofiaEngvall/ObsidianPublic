# How to run a Free Kali VM in the Cloud 2025

Do you need to run a fully capable Kali VM in the cloud? Here's an easy to follow step-by-step guide!

Log in to aws.amazon.com or create a new account if you don't have one.

Observe that free tier only works the first year after the account was created!




on local linux
```sh
chmod 600 FixIt42-AWS-kali.pem
ssh -i FixIt42-AWS-kali.pem kali@51.20.141.231
```

on aws
```sh
sudo apt update
sudo apt install kali-linux-default
sudo apt install kali-desktop-xfce
```

if you just want a headless server, no gui, you can instead do:
```sh
sudo apt update && sudo apt install -y kali-linux-headless
```

I have not tested this but you're supposed to be able to get faster cracking speeds if you run:
```sh
sudo apt update
sudo apt full-upgrade
sudo apt install linux-headers-5.7.0-kali3-cloud-amd64
sudo reboot

#after reboot
sudo apt install -y nvidia-driver nvidia-cuda-toolkit
```

### VNC

```sh
ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194

sudo apt install tightvncserver

sudo reboot

tightvncserver :1 -geometry 1920x1080
#set password when asked

#to close
tightvncserver -kill :1

#on connecting machine
vncviewer localhost:5901

#or remmina whick supports no edges
remmina

```


getting started in windows
powershell
```sh
PS C:\Users\sofia\Downloads> ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194
The authenticity of host '13.60.203.194 (13.60.203.194)' can't be established.
ED25519 key fingerprint is SHA256:t6L4msydTbNSyBrxDgnwYWlVwV0xaPsWoVwjPO9WP1w.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '13.60.203.194' (ED25519) to the list of known hosts.
Bad permissions. Try removing permissions for user: MAIN-I732\\linus (S-1-5-21-1191888695-326032422-535987215-1004) on file C:/Users/sofia/Downloads/FixIt42-AWS-kali.pem.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions for 'FixIt42-AWS-kali.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "FixIt42-AWS-kali.pem": bad permissions
kali@13.60.203.194: Permission denied (publickey).
```

changed the file's advanced permissions - disabled inheritance (button) and gave my user only read permissions (add button, write username, check read only)
or this could also be used:
```sh
Icacls file.pem /Inheritance:r
Icacls file.pem /Grant:r "%Username%":"(R)"
```

```sh
PS C:\Users\sofia\Downloads> ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194
Linux kali 6.12.13-cloud-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.12.13-1kali1 (2025-02-11) x86_64

The programs included with the Kali GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Kali GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Mar 18 19:19:14 2025 from 31.208.161.82
┏━(Message from Kali developers)
┃
┃ This is a cloud installation of Kali Linux. Learn more about
┃ the specificities of the various cloud images:
┃ ⇒ https://www.kali.org/docs/troubleshooting/common-cloud-setup/
┃
┗━(Run: “touch ~/.hushlogin” to hide this message)
┌──(kali㉿kali)-[~]
└─$ 
```

vnc on windows, can do full screen:
https://www.realvnc.com/en/connect/download/viewer/windows/


### RDP

```sh
sudo apt install xrdp
systemctl enable xrdp
#systemctl enable xrdp-sesman     #installed but later uninstalled and it still worked
```

windows fails to even try to connect to localhost:3389 as it is in use so we have to change the port:
```sh
sudo nano /etc/xrdp/xrdp.ini
```
change `port=3389` to `port=3390`

restart ssh connection with the new port:
```sh
PS C:\Users\sofia\Downloads> ssh -L 3390:localhost:3390 -i FixIt42-AWS-kali.pem kali@13.60.203.194
```

fix the permissions so that we can log in
```sh
┌──(kali㉿kali)-[~]
└─$ echo kali:password | sudo chpasswd
```
`sudo passwd kali`

```sh
sudo /etc/init.d/xrdp start
```

```sh
git clone https://github.com/SofiaEngvall/ObsidianPublic.git
```