
```sh
┌──(kali㉿kali)-[~/asm]
└─$ ssh ctf-player@venus.picoctf.net -p 57483
The authenticity of host '[venus.picoctf.net]:57483 ([3.131.124.143]:57483)' can't be established.
ED25519 key fingerprint is SHA256:P1f6h95BrSVnJbm2AKhphfHHGEyAeThib/rN/AwKs24.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[venus.picoctf.net]:57483' (ED25519) to the list of known hosts.
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls -la
total 16
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 .
drwxr-xr-x 1 ctf-player ctf-player 4096 Aug  5 21:10 ..
-rw-r--r-- 1 ctf-player ctf-player   14 Mar 16  2021 1of3.flag.txt
-rw-r--r-- 1 ctf-player ctf-player   56 Mar 16  2021 instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls -la
total 92
drwxr-xr-x   1 root root 4096 Aug  5 21:09 .
drwxr-xr-x   1 root root 4096 Aug  5 21:09 ..
-rwxr-xr-x   1 root root    0 Aug  5 21:09 .dockerenv
-rw-r--r--   1 root root   17 Mar 16  2021 2of3.flag.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Aug  5 21:09 dev
drwxr-xr-x   1 root root 4096 Aug  5 21:09 etc
drwxr-xr-x   1 root root 4096 Mar 16  2021 home
-rw-r--r--   1 root root   51 Mar 16  2021 instructions-to-3of3.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 lib
drwxr-xr-x   2 root root 4096 Feb 22  2021 lib64
drwxr-xr-x   2 root root 4096 Feb 22  2021 media
drwxr-xr-x   2 root root 4096 Feb 22  2021 mnt
drwxr-xr-x   1 root root 4096 Mar 16  2021 opt
dr-xr-xr-x 182 root root    0 Aug  5 21:09 proc
drwx------   2 root root 4096 Feb 22  2021 root
drwxr-xr-x   1 root root 4096 Aug  5 21:10 run
drwxr-xr-x   1 root root 4096 Mar 16  2021 sbin
drwxr-xr-x   2 root root 4096 Feb 22  2021 srv
dr-xr-xr-x  13 root root    0 Aug  5 21:09 sys
drwxrwxrwt   1 root root 4096 Mar 16  2021 tmp
drwxr-xr-x   1 root root 4096 Feb 22  2021 usr
drwxr-xr-x   1 root root 4096 Feb 22  2021 var
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls -la
total 32
drwxr-xr-x 1 ctf-player ctf-player 4096 Aug  5 21:10 .
drwxr-xr-x 1 root       root       4096 Mar 16  2021 ..
drwx------ 2 ctf-player ctf-player 4096 Aug  5 21:10 .cache
-rw-r--r-- 1 ctf-player ctf-player   80 Mar 16  2021 .profile
drw------- 1 ctf-player ctf-player 4096 Mar 16  2021 .ssh
-rw-r--r-- 1 ctf-player ctf-player   10 Mar 16  2021 3of3.flag.txt
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 
5190b070}
ctf-player@pico-chall$ Connection to venus.picoctf.net closed by remote host.
Connection to venus.picoctf.net closed.



```sh
┌──(kali㉿kali)-[~/asm]
└─$ ssh -p 54193 ctf-player@rhea.picoctf.net
The authenticity of host '[rhea.picoctf.net]:54193 ([3.136.191.228]:54193)' can´t be established.
ED25519 key fingerprint is SHA256:QKdv+RGJL0UYRDM66IiGQ5dsXOX7DQFqB7umTylh+IU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[rhea.picoctf.net]:54193' (ED25519) to the list of known hosts.
ctf-player@rhea.picoctf.net's password: 
Permission denied, please try again.
ctf-player@rhea.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls -la
total 20
drwxr-xr-x 3 ctf-player ctf-player   57 Mar  9 17:05 .
drwxr-xr-x 1 ctf-player ctf-player   20 Aug  5 21:16 ..
-rw-r--r-- 1 root       root         65 Mar  9 17:05 checksum.txt
-rwxr-xr-x 1 root       root        856 Mar  9 17:05 decrypt.sh
drwxr-xr-x 2 ctf-player ctf-player 8192 Mar  9 17:05 files
ctf-player@pico-chall$ cat checksum.txt 
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
ctf-player@pico-chall$ cat decrypt.sh 

        #!/bin/bash

        # Check if the user provided a file name as an argument
        if [ $# -eq 0 ]; then
            echo "Expected usage: decrypt.sh <filename>"
            exit 1
        fi

        # Store the provided filename in a variable
        file_name="$1"

        # Check if the provided argument is a file and not a folder
        if [ ! -f "/home/ctf-player/drop-in/$file_name" ]; then
            echo "Error: '$file_name' is not a valid file. Look inside the 'files' folder with 'ls -R'!"
            exit 1
        fi

        # If there´s an error reading the file, print an error message
        if ! openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF; then
            echo "Error: Failed to decrypt '$file_name'. This flag is fake! Keep looking!"
        fi
        ctf-player@pico-chall$ 
ctf-player@pico-chall$ ls -la files/*
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/00011a60
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/022cvpdN
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/04nLilRD
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0MT2Wrui
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0SGMttmR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0fCDySFB
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0hHVJSPh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0mPyFlda
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/0xknvebh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/1kTWMoOI
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/1mGlW6Ts
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2JKdkggW
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2Jr8UtbZ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2K4XCmfE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2MYWkWLC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2QpRnoZQ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2emuPVOb
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2gP5wDgq
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2w5vJlLG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/2yMtx5qd
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/303DzMmf
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/33CFCJ0y
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/36tjTWoF
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/3KZwXc8s
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/3Vs8v8kW
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/3qDKN57P
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/4CwloraZ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/4XqPqs6B
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/4k4veVKp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/4sczhCZl
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/58BnWcOc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/5bSdd2sp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/5gxjbRbh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/5rHRNllE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/63MqIIVV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/64nJlBLv
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/69JSHBh1
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/6vgioqew
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/76rj6cv7
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/7j2g9w9w
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/7ye3lPVb
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/870YaC5g
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/8Shyigig
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/8d0Ncqme
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/8hKIvq38
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/8rIuGenM
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/91cLOGeN
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/9DNfzhUK
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/9KIFXofB
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/9pluLfgA
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ADMuzktV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AEJxVlNY
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AGOEyD4N
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AVdbk5eX
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AXFWLqwI
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AdzCNBlC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AiUxYmz8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/AmsN0Lkj
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ArUDDIQ3
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Azqf6EEw
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/B8pBCEvG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/BN0HxLxE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/BOeN3lXR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/BdO65Tk4
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Bh5xju3q
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/C1kYNpjq
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/CF4c5xR8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/CGkVyMxT
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/CLCyTz85
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/CNvsyU3W
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Cb22Z7FO
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Ce5TrzJu
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ClWGbsxu
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/DCn7KnqG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/DSKHZ66z
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Dmsex2Ug
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/EBBoQm7M
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/EG1lW2KR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/EXQ6DiO5
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/F6yHlWpt
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/FJBePm2b
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/FLsBEmlR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/FOxKdaVP
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/FtMorZ65
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/G7enzzui
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Gcv1H8Qs
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/GhrShrXN
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Gtk4Kn9w
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/GufDk3Mb
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HDLWGApz
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HIeYL84k
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HJIPzwjJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HMq6348V
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HUjCgnh4
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HWRVc59e
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Hmr54gXd
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/HqxLJgMp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/IDQQR4nq
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/IITtRrrR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/IbMiqCHJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Ie0xOcl5
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/IikIpp05
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/IlQwVZcY
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ItYR0Da2
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Izq2bmb5
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/J16J63tC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/JVEoV1Bn
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Jcwq4RxP
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Jk8UBmcS
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/KCL5hW02
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/KKRWbrqC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/KUIfl2m7
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/KbGMgDus
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/KlqDh1ZQ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/L58tTvhF
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/L7gltlCF
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/LCLocE1C
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/LMavH6jA
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Lq3dNalV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/LrYo1dnu
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/MPeS8YHI
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/N8vFOGDF
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/NC6PZdoL
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/NS9xPzIA
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Ndyi6bnx
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/NxdIqu0S
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/O5tEUFhw
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/OH3906gp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/OIYZeUCB
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/OPqDbOIH
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Oe0SOw16
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/OnCx4O4u
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/P7orF8IR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/PECjZnzJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/PpktRW9a
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/QHv46Plh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/QbiQCWZr
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/QcIkjhJ0
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/QgmCuMSV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Qxrlj2uk
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/R3rVsQa8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RAXeLvjl
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RFLWtody
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RHjAw3hj
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RPVIP1xx
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RQWaIGxG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RVejZvvP
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/RdYwRe68
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Rgs7l9CZ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ScOtAOiZ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/SwrcVnay
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/T5IkmqtJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/T6AHhqdE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TPBDRCiJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TRyxUwzw
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TXsLzqsp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TeaXjOeh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TeyHF78l
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ToT9QPKf
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/TtPblPd6
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/U3BoYTr9
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/UDI6pN8S
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/UF1urDfG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/UUiDNDlO
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/UuC7t9JQ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/V2eK2wiC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/V4VMSZd9
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/VhBNGSYV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/WBpZ7iz6
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/WjY12GNe
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Ww6oTYL8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/X5rRZ32p
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/XGTpUJIw
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/XJiFKTlc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/XcmGmkwD
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/YAZlvEou
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/YKQLrxBm
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/YdTZkUcM
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/Z2rLXuyp
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ZWIiY84t
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ZXqAvkcE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ZdPbKJh1
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ZyNsHVFW
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/aGVRRt1d
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/aHFaEXKf
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/aIz8E0Iy
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/afLk75aO
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/b9YCg3Tz
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/bDK7A26M
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/bDZN0f4B
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/bcZupFpi
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/bjtBJwTc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/c3Z3JN0m
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/cIDWC9cb
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/dDoFZTXh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/dKYP6pnk
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/dKisxYdK
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/deppMJSV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/dv0Mm4vr
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/e1x51vcc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/e2umkBxy
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/e5b74XZq
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/eFlmUkb6
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/eNfM7vPK
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/eZ4ehccg
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/efpcZmHN
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ekSs7xW4
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/eknrQKQh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/fZHEnAvZ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/g2E6RkkX
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/g2nu6vlR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/gLAo3J0D
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/gem657x8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/hNqXyUX2
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/hZxbAqts
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/haNCaZmC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/iGwCDzaU
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/iILvZZya
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ih6levXk
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/j1v0LBVe
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jIlhVDLw
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jObn0z94
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jVkxEmtq
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jVlaDg4q
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jcMzi4VO
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jdYv9CQ3
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/jzmPaO2D
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/kDPV8ASY
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/kKVvPy8S
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/kWjYWiLD
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/kZ6DTcql
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/kbumrMcy
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/knHTEYup
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ksIZWNZR
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/lZiPMwX4
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/lcYptJNC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ld12od7V
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/lmr9cGCE
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/lxv6mvZ6
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/m1NnTZoo
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/m3bsNhyN
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/mWWBZCgt
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/mdFDpW9k
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/n2XnM9Nc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/n7Vs8Bjh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/n8r2Ejk9
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/nldOsSfJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/nnZ33FAt
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/nrwKQbJk
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/oNnB9jru
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/oi96tAtc
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/oiy29oCW
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/p1LgEQdu
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/p5INCxLV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/p5INQHq8
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/pXJHJUbH
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/pb1E0Y3Z
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/pnycz11G
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/q53EoTzu
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qCTrc9yM
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qHwcKaSC
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qK35XlHM
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qSn3WAyi
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qV83Dmye
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qWv24Da7
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qZ7TLGA0
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/qojIz6XF
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/r3HVTaJd
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/r3Pw8pFI
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/r8vIZE1F
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/rzYX4BnS
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/s9TOeOaJ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/sAy34VP4
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/sKi8TaSn
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/sNI2Q6oa
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/sRaKyq1f
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/svmptIxV
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/tFGQywwr
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/tY2epsSy
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/tuma818A
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/uMpXxbqr
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/uUI8gJNi
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/ugeJ5RN3
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vJDrHtxo
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vMv1M1qs
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vWguQ8rQ
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vc1wGQhn
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vjypfsoh
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/vsGKdf0J
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/w1XGgnr9
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/w8DmFhfg
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/woaiQu5g
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/wvhWmTPt
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/xQJV5GcG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/xlqXOqhL
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/yACAaKqG
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/yYRsKiUO
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/yg7uBent
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/zYz6howf
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/zjkul95p
-rw-r--r-- 1 root root 64 Mar  9 17:05 files/zoz7gvVr
ctf-player@pico-chall$ cd files
ctf-player@pico-chall$ ls -la
total 1216
drwxr-xr-x 2 ctf-player ctf-player 8192 Mar  9 17:05 .
drwxr-xr-x 3 ctf-player ctf-player   57 Mar  9 17:05 ..
-rw-r--r-- 1 root       root         64 Mar  9 17:05 00011a60
-rw-r--r-- 1 root       root         64 Mar  9 17:05 022cvpdN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 04nLilRD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0MT2Wrui
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0SGMttmR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0fCDySFB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0hHVJSPh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0mPyFlda
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0xknvebh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 1kTWMoOI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 1mGlW6Ts
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2JKdkggW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2Jr8UtbZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2K4XCmfE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2MYWkWLC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2QpRnoZQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2emuPVOb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2gP5wDgq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2w5vJlLG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2yMtx5qd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 303DzMmf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 33CFCJ0y
-rw-r--r-- 1 root       root         64 Mar  9 17:05 36tjTWoF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3KZwXc8s
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3Vs8v8kW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3qDKN57P
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4CwloraZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4XqPqs6B
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4k4veVKp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4sczhCZl
-rw-r--r-- 1 root       root         64 Mar  9 17:05 58BnWcOc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5bSdd2sp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5gxjbRbh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5rHRNllE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 63MqIIVV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 64nJlBLv
-rw-r--r-- 1 root       root         64 Mar  9 17:05 69JSHBh1
-rw-r--r-- 1 root       root         64 Mar  9 17:05 6vgioqew
-rw-r--r-- 1 root       root         64 Mar  9 17:05 76rj6cv7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 7j2g9w9w
-rw-r--r-- 1 root       root         64 Mar  9 17:05 7ye3lPVb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 870YaC5g
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8Shyigig
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8d0Ncqme
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8hKIvq38
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8rIuGenM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 91cLOGeN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9DNfzhUK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9KIFXofB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9pluLfgA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ADMuzktV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AEJxVlNY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AGOEyD4N
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AVdbk5eX
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AXFWLqwI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AdzCNBlC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AiUxYmz8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AmsN0Lkj
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ArUDDIQ3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Azqf6EEw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 B8pBCEvG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BN0HxLxE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BOeN3lXR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BdO65Tk4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Bh5xju3q
-rw-r--r-- 1 root       root         64 Mar  9 17:05 C1kYNpjq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CF4c5xR8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CGkVyMxT
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CLCyTz85
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CNvsyU3W
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Cb22Z7FO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ce5TrzJu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ClWGbsxu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 DCn7KnqG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 DSKHZ66z
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Dmsex2Ug
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EBBoQm7M
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EG1lW2KR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EXQ6DiO5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 F6yHlWpt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FJBePm2b
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FLsBEmlR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FOxKdaVP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FtMorZ65
-rw-r--r-- 1 root       root         64 Mar  9 17:05 G7enzzui
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Gcv1H8Qs
-rw-r--r-- 1 root       root         64 Mar  9 17:05 GhrShrXN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Gtk4Kn9w
-rw-r--r-- 1 root       root         64 Mar  9 17:05 GufDk3Mb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HDLWGApz
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HIeYL84k
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HJIPzwjJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HMq6348V
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HUjCgnh4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HWRVc59e
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Hmr54gXd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HqxLJgMp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IDQQR4nq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IITtRrrR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IbMiqCHJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ie0xOcl5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IikIpp05
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IlQwVZcY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ItYR0Da2
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Izq2bmb5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 J16J63tC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 JVEoV1Bn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Jcwq4RxP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Jk8UBmcS
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KCL5hW02
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KKRWbrqC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KUIfl2m7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KbGMgDus
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KlqDh1ZQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 L58tTvhF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 L7gltlCF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LCLocE1C
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LMavH6jA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Lq3dNalV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LrYo1dnu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 MPeS8YHI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 N8vFOGDF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NC6PZdoL
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NS9xPzIA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ndyi6bnx
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NxdIqu0S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 O5tEUFhw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OH3906gp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OIYZeUCB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OPqDbOIH
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Oe0SOw16
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OnCx4O4u
-rw-r--r-- 1 root       root         64 Mar  9 17:05 P7orF8IR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 PECjZnzJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 PpktRW9a
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QHv46Plh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QbiQCWZr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QcIkjhJ0
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QgmCuMSV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Qxrlj2uk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 R3rVsQa8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RAXeLvjl
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RFLWtody
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RHjAw3hj
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RPVIP1xx
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RQWaIGxG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RVejZvvP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RdYwRe68
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Rgs7l9CZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ScOtAOiZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 SwrcVnay
-rw-r--r-- 1 root       root         64 Mar  9 17:05 T5IkmqtJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 T6AHhqdE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TPBDRCiJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TRyxUwzw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TXsLzqsp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TeaXjOeh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TeyHF78l
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ToT9QPKf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TtPblPd6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 U3BoYTr9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UDI6pN8S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UF1urDfG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UUiDNDlO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UuC7t9JQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 V2eK2wiC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 V4VMSZd9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 VhBNGSYV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 WBpZ7iz6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 WjY12GNe
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ww6oTYL8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 X5rRZ32p
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XGTpUJIw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XJiFKTlc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XcmGmkwD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YAZlvEou
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YKQLrxBm
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YdTZkUcM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Z2rLXuyp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZWIiY84t
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZXqAvkcE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZdPbKJh1
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZyNsHVFW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aGVRRt1d
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aHFaEXKf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aIz8E0Iy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 afLk75aO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 b9YCg3Tz
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bDK7A26M
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bDZN0f4B
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bcZupFpi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bjtBJwTc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 c3Z3JN0m
-rw-r--r-- 1 root       root         64 Mar  9 17:05 cIDWC9cb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dDoFZTXh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dKYP6pnk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dKisxYdK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 deppMJSV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dv0Mm4vr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e1x51vcc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e2umkBxy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e5b74XZq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eFlmUkb6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eNfM7vPK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eZ4ehccg
-rw-r--r-- 1 root       root         64 Mar  9 17:05 efpcZmHN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ekSs7xW4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eknrQKQh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 fZHEnAvZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 g2E6RkkX
-rw-r--r-- 1 root       root         64 Mar  9 17:05 g2nu6vlR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 gLAo3J0D
-rw-r--r-- 1 root       root         64 Mar  9 17:05 gem657x8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 hNqXyUX2
-rw-r--r-- 1 root       root         64 Mar  9 17:05 hZxbAqts
-rw-r--r-- 1 root       root         64 Mar  9 17:05 haNCaZmC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 iGwCDzaU
-rw-r--r-- 1 root       root         64 Mar  9 17:05 iILvZZya
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ih6levXk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 j1v0LBVe
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jIlhVDLw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jObn0z94
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jVkxEmtq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jVlaDg4q
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jcMzi4VO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jdYv9CQ3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jzmPaO2D
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kDPV8ASY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kKVvPy8S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kWjYWiLD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kZ6DTcql
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kbumrMcy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 knHTEYup
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ksIZWNZR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lZiPMwX4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lcYptJNC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ld12od7V
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lmr9cGCE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lxv6mvZ6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 m1NnTZoo
-rw-r--r-- 1 root       root         64 Mar  9 17:05 m3bsNhyN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 mWWBZCgt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 mdFDpW9k
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n2XnM9Nc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n7Vs8Bjh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n8r2Ejk9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nldOsSfJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nnZ33FAt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nrwKQbJk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oNnB9jru
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oi96tAtc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oiy29oCW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p1LgEQdu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p5INCxLV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p5INQHq8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pXJHJUbH
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pb1E0Y3Z
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pnycz11G
-rw-r--r-- 1 root       root         64 Mar  9 17:05 q53EoTzu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qCTrc9yM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qHwcKaSC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qK35XlHM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qSn3WAyi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qV83Dmye
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qWv24Da7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qZ7TLGA0
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qojIz6XF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r3HVTaJd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r3Pw8pFI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r8vIZE1F
-rw-r--r-- 1 root       root         64 Mar  9 17:05 rzYX4BnS
-rw-r--r-- 1 root       root         64 Mar  9 17:05 s9TOeOaJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sAy34VP4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sKi8TaSn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sNI2Q6oa
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sRaKyq1f
-rw-r--r-- 1 root       root         64 Mar  9 17:05 svmptIxV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tFGQywwr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tY2epsSy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tuma818A
-rw-r--r-- 1 root       root         64 Mar  9 17:05 uMpXxbqr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 uUI8gJNi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ugeJ5RN3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vJDrHtxo
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vMv1M1qs
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vWguQ8rQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vc1wGQhn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vjypfsoh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vsGKdf0J
-rw-r--r-- 1 root       root         64 Mar  9 17:05 w1XGgnr9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 w8DmFhfg
-rw-r--r-- 1 root       root         64 Mar  9 17:05 woaiQu5g
-rw-r--r-- 1 root       root         64 Mar  9 17:05 wvhWmTPt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 xQJV5GcG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 xlqXOqhL
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yACAaKqG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yYRsKiUO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yg7uBent
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zYz6howf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zjkul95p
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zoz7gvVr
ctf-player@pico-chall$ decrypt.sh
Expected usage: decrypt.sh <filename>
ctf-player@pico-chall$ decrypt.sh *
Error: '00011a60' is not a valid file. Look inside the 'files' folder with 'ls -R'!
ctf-player@pico-chall$ pwd
/home/ctf-player/drop-in/files
ctf-player@pico-chall$ ls -R
.:
00011a60  4CwloraZ  AGOEyD4N  EXQ6DiO5  Izq2bmb5  Oe0SOw16  TeaXjOeh  ZyNsHVFW  fZHEnAvZ  lZiPMwX4  qHwcKaSC  vc1wGQhn
022cvpdN  4XqPqs6B  AVdbk5eX  F6yHlWpt  J16J63tC  OnCx4O4u  TeyHF78l  aGVRRt1d  g2E6RkkX  lcYptJNC  qK35XlHM  vjypfsoh
04nLilRD  4k4veVKp  AXFWLqwI  FJBePm2b  JVEoV1Bn  P7orF8IR  ToT9QPKf  aHFaEXKf  g2nu6vlR  ld12od7V  qSn3WAyi  vsGKdf0J
0MT2Wrui  4sczhCZl  AdzCNBlC  FLsBEmlR  Jcwq4RxP  PECjZnzJ  TtPblPd6  aIz8E0Iy  gLAo3J0D  lmr9cGCE  qV83Dmye  w1XGgnr9
0SGMttmR  58BnWcOc  AiUxYmz8  FOxKdaVP  Jk8UBmcS  PpktRW9a  U3BoYTr9  afLk75aO  gem657x8  lxv6mvZ6  qWv24Da7  w8DmFhfg
0fCDySFB  5bSdd2sp  AmsN0Lkj  FtMorZ65  KCL5hW02  QHv46Plh  UDI6pN8S  b9YCg3Tz  hNqXyUX2  m1NnTZoo  qZ7TLGA0  woaiQu5g
0hHVJSPh  5gxjbRbh  ArUDDIQ3  G7enzzui  KKRWbrqC  QbiQCWZr  UF1urDfG  bDK7A26M  hZxbAqts  m3bsNhyN  qojIz6XF  wvhWmTPt
0mPyFlda  5rHRNllE  Azqf6EEw  Gcv1H8Qs  KUIfl2m7  QcIkjhJ0  UUiDNDlO  bDZN0f4B  haNCaZmC  mWWBZCgt  r3HVTaJd  xQJV5GcG
0xknvebh  63MqIIVV  B8pBCEvG  GhrShrXN  KbGMgDus  QgmCuMSV  UuC7t9JQ  bcZupFpi  iGwCDzaU  mdFDpW9k  r3Pw8pFI  xlqXOqhL
1kTWMoOI  64nJlBLv  BN0HxLxE  Gtk4Kn9w  KlqDh1ZQ  Qxrlj2uk  V2eK2wiC  bjtBJwTc  iILvZZya  n2XnM9Nc  r8vIZE1F  yACAaKqG
1mGlW6Ts  69JSHBh1  BOeN3lXR  GufDk3Mb  L58tTvhF  R3rVsQa8  V4VMSZd9  c3Z3JN0m  ih6levXk  n7Vs8Bjh  rzYX4BnS  yYRsKiUO
2JKdkggW  6vgioqew  BdO65Tk4  HDLWGApz  L7gltlCF  RAXeLvjl  VhBNGSYV  cIDWC9cb  j1v0LBVe  n8r2Ejk9  s9TOeOaJ  yg7uBent
2Jr8UtbZ  76rj6cv7  Bh5xju3q  HIeYL84k  LCLocE1C  RFLWtody  WBpZ7iz6  dDoFZTXh  jIlhVDLw  nldOsSfJ  sAy34VP4  zYz6howf
2K4XCmfE  7j2g9w9w  C1kYNpjq  HJIPzwjJ  LMavH6jA  RHjAw3hj  WjY12GNe  dKYP6pnk  jObn0z94  nnZ33FAt  sKi8TaSn  zjkul95p
2MYWkWLC  7ye3lPVb  CF4c5xR8  HMq6348V  Lq3dNalV  RPVIP1xx  Ww6oTYL8  dKisxYdK  jVkxEmtq  nrwKQbJk  sNI2Q6oa  zoz7gvVr
2QpRnoZQ  870YaC5g  CGkVyMxT  HUjCgnh4  LrYo1dnu  RQWaIGxG  X5rRZ32p  deppMJSV  jVlaDg4q  oNnB9jru  sRaKyq1f
2emuPVOb  8Shyigig  CLCyTz85  HWRVc59e  MPeS8YHI  RVejZvvP  XGTpUJIw  dv0Mm4vr  jcMzi4VO  oi96tAtc  svmptIxV
2gP5wDgq  8d0Ncqme  CNvsyU3W  Hmr54gXd  N8vFOGDF  RdYwRe68  XJiFKTlc  e1x51vcc  jdYv9CQ3  oiy29oCW  tFGQywwr
2w5vJlLG  8hKIvq38  Cb22Z7FO  HqxLJgMp  NC6PZdoL  Rgs7l9CZ  XcmGmkwD  e2umkBxy  jzmPaO2D  p1LgEQdu  tY2epsSy
2yMtx5qd  8rIuGenM  Ce5TrzJu  IDQQR4nq  NS9xPzIA  ScOtAOiZ  YAZlvEou  e5b74XZq  kDPV8ASY  p5INCxLV  tuma818A
303DzMmf  91cLOGeN  ClWGbsxu  IITtRrrR  Ndyi6bnx  SwrcVnay  YKQLrxBm  eFlmUkb6  kKVvPy8S  p5INQHq8  uMpXxbqr
33CFCJ0y  9DNfzhUK  DCn7KnqG  IbMiqCHJ  NxdIqu0S  T5IkmqtJ  YdTZkUcM  eNfM7vPK  kWjYWiLD  pXJHJUbH  uUI8gJNi
36tjTWoF  9KIFXofB  DSKHZ66z  Ie0xOcl5  O5tEUFhw  T6AHhqdE  Z2rLXuyp  eZ4ehccg  kZ6DTcql  pb1E0Y3Z  ugeJ5RN3
3KZwXc8s  9pluLfgA  Dmsex2Ug  IikIpp05  OH3906gp  TPBDRCiJ  ZWIiY84t  efpcZmHN  kbumrMcy  pnycz11G  vJDrHtxo
3Vs8v8kW  ADMuzktV  EBBoQm7M  IlQwVZcY  OIYZeUCB  TRyxUwzw  ZXqAvkcE  ekSs7xW4  knHTEYup  q53EoTzu  vMv1M1qs
3qDKN57P  AEJxVlNY  EG1lW2KR  ItYR0Da2  OPqDbOIH  TXsLzqsp  ZdPbKJh1  eknrQKQh  ksIZWNZR  qCTrc9yM  vWguQ8rQ
ctf-player@pico-chall$ ls -la
total 1216
drwxr-xr-x 2 ctf-player ctf-player 8192 Mar  9 17:05 .
drwxr-xr-x 3 ctf-player ctf-player   57 Mar  9 17:05 ..
-rw-r--r-- 1 root       root         64 Mar  9 17:05 00011a60
-rw-r--r-- 1 root       root         64 Mar  9 17:05 022cvpdN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 04nLilRD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0MT2Wrui
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0SGMttmR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0fCDySFB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0hHVJSPh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0mPyFlda
-rw-r--r-- 1 root       root         64 Mar  9 17:05 0xknvebh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 1kTWMoOI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 1mGlW6Ts
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2JKdkggW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2Jr8UtbZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2K4XCmfE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2MYWkWLC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2QpRnoZQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2emuPVOb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2gP5wDgq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2w5vJlLG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 2yMtx5qd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 303DzMmf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 33CFCJ0y
-rw-r--r-- 1 root       root         64 Mar  9 17:05 36tjTWoF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3KZwXc8s
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3Vs8v8kW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 3qDKN57P
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4CwloraZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4XqPqs6B
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4k4veVKp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 4sczhCZl
-rw-r--r-- 1 root       root         64 Mar  9 17:05 58BnWcOc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5bSdd2sp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5gxjbRbh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 5rHRNllE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 63MqIIVV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 64nJlBLv
-rw-r--r-- 1 root       root         64 Mar  9 17:05 69JSHBh1
-rw-r--r-- 1 root       root         64 Mar  9 17:05 6vgioqew
-rw-r--r-- 1 root       root         64 Mar  9 17:05 76rj6cv7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 7j2g9w9w
-rw-r--r-- 1 root       root         64 Mar  9 17:05 7ye3lPVb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 870YaC5g
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8Shyigig
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8d0Ncqme
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8hKIvq38
-rw-r--r-- 1 root       root         64 Mar  9 17:05 8rIuGenM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 91cLOGeN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9DNfzhUK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9KIFXofB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 9pluLfgA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ADMuzktV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AEJxVlNY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AGOEyD4N
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AVdbk5eX
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AXFWLqwI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AdzCNBlC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AiUxYmz8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 AmsN0Lkj
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ArUDDIQ3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Azqf6EEw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 B8pBCEvG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BN0HxLxE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BOeN3lXR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 BdO65Tk4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Bh5xju3q
-rw-r--r-- 1 root       root         64 Mar  9 17:05 C1kYNpjq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CF4c5xR8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CGkVyMxT
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CLCyTz85
-rw-r--r-- 1 root       root         64 Mar  9 17:05 CNvsyU3W
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Cb22Z7FO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ce5TrzJu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ClWGbsxu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 DCn7KnqG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 DSKHZ66z
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Dmsex2Ug
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EBBoQm7M
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EG1lW2KR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 EXQ6DiO5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 F6yHlWpt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FJBePm2b
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FLsBEmlR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FOxKdaVP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 FtMorZ65
-rw-r--r-- 1 root       root         64 Mar  9 17:05 G7enzzui
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Gcv1H8Qs
-rw-r--r-- 1 root       root         64 Mar  9 17:05 GhrShrXN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Gtk4Kn9w
-rw-r--r-- 1 root       root         64 Mar  9 17:05 GufDk3Mb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HDLWGApz
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HIeYL84k
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HJIPzwjJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HMq6348V
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HUjCgnh4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HWRVc59e
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Hmr54gXd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 HqxLJgMp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IDQQR4nq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IITtRrrR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IbMiqCHJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ie0xOcl5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IikIpp05
-rw-r--r-- 1 root       root         64 Mar  9 17:05 IlQwVZcY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ItYR0Da2
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Izq2bmb5
-rw-r--r-- 1 root       root         64 Mar  9 17:05 J16J63tC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 JVEoV1Bn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Jcwq4RxP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Jk8UBmcS
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KCL5hW02
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KKRWbrqC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KUIfl2m7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KbGMgDus
-rw-r--r-- 1 root       root         64 Mar  9 17:05 KlqDh1ZQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 L58tTvhF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 L7gltlCF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LCLocE1C
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LMavH6jA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Lq3dNalV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 LrYo1dnu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 MPeS8YHI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 N8vFOGDF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NC6PZdoL
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NS9xPzIA
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ndyi6bnx
-rw-r--r-- 1 root       root         64 Mar  9 17:05 NxdIqu0S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 O5tEUFhw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OH3906gp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OIYZeUCB
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OPqDbOIH
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Oe0SOw16
-rw-r--r-- 1 root       root         64 Mar  9 17:05 OnCx4O4u
-rw-r--r-- 1 root       root         64 Mar  9 17:05 P7orF8IR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 PECjZnzJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 PpktRW9a
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QHv46Plh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QbiQCWZr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QcIkjhJ0
-rw-r--r-- 1 root       root         64 Mar  9 17:05 QgmCuMSV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Qxrlj2uk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 R3rVsQa8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RAXeLvjl
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RFLWtody
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RHjAw3hj
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RPVIP1xx
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RQWaIGxG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RVejZvvP
-rw-r--r-- 1 root       root         64 Mar  9 17:05 RdYwRe68
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Rgs7l9CZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ScOtAOiZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 SwrcVnay
-rw-r--r-- 1 root       root         64 Mar  9 17:05 T5IkmqtJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 T6AHhqdE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TPBDRCiJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TRyxUwzw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TXsLzqsp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TeaXjOeh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TeyHF78l
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ToT9QPKf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 TtPblPd6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 U3BoYTr9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UDI6pN8S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UF1urDfG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UUiDNDlO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 UuC7t9JQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 V2eK2wiC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 V4VMSZd9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 VhBNGSYV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 WBpZ7iz6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 WjY12GNe
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Ww6oTYL8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 X5rRZ32p
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XGTpUJIw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XJiFKTlc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 XcmGmkwD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YAZlvEou
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YKQLrxBm
-rw-r--r-- 1 root       root         64 Mar  9 17:05 YdTZkUcM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 Z2rLXuyp
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZWIiY84t
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZXqAvkcE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZdPbKJh1
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ZyNsHVFW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aGVRRt1d
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aHFaEXKf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 aIz8E0Iy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 afLk75aO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 b9YCg3Tz
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bDK7A26M
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bDZN0f4B
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bcZupFpi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 bjtBJwTc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 c3Z3JN0m
-rw-r--r-- 1 root       root         64 Mar  9 17:05 cIDWC9cb
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dDoFZTXh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dKYP6pnk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dKisxYdK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 deppMJSV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 dv0Mm4vr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e1x51vcc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e2umkBxy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 e5b74XZq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eFlmUkb6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eNfM7vPK
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eZ4ehccg
-rw-r--r-- 1 root       root         64 Mar  9 17:05 efpcZmHN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ekSs7xW4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 eknrQKQh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 fZHEnAvZ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 g2E6RkkX
-rw-r--r-- 1 root       root         64 Mar  9 17:05 g2nu6vlR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 gLAo3J0D
-rw-r--r-- 1 root       root         64 Mar  9 17:05 gem657x8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 hNqXyUX2
-rw-r--r-- 1 root       root         64 Mar  9 17:05 hZxbAqts
-rw-r--r-- 1 root       root         64 Mar  9 17:05 haNCaZmC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 iGwCDzaU
-rw-r--r-- 1 root       root         64 Mar  9 17:05 iILvZZya
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ih6levXk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 j1v0LBVe
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jIlhVDLw
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jObn0z94
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jVkxEmtq
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jVlaDg4q
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jcMzi4VO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jdYv9CQ3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 jzmPaO2D
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kDPV8ASY
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kKVvPy8S
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kWjYWiLD
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kZ6DTcql
-rw-r--r-- 1 root       root         64 Mar  9 17:05 kbumrMcy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 knHTEYup
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ksIZWNZR
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lZiPMwX4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lcYptJNC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ld12od7V
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lmr9cGCE
-rw-r--r-- 1 root       root         64 Mar  9 17:05 lxv6mvZ6
-rw-r--r-- 1 root       root         64 Mar  9 17:05 m1NnTZoo
-rw-r--r-- 1 root       root         64 Mar  9 17:05 m3bsNhyN
-rw-r--r-- 1 root       root         64 Mar  9 17:05 mWWBZCgt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 mdFDpW9k
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n2XnM9Nc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n7Vs8Bjh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 n8r2Ejk9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nldOsSfJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nnZ33FAt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 nrwKQbJk
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oNnB9jru
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oi96tAtc
-rw-r--r-- 1 root       root         64 Mar  9 17:05 oiy29oCW
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p1LgEQdu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p5INCxLV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 p5INQHq8
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pXJHJUbH
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pb1E0Y3Z
-rw-r--r-- 1 root       root         64 Mar  9 17:05 pnycz11G
-rw-r--r-- 1 root       root         64 Mar  9 17:05 q53EoTzu
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qCTrc9yM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qHwcKaSC
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qK35XlHM
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qSn3WAyi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qV83Dmye
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qWv24Da7
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qZ7TLGA0
-rw-r--r-- 1 root       root         64 Mar  9 17:05 qojIz6XF
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r3HVTaJd
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r3Pw8pFI
-rw-r--r-- 1 root       root         64 Mar  9 17:05 r8vIZE1F
-rw-r--r-- 1 root       root         64 Mar  9 17:05 rzYX4BnS
-rw-r--r-- 1 root       root         64 Mar  9 17:05 s9TOeOaJ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sAy34VP4
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sKi8TaSn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sNI2Q6oa
-rw-r--r-- 1 root       root         64 Mar  9 17:05 sRaKyq1f
-rw-r--r-- 1 root       root         64 Mar  9 17:05 svmptIxV
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tFGQywwr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tY2epsSy
-rw-r--r-- 1 root       root         64 Mar  9 17:05 tuma818A
-rw-r--r-- 1 root       root         64 Mar  9 17:05 uMpXxbqr
-rw-r--r-- 1 root       root         64 Mar  9 17:05 uUI8gJNi
-rw-r--r-- 1 root       root         64 Mar  9 17:05 ugeJ5RN3
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vJDrHtxo
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vMv1M1qs
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vWguQ8rQ
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vc1wGQhn
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vjypfsoh
-rw-r--r-- 1 root       root         64 Mar  9 17:05 vsGKdf0J
-rw-r--r-- 1 root       root         64 Mar  9 17:05 w1XGgnr9
-rw-r--r-- 1 root       root         64 Mar  9 17:05 w8DmFhfg
-rw-r--r-- 1 root       root         64 Mar  9 17:05 woaiQu5g
-rw-r--r-- 1 root       root         64 Mar  9 17:05 wvhWmTPt
-rw-r--r-- 1 root       root         64 Mar  9 17:05 xQJV5GcG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 xlqXOqhL
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yACAaKqG
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yYRsKiUO
-rw-r--r-- 1 root       root         64 Mar  9 17:05 yg7uBent
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zYz6howf
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zjkul95p
-rw-r--r-- 1 root       root         64 Mar  9 17:05 zoz7gvVr
ctf-player@pico-chall$ decrypt.sh zoz7gvVr 
Error: 'zoz7gvVr' is not a valid file. Look inside the 'files' folder with 'ls -R'!
ctf-player@pico-chall$ find . -type f -exec sha256sum {} + 2>/dev/null
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8  ./00011a60
eb6573551001fb6324dd7a5cd0e71a74b5e913caaca9602de4af3ae5703496c2  ./022cvpdN
361ad57a3e02f41d5d4b783e03a85818aeac7445f84f5843d64f7e3112a7e9db  ./04nLilRD
ea0b454f15f4e4ebd047fcebe3662399402e27648bc9d28358c9928808263a78  ./0MT2Wrui
98084160f9db93b126b79b7ff34e3ec6c3b74a07d65c3e16a63e6eea6ab15ea3  ./0SGMttmR
549f9a2225a3704c506dde3eb18d7871336fc0907fa4cf41757b82190e1b8358  ./0fCDySFB
b1a6ab2a2dca6a4b13e103cf39702fcc57cda3ffd0eee5e0de05b3181e0faab4  ./0hHVJSPh
d29e7d6917556bbd13d4da8e7664c7ec60c7945b5f276ab05117cd61b5be5b19  ./0mPyFlda
a9f5296a580019e29331cf486430555c8b4311fc394aff9254adf870ab7e559f  ./0xknvebh
039d4e4891f52de0c5e06be5eb904faa20982855377d25220c6e3be4e6b4e7fc  ./1kTWMoOI
0920e8dfe825bf0b68a67f2f78ccc5760f706a622731470406a8d28c9077e54f  ./1mGlW6Ts
37d9b435a5710102dfd40f09f4e66bac877ed8c364b264bd6771d9aedbc8c12b  ./2JKdkggW
403e9ec85daf7f2e88b4f2a8c52405204f6f91fa66d0487479053a69741f46c5  ./2Jr8UtbZ
973935efe0ef50f4d3a776bd53d13d06b5d9a6fa2a85714b292d9483d9e0b2d9  ./2K4XCmfE
4558de5dffd35cb7378f9eae004bc2d3a3e3cc6478197cad46eafed24e4ea928  ./2MYWkWLC
d772591e7be3c881279f827436028d60ede0dd6d2c1da4d0912a36bf65ad235a  ./2QpRnoZQ
8ad74224d5d55947fae7dcfcf324d71766b53e4f9bf2a51ecc31a62011a6e7a0  ./2emuPVOb
6e1ce0ccb79eb4cc9aefe250752138f03667ccdf56d4fcc802f963df74d07007  ./2gP5wDgq
bd69460bbf3949a065808bd522423ecf3d7b8cf0cf122879a10aadf42e20d003  ./2w5vJlLG
3b3d197f7c95642076495dc5d7154f101fe61a35dc3ff735f0e215cd82230f5c  ./2yMtx5qd
b54c17bd5819b838f724e455329e315d52914e9fa2b7717f497b3ef7c3a26ad5  ./303DzMmf
a50fe61ae10c17e7b0251d08f1706278e8ae00dad0204ca8f090f7c4ebfb7742  ./33CFCJ0y
a6cc93cff0a5e480d4847c17b1de1685a2d77ea3d279530bf09d286d3d65d29c  ./36tjTWoF
581338a120b7f515274800a249a67a52106f9ebde65901623e044269756207b4  ./3KZwXc8s
9a2d84874f0020f65612733e7f7595282e22d4bd73fcabafc7a505483f119638  ./3Vs8v8kW
e4ecf4d1ea28494c6cc9f51619389fa5f8e71a5c729dfdc62584fd75aea79acf  ./3qDKN57P
cdc68b187592affd1d2b58dfb5fb8d781cb752245a83dfe3ab2240068eb2f0af  ./4CwloraZ
c9043aac0b46987d17035595c1f7aaaaeb543e41cbc0f95950c19a7b826434d2  ./4XqPqs6B
944a3a876d48273f749a875563b2314df203b201fa949693004284e6c311be26  ./4k4veVKp
d45e1cda8fe8b8d7435bc263fd07bd154fa004b4ecc85a5c9b66f050f2e378ce  ./4sczhCZl
8834a1ec5644e5d3d30ef0b92a1901c36d059769609034d5a3013d927e4fe865  ./58BnWcOc
13eb9e85ffbc467ff81f451f43edd55c501c9f3d6e919dc5b4e131a4359e974a  ./5bSdd2sp
e65c3e32a92931a2c9d8249696ecf679b9434d81a5f0da5d487761dd474a2309  ./5gxjbRbh
f6f1e2d8a6f58e90d631584c30d7d5ebb4a2624cda2b4fef0a96064226c50642  ./5rHRNllE
c3f7e58d90b63a26a7dc068004a1209c3548ee06125e0ade7dfa15bc18f5c822  ./63MqIIVV
b7b5a6f3b260534379b5dfa467bf3f2e131f2b8df23f5e369200edcce96b0a6d  ./64nJlBLv
ee9afd7a75f321463670a3cd1f9074b8f03cdf84c5d7f4976cc6fcea6e74b3e4  ./69JSHBh1
ef627a9c08ab7c411bfb75a1f5ba2bd3b825118ba3ab8d1c3c874ac447e93879  ./6vgioqew
2c527cef849d3e80c581b9c74d903be1e0fa433bf62d1c1d1766fb804aa63705  ./76rj6cv7
135172789252463262546155e5ec4e8216424d0f5f17c9c27e20c0418a32452f  ./7j2g9w9w
575d71c9ffdbf387c6e84d210670d3fb28811dd475af4a5461a603f2cd62e007  ./7ye3lPVb
8b2e6e08c913d27c871017408567a267a2945f9d79aadea3d8bbc100e4c25a8b  ./870YaC5g
00071ef61f9317f871486a0efd51744c4328c2b028f703dc0bb6bd9eac675a7a  ./8Shyigig
12e6e37f83c412cda8c804f33fc021998baf657eb555574cbc337bc1e80399e1  ./8d0Ncqme
b827b07b64c261779959adfee3f88eb1fc0f93f70eaa44897cef1c3d3b07612e  ./8hKIvq38
007d6ee87885a7ecbf000489e64ce429ca2910c3472830932c07af7e265d8fe5  ./8rIuGenM
3387f7cbc59a5356fbe8e45f25367073cbade08e9debf89aa1bad9455fac286d  ./91cLOGeN
e7659b5bc805fec74aee5cc2bb4ad5abd3330113aff3dcd614edc2c499c04c2a  ./9DNfzhUK
c5640b331435d90cc331fa46e08a35cd31e6c3309e616778238aa169b6524862  ./9KIFXofB
f3f9b3cea5ad74b9d97cfac50b552db597111e95641f1efccfd178bf32ea2eb5  ./9pluLfgA
a1edcfdacac04ec76fca1a1b72608b809a25f43aeb318c070570374e0bc36278  ./ADMuzktV
f743f39110bfa881972fc02f473c7e858adeb7bee5f23ee3a6628956002132ca  ./AEJxVlNY
b51bac4960d16df12c1cd8598590f2c9bfd8afaeeea397e3af345b42eed3693f  ./AGOEyD4N
9f5b889bf015d4052102c7e76cad6605f621c7e61301a7494d00c465250bf2c2  ./AVdbk5eX
855cbe62f628a40e79feca1b6ce07e6a04e538129bc972333e339427c8abb0ca  ./AXFWLqwI
4aa26d3ce74ff70aab06bcd8feb83c1574f5901e42ad64a02e0f58173ff1e266  ./AdzCNBlC
73bb2a65cc2e5f18fdd8bb273aad804b6dcbc5ce62b23cb5502c99b780268270  ./AiUxYmz8
ad547edc36c4744e43f9b9c223eea71b69e94d84b9f4036eea3a4c874684a9fd  ./AmsN0Lkj
41376d36a597b606a33d8c1cc464587b6e78ce6107b97acb5220050596f7c9a0  ./ArUDDIQ3
816455a06f7f3b02f61244a9b9c091471b9e6c117ef670b5e4a99822c4032dbb  ./Azqf6EEw
21094fdd36dde6752f3ae6d7453d6fb46907c9bd3c017df2fda56c9985b49649  ./B8pBCEvG
7323d7324e01e570c06e805d0e976ee599374a6b0d144f0db7c928305c5673f9  ./BN0HxLxE
ee0e99fa63b66930ff9804857cf6e5d1eda239a2120bd8742b5e8f1339b31678  ./BOeN3lXR
6e11b61f929bca1dc9cd6d38044cbcc401720b31c9fedf29530da60f96dbe480  ./BdO65Tk4
d61ab0860a384fa795721cb52d2abd936ef4e92fe9e3e507acdd20cefd03dee9  ./Bh5xju3q
d81b1c0817a56264373b65d2dbf57ec7c880c7d71d74abbce586e61ce0aea0aa  ./C1kYNpjq
bd158aaee7e0ac22c7906dd846cd43f030c3799e2be2d8ed3f5bc42276a5b136  ./CF4c5xR8
b67bd9bac6f50ffc33e14003b7bb6443b87ae4320cb71be92bdbd748d161a049  ./CGkVyMxT
c30c196ba654aa64348fccdf52715b1fb086af193570aadaa73ecdcae787faf0  ./CLCyTz85
3f6b2383dc7b535b6b46ce758997daf33c9e7af258573bb3fc18e203425f6cf3  ./CNvsyU3W
66f7c78259236b8edab5984e8d415a6821ae692f8bb9a81030f20f677ece1d5f  ./Cb22Z7FO
e12244de00e94e3eb0effc1617902e4ca3d54923889b28f73a0c89d770f11afb  ./Ce5TrzJu
2f673fb40e87114ddcd11d58b26be5f7cffd437a78e36a8ee1e4a75e728cc69e  ./ClWGbsxu
eaec30498f3e1dc40d733b4a0da7684a85e9de8060909e72fa886e144e33f7a1  ./DCn7KnqG
054385690a1a3c69b37199ff8680e021e09d73a0d920125ccc060d844845315b  ./DSKHZ66z
246f6529ab0ee9d04064aa54c8038a42763d065946745e05a3a55d48360a9928  ./Dmsex2Ug
c20b3be2a86293600161f87209fc5c104710be1fdab154ce14108fc1e46c75c0  ./EBBoQm7M
1717f140a260452f642a02541aa08072743e30c2c7a9eb7f3a8be4e564706998  ./EG1lW2KR
d42bd5f265a2d7e6c6b330ff605fbf9622e52434e8dff151305309c1f8781f68  ./EXQ6DiO5
24c329942a1359bedd1dc4988f79de79816aa2bf18c052aeca8977a92dd57fe4  ./F6yHlWpt
214d9d3766e11a634d94b6dce6d89eb789ebc6fa05735eb8f03f7f0a09ac8581  ./FJBePm2b
ba0f5b97c07afdffa9a2bb6945053bc2963bb918df89e183c74aa7ea629501e1  ./FLsBEmlR
497fa5c542ddf07a18ef26ed4e7f9ab028b121cd9eb920f445add409bc5ec100  ./FOxKdaVP
43c9324404398a6f2260fcbacb2e867d341005d0a5467ef533de98230c868496  ./FtMorZ65
5852a8e0307cf5e4253da1c3ee0e278898831e77f3035cf5671519a92a04ad58  ./G7enzzui
b3c96d9e28f9c14f9e48efbdd7dfa6cdc8864f735f4fd7549ad725510533b7c3  ./Gcv1H8Qs
36e01e217da80d065ffa900daf45b703540a39115e9a2e1f2b5dc2eec7486628  ./GhrShrXN
9d1d9b34199bb9988b1088096921400bba652ace4b29ce269bb3b700b37e233f  ./Gtk4Kn9w
0224d53c48a2b42e863114f996144726061d9e84a634535d9df29bdd291f9a3e  ./GufDk3Mb
593b8cf7a8b902c32c167c385ea8e60d3a1f3d7dc56d422bb5922ec05af4f447  ./HDLWGApz
6c3cd803b137ebe03a1d92fb843d8a008f1b6d1a896d472ca24e37584f521dcb  ./HIeYL84k
1c797ae46cdde8f35e325fdff8e9fda013879369b966bdb81c2cfe34839bfdeb  ./HJIPzwjJ
1451080d01fe0b638c02e5b1ece9735454e0320c1850ea5b2395b28658df9c6b  ./HMq6348V
a9c710f7003bade97065a1df85aa996d93bfb8a4ccb8008046fd48cdbdc163a1  ./HUjCgnh4
94093b2fd9189fe726e71f9b3ec14185b2b4c1f2086714b4825cdf2c7c7e89f6  ./HWRVc59e
91441fdf5b1796ded6786bdf361de6f891c5bf6d864d7fabb2b57dd427fb4e20  ./Hmr54gXd
92ebb16b3383d1a5db8fbb59752fa020bdf2a2c34ce8a4bcae0c9f844da7f7bc  ./HqxLJgMp
88b2de7bd8a02d66c95c4e7d1fee244fa22cfad6ab03c59eea5371a57abea455  ./IDQQR4nq
6f1d9df84a12925691a4b8386087562299a4758a141956f0ce040f4d695db140  ./IITtRrrR
272f5fe9eb34034b2ab1a93e0db8271f2f97d4dceb3c875429df3cdb9a4697d9  ./IbMiqCHJ
126b24aacbada2f18153186ecdb567e514522d8eb5efa5ac0c59f68656c60e7b  ./Ie0xOcl5
63071c1e4da2981f65a17e7f23d35d0365a75174be6181250cf2189d84aba977  ./IikIpp05
a82dbc2347f4096a360664878788ea909368643da1b0ed4af65d87330d7884ab  ./IlQwVZcY
6e0afffedaa28abef139b1a1c0a5c5f6eb1282ae979fd9c33744587ad5c8a2bc  ./ItYR0Da2
4d83e31edc0227f241d1f2f4660922dfb10bf93e8b9d87ab61c77a017d585d86  ./Izq2bmb5
7dca60cb2a9c7848526efd10777527d134232a91d9403acee7346461b5adae07  ./J16J63tC
288dc1660637a1b78728788e772f65291d9506566858d4f856105f886a8df5de  ./JVEoV1Bn
d2333158c3ca35ac8c3e9ded3ebc62e09c2411343657582a1a61c4e1fa1559e3  ./Jcwq4RxP
946d1f1db6584ce500f325214e98fd43fabdc534377a0ad4bd3afc1b1556fbf7  ./Jk8UBmcS
008eeeffef27469f34380bdd3df8ffc70f0d2ca6c14d1827d93c44e852558fc7  ./KCL5hW02
92b1bad6bb21883279260d64b857d6e3b33739d385536f0475794bf2f776cc02  ./KKRWbrqC
263f943bbb6a08868e6f260f3108efb035ff429e35269fa310ea9a31c3fa7be2  ./KUIfl2m7
17bd72aac879365d69487e2c98cf9341fcf9a4bace768b3855fe172627c9c2fd  ./KbGMgDus
c445f000d8ecf46866c88b9e7e2f8781eca08fa227f75a201c704c6940858af3  ./KlqDh1ZQ
90049a5d6aed6b03809950fbd127dc64fab9a0080d57561205067623a452f45e  ./L58tTvhF
74b4b005e4e9288434c3f94f1c4cffc2b9514a3f3a7fd67dc0a894d1e0cea3e2  ./L7gltlCF
d47140dc2c12248de67a780a210d2aab8da610e1e48e239ee19f39b2bb95e7d9  ./LCLocE1C
e03e19f4d7541f06cd0d0b2abfc08802cef1e8a01227812841837e42dcf9cf5e  ./LMavH6jA
c431b1a8925021e5edeb740689823f7ed558a0ab3c479ffd9a98b6a01607efde  ./Lq3dNalV
47a02c84973a7d6040bb38bbebb599b786bcef4f7675fc7c8bc038e23689fefa  ./LrYo1dnu
823c16b3b6acfe0edc55d784be27f9348c2edad597b406449d67549949132bc1  ./MPeS8YHI
25b999f528aa4ab7e8d758ab04014da7c8062ae48f817fa76649208b4de1ee09  ./N8vFOGDF
fe4ae088aeeef96e7a018cd83faaa6c1858231737675b9eec29313ebfb27f175  ./NC6PZdoL
b16be65f35062bca3c754565ae5ef77a805606be2e414be1edea800dbe11db2f  ./NS9xPzIA
f34b81a42778d749982808a7449d6339709078e5b94a5e735e19e0f8338acae7  ./Ndyi6bnx
063abf24f705ede62454c2e78b5065761e7c87e4c7985fbad85ecfa178c7003a  ./NxdIqu0S
627af0953fdc7db69c6d054b015920939b4a1a2a8ea3f9f8dbbc7488cedf8534  ./O5tEUFhw
eab929b7750c2c46e1ac8b1c02215b3454a8c48f32fd602707069f449a2fb1c3  ./OH3906gp
2dd8b0507aae0eae3b7e5495d10882047863e36905662936322160e538b73a23  ./OIYZeUCB
cbcad60ac22a32e11d4a8031230d6d86de8e911d60d9ef78a12338bacba17247  ./OPqDbOIH
adca1593193c86e46062b0bc0cff28cb65f152e09180addef9abd8436c198f36  ./Oe0SOw16
263cd3ff2485ec290b1561e38a8951c28b6e7a8f9b525a794b07ab8606798ab7  ./OnCx4O4u
f8e0ec1fe705b287d947daf64a1455f7b2d82774c104378e7e8f99cadfc460e7  ./P7orF8IR
d6dc5118322732a156babb343939d3ba784796375c2a36939cf2aa8a37636e4b  ./PECjZnzJ
6781d8065524fce22b0373ef9bd33cbb3e49f09c779f23ff550f9e54d3b575fa  ./PpktRW9a
623000b0e603e75e05b13efe5739cfd615f2872e899b24c106078227dcacc991  ./QHv46Plh
9635e2726c95db0562f2102ee9369f611b9cff5c9def3bb120a260170db487d6  ./QbiQCWZr
100adebc08d243c472d809a46cb2e75b10c554243281d9c9e1f2e69df440d2f0  ./QcIkjhJ0
d91cb75fa0213830cd6aa41293af3157f384abe73cf53c4d76611df6db8a39e4  ./QgmCuMSV
92e1e7820b6ddeaeec39ccdc173ce0a0ae9d862598d07385c010be8b95e8b148  ./Qxrlj2uk
279440248f97e0cda869f78bdff3f5ac5f6a9a1b3063d95de1480b2ef84b80cc  ./R3rVsQa8
538c01303257a744853b5ccee6808696fa4b1fd5d1ae9935f681b453a55851b9  ./RAXeLvjl
0ec59f74b660f2c1f8466df2c30588e2ff22626186fe70920d1596201b0aabda  ./RFLWtody
395621e1c82acd38409bd917361c63c7196b047407bf36774e605cc9ef932036  ./RHjAw3hj
253e55baf3b500d6a1d31aa10de77bb2c1fcc3bcd3a9ef4ca4d104cf209bc170  ./RPVIP1xx
ab5505988644d10ae2db50654235d6e478d7c0b79845b479c1104f151ff26713  ./RQWaIGxG
e4cbe63f24a3355efb84c5a6a725387a911ed2da4394f1916b9e9d4ead4377ab  ./RVejZvvP
ef30bbbf91e241d6b9414fd29e7904a23f70f2667a2b452b9c9b6e5f9aaaa403  ./RdYwRe68
0d86ae1a6b0f0384cbc4ea6e768baf17332f398acba9a58e09725c297b8b1e78  ./Rgs7l9CZ
3f2e52e946158b090057ee5e5f9258e6b6a6970157f4d8e6d7e118c4de14c13a  ./ScOtAOiZ
add16ab305221bcbf691cda2bd38b0bc3f96afe561811be77f53bcff62db5524  ./SwrcVnay
5e6fa883009f4555a4d8d241d885203d8bbd5e9969039e73f745adeb5aa4d8c4  ./T5IkmqtJ
496e2b16104af07c104798c8a90c76b3ee8c7df4634241281c18b0e1d3c71d66  ./T6AHhqdE
bb10b47b2b9f945956b54a3673585a6209f3255ae425e0ed8b2a6d6a4d72e84a  ./TPBDRCiJ
9340fd16c34134c714a0d8fde2bacdebfead494839f85f3b29c988d4e2303292  ./TRyxUwzw
74280af7b4c2fba191170a62b99e4c228ba6588f379648a74662bbec17f9c0df  ./TXsLzqsp
65e1c5d17adbe186a5e876f713a2c2a7df363365e77a43827d51e31d5d8b852a  ./TeaXjOeh
34ceea21314b2307b8434ffb79b0aca0502565e78d08a5d96c5ade78b9ba249d  ./TeyHF78l
3ee8dcd523fdb57ed46f79bfda796c9bc9f789dde31fcd7c4eee1ee83353c45d  ./ToT9QPKf
dbd4afef169da429252ad686a3dd2adaebbaf4a5b239234b118115c73836ad7e  ./TtPblPd6
8834598b63b9bc75c57dd39a4e09f1f4cfe6e18a76cb72712b9ab58b91fd29b9  ./U3BoYTr9
8a02b7420bd0cb68b517ea612b3d30e89d2d9fccb8558b225e52faf1fc67b2f3  ./UDI6pN8S
cf5fb47eaa09e06dfb5266c58b31a1583a2e3e2d8b05fb9f646877fc8a0bdc89  ./UF1urDfG
c0a946ac9ec7bd98102b295d0cf5cf41f2d7e86f9e3a1cbf4dc0982906e21172  ./UUiDNDlO
845e390c91ce48fe183878dae17cf3d0c6c040ad2dfa8b4e2495976293175b3a  ./UuC7t9JQ
9237429a62e06cd51766713fa5b5faef975d832f06717b4296da9a677d171064  ./V2eK2wiC
197fbe2c20925d9e8cd5be02f644eadd03cf0cf24b8460805fd908f74d8d3434  ./V4VMSZd9
0efdaa40ed82921ef5af5d7bf94d3c1d638ec2fb60c3ab9a3c446b56f38d85bc  ./VhBNGSYV
01a60bb704bf39ed79895462136fb07cdc53faa8495bcfbc369a29a15267e735  ./WBpZ7iz6
a35c78acce6e7f7c87223554246ea6fb7d96cdd317f18e362b7ca15c2fef57f4  ./WjY12GNe
d09aebd43b4adeebefac4ae06344ad7c983b5b8ae29a7e7c203670ae90f648b3  ./Ww6oTYL8
1b4129df0fe5e99898b84f627fbf161178932efc836e40b1ed242147679da655  ./X5rRZ32p
d6bd629714f053e9b7c1875f7d1ebb508f19659fec2b3671a89df836ffeea2bf  ./XGTpUJIw
7bcbe06a5b9d5e5b58d451b5a12952e004ef3851c33e92ea8ad2c7cef8fedf77  ./XJiFKTlc
018a88c45b7f77ae9024eece7ac276e5b0747a08482c232e9317a265dad7d2e3  ./XcmGmkwD
05037dc990e1950d0272921f061e2e3be5e535f97e02c745a09c4cebb422901b  ./YAZlvEou
c42ba9fe1bb9df6fc7e6dca7836d9f835c8008883b4498e9f9059d15046fffa4  ./YKQLrxBm
8d0ef5a09f3c7d2c53b05102ec310da982a9f80f4e7245cbd2b0dd1bcb7ca3d3  ./YdTZkUcM
92c6f0f7d5b6b3e49ff0a80a70cc0e0ea240d93ffb3f2b16d3256297009fc81c  ./Z2rLXuyp
bbb9828a718ff4acb2dfb6c1d2e7fb9859c0ab08cf19231f283a1272a30deaa5  ./ZWIiY84t
79756de813d20081cdeec93f250ed6c1c5e3227fb5ca50449bdb6a4524c8a5ab  ./ZXqAvkcE
9afa372ea66423e87cbe598d24c0204df5469b6a5ebe212bf4908d92a0a33012  ./ZdPbKJh1
fac637ed7be9b838b8c2271f16ff6af443fb1ffec8ae461e745fe9caef548395  ./ZyNsHVFW
3555a32edcd6c2e6a897e30d385024b8dddb07936f5215e607e4eff3d7a6968e  ./aGVRRt1d
e59a37e6cbf6ae588bcd3ce07d25a9be4075b4cb973c88cec6b54cc126378f08  ./aHFaEXKf
38bc37ce6e19d7b9c708cdcdbe547bf47a44172f163487a95f9d2675dc2e414f  ./aIz8E0Iy
42a1c939d12823b9f82b51aa339e044506ddb6541d34cd04084b5ed2f19407ea  ./afLk75aO
cc0b639c58eeb7ab4ac790e305e22a5246d0951d3b593449fbd4c45e11833539  ./b9YCg3Tz
ca28f9298674b2217360fb47228da2a617df218d626c2c9c5a6542f8d3dbed89  ./bDK7A26M
d25445621af9d59fe15eae4201def9609539b47e0e201d9ba60ad8895e00b53b  ./bDZN0f4B
e4c65fe85f5d7d9e666c7de5d95b4f0ce30c7b97975e350a37c392727593f6dd  ./bcZupFpi
7ce02d4ed1e0e8c97fbc3356719308d8d4b41b96ba4d2834a4b94aa26d6b324a  ./bjtBJwTc
7f337ae3bfc429add236eada122fe816835a932728cf3a496c2cfbff4ddd2eed  ./c3Z3JN0m
cb351a3cb1490b2346438a2786de87eb338f79ccdde6bac8670966b072e85e79  ./cIDWC9cb
65169f788002127de9830be22a8f370c47c491ebc1d1dcc36542a9ded3e05f48  ./dDoFZTXh
41b79a68cf05b8d4a12f57b4bd70e732576bd2776d5076d31dcc80dd233f6d8f  ./dKYP6pnk
247ef4efa81de114a42715e8858b3cb80dcbf348f3b6fb57d6394bac16bff8bf  ./dKisxYdK
c3b4d817a62b724a74bc7b9be2da210244bd050d66e6945ec980deba1540ed71  ./deppMJSV
c0092521bda4434cd5d32a719278468314c2c0472d415fa27260d8df7a855d97  ./dv0Mm4vr
71dc0430aa88d1b2a0cbae0c64483fdfa5ef85f112493d1ad04fe351b2008aa7  ./e1x51vcc
35172d545d8d903c648bfef1566d33178d46adc3043425a403b4407aef128760  ./e2umkBxy
cd4f7f5e780934f95a1ac4869f3cccd08d5a130e9d90686e5d44c79db95c4c12  ./e5b74XZq
0e502c2a53f0abb3ce5d7a171192d993df7846f33d9e5ca7a3af5b5a1ebcff62  ./eFlmUkb6
d9fa33fceaa1d31d5d8938d9169dd550e74f7edef05f8cf82858c87f6fae7423  ./eNfM7vPK
f2ad73aa8180c8d567d169aa0e87e2c6a8db4e90c6ffb93b9164173579ac2020  ./eZ4ehccg
80f1931b822c54008442928418681236d2a72c8a4d5fa45245b0156b3bf06918  ./efpcZmHN
d503e5c196a7d9d69128419c43fb3a77a15df6097ad34a255558e0656e802ecf  ./ekSs7xW4
541b17d13d6c7efa576697b47d066710971ca5fc427e1658e8488c62b803073d  ./eknrQKQh
bfd920efc7142fa3b4891cdb6a9da16307d43538783732053b31103d227b6391  ./fZHEnAvZ
413de10c45686255cd91bfdf13fb1a66b8d4bee02d71217a7c160642d73f7d0b  ./g2E6RkkX
434f44181d65b07bb4f7ab10c83febeb2abc2fe9ce773d9dd0d61c14f0838878  ./g2nu6vlR
220efa03bd524830c9848f0211260d5efbb8b69b62fd118af92f3c751414f813  ./gLAo3J0D
e56af668ce5ff2f18d95f52b9a0b10f16b1fc87d3c1799010eef9b3f69916e04  ./gem657x8
525b34e1958f58cf2a9924396c397736822fd3670ef131dabca20ff439cf4e7c  ./hNqXyUX2
a5034d519c16a478f1d4a973f6a2b6a4da5ea15d0301769df7195386227ea522  ./hZxbAqts
8b7a6ae53567fec501bb43ea8a4b99ec75be6cee74b4d272aedffad2ad3ec1da  ./haNCaZmC
83951ccf210dcf6f2f766b55d0c023ea985ea1b2b04677bbf0469d00210bd000  ./iGwCDzaU
8956e000390770f99926dfedcfc2ad0d90ac3061837a740e96e3c25f6da6c69c  ./iILvZZya
835e13d9d30cee83024aa99ca20fc4a231322f26b4a183b0260abadb51543a1e  ./ih6levXk
106f9d6706bed8e7453ace5bc563ccae72b2f0cb043b1ec16264a66e39c2bc60  ./j1v0LBVe
1522cb9b7fe9f48f134b4d66bfdcd5dd6c8a480d57f45f22fabc1d4bdc73dc35  ./jIlhVDLw
9088ec7999737ade92edeab6dc84dcf51d3047540417db0a10d8c1de60f22ac6  ./jObn0z94
2b8e8484f51a247124b44791d2b1fed3f238ee759a011e3c8b33b5e5bfa270f5  ./jVkxEmtq
a35646f903213fe5fe11e93ceda3850e5ced5e01a2ffbaf29f2a07ca55e4c4b7  ./jVlaDg4q
24f2ef646fe901e6aa5dd29b9c8fbc9a9a4e4270cec543abfab636d3e6aec7a8  ./jcMzi4VO
b49916c0abafe51723e914bb6c9ebb7f8e31d55d01f5acb7064e3114e5eddd10  ./jdYv9CQ3
155fdb55a2e9ce04a72f3297783b85ee9bdf9b1e18d69514f73454255eae903e  ./jzmPaO2D
1412a158607aa0cdfde028fa9a74721bc8050292d7004613b676990c2dad1269  ./kDPV8ASY
9c3dae1e97d55922dc74f3acfc0545cb01d4a93f1c3ee3bcb911680d02a74a81  ./kKVvPy8S
846514c0523d3b28ccd0c181f7043b2ccdf68dc16b4f12d320bc26fc0b9c1506  ./kWjYWiLD
9d61654933a16b4c8651401948bd25619128bc9ff42a165007ab2351ab93f0c4  ./kZ6DTcql
7a8bead57c2034417e8ebe4abda6a2496b8f91806c63a7251e17cb2806d97a55  ./kbumrMcy
3c8179a6177278404be0c99dc525fab3a05641349536ae597e350245025e852f  ./knHTEYup
9d028a67d434299587211e0d02906bb018a4b722a9d9d32c2af7eb6c40af7181  ./ksIZWNZR
d8a80350572a9d7d4b75d02f6337bb4c1b8224d98525d3a99bcc8dc1bb738c0d  ./lZiPMwX4
2a8b6c2c8c1e1a60d02a68efbfd3cb03f35bd88554882bd4bfe08ab3e9e67dc7  ./lcYptJNC
0faa0b43ffa46bffb8d9f3891c530ee3624ab07d16efaa34b850458afbb482d1  ./ld12od7V
044c50dc2f071577ff85c824e07b9b080fa81f95b935afe972806c193da53717  ./lmr9cGCE
d8f102814eb69aea7388dff5e659ababe3076a13b66a27ae1d408a0796161394  ./lxv6mvZ6
dabaf4a7d09ef43aaa573af8c1ba1175538acd3a452ce962cab962219ed0cc1e  ./m1NnTZoo
8d4b8ae492e1ad6d585c787a71f1f1c243193d07c52879f48c4cb669c0c07ef4  ./m3bsNhyN
1374bf2b59cd10700f6b5fa31a345beaf8e66ad8bc54397da0c1ea0de6f80238  ./mWWBZCgt
51ea91abe82fc259384bc60a87980d758a92313f059c381ab0647bad8afb4251  ./mdFDpW9k
d47abb4785e109e5b3ac637d7e38f879b94778960ad0c881415fac65e0cd8a31  ./n2XnM9Nc
62e489745042be31791f56c0a2eab8b21a73e30b59b72d32190378506701d75e  ./n7Vs8Bjh
1947091cb4d18a902d5a3a8fc5e4d3ac98df2b302769bf5991ed4bdcfd15c1a3  ./n8r2Ejk9
f3e5d278a6af6778eea75b1614392ba9601a910b6a52820d99c3ef069eb5b8c7  ./nldOsSfJ
f2165b2af46c6abc20182dee5fb660eabd92500971ad0e1636ec8b7218fff124  ./nnZ33FAt
5377e26a1fb07509b64298fe29ef2dfaaf89d49a1a98dff6dbac929edbbd41aa  ./nrwKQbJk
adfcaf453606125668b6199736f6091bf31c89ebc65e52f163c54b3cdfea0358  ./oNnB9jru
d3ff67d8c1a44dd0bd56138645b64a168a58c81dd59f3e475fac2fd042cf67e2  ./oi96tAtc
8755116bc7221404a47e148d44ce9675a9a9de4772664c173a6739b28b6a7625  ./oiy29oCW
b65b708a20c306eb16f98a900fa1af4927de2e3d339080ea2f5ae8e2f1a4a345  ./p1LgEQdu
8b58b8b04fce542c060fa1bbdc3a0bb1b3eca02ee03292fbc51971ad07e1c896  ./p5INCxLV
4a2064251e613059ab39eef036bfeb572fc97f454b2b6e1043170fb571796dff  ./p5INQHq8
1aec310ec4f09e6204c3b541b022e23866a0c032520f9be7efd605efdfe6f145  ./pXJHJUbH
63ff4276aea63fdfac53eb3f1d1d16755146467043152b16128df917cb467e6d  ./pb1E0Y3Z
0fcd8c83c1cd7a9f3ced98348a7d6431fb7bf92277fb27327cbe1f76a2faddf3  ./pnycz11G
10e26ea7ebb016313d3df66b6b1d9007baaa52b2cab1aadafd049c4bd6a72342  ./q53EoTzu
3d52f856d49e28d972bdbb42032cdf51d45ddbe7e86e92fcdf8a2957a7471937  ./qCTrc9yM
42f969b6bbc2e71c52710d46ef20b7094346341c68025e25b6310de6546ee8fa  ./qHwcKaSC
6bcfee18f65c7fc5252d9dcdce7d27cfc0e4991e0ca745c513fa18c3dd833a9c  ./qK35XlHM
58f5b74220c263ee37af886502c88c8eb004272412a75f6acd38be309378085e  ./qSn3WAyi
291ab311b7ad9ef32243461e981320b2c91b5b24bc24ecc7c6b611ad4b5ce2b1  ./qV83Dmye
dbe973977a5b530fedb14343c1932a5286e166fae90fbb6d1a23209643af0cb4  ./qWv24Da7
3e443f157b2164bc9c8c43843fef24e414ba20c6946c813bde3f9f8461c33b47  ./qZ7TLGA0
ef709efc8f558e5af0c5cef8c9fa154c940d62f374b141bd4fb50b618fa65877  ./qojIz6XF
ec189f22f55e456aacbab680a4e43c29c80264e84ca61a1bfa56acf4b168737b  ./r3HVTaJd
60a9dcad0900b025fd8509a80e96bdf1e70e3a4043b87c1968d0e9ff800826e4  ./r3Pw8pFI
cf0850306755e76bd61b57c3d299725037f17ec91a94910e22ed6b381b9a99cd  ./r8vIZE1F
37ad65cea695690849d23ae80c48fd6cb98a7c5351f0d9c6bbce3215bedda2b2  ./rzYX4BnS
929133170fb7e7bb7705175272f5e0fed5f7c3a1968a1a95c9b2e9227e190ae8  ./s9TOeOaJ
d7ba74c30417a8fa8d75ace89bad744e4e2cb5386a677a01410275cee1cc4306  ./sAy34VP4
4d24c1d1587b6ae0985c17adb50cd7c89f69a742593c4146bff5f4fb0568f8b8  ./sKi8TaSn
851fe75e8171d89b51fc9731a7871dd20c774b9dd5be715ddd0c95c572ead28a  ./sNI2Q6oa
1fc54184bd32bcb0776a959d5614a7a5eadb8b0f1bbcf4313574590131ec3c74  ./sRaKyq1f
2971a72cb19c0c855bd148ab2d59a424394e8daf1a0dced47e50338d024af4cf  ./svmptIxV
61e19a5a1f9429fb82e1bb0e544844896d3167ad3f9a11b6338efb39190a5b31  ./tFGQywwr
a5bf4a1b98570d489e5cddb9dfc88ed589981185a324b17b0caefd871bbc2ff0  ./tY2epsSy
a99dc42310310d51839ad5659463172014581d1ce8f988aa2ee4ef2283d34abc  ./tuma818A
4c6377bd2fcf69bd6677a639906663f0c47641e600de7824cb33c3b2602b263f  ./uMpXxbqr
114a17fcc9a751a66edfc9021be66903b2f36658b87ad81f88fffd9c3907cfc6  ./uUI8gJNi
80aa21d1a0c1c034810743492943605d430004281ff3bf9bbfbe3f716d7b9a61  ./ugeJ5RN3
cb8e1928fabadeb2f0dca057fecfab50f5ea1929cd80bff203519973dea477a1  ./vJDrHtxo
8d8f9b7727d9b995571e128c6b8d2645ac8df2168e13e75333928904b5831e0a  ./vMv1M1qs
c4aa78fcce66be4f58daeccf5b077c19bf722bd3bce55dbe61272f638fc2de63  ./vWguQ8rQ
b2a7b466c80d9bffbd52e8dc37622fc3309201597be37e6966c1133ebfad5f59  ./vc1wGQhn
b2debd7cf7faec289563d66ea1371f8d93d0ea24c0e42ba15b37d8aa025521d0  ./vjypfsoh
b46069fe557cc25b722268081033d2b6eac6a364ea00f0e271a8493ebd660133  ./vsGKdf0J
1f67fb2ce9ad96af93b0fb83eb35c217069d70d9bbe65928f0bbcf699c1f0277  ./w1XGgnr9
c596e73ba6183b89c01cf6a9f9f9f98df78eed109f0e893deef58180414b35b9  ./w8DmFhfg
891c0da5110e5933bc854625950d338b2350641f36c1a59d311150676666b338  ./woaiQu5g
8a27e2c28d7bdf60c3da69efe0c4084e9fb345d76c9774b92984a5ed6648d735  ./wvhWmTPt
16af3f92614e4ff16ab56e46342383d4f5f5422d17ecdabeae3f2f2ac86e459a  ./xQJV5GcG
b3c9cf5714c747bdf5601027568f84f7c0b5d94d49d82529d21908ef1c841b76  ./xlqXOqhL
dddc54d46f35f75188dccfee040644609313bc76d219afe4a66d09a93bec3287  ./yACAaKqG
84ab7c7757ed092ef4fa18278deb3081d8ce5aab7b877a358b9a5d22f15a590a  ./yYRsKiUO
9a353d27c8d25e6da87373c8061e6654056594cff6b3169b339ad5c2c4b3ba5b  ./yg7uBent
d57464c26034e2cf5e85d233c6eadf73c314537d7af597f6b8c506e252b6b405  ./zYz6howf
e67abb530a5413dd203129f4cfcfe35e303ee749b2fe635e4d475990bd24b1a4  ./zjkul95p
f25e635561b48434f6fc1b85076a98c0f5c38e7c95163a4d37a1f94a5fd2b4f1  ./zoz7gvVr
ctf-player@pico-chall$ decrypt.sh ./00011a60
Error: './00011a60' is not a valid file. Look inside the 'files' folder with 'ls -R'!                                         
ctf-player@pico-chall$ cd ..
ctf-player@pico-chall$ ./decrypt.sh files/00011a60
picoCTF{trust_but_verify_00011a60}
ctf-player@pico-chall$ Connection to rhea.picoctf.net closed by remote host.
Connection to rhea.picoctf.net closed.

```