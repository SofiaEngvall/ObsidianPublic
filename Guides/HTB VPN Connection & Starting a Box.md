
## How to download a VPN file from HackTheBox

### If you're taking part of a meetup

Just click the buttons in the images

![[Images/Pasted image 20250429001917.png]]

![[Images/Pasted image 20250429002003.png]]

![[Images/Pasted image 20250429002313.png]]

![[Images/Pasted image 20250429002354.png]]
Select a suitable VPN
*Save the file where you can find it later*

### If you're doing Labs

Just click the buttons in the images

![[Images/Pasted image 20250429001917.png]]

![[Images/Pasted image 20250429002201.png]]

![[Images/Pasted image 20250429002246.png]]

![[Images/Pasted image 20250429002616.png]]
Select a suitable VPN
*Save the file where you can find it later*

## Starting the VPN (on Linux)

Got to where you saved your VPN file
```sh
┌──(kali㉿proxli)-[~/vpn]
└─$ ls -la *.ovpn
-rw-r--r-- 1 kali kali 3375 Apr 29 00:32 Dedicated_Lab_FixIt42.ovpn
-rw-r--r-- 1 kali kali 3343 Apr 29 00:12 lab_FixIt42.ovpn
```

Start openvpn like this using your files name
```sh
┌──(kali㉿proxli)-[~/vpn]
└─$ sudo openvpn lab_FixIt42.ovpn
[sudo] password for kali: 
```
A lot off text will appear. As long as you don't get any error messages or the program closes you're all good.
Keep this terminal open as long as you want to be connected to HackTheBox.

## Starting a Box

### If you're taking part of a meetup

Click the Meetup
![[Images/Pasted image 20250429004416.png]]

Click LAB
![[Images/Pasted image 20250429004515.png]]

Click PLAY on your selected machine
![[Images/Pasted image 20250429004648.png]]

Spawn your machine
![[Images/Pasted image 20250429004903.png]]
*Since this is a machine only for you it will take some time to start!*

![[Images/Pasted image 20250429010009.png]]
And you're ready to start hacking!
*Follow the questions in Guided mode for hints*

### If you're doing Labs

Click machines for a list or
![[Images/Pasted image 20250429005338.png]]
search
![[Images/Pasted image 20250429005420.png]]

When you have chosen a machine, Join
![[Images/Pasted image 20250429005541.png]]

And ready to start hacking!
*Follow the questions in Guided mode for hints*
![[Images/Pasted image 20250429005654.png]]

