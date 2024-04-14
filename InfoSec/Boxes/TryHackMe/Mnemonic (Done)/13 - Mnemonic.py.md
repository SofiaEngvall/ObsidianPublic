
```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ls -la                                        
total 184
drwxr-xr-x  3 kali kali   4096 Mar 25 11:04 .
drwxr-xr-x 11 kali kali   4096 Mar 20 10:03 ..
drwxrwxr-x  2 kali kali   4096 Mar 20 10:33 backups
-rw-r--r--  1 kali kali    409 Mar 20 10:00 backups.zip
-rw-------  1 kali kali   1766 Jul 13  2020 id_rsa
-rw-r--r--  1 kali kali 154514 Mar 25 11:04 maxresdefault.jpg
-rw-r--r--  1 kali kali     31 Jul 13  2020 not.txt
-rw-r--r--  1 kali kali   2458 Mar 20 11:24 sshhash
-rw-r--r--  1 kali kali    261 Mar 20 10:19 ziphash.txt
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ git clone https://github.com/MustafaTanguner/Mnemonic.git                                                            
Cloning into 'Mnemonic'...
remote: Enumerating objects: 193, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (51/51), done.
remote: Total 193 (delta 20), reused 1 (delta 0), pack-reused 141
Receiving objects: 100% (193/193), 6.78 MiB | 2.64 MiB/s, done.
Resolving deltas: 100% (88/88), done.
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ls -la
total 188
drwxr-xr-x  4 kali kali   4096 Mar 25 11:34 .
drwxr-xr-x 11 kali kali   4096 Mar 20 10:03 ..
drwxr-xr-x  5 kali kali   4096 Mar 25 11:34 Mnemonic
drwxrwxr-x  2 kali kali   4096 Mar 20 10:33 backups
-rw-r--r--  1 kali kali    409 Mar 20 10:00 backups.zip
-rw-------  1 kali kali   1766 Jul 13  2020 id_rsa
-rw-r--r--  1 kali kali 154514 Mar 25 11:04 maxresdefault.jpg
-rw-r--r--  1 kali kali     31 Jul 13  2020 not.txt
-rw-r--r--  1 kali kali   2458 Mar 20 11:24 sshhash
-rw-r--r--  1 kali kali    261 Mar 20 10:19 ziphash.txt
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cd Mnemonic        
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ ls -la
total 80
drwxr-xr-x 5 kali kali  4096 Mar 25 11:34 .
drwxr-xr-x 4 kali kali  4096 Mar 25 11:34 ..
drwxr-xr-x 8 kali kali  4096 Mar 25 11:34 .git
-rw-r--r-- 1 kali kali    32 Mar 25 11:34 .gitattributes
-rw-r--r-- 1 kali kali  1694 Mar 25 11:34 .gitignore
-rw-r--r-- 1 kali kali 35129 Mar 25 11:34 LICENSE
-rw-r--r-- 1 kali kali  6964 Mar 25 11:34 Mnemonic.py
-rw-r--r-- 1 kali kali   959 Mar 25 11:34 README.md
drwxr-xr-x 2 kali kali  4096 Mar 25 11:34 __pycache__
drwxr-xr-x 2 kali kali  4096 Mar 25 11:34 image
-rw-r--r-- 1 kali kali  1625 Mar 25 11:34 sozlukler.py
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ cd ..      
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ls -la
total 188
drwxr-xr-x  4 kali kali   4096 Mar 25 11:34 .
drwxr-xr-x 11 kali kali   4096 Mar 20 10:03 ..
drwxr-xr-x  5 kali kali   4096 Mar 25 11:34 Mnemonic
drwxrwxr-x  2 kali kali   4096 Mar 20 10:33 backups
-rw-r--r--  1 kali kali    409 Mar 20 10:00 backups.zip
-rw-------  1 kali kali   1766 Jul 13  2020 id_rsa
-rw-r--r--  1 kali kali 154514 Mar 25 11:04 maxresdefault.jpg
-rw-r--r--  1 kali kali     31 Jul 13  2020 not.txt
-rw-r--r--  1 kali kali   2458 Mar 20 11:24 sshhash
-rw-r--r--  1 kali kali    261 Mar 20 10:19 ziphash.txt
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ pip3 install colored                  
Defaulting to user installation because normal site-packages is not writeable
Collecting colored
  Downloading colored-2.2.4-py3-none-any.whl.metadata (3.6 kB)
Downloading colored-2.2.4-py3-none-any.whl (16 kB)
Installing collected packages: colored
Successfully installed colored-2.2.4
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ pip3 install opencv-python
Defaulting to user installation because normal site-packages is not writeable
Collecting opencv-python
  Downloading opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (20 kB)
Requirement already satisfied: numpy>=1.21.2 in /usr/lib/python3/dist-packages (from opencv-python) (1.24.2)
Downloading opencv_python-4.9.0.80-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (62.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.2/62.2 MB 8.2 MB/s eta 0:00:00
Installing collected packages: opencv-python
Successfully installed opencv-python-4.9.0.80
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ python3 ./Mnemonic/Mnemonic.py

                                                                                                                             
ooo        ooooo                                                                o8o                                          
`88.       .888'                                                                `"'                                          
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.                                
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8                               
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888                                     
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8                               
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P'                               
                                                                                                                             
                                                                                                                             
******************************* Welcome to Mnemonic Encryption Software *********************************
*********************************************************************************************************
***************************************** Author:@villwocki *********************************************
*********************************************************************************************************
****************************** https://www.youtube.com/watch?v=pBSR3DyobIY ******************************
---------------------------------------------------------------------------------------------------------


Access Code image file Path:./maxresdefault.jpg
File exists and is readable


Processing:0.txt'dir.


*************** PROCESS COMPLETED ***************
Traceback (most recent call last):
  File "/home/kali/thm/mnemonic/./Mnemonic/Mnemonic.py", line 132, in <module>
    f.write("%s" % item)
            ~~~~~^~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ python3 Mnemonic.py                               

                                                                                                                             
ooo        ooooo                                                                o8o                                          
`88.       .888'                                                                `"'                                          
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.                                
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8                               
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888                                     
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8                               
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P'                               
                                                                                                                             
                                                                                                                             
******************************* Welcome to Mnemonic Encryption Software *********************************
*********************************************************************************************************
***************************************** Author:@villwocki *********************************************
*********************************************************************************************************
****************************** https://www.youtube.com/watch?v=pBSR3DyobIY ******************************
---------------------------------------------------------------------------------------------------------


Access Code image file Path:../maxresdefault.jpg
File exists and is readable


Processing:0.txt'dir.


*************** PROCESS COMPLETED ***************
Traceback (most recent call last):
  File "/home/kali/thm/mnemonic/Mnemonic/Mnemonic.py", line 132, in <module>
    f.write("%s" % item)
            ~~~~~^~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ mv maxresdefault.jpg Mnemonic
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ls -la
total 44
drwxr-xr-x  4 kali kali 4096 Mar 25 12:04 .
drwxr-xr-x 11 kali kali 4096 Mar 20 10:03 ..
-rw-r--r--  1 kali kali    0 Mar 25 11:49 0.txt
drwxr-xr-x  5 kali kali 4096 Mar 25 12:04 Mnemonic
drwxrwxr-x  2 kali kali 4096 Mar 20 10:33 backups
-rw-r--r--  1 kali kali  409 Mar 20 10:00 backups.zip
-rw-------  1 kali kali 1766 Jul 13  2020 id_rsa
-rw-r--r--  1 kali kali   31 Jul 13  2020 not.txt
-rw-r--r--  1 kali kali   53 Mar 25 11:49 pixel.txt
-rw-r--r--  1 kali kali 2458 Mar 20 11:24 sshhash
-rw-r--r--  1 kali kali  153 Mar 25 11:49 veriler.txt
-rw-r--r--  1 kali kali  261 Mar 20 10:19 ziphash.txt
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cd Mnemonic 
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ ls -la
total 240
drwxr-xr-x 5 kali kali   4096 Mar 25 12:04 .
drwxr-xr-x 4 kali kali   4096 Mar 25 12:04 ..
drwxr-xr-x 8 kali kali   4096 Mar 25 11:34 .git
-rw-r--r-- 1 kali kali     32 Mar 25 11:34 .gitattributes
-rw-r--r-- 1 kali kali   1694 Mar 25 11:34 .gitignore
-rw-r--r-- 1 kali kali      0 Mar 25 12:01 0.txt
-rw-r--r-- 1 kali kali  35129 Mar 25 11:34 LICENSE
-rw-r--r-- 1 kali kali   6964 Mar 25 11:34 Mnemonic.py
-rw-r--r-- 1 kali kali    959 Mar 25 11:34 README.md
drwxr-xr-x 2 kali kali   4096 Mar 25 11:48 __pycache__
drwxr-xr-x 2 kali kali   4096 Mar 25 11:34 image
-rw-r--r-- 1 kali kali 154514 Mar 25 11:04 maxresdefault.jpg
-rw-r--r-- 1 kali kali     53 Mar 25 12:01 pixel.txt
-rw-r--r-- 1 kali kali   1625 Mar 25 11:34 sozlukler.py
-rw-r--r-- 1 kali kali    153 Mar 25 12:01 veriler.txt
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ python3 Mnemonic.py                               

                                                                                                                             
ooo        ooooo                                                                o8o                                          
`88.       .888'                                                                `"'                                          
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.                                
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8                               
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888                                     
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8                               
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P'                               
                                                                                                                             
                                                                                                                             
******************************* Welcome to Mnemonic Encryption Software *********************************
*********************************************************************************************************
***************************************** Author:@villwocki *********************************************
*********************************************************************************************************
****************************** https://www.youtube.com/watch?v=pBSR3DyobIY ******************************
---------------------------------------------------------------------------------------------------------


Access Code image file Path:maxresdefault.jpg
File exists and is readable


Processing:0.txt'dir.


*************** PROCESS COMPLETED ***************
Traceback (most recent call last):
  File "/home/kali/thm/mnemonic/Mnemonic/Mnemonic.py", line 132, in <module>
    f.write("%s" % item)
            ~~~~~^~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ python3 Mnemonic.py

                                                                                                                             
ooo        ooooo                                                                o8o                                          
`88.       .888'                                                                `"'                                          
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.                                
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8                               
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888                                     
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8                               
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P'                               
                                                                                                                             
                                                                                                                             
******************************* Welcome to Mnemonic Encryption Software *********************************
*********************************************************************************************************
***************************************** Author:@villwocki *********************************************
*********************************************************************************************************
****************************** https://www.youtube.com/watch?v=pBSR3DyobIY ******************************
---------------------------------------------------------------------------------------------------------


Access Code image file Path:qwerqwer
Either the file is missing or not readable
Access Code image file Path:^CTraceback (most recent call last):
  File "/home/kali/thm/mnemonic/Mnemonic/Mnemonic.py", line 35, in <module>
    gelen = input(colored("Access Code image file Path:",'cyan'))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

                                                                                                                             
┌──(kali㉿kali)-[~/thm/mnemonic/Mnemonic]
└─$ 

```