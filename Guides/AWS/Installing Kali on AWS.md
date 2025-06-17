# How to run a Free Kali VM in the Cloud 2025

- Starting a Free Kali VM on AWS
- Setting permissions on PEM file
	- Setting Permissions on Linux
	- Setting permissions on Windows
	- Setting permissions on Windows using GUI
- Connecting to the AWS VM using ssh
	- Connecting from Linux or Windows
- Upgrading to full Kali with GUI
- Connecting with GUI
- VNC - Virtual Network Computing
	- Installing, Stopping and Starting the VNC service
	- Connecting from Linux
	- Connecting from Windows
- RDP - Remote Desktop Protocol
	- Installing, Configuring and Uninstalling the RDP service
	- Connecting from Linux
	- Connecting from Windows

## Starting a Free Kali VM on AWS

Do you need to run a fully capable Kali VM in the cloud? Here's an easy to follow step-by-step guide!

The guide also includes different ways of connecting to the VMs Graphical User Interface (You don't have to read them all ;) )

Log in to aws.amazon.com or create a new account if you don't have one.

Observe that free tier only works the first year after the account was created!

![[Images/Pasted image 20250424135642.png]]

![[Images/Pasted image 20250424135721.png]]

on the right side, click Launch instance
![[Images/Pasted image 20250424135824.png]]

![[Images/Pasted image 20250424140228.png]]

![[Images/Pasted image 20250424140349.png]]

![[Images/Pasted image 20250424141005.png]]

![[Images/Pasted image 20250424141031.png]]

![[Images/Pasted image 20250424141141.png]]

![[Images/Pasted image 20250424141227.png]]

![[Images/Pasted image 20250424141251.png]]

![[Images/Pasted image 20250424141329.png]]

we get back to the launch instance page with free tier eligable kali selected

![[Images/Pasted image 20250424141501.png]]

keep the only free tier option for instance type:
![[Images/Pasted image 20250424141601.png]]

![[Images/Pasted image 20250424141646.png]]

create a key pair:

![[Images/Pasted image 20250424141820.png]]
you can select ED25519 if you want
save the key file in a place you remember

if you know all its you will access this vm from you can enter them here for higher security, otherwise just leave it as it is
![[Images/Pasted image 20250424142020.png]]

here we need more space to fit full kali, so set it to the maximum free tier eligible option, for my it says 30GB
![[Images/Pasted image 20250424142337.png]]
![[Images/Pasted image 20250424142426.png]]

![[Images/Pasted image 20250424142609.png]]

Observe the information:
***Free tier:** In your first year of opening an AWS account, you get 750 hours per month of t2.micro instance usage (or t3.micro where t2.micro isn't available) when used with free tier AMIs, 750 hours per month of public IPv4 address usage, 30 GiB of EBS storage, 2 million I/Os, 1 GB of snapshots, and 100 GB of bandwidth to the internet.*

![[Images/Pasted image 20250424142756.png]]

![[Images/Pasted image 20250424142835.png]]

![[Images/Pasted image 20250424143306.png]]

Make sure to note down the IP address

We now have a free kali vm running but it's very limited:
- only a minimal installation of kali linux
- no graphical user interface

We want a Kali installation with all tools available and a graphical user interface


fix the permissions so that we can log in
first we set it to password as this is clear text and might be seen
```sh
┌──(kali㉿kali)-[~]
└─$ echo kali:password | sudo chpasswd
```

now when kali has a password we can set it the normal way
```
┌──(kali㉿kali)-[~]
└─$ sudo passwd kali
```

![[Images/Pasted image 20250425205208.png]]

## Setting permissions on PEM file

Since the PEM file is a secret file that gives you permissions, ssh won't connect unless it has secure permissions.

```sh
PS C:\Users\sofia\Downloads\AWS> ssh -i kali-key.pem kali@56.228.19.43
The authenticity of host '56.228.19.43 (56.228.19.43)' can't be established.
ED25519 key fingerprint is SHA256:Osq9yZO6FOVqQVHTWSLeq+LfDiF9mMlKQwujuivL+wc.
This host key is known by the following other names/addresses:
    C:\Users\sofia/.ssh/known_hosts:4: 56.228.13.62
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '56.228.19.43' (ED25519) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions for 'kali-key.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "kali-key.pem": bad permissions
kali@56.228.19.43: Permission denied (publickey).
```

### Setting permissions on the PEM file in Linux

```sh
chmod 600 FixIt42-AWS-kali.pem
```

![[Images/Pasted image 20250425165729.png]]

### Setting permissions on the PEM file in Windows command line

Change the file's advanced permissions:
- Disable inheritance
- give your user permissions

```sh
Icacls kali-key.pem /Inheritance:r
Icacls kali-key.pem /Grant:r "$($env:USERNAME):(R)"
```

![[Images/Pasted image 20250425163911.png]]
![[Images/Pasted image 20250425164051.png]]

### Setting permissions on the PEM file in Windows, using GUI

![[Images/Pasted image 20250424144018.png]]

![[Images/Pasted image 20250424144131.png]]

![[Images/Pasted image 20250424144255.png]]

![[Images/Pasted image 20250424144329.png]]

![[Images/Pasted image 20250424144403.png]]

![[Images/Pasted image 20250424144419.png]]

![[Images/Pasted image 20250424144438.png]]

![[Images/Pasted image 20250424144522.png]]

![[Images/Pasted image 20250424144610.png]]

## Connecting to the AWS VM using ssh

### Connecting from Linux or Windows

```sh
ssh -i kali-key.pem kali@56.228.19.43
```
(use your ip address)

![[Images/Pasted image 20250425170650.png]]

![[Images/Pasted image 20250424145028.png]]

## Upgrading to full Kali with GUI on the AWS VM

### Installation of Kali with GUI

```sh
sudo apt update
sudo apt full-upgrade
sudo apt install kali-linux-default
sudo apt install kali-desktop-xfce

sudo reboot
```

### Add FULL Kali tools (Doesn't fit on 30 GB anymore)

```sh
sudo apt install kali-linux-everything
```

### Add Large Kali tools (Fits on the 30 GB free drive)

```sh
sudo apt install kali-linux-large
```

### Installation of headless Kali

```sh
sudo apt update && sudo apt install -y kali-linux-headless
```

### Installation of NVidia drivers

I have not tested this but you're supposed to be able to get faster cracking speeds if you run:
```sh
sudo apt update
sudo apt full-upgrade
sudo apt install linux-headers-5.7.0-kali3-cloud-amd64
sudo reboot

#after reboot
sudo apt install -y nvidia-driver nvidia-cuda-toolkit
```

## VNC

### Installing, Starting and Stopping the VNC service

Here we use -L ...

```sh
ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194
```

Install VNC (already installed if you installed kali-linux-default or everything):
```
sudo apt install tightvncserver

sudo reboot
```

Start VNC:
```
tightvncserver :1 -geometry 1920x1080
```
*set password when asked - remember we also need the ssh connection running and have the security of it's PEM-file*

![[Images/Pasted image 20250425183528.png|800]]

Stop VLC:
```sh
tightvncserver -kill :1
```

Security TODO! check that we can't connect externally

### Connecting from Linux

Connect with ssh:
```sh
ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194
```

When connected, start the VNC sever:
```sh
tightvncserver :1 -geometry 1920x1080
```

Start Remmina:
![[Images/Pasted image 20250425195617.png]]

Select VNC:
![[Images/Pasted image 20250425200057.png]]

enter `localhost:5901`
![[Images/Pasted image 20250425200220.png]]

log in with your selected password:
![[Images/Pasted image 20250425200403.png]]

Enter Full-screen mode
![[Images/Pasted image 20250425200551.png]]

We're in Kali GUI with a lot of tools!
![[Images/Pasted image 20250425200946.png]]

To exit full screen mode, move the mouse over the upper middle of the screen, over the white line, and it expands into a menu. Click Toggle Full Screen mode.
![[Images/Pasted image 20250425201357.png]]

### Connecting from Windows

Connect with ssh:
```sh
ssh -L 5901:localhost:5901 -i FixIt42-AWS-kali.pem kali@13.60.203.194
```

When connected, start the VNC sever:
```sh
tightvncserver :1 -geometry 1920x1080
```

RealVNC is a viewer on windows that can do full screen:
Download here: https://www.realvnc.com/en/connect/download/viewer/windows/

![[Images/Pasted image 20250425184622.png]]

![[Images/Pasted image 20250425184801.png]]

![[Images/Pasted image 20250425202132.png]]

![[Images/Pasted image 20250425202205.png]]

![[Images/Pasted image 20250425202247.png]]

![[Images/Pasted image 20250425202345.png]]

We're in Kali GUI with a lot of tools!
![[Images/Pasted image 20250425202524.png]]

To exit full screen mode, move the mouse over the upper middle of the screen, over the white line, and it expands into a menu. Click Toggle Full Screen mode.
![[Images/Pasted image 20250425202655.png]]

## RDP

### Installing, Configuring and Uninstalling the RDP service

Here we use -L ...

```sh
ssh -L 3390:localhost:3390 -i FixIt42-AWS-kali.pem kali@13.60.203.194
```

Install RDP:
```sh
sudo apt install xrdp
systemctl enable xrdp
#systemctl enable xrdp-sesman     #installed but later uninstalled and it still worked
```

![[Images/Pasted image 20250425211356.png]]

Since port 3389 will already be in use on windows machines and we might want to connect from windows, we need to change the port RDP uses:
```sh
sudo nano /etc/xrdp/xrdp.ini
```

![[Images/Pasted image 20250425211538.png]]
Edit the file and change `port=3389` to `port=3390`
Save and exit by pressing Ctrl + s x

```sh
sudo /etc/init.d/xrdp start
```

![[Images/Pasted image 20250425211922.png]]

### Connecting from Linux

Connect with ssh:
```sh
ssh -L 3390:localhost:3390 -i kali-key.pem kali@13.60.203.194
```

Start Remmina:
![[Images/Pasted image 20250425195617.png]]

![[Images/Pasted image 20250425215614.png]]

![[Images/Pasted image 20250425215707.png]]


![[Images/Pasted image 20250425215839.png]]

![[Images/Pasted image 20250425220108.png]]

![[Images/Pasted image 20250425221340.png]]

![[Images/Pasted image 20250425220238.png]]

We're in Kali GUI with a lot of tools!
![[Images/Pasted image 20250425221419.png]]

![[Images/Pasted image 20250425221732.png]]

### Connecting from Windows

Connect with ssh:
```sh
ssh -L 3390:localhost:3390 -i kali-key.pem kali@13.60.203.194
```

start Remote Desktop Connection:
![[Images/Pasted image 20250425214055.png]]

![[Images/Pasted image 20250425214151.png]]

![[Images/Pasted image 20250425214400.png]]

![[Images/Pasted image 20250425214528.png]]

![[Images/Pasted image 20250425214641.png]]

We're in Kali GUI with a lot of tools!
![[Images/Pasted image 20250425214737.png]]

Exit fullscreen here
![[Images/Pasted image 20250425214956.png]]


Free 
![[Images/Pasted image 20250424135604.png]]


nmap scan with RDP but not VNC running
```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p- -sC -sV -Pn 56.228.19.43
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-25 23:19 CEST
Nmap scan report for ec2-56-228-19-43.eu-north-1.compute.amazonaws.com (56.228.19.43)
Host is up (0.0035s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.9p2 Debian 2 (protocol 2.0)
| ssh-hostkey: 
|   256 6e:6a:73:81:68:59:c7:78:42:28:5b:ee:86:00:62:94 (ECDSA)
|_  256 b1:c0:7b:6d:cd:7a:07:ca:b8:59:cd:47:0e:a2:ab:fd (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 113.20 seconds
```

