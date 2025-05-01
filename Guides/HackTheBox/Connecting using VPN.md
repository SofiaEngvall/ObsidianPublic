
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
