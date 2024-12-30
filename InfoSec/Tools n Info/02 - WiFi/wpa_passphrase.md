
```sh
┌──(kali㉿kali)-[~/wifi-test]
└─$ wpa_passphrase phone 'qwerty123'         
network={
        ssid="phone"
        #psk="qwerty123"
        psk=45e6b2f43fa6a4e8b7565b326c3135c0b9b071b9febf045cb475ad511f15a541
}
```

### Help

```sh
WPA_PASSPHRASE(8)                                                                                          WPA_PASSPHRASE(8)

NAME
       wpa_passphrase - Generate a WPA PSK from an ASCII passphrase for a SSID

SYNOPSIS
       wpa_passphrase [ ssid ] [ passphrase ]

OVERVIEW
       wpa_passphrase  pre-computes  PSK  entries  for  network configuration blocks of a wpa_supplicant.conf file. An ASCII
       passphrase and SSID are used to generate a 256-bit PSK.

OPTIONS
       ssid   The SSID whose passphrase should be derived.

       passphrase
              The passphrase to use. If not included on the command line, passphrase will be read from standard input.

SEE ALSO
       wpa_supplicant.conf(5) wpa_supplicant(8)
```