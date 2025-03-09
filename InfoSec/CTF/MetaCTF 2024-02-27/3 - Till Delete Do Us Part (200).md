(solved by 155 teams)

I was messing with trying to dual boot, and while trying to fix partitions, I accidentally deleted the one on my wedding flash drive I carelessly had plugged in! Please help me recover it!

Download the artifact [here.](https://metaproblems.com/dba7388405074d8329a71f18f2beef8c/usb.zip)

---

```sh
──(kali㉿kali)-[~/Downloads/usb]
└─$ unzip usb            
Archive:  usb.zip
  inflating: usb.img
  
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ ls -la
total 264444
drwxrwxr-x 2 kali kali      4096 Feb 27 23:29 .
drwxr-xr-x 6 kali kali     77824 Feb 27 23:29 ..
-rw-r--r-- 1 kali kali 268435456 Feb 27 19:54 usb.img
-rw-rw-r-- 1 kali kali   2262733 Feb 27 23:29 usb.zip
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ binwalk usb.img -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
5182976       0x4F1600        Zip archive data, at least v2.0 to extract, compressed size: 149, uncompressed size: 205, name: docProps/app.xml
5183171       0x4F16C3        Zip archive data, at least v2.0 to extract, compressed size: 239, uncompressed size: 555, name: docProps/core.xml
5183457       0x4F17E1        Zip archive data, at least v2.0 to extract, compressed size: 1552, uncompressed size: 10140, name: xl/theme/theme1.xml
5185058       0x4F1E22        Zip archive data, at least v2.0 to extract, compressed size: 446, uncompressed size: 1160, name: xl/worksheets/sheet1.xml
5185558       0x4F2016        Zip archive data, at least v2.0 to extract, compressed size: 593, uncompressed size: 2550, name: xl/styles.xml
5186194       0x4F2292        Zip archive data, at least v2.0 to extract, compressed size: 192, uncompressed size: 531, name: _rels/.rels
5186427       0x4F237B        Zip archive data, at least v2.0 to extract, compressed size: 314, uncompressed size: 555, name: xl/workbook.xml
5186786       0x4F24E2        Zip archive data, at least v2.0 to extract, compressed size: 173, uncompressed size: 504, name: xl/_rels/workbook.xml.rels
5187015       0x4F25C7        Zip archive data, at least v2.0 to extract, compressed size: 281, uncompressed size: 975, name: [Content_Types].xml
5188096       0x4F2A00        Zip archive data, at least v2.0 to extract, compressed size: 405, uncompressed size: 1738, name: [Content_Types].xml
5188550       0x4F2BC6        Zip archive data, at least v2.0 to extract, compressed size: 248, uncompressed size: 734, name: _rels/.rels
5188839       0x4F2CE7        Zip archive data, at least v2.0 to extract, compressed size: 361, uncompressed size: 721, name: docProps/core.xml
5189247       0x4F2E7F        Zip archive data, at least v2.0 to extract, compressed size: 491, uncompressed size: 1132, name: docProps/app.xml
5189784       0x4F3098        Zip archive data, at least v2.0 to extract, compressed size: 647, uncompressed size: 1809, name: word/document.xml
5190478       0x4F334E        Zip archive data, at least v2.0 to extract, compressed size: 306, uncompressed size: 1227, name: word/_rels/document.xml.rels
5190842       0x4F34BA        Zip archive data, at least v2.0 to extract, compressed size: 12147, uncompressed size: 349458, name: word/styles.xml
5203034       0x4F645A        Zip archive data, at least v2.0 to extract, compressed size: 13625, uncompressed size: 438131, name: word/stylesWithEffects.xml
5216715       0x4F99CB        Zip archive data, at least v2.0 to extract, compressed size: 959, uncompressed size: 2535, name: word/settings.xml
5217721       0x4F9DB9        Zip archive data, at least v2.0 to extract, compressed size: 256, uncompressed size: 438, name: word/webSettings.xml
5218027       0x4F9EEB        Zip archive data, at least v2.0 to extract, compressed size: 611, uncompressed size: 2811, name: word/fontTable.xml
5218686       0x4FA17E        Zip archive data, at least v2.0 to extract, compressed size: 1734, uncompressed size: 10939, name: word/theme/theme1.xml
5220471       0x4FA877        Zip archive data, at least v2.0 to extract, compressed size: 167, uncompressed size: 262, name: customXml/item1.xml
5220687       0x4FA94F        Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 295, name: customXml/_rels/item1.xml.rels
5220936       0x4FAA48        Zip archive data, at least v2.0 to extract, compressed size: 225, uncompressed size: 354, name: customXml/itemProps1.xml
5221215       0x4FAB5F        Zip archive data, at least v2.0 to extract, compressed size: 875, uncompressed size: 5513, name: word/numbering.xml
5222138       0x4FAEFA        Zip archive data, at least v2.0 to extract, compressed size: 1469, uncompressed size: 8324, name: docProps/thumbnail.jpeg
5224960       0x4FBA00        Zip archive data, at least v2.0 to extract, compressed size: 405, uncompressed size: 1738, name: [Content_Types].xml
5225414       0x4FBBC6        Zip archive data, at least v2.0 to extract, compressed size: 248, uncompressed size: 734, name: _rels/.rels
5225703       0x4FBCE7        Zip archive data, at least v2.0 to extract, compressed size: 361, uncompressed size: 721, name: docProps/core.xml
5226111       0x4FBE7F        Zip archive data, at least v2.0 to extract, compressed size: 491, uncompressed size: 1132, name: docProps/app.xml
5226648       0x4FC098        Zip archive data, at least v2.0 to extract, compressed size: 621, uncompressed size: 1760, name: word/document.xml
5227316       0x4FC334        Zip archive data, at least v2.0 to extract, compressed size: 306, uncompressed size: 1227, name: word/_rels/document.xml.rels
5227680       0x4FC4A0        Zip archive data, at least v2.0 to extract, compressed size: 12147, uncompressed size: 349458, name: word/styles.xml
5239872       0x4FF440        Zip archive data, at least v2.0 to extract, compressed size: 13625, uncompressed size: 438131, name: word/stylesWithEffects.xml
5253553       0x5029B1        Zip archive data, at least v2.0 to extract, compressed size: 959, uncompressed size: 2535, name: word/settings.xml
5254559       0x502D9F        Zip archive data, at least v2.0 to extract, compressed size: 256, uncompressed size: 438, name: word/webSettings.xml
5254865       0x502ED1        Zip archive data, at least v2.0 to extract, compressed size: 611, uncompressed size: 2811, name: word/fontTable.xml
5255524       0x503164        Zip archive data, at least v2.0 to extract, compressed size: 1734, uncompressed size: 10939, name: word/theme/theme1.xml
5257309       0x50385D        Zip archive data, at least v2.0 to extract, compressed size: 167, uncompressed size: 262, name: customXml/item1.xml
5257525       0x503935        Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 295, name: customXml/_rels/item1.xml.rels
5257774       0x503A2E        Zip archive data, at least v2.0 to extract, compressed size: 225, uncompressed size: 354, name: customXml/itemProps1.xml
5258053       0x503B45        Zip archive data, at least v2.0 to extract, compressed size: 875, uncompressed size: 5513, name: word/numbering.xml
5258976       0x503EE0        Zip archive data, at least v2.0 to extract, compressed size: 1469, uncompressed size: 8324, name: docProps/thumbnail.jpeg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ grep -ri "MetaCTF" .         
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ strings usb.img | grep -i "MetaCTF"
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ strings usb.img      
mkfs.fat
NO NAME    FAT32   
This is not a bootable disk.  Please insert a bootable floppy and
press any key to try again ... 
RRaA
rrAa
mkfs.fat
NO NAME    FAT32   
This is not a bootable disk.  Please insert a bootable floppy and
press any key to try again ... 
RRaA
rrAa}
WEDDIN~1   
[Z[Z
DOCUME~1   
[Z[Z
INVITES    
[Z[Z
RECEIPTS   
[Z[Z
MUSIC      
[Z[Z
VOWS       
[Z[Z
BACKUP     
[Z[Z
.          
[Z[Z
..         
[Z[Z
HOTO_1 JPG 
[Z[Z
PHOTO_2 JPG 
PHOTO_3 JPG 
PHOTO_4 JPG 
COVER   JPG 
.          
[Z[Z
..         
[Z[Z
URPRISETXT 
[Z[Z
.          
[Z[Z
..         
[Z[Z
WEDDIN~1TXT 
.          
[Z[Z
..         
[Z[Z
AKE    TXT 
[Z[Z
FINAL_~1XLS 
.          
[Z[Z
..         
[Z[Z
PLAYLISTTXT 
.          
[Z[Z
..         
[Z[Z
ALICE_~1DOC 
[Z6X
BOB_VO~1DOC 
[Z0V
(0V]
.          
[Z[Z
..         
[Z[Z
Dear Friends and Family,
We are thrilled to invite you to celebrate our wedding!
Join us on our special day:
Date: June 24, 2024
Time: 4:00 PM
Location: Sunset Beach Resort
RSVP by May 10, 2024
With love, Alice & Bob
b[ZF
docProps/app.xmlM
?nyy
.Fgu
docProps/core.xml
2'|n
g<@P
z%x-
xl/theme/theme1.xml
Gd`}^,h@
```
...
```sh
D8_/m
1. Perfect - Ed Sheeran
2. A Thousand Years - Christina Perri
3. Can't Help Falling in Love - Elvis Presley
4. You Are the Best Thing - Ray LaMontagne
.          
[Z[Z
..         
[Z[Z
CTF        
[Z[Z
META~1     
[Z[Z
.          
[Z[Z
..         
[Z[Z
{N         
[Z[Z
.          
[Z[Z
..         
[Z[Z
0          
[Z[Z
.          
[Z[Z
..         
[Z[Z
T          
[Z[Z
.          
[Z[Z
..         
[Z[Z
_          
[Z[Z
.          
[Z[Z
..         
[Z[Z
EV         
[Z[Z
.          
[Z[Z
..         
[Z[Z
3N         
[Z[Z
.          
[Z[Z
..         
[Z[Z
_          
[Z[Z
.          
[Z[Z
..         
[Z[Z
D3         
[Z[Z
.          
[Z[Z
..         
[Z[Z
L3T        
[Z[Z
.          
[Z[Z
..         
[Z[Z
10N        
[Z[Z
.          
[Z[Z
..         
[Z[Z
_          
[Z[Z
.          
[Z[Z
..         
[Z[Z
C4         
[Z[Z
.          
[Z[Z
..         
[Z[Z
N          
[Z[Z
.          
[Z[Z
..         
[Z[Z
_          
[Z[Z
.          
[Z[Z
..         
[Z[Z
S3         
[Z[Z
.          
[Z[Z
..         
[Z[Z
PART       
[Z[Z
.          
[Z[Z
..         
[Z[Z
3_         
[Z[Z
.          
[Z[Z
..         
[Z[Z
U          
[Z[Z
.          
[Z[Z
..         
[Z[Z
5}         
[Z[Z
.          
[Z[Z
..         
[Z[Z
CLUE    TXT 
Our path to marriage was filed with countless green flags
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ file usb.img    
usb.img: DOS/MBR boot sector
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ mkdir mount

┌──(kali㉿kali)-[~/Downloads/usb]
└─$  sudo mount -r usb.img mount/
mount: /home/kali/Downloads/usb/mount: wrong fs type, bad option, bad superblock on /dev/loop0, missing codepage or helper program, or other error.
       dmesg(1) may have more information after failed mount system call.
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ fdisk -l usb.img 
Disk usb.img: 256 MiB, 268435456 bytes, 524288 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xf4fa0c7e
```
There's no partition.

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ testdisk usb.img              
TestDisk 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org
You have to reboot for the change to take effect.
```
Opens gui were the logical choices restores the partition.

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ fdisk -l usb.img
Disk usb.img: 256 MiB, 268435456 bytes, 524288 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xf4fa0c7e

Device     Boot Start    End Sectors  Size Id Type
usb.img1   *     2048 524287  522240  255M  b W95 FAT32
```
We got the deleted partition back. We just need to read it.

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ sudo kpartx -av usb.img
add map loop1p1 (254:0): 0 522240 linear 7:1 2048
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ sudo mount /dev/mapper/loop1p1 mount
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb]
└─$ cd mount      

┌──(kali㉿kali)-[~/Downloads/usb/mount]
└─$ ls -la
total 9
drwxr-xr-x 10 root root 1024 Jan  1  1970 .
drwxrwxr-x  4 kali kali 4096 Feb 27 23:36 ..
drwxr-xr-x  3 root root  512 Feb 27 18:21 .Meta
drwxr-xr-x  2 root root  512 Feb 27 18:21 Backup
drwxr-xr-x  2 root root  512 Feb 27 18:21 Documents
drwxr-xr-x  2 root root  512 Feb 27 18:21 Invites
drwxr-xr-x  2 root root  512 Feb 27 18:21 Music
drwxr-xr-x  2 root root  512 Feb 27 18:21 Receipts
drwxr-xr-x  2 root root  512 Feb 27 18:21 Vows
drwxr-xr-x  2 root root  512 Feb 27 18:21 Wedding_Photos
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb/mount]
└─$ cd .Meta 

┌──(kali㉿kali)-[~/Downloads/usb/mount/.Meta]
└─$ ls -la
total 2
drwxr-xr-x  3 root root  512 Feb 27 18:21 .
drwxr-xr-x 10 root root 1024 Jan  1  1970 ..
drwxr-xr-x  3 root root  512 Feb 27 18:21 CTF

┌──(kali㉿kali)-[~/Downloads/usb/mount/.Meta]
└─$ cd ctf

┌──(kali㉿kali)-[~/…/usb/mount/.Meta/ctf]
└─$ ls -la
total 2
drwxr-xr-x 3 root root 512 Feb 27 18:21 .
drwxr-xr-x 3 root root 512 Feb 27 18:21 ..
drwxr-xr-x 3 root root 512 Feb 27 18:21 {n
```

```sh
.Meta]
└─$ tree
.
└── CTF
    └── {n
        └── 0
            └── t
                └── _
                    └── ev
                        └── 3n
                            └── _
                                └── d3
                                    └── l3t
                                        └── 10n
                                            └── _
                                                └── c4
                                                    └── n
                                                        └── _
                                                            └── s3
                                                                └── part
                                                                    └── 3_
                                                                        └── u
                                                                            └── 5}
                                                                                └── clue.txt

21 directories, 1 file
```

```sh
┌──(kali㉿kali)-[~/Downloads/usb/mount/.Meta]
└─$ find . -name clue.txt -exec ls -la {} \; 2> /dev/null
-rwxr-xr-x 1 root root 57 Dec 18  2023 ./CTF/{n/0/t/_/ev/3n/_/d3/l3t/10n/_/c4/n/_/s3/part/3_/u/5}/clue.txt
```

`MetaCTF{n0t_ev3n_d3l3t10n_c4n_s3part3_u5}`

