
Arris NVG468Q
similar Frontier FiOS Arris NVG468MQ

Broadcom BCM963148

https://fccid.io/GZ5NVG4XXQ/User-Manual/Users-Manual-NVG468MQ-pdf-3005771
https://www.amazon.com/NVG468MQ-802-11ac-MoCA%C2%AE2-0-Frontier-Wireless-AC/dp/B073F17BSG
https://oldwiki.archive.openwrt.org/doc/techref/bootloader/cfe
https://www.commscope.com/contact-us/contact-arris/ - might have firmware


```sh
┌──(kali㉿kali)-[~/shells]
└─$ lsusb 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 002: ID 0e0f:0003 VMware, Inc. Virtual Mouse
Bus 002 Device 003: ID 0e0f:0002 VMware, Inc. Virtual USB Hub
Bus 002 Device 004: ID 0e0f:0008 VMware, Inc. Virtual Bluetooth Adapter
Bus 002 Device 005: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
```

```sh
┌──(kali㉿kali)-[~/shells]
└─$ dmesg | grep tty
[    0.729617] printk: legacy console [tty0] enabled
[    4.448031] 00:05: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    8.275148] systemd[1]: Created slice system-getty.slice - Slice /system/getty.
[17391.962803] usb 2-2.2: cp210x converter now attached to ttyUSB0
```

the cp210x is on ttyUSB0 so we're using the command `screen /dev/ttyUSB0 115200`

### Connection with screen

```sh
┌──(kali㉿kali)-[~/hw]
└─$ script -f 1.log           
Script started, output log file is '1.log'.

┌──(kali㉿kali)-[~/hw]
└─$ screen /dev/ttyUSB0 115200
[screen is terminating]

┌──(kali㉿kali)-[~/hw]
└─$ exit
Script done.

┌──(kali㉿kali)-[~/hw]
└─$ ls -la
total 48
drwxrwxr-x  2 kali kali  4096 Dec  4 22:36 .
drwx------ 60 kali kali  4096 Dec  4 22:55 ..
-rw-rw-r--  1 kali kali 38580 Dec  4 22:55 1.log
```

The output file [[1.log]]

`-Logfile [file]` to make screen log stuff, might need L

What I don't like about screen is that we can't scroll up

### Connecting with minicom

```sh
┌──(kali㉿kali)-[~/hw]
└─$ minicom -D /dev/ttyUSB0 -b 115200

Welcome to minicom 2.9

...
```

Ctrl+A, X to exit minicom

We can also tee it like to get a logfile:
```sh
┌──(kali㉿kali)-[~/hw]
└─$ minicom -D /dev/ttyUSB0 -b 115200 | tee 2.log

```


Info when starting:
```sh
Base: 5.2_05p1
CFE version 1.0.38-163.181 for BCM963148 (32bit,SP,LE)
Build Date: Tue Aug 20 18:50:03 EDT 2019 (fwbuild@itoengbld01)
Copyright (C) 2000-2015 Broadcom Corporation.

Boot Strap Register:  0x7ffff42f
Chip ID: BCM63149_A1, Broadcom B15 Dual Core: 1500MHz
Total Memory: 536870912 bytes (512MB)
NAND ECC BCH-4, page size 0x800 bytes, spare size used 64 bytes
NAND flash device: Spansion S34ML01G1, id 0x01f1 block 128KB size 131072KB
pmc_init:PMC using DQM mode
Board IP address                  : 192.168.1.254:ffffff00  
Host IP address                   : 192.168.1.100  
Gateway IP address                :   
Run from flash/host/tftp (f/h/c)  : f  
Default host run file name        : vmlinux  
Default host flash file name      : bcm963xx_fs_kernel  
Boot delay (0-9 seconds)          : 1  
Boot image (0=latest, 1=previous) : 0  
Default host ramdisk file name    :   
Default ramdisk store address     :   
Default DTB file name             :   
Board Id                          : NVG468Q  
Number of MAC Addresses (1-64)    : 11  
Base MAC Address                  : 02:13:80:01:5e:10  
PSI Size (1-512) KBytes           : 48  
Enable Backup PSI [0|1]           : 0  
System Log Size (0-256) KBytes    : 0  
Auxillary File System Size Percent: 0  
MC memory allocation (MB)         : 4  
TM memory allocation (MB)         : 20  
DHD 0 memory allocation (MB)      : 0  
DHD 1 memory allocation (MB)      : 0  
DHD 2 memory allocation (MB)      : 0  
WLan Feature                      : 0x02  
Voice Board Configuration (0-53)  : LE9642_ZSI_BB  
Partition 1 Size (MB)             : 0M  
Partition 2 Size (MB)             : 0M  
Partition 3 Size (MB)             : 0M  
Partition 4 Size (MB) (Data)      : 32M 
```


### Bootloader

When we press enter just when the device boots we get a CFE-prompt.

[[CFE]]

