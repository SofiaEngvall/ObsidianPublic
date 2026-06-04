



```
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ unrar e object26

UNRAR 7.20 beta 2 freeware      Copyright (c) 1993-2025 Alexander Roshal

Unexpected end of archive
Extracting from object26

Enter password (will not be echoed) for TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png: 

The specified password is incorrect.
Enter password (will not be echoed) for TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png: 

Extracting  OPTI_CAM_01_OCRSCAN_000001.png                           100%
TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png - checksum error
Unexpected end of archive
Total errors: 3
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la
total 1096
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 12:41 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:27 ..
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ cat                          
^C
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ cat -h
cat: invalid option -- 'h'
Try 'cat --help' for more information.
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ cat --help
Usage: cat [OPTION]... [FILE]...
Concatenate FILE(s) to standard output.

With no FILE, or when FILE is -, read standard input.

  -A, --show-all           equivalent to -vET
  -b, --number-nonblank    number nonempty output lines, overrides -n
  -e                       equivalent to -vE
  -E, --show-ends          display $ at end of each line
  -n, --number             number all output lines
  -s, --squeeze-blank      suppress repeated empty output lines
  -t                       equivalent to -vT
  -T, --show-tabs          display TAB characters as ^I
  -u                       (ignored)
  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
      --help        display this help and exit
      --version     output version information and exit

Examples:
  cat f - g  Output f's contents, then standard input, then g's contents.
  cat        Copy standard input to standard output.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/cat>
or available locally via: info '(coreutils) cat invocation'
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la    
total 1096
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 12:41 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:27 ..
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ cat object26 object28 object35 object36 object38 object39 object48>object.rar
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la
total 1424
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 12:44 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:27 ..
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
-rw-rw-r-- 1 fixit42 fixit42 334179 Mar 21 12:44 object.rar
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ unrar e object.rar                                                           

UNRAR 7.20 beta 2 freeware      Copyright (c) 1993-2025 Alexander Roshal

Unexpected end of archive
Extracting from object.rar

Enter password (will not be echoed) for TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png: 

Extracting  OPTI_CAM_01_OCRSCAN_000001.png                           100%
TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png - checksum error
Unexpected end of archive
Total errors: 3
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la
total 2928
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 12:57 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:48 ..
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-rw-r-- 1 fixit42 fixit42 770285 Mar 21 12:21 KaptenStrang.pcap
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
-rw-rw-r-- 1 fixit42 fixit42 334179 Mar 21 12:44 object.rar
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:57 raw.data
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ grep -oba 'Rar!' dump.bin                                   
grep: dump.bin: No such file or directory
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ grep -oba 'Rar!' raw.data
2988:Rar!
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ dd if=raw.data of=clean.rar bs=1 skip=12345
753226+0 records in
753226+0 records out
753226 bytes (753 kB, 736 KiB) copied, 1.83761 s, 410 kB/s
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ dd if=raw.data of=clean.rar bs=1 skip=2988
762583+0 records in
762583+0 records out
762583 bytes (763 kB, 745 KiB) copied, 1.85727 s, 411 kB/s
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ unrar t clean.rar

UNRAR 7.20 beta 2 freeware      Copyright (c) 1993-2025 Alexander Roshal

Testing archive clean.rar

Enter password (will not be echoed) for TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png: 

Testing     TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png                      OK 
FROM_HQ/PRIO_UPPDRAG_HK.txt - use current password? [Y]es, [N]o, [A]ll y

Testing     FROM_HQ/PRIO_UPPDRAG_HK.txt                               OK 
Testing     TO_HQ                                                     OK
Testing     FROM_HQ                                                   OK
All OK
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la
total 3676
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 13:00 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:48 ..
-rw-rw-r-- 1 fixit42 fixit42 762583 Mar 21 13:01 clean.rar
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-rw-r-- 1 fixit42 fixit42 770285 Mar 21 12:21 KaptenStrang.pcap
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
-rw-rw-r-- 1 fixit42 fixit42 334179 Mar 21 12:44 object.rar
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:57 raw.data
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ unrar e clean.rar

UNRAR 7.20 beta 2 freeware      Copyright (c) 1993-2025 Alexander Roshal

Extracting from clean.rar

Enter password (will not be echoed) for TO_HQ/OPTI_CAM_01_OCRSCAN_000001.png: 

Extracting  OPTI_CAM_01_OCRSCAN_000001.png                            OK 
FROM_HQ/PRIO_UPPDRAG_HK.txt - use current password? [Y]es, [N]o, [A]ll y

Extracting  PRIO_UPPDRAG_HK.txt                                       OK 
All OK
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ ls -la
total 4432
drwxrwxr-x 2 fixit42 fixit42   4096 Mar 21 13:02 .
drwxr-xr-x 7 fixit42 fixit42   4096 Mar 21 12:48 ..
-rw-rw-r-- 1 fixit42 fixit42 762583 Mar 21 13:01 clean.rar
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:33 file.rar
-rw-rw-r-- 1 fixit42 fixit42    106 Mar 21 12:39 hash
-rw-rw-r-- 1 fixit42 fixit42 770285 Mar 21 12:21 KaptenStrang.pcap
-rw-r--r-- 1 fixit42 fixit42  46616 Mar 21 12:27 object26
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object28
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object35
-rw-r--r-- 1 fixit42 fixit42  43776 Mar 21 12:27 object36
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object38
-rw-r--r-- 1 fixit42 fixit42  25269 Mar 21 12:27 object39
-rw-r--r-- 1 fixit42 fixit42  65483 Mar 21 12:27 object48
-rw-rw-r-- 1 fixit42 fixit42 334179 Mar 21 12:44 object.rar
-rw-rw-r-- 1 fixit42 fixit42 766805 Jan 21 18:17 OPTI_CAM_01_OCRSCAN_000001.png
-rw-rw-r-- 1 fixit42 fixit42   1700 Jan  8 21:18 PRIO_UPPDRAG_HK.txt
-rw-rw-r-- 1 fixit42 fixit42 765571 Mar 21 12:57 raw.data
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut]
└─$ exiftool OPTI_CAM_01_OCRSCAN_000001.png 
ExifTool Version Number         : 13.36
File Name                       : OPTI_CAM_01_OCRSCAN_000001.png
Directory                       : .
File Size                       : 767 kB
File Modification Date/Time     : 2026:01:21 18:17:28+01:00
File Access Date/Time           : 2026:03:21 13:03:03+01:00
File Inode Change Date/Time     : 2026:03:21 13:02:40+01:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1024
Image Height                    : 559
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Optics pov frame                : undut{periskopdjup_-8m}
Image Size                      : 1024x559
Megapixels                      : 0.572

```