
![[Pasted image 20231014160549.png|600]]
5 GHz can't pass through walls as well as 2.4
2.4GHz, 14 channels, 1-11 in us. 1, 6 & 11 most common.
5 more channels



ip a

iwconfig

sudo airmon-ng start wlan0

iwconfig

sudo airmon-ng

sudo airodump-ng wlan0mon
a to tab through filters
	sta = devices connected to the aps
	station = mac of device
	bssid = where it is connected
	

test for packet injection
sudo aireplay-ng --test wlan0mon


