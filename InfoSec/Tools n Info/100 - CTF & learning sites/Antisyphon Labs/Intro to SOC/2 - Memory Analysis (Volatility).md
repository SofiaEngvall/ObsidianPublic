
https://github.com/KAISERaustin/IntroLabsRemastered/blob/master/IntroClassFiles/Tools/IntroClass/Memory/MemoryAnalysis(Volatility).md

we want root permissions
```sh
sudo su - 
```

Find pages in the memory that have read, write, and execute privileges
```sh
cd /opt/volatility3-1.0.0
python3 vol.py -f ./memdump.vmem windows.malfind.Malfid
```

network connections:
```sh
python3 vol.py -f ./memdump.vmem windows.netscan
```

processes:
```sh
python3 vol.py -f ./memdump.vmem windows.pslist
```

more details
```
python3 vol.py -f ./memdump.vmem windows.pstree
```

get info on a processes dlls
```sh
python3 vol.py -f ./memdump.vmem dlllist --pid 5452
```


### Lab output

```sh
┌──(kali㉿kali)-[~]
└─$ sudo su -
┏━(Message from Kali developers)
┃
┃ This is a cloud installation of Kali Linux. Learn more about
┃ the specificities of the various cloud images:
┃ ⇒ https://www.kali.org/docs/troubleshooting/common-cloud-setup/
┃
┗━(Run: “touch ~/.hushlogin” to hide this message)
┌──(root㉿kali)-[~]
└─# cd /opt/                 
                                                                                                                                                              
┌──(root㉿kali)-[/opt]
└─# ls -la           
total 460
drwxr-xr-x 20 root root   4096 Jun 14  2024 .
drwxr-xr-x 19 root root   4096 Feb  7 19:17 ..
drwxr-xr-x 10 root root   4096 Jun 12  2024 JohnTheRipper
drwxr-xr-x  2 root root   4096 Jun 13  2024 LinuxCLI
drwxr-xr-x  2 root root   4096 Jun 13  2024 Password_Cracking
drwxr-xr-x  9 root root   4096 Jun 12  2024 Responder
drwxr-xr-x  3 root root   4096 Jun 12  2024 WebTrap
drwxr-xr-x  2 root root   4096 Jun 14  2024 Web_Testing
drwxr-xr-x  2 root root   4096 Jun 12  2024 covert
drwxr-xr-x 13 root root   4096 Jun 12  2024 cowrie
drwxr-xr-x  2 root root   4096 Jun 13  2024 firewall_log
drwxr-xr-x  5 root root   4096 Jun 12  2024 honeybadger
drwxr-xr-x  3 root root   4096 Jun 12  2024 honeyports
drwxr-xr-x 10 root root   4096 Jun 12  2024 impacket
drwxr-xr-x  3 root root   4096 May  5  2022 microsoft
drwxr-xr-x  8 root root   4096 Jun 12  2024 owa-honeypot
drwxr-xr-x  8 root root   4096 Jun 12  2024 portspoof
drwxr-xr-x  3 root root   4096 Jun 12  2024 spidertrap
drwxr-xr-x  2 root root   4096 Jun 13  2024 tcpdump
drwxrwxr-x  6 root root   4096 Jun 13  2024 volatility3-1.0.0
-rw-r--r--  1 root root 388314 Jun 13  2024 volatility3-1.0.0.tar.gz
                                                                                                                                                              
┌──(root㉿kali)-[/opt]
└─# cd volatility3-1.0.0 
                                                                                                                                          
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# ls -la
total 1048684
drwxrwxr-x  6 root root       4096 Jun 13  2024 .
drwxr-xr-x 20 root root       4096 Jun 14  2024 ..
drwxrwxr-x  4 root root       4096 Feb  1  2021 .github
-rw-rw-r--  1 root root        394 Feb  1  2021 .gitignore
-rw-rw-r--  1 root root        532 Feb  1  2021 .readthedocs.yml
-rw-rw-r--  1 root root       7940 Feb  1  2021 .style.yapf
-rw-rw-r--  1 root root       3920 Feb  1  2021 LICENSE.txt
-rw-rw-r--  1 root root        180 Feb  1  2021 MANIFEST.in
-rw-rw-r--  1 root root       5001 Feb  1  2021 README.md
drwxrwxr-x  4 root root       4096 Jun 17  2024 development
drwxrwxr-x  3 root root       4096 Feb  1  2021 doc
-rwxr-xr-x  1 root root 1073741824 Jun 13  2024 memdump.vmem
-rw-rw-r--  1 root root         79 Feb  1  2021 mypy.ini
-rw-rw-r--  1 root root       2089 Feb  1  2021 setup.py
-rwxrwxr-x  1 root root        290 Feb  1  2021 vol.py
-rw-rw-r--  1 root root       5423 Feb  1  2021 vol.spec
drwxrwxr-x  8 root root       4096 Jun 13  2024 volatility3
-rw-rw-r--  1 root root        297 Feb  1  2021 volshell.py
-rw-rw-r--  1 root root       2963 Feb  1  2021 volshell.spec
                                                                                                                                                              
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# python3 vol.py -f ./memdump.vmem windows.malfind.Malfind
Volatility 3 Framework 1.0.0
Progress:  100.00PDB scanning finished                     
PIDProcessStart VPNEnd VPNTagProtectionCommitChargePrivateMemoryFile outputHexdumpDisasm

5452TrustMe.exe0x4500000x480fffVadSPAGE_EXECUTE_READWRITE491Disabled
4d 5a e8 00 00 00 00 5bMZ.....[
52 45 55 89 e5 81 c3 93REU.....
45 00 00 ff d3 81 c3 66E......f
62 02 00 89 3b 53 6a 04b...;Sj.
50 ff d0 00 00 00 00 00P.......
00 00 00 00 00 00 00 00........
00 00 00 00 00 00 00 00........
00 00 00 00 f8 00 00 00........
0x450000:decebp
0x450001:popedx
0x450002:call0x450007
0x450007:popebx
0x450008:pushedx
0x450009:incebp
0x45000a:pushebp
0x45000b:movebp, esp
0x45000d:addebx, 0x4593
0x450013:callebx
0x450015:addebx, 0x26266
0x45001b:movdword ptr [ebx], edi
0x45001d:pushebx
0x45001e:push4
0x450020:pusheax
0x450021:calleax
0x450023:addbyte ptr [eax], al
0x450025:addbyte ptr [eax], al
0x450027:addbyte ptr [eax], al
0x450029:addbyte ptr [eax], al
0x45002b:addbyte ptr [eax], al
0x45002d:addbyte ptr [eax], al
0x45002f:addbyte ptr [eax], al
0x450031:addbyte ptr [eax], al
0x450033:addbyte ptr [eax], al
0x450035:addbyte ptr [eax], al
0x450037:addbyte ptr [eax], al
0x450039:addbyte ptr [eax], al
0x45003b:addal, bh
0x45003d:addbyte ptr [eax], al
5452TrustMe.exe0x5100000x56efffVadSPAGE_EXECUTE_READWRITE951Disabled
4d 5a 90 00 03 00 00 00MZ......
04 00 00 00 ff ff 00 00........
b8 00 00 00 00 00 00 00........
40 00 00 00 00 00 00 00@.......
00 00 00 00 00 00 00 00........
00 00 00 00 00 00 00 00........
00 00 00 00 00 00 00 00........
00 00 00 00 f8 00 00 00........
0x510000:decebp
0x510001:popedx
0x510002:nop
0x510003:addbyte ptr [ebx], al
0x510005:addbyte ptr [eax], al
0x510007:addbyte ptr [eax + eax], al
0x51000a:addbyte ptr [eax], al
5452TrustMe.exe0x8400000x85ffffVadSPAGE_EXECUTE_READWRITE321Disabled
4d 5a 90 00 03 00 00 00MZ......
04 00 00 00 ff ff 00 00........
b8 00 00 00 00 00 00 00........
40 00 00 00 00 00 00 00@.......
00 00 00 00 00 00 00 00........
00 00 00 00 00 00 00 00........
00 00 00 00 00 00 00 00........
00 00 00 00 e0 00 00 00........
0x840000:decebp
0x840001:popedx
0x840002:nop
0x840003:addbyte ptr [ebx], al
0x840005:addbyte ptr [eax], al
0x840007:addbyte ptr [eax + eax], al
0x84000a:addbyte ptr [eax], al
1124SearchUI.exe0x25a1d0300000x25a1d04ffffVadSPAGE_EXECUTE_READWRITE21Disabled
48 89 54 24 10 48 89 4cH.T$.H.L
24 08 4c 89 44 24 18 4c$.L.D$.L
89 4c 24 20 48 8b 41 28.L$.H.A(
48 8b 50 60 48 83 e2 f8H.P`H...
48 8b ca 48 b8 58 00 03H..H.X..
1d 5a 02 00 00 48 2b c8.Z...H+.
48 81 f9 78 0f 00 00 76H..x...v
09 48 c7 c1 05 00 00 00.H......
0x25a1d030000:movqword ptr [rsp + 0x10], rdx
0x25a1d030005:movqword ptr [rsp + 8], rcx
0x25a1d03000a:movqword ptr [rsp + 0x18], r8
0x25a1d03000f:movqword ptr [rsp + 0x20], r9
0x25a1d030014:movrax, qword ptr [rcx + 0x28]
0x25a1d030018:movrdx, qword ptr [rax + 0x60]
0x25a1d03001c:andrdx, 0xfffffffffffffff8
0x25a1d030020:movrcx, rdx
0x25a1d030023:movabsrax, 0x25a1d030058
0x25a1d03002d:subrcx, rax
0x25a1d030030:cmprcx, 0xf78
0x25a1d030037:jbe0x25a1d030042
0x25a1d030039:movrcx, 5
                                                                                                                                                          
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# python3 vol.py -f ./memdump.vmem windows.netscan        
Volatility 3 Framework 1.0.0
Progress:  100.00PDB scanning finished                     
OffsetProtoLocalAddrLocalPortForeignAddrForeignPortStatePIDOwnerCreated

0xa98dc808bec0TCPv40.0.0.015370.0.0.00LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xa98dc808e010TCPv40.0.0.015380.0.0.00LISTENING872svchost.exe2020-11-30 17:40:29.000000 
0xa98dc808e010TCPv6::1538::0LISTENING872svchost.exe2020-11-30 17:40:29.000000 
0xa98dc8095010TCPv40.0.0.015370.0.0.00LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xa98dc8095010TCPv6::1537::0LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xa98dc80b0b80UDPv4192.168.192.145138*04System2020-11-30 17:40:29.000000 
0xa98dc824e260TCPv40.0.0.059850.0.0.00LISTENING4System2020-11-30 17:42:35.000000 
0xa98dc824e260TCPv6::5985::0LISTENING4System2020-11-30 17:42:35.000000 
0xa98dc84e1220UDPv40.0.0.05355*01320svchost.exe2020-11-30 20:40:29.000000 
0xa98dc93576f0UDPv40.0.0.062883*01320svchost.exe2020-11-30 18:40:29.000000 
0xa98dc93576f0UDPv6::62883*01320svchost.exe2020-11-30 18:40:29.000000 
0xa98dc97c1710UDPv40.0.0.03702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dc97c1710UDPv6::3702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dc98e10e0TCPv40.0.0.015380.0.0.00LISTENING872svchost.exe2020-11-30 17:40:29.000000 
0xa98dc9ae3420UDPv40.0.0.00*01952svchost.exe2020-11-30 17:40:31.000000 
0xa98dc9ae3420UDPv6::0*01952svchost.exe2020-11-30 17:40:31.000000 
0xa98dc9ae3740UDPv40.0.0.00*01952svchost.exe2020-11-30 17:40:31.000000 
0xa98dc9ae8a80UDPv40.0.0.00*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dc9ae8a80UDPv6::0*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dc9b0f880UDPv40.0.0.05353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dc9b0f880UDPv6::5353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dc9b604c0TCPv40.0.0.0220.0.0.00LISTENING2136svchost.exe2020-11-30 17:40:32.000000 
0xa98dc9b604c0TCPv6::22::0LISTENING2136svchost.exe2020-11-30 17:40:32.000000 
0xa98dc9c21420UDPv40.0.0.05355*01320svchost.exe2020-11-30 19:25:29.000000 
0xa98dc9c21880TCPv40.0.0.015650.0.0.00LISTENING768lsass.exe2020-11-30 17:40:38.000000 
0xa98dc9c21880TCPv6::1565::0LISTENING768lsass.exe2020-11-30 17:40:38.000000 
0xa98dc9c21b60TCPv40.0.0.015650.0.0.00LISTENING768lsass.exe2020-11-30 17:40:38.000000 
0xa98dc9c341f0TCPv4192.168.192.1451605192.168.192.146445ESTABLISHED4System2020-11-30 17:44:38.000000 
0xa98dc9c50490TCPv4192.168.192.1451716172.104.59.604444CLOSED5452TrustMe.exe2020-11-30 20:46:30.000000 
0xa98dc9cbd5c0TCPv40.0.0.0470010.0.0.00LISTENING4System2020-11-30 17:42:35.000000 
0xa98dc9cbd5c0TCPv6::47001::0LISTENING4System2020-11-30 17:42:35.000000 
0xa98dc9d756c0UDPv40.0.0.05355*01320svchost.exe2020-11-30 18:40:29.000000 
0xa98dc9da6590TCPv4192.168.192.1451697204.79.197.200443CLOSED1124SearchUI.exe2020-11-30 18:40:39.000000 
0xa98dc9daeec0UDPv4169.254.183.70138*04System2020-11-30 17:40:37.000000 
0xa98dc9daf480UDPv4169.254.183.70137*04System2020-11-30 17:40:37.000000 
0xa98dc9daf8a0UDPv4127.0.0.11900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9db2940UDPv4192.168.192.14560730*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9db64e0UDPv4169.254.183.7060731*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9dcabf0UDPv6::160729*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9dcbb80TCPv4169.254.183.701390.0.0.00LISTENING4System2020-11-30 17:40:37.000000 
0xa98dc9e05a40TCPv4192.168.192.1451390.0.0.00LISTENING4System2020-11-30 17:40:29.000000 
0xa98dc9e08b50UDPv4192.168.192.145137*04System2020-11-30 17:40:29.000000 
0xa98dc9e8c0c0UDPv40.0.0.05353*01320svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9ed56e0UDPv40.0.0.05353*01320svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9ed56e0UDPv6::5353*01320svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9edaec0UDPv40.0.0.00*01320svchost.exe2020-11-30 17:40:37.000000 
0xa98dc9edaec0UDPv6::0*01320svchost.exe2020-11-30 17:40:37.000000 
0xa98dca053460TCPv40.0.0.015360.0.0.00LISTENING664wininit.exe2020-11-30 17:40:28.000000 
0xa98dca054010TCPv40.0.0.015360.0.0.00LISTENING664wininit.exe2020-11-30 17:40:28.000000 
0xa98dca054010TCPv6::1536::0LISTENING664wininit.exe2020-11-30 17:40:28.000000 
0xa98dca184ec0TCPv40.0.0.01350.0.0.00LISTENING896svchost.exe2020-11-30 17:40:28.000000 
0xa98dca18bc00TCPv40.0.0.01350.0.0.00LISTENING896svchost.exe2020-11-30 17:40:28.000000 
0xa98dca18bc00TCPv6::135::0LISTENING896svchost.exe2020-11-30 17:40:28.000000 
0xa98dca321780UDPv40.0.0.05353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dca321780UDPv6::5353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dca330be0TCPv4192.168.192.1451716172.104.59.604444SYN_SENT5452TrustMe.exe2020-11-30 20:46:30.000000 
0xa98dca339430UDPv40.0.0.05353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dca41fb20UDPv40.0.0.056986*01320svchost.exe2020-11-30 20:50:11.000000 
0xa98dca41fb20UDPv6::56986*01320svchost.exe2020-11-30 20:50:11.000000 
0xa98dca460b90TCPv4192.168.192.1451698204.79.197.200443CLOSED1124SearchUI.exe2020-11-30 18:40:39.000000 
0xa98dca49e2c0UDPv40.0.0.05353*04160chrome.exe2020-11-30 17:42:43.000000 
0xa98dca4a46a0TCPv4192.168.192.145169252.242.211.89443ESTABLISHED608svchost.exe2020-11-30 18:28:16.000000 
0xa98dca52c820UDPv40.0.0.05355*01320svchost.exe2020-11-30 19:10:29.000000 
0xa98dca5ec6f0UDPv40.0.0.055107*01320svchost.exe2020-11-30 18:40:29.000000 
0xa98dca5ec6f0UDPv6::55107*01320svchost.exe2020-11-30 18:40:29.000000 
0xa98dca5f0950TCPv4192.168.192.1451700172.104.59.604444CLOSED5452TrustMe.exe2020-11-30 18:45:35.000000 
0xa98dca6e1ca0UDPv40.0.0.05355*01320svchost.exe2020-11-30 20:40:29.000000 
0xa98dca6e1ca0UDPv6::5355*01320svchost.exe2020-11-30 20:40:29.000000 
0xa98dcaac6110TCPv40.0.0.053570.0.0.00LISTENING4System2020-11-30 17:40:30.000000 
0xa98dcaac6110TCPv6::5357::0LISTENING4System2020-11-30 17:40:30.000000 
0xa98dcaad9d30UDPv40.0.0.03702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcaaea520UDPv40.0.0.03702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcaaeb5c0UDPv40.0.0.03702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcaaeb5c0UDPv6::3702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcaaec7b0UDPv40.0.0.03702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcaaec7b0UDPv6::3702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcaaed1a0UDPv40.0.0.064435*01792svchost.exe2020-11-30 17:40:30.000000 
0xa98dcaaee610UDPv40.0.0.064436*01792svchost.exe2020-11-30 17:40:30.000000 
0xa98dcaaee610UDPv6::64436*01792svchost.exe2020-11-30 17:40:30.000000 
0xa98dcab19880UDPv40.0.0.0500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab1aec0UDPv40.0.0.04500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab1bec0UDPv40.0.0.0500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab1bec0UDPv6::500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab1cec0UDPv40.0.0.04500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab1cec0UDPv6::4500*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab36ec0UDPv40.0.0.00*0608svchost.exe2020-11-30 17:40:31.000000 
0xa98dcab3ca90TCPv40.0.0.04450.0.0.00LISTENING4System2020-11-30 17:40:31.000000 
0xa98dcab3ca90TCPv6::445::0LISTENING4System2020-11-30 17:40:31.000000 
0xa98dcb7b5900UDPv40.0.0.03702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dcb7d08d0TCPv40.0.0.015490.0.0.00LISTENING760services.exe2020-11-30 17:40:33.000000 
0xa98dcb7d0a20TCPv40.0.0.015490.0.0.00LISTENING760services.exe2020-11-30 17:40:33.000000 
0xa98dcb7d0a20TCPv6::1549::0LISTENING760services.exe2020-11-30 17:40:33.000000 
0xa98dcb7d3ec0UDPv40.0.0.03702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dcb7d4010UDPv6::11900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcb7d7010UDPv6fe80::b562:351a:c3db:b7461900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcb7dea00UDPv40.0.0.03702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dcb7dea00UDPv6::3702*02372dasHost.exe2020-11-30 17:40:37.000000 
0xa98dcb7ec750UDPv40.0.0.03702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc17de10TCPv40.0.0.0220.0.0.00LISTENING2136svchost.exe2020-11-30 17:40:32.000000 
0xa98dcc180310TCPv40.0.0.015390.0.0.00LISTENING1952svchost.exe2020-11-30 17:40:32.000000 
0xa98dcc180310TCPv6::1539::0LISTENING1952svchost.exe2020-11-30 17:40:32.000000 
0xa98dcc180c70TCPv40.0.0.015390.0.0.00LISTENING1952svchost.exe2020-11-30 17:40:32.000000 
0xa98dcc189d00TCPv4192.168.192.145170523.206.169.12180CLOSED1320svchost.exe2020-11-30 19:26:34.000000 
0xa98dcc197a70UDPv4127.0.0.160732*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcc1a1010UDPv40.0.0.03702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1a1010UDPv6::3702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1a1250UDPv40.0.0.03702*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1b2200UDPv40.0.0.063029*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1b2200UDPv6::63029*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1b2cf0UDPv40.0.0.063028*01180svchost.exe2020-11-30 17:41:34.000000 
0xa98dcc1cad30UDPv40.0.0.05050*01180svchost.exe2020-11-30 17:40:33.000000 
0xa98dcc1d7600UDPv6fe80::9d74:69:a81a:95a660727*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dcc1d7750UDPv6fe80::b562:351a:c3db:b74660728*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccb743e0UDPv4169.254.183.701900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccb74530UDPv4192.168.192.1451900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccb91850UDPv40.0.0.03702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccb91850UDPv6::3702*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccb959d0UDPv6fe80::9d74:69:a81a:95a61900*01792svchost.exe2020-11-30 17:40:37.000000 
0xa98dccbf2530UDPv40.0.0.050512*02372dasHost.exe2020-11-30 17:40:33.000000 
0xa98dccbf6ec0UDPv40.0.0.050513*02372dasHost.exe2020-11-30 17:40:33.000000 
0xa98dccbf6ec0UDPv6::50513*02372dasHost.exe2020-11-30 17:40:33.000000 
0xf3800008bec0TCPv40.0.0.015370.0.0.00LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xf3800008e010TCPv40.0.0.015380.0.0.00LISTENING872svchost.exe2020-11-30 17:40:29.000000 
0xf3800008e010TCPv6::1538::0LISTENING872svchost.exe2020-11-30 17:40:29.000000 
0xf38000095010TCPv40.0.0.015370.0.0.00LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xf38000095010TCPv6::1537::0LISTENING608svchost.exe2020-11-30 17:40:29.000000 
0xf380000b0b80UDPv4192.168.192.145138*04System2020-11-30 17:40:29.000000 
                                                                                                                                                              
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# python3 vol.py -f ./memdump.vmem windows.pslist 
Volatility 3 Framework 1.0.0
Progress:  100.00PDB scanning finished                     
PIDPPIDImageFileNameOffset(V)ThreadsHandlesSessionIdWow64CreateTimeExitTimeFile output

40System0xa98dc80576c085-N/AFalse2020-11-30 17:40:26.000000 N/ADisabled
5124smss.exe0xa98dc98364802-N/AFalse2020-11-30 17:40:26.000000 N/ADisabled
588580csrss.exe0xa98dc9a560809-0False2020-11-30 17:40:27.000000 N/ADisabled
656512smss.exe0xa98dc98e60800-1False2020-11-30 17:40:27.000000 2020-11-30 17:40:27.000000 Disabled
664580wininit.exe0xa98dc9f748001-0False2020-11-30 17:40:27.000000 N/ADisabled
672656csrss.exe0xa98dca06b08011-1False2020-11-30 17:40:27.000000 N/ADisabled
744656winlogon.exe0xa98dca06a3402-1False2020-11-30 17:40:27.000000 N/ADisabled
760664services.exe0xa98dca0f10804-0False2020-11-30 17:40:27.000000 N/ADisabled
768664lsass.exe0xa98dca0f80807-0False2020-11-30 17:40:27.000000 N/ADisabled
856760svchost.exe0xa98dca15280016-0False2020-11-30 17:40:28.000000 N/ADisabled
896760svchost.exe0xa98dca17e80010-0False2020-11-30 17:40:28.000000 N/ADisabled
988744dwm.exe0xa98dca1c808011-1False2020-11-30 17:40:28.000000 N/ADisabled
608760svchost.exe0xa98dcab7a80056-0False2020-11-30 17:40:28.000000 N/ADisabled
756760svchost.exe0xa98dcab9780023-0False2020-11-30 17:40:28.000000 N/ADisabled
872760svchost.exe0xa98dcaba880018-0False2020-11-30 17:40:28.000000 N/ADisabled
976760svchost.exe0xa98dcabb180013-0False2020-11-30 17:40:28.000000 N/ADisabled
1180760svchost.exe0xa98dc809480019-0False2020-11-30 17:40:29.000000 N/ADisabled
1204760vmacthlp.exe0xa98dc80be0801-0False2020-11-30 17:40:29.000000 N/ADisabled
1320760svchost.exe0xa98dc9e1880024-0False2020-11-30 17:40:29.000000 N/ADisabled
1420760svchost.exe0xa98dc9e3f8005-0False2020-11-30 17:40:29.000000 N/ADisabled
1472760svchost.exe0xa98dc9ead8009-0False2020-11-30 17:40:29.000000 N/ADisabled
1792760svchost.exe0xa98dcaa8580012-0False2020-11-30 17:40:30.000000 N/ADisabled
1952760svchost.exe0xa98dcab011404-0False2020-11-30 17:40:30.000000 N/ADisabled
1052760svchost.exe0xa98dcab5280011-0False2020-11-30 17:40:31.000000 N/ADisabled
1372760svchost.exe0xa98dcac111805-0False2020-11-30 17:40:31.000000 N/ADisabled
1600760svchost.exe0xa98dcac294c02-0False2020-11-30 17:40:31.000000 N/ADisabled
1784760vmtoolsd.exe0xa98dcac2a5409-0False2020-11-30 17:40:31.000000 N/ADisabled
1928760VGAuthService.0xa98dc9ab83002-0False2020-11-30 17:40:31.000000 N/ADisabled
2136760svchost.exe0xa98dc9b508004-0False2020-11-30 17:40:31.000000 N/ADisabled
2372976dasHost.exe0xa98dc9b630803-0False2020-11-30 17:40:32.000000 N/ADisabled
2416856WmiPrvSE.exe0xa98dcc1a25409-0False2020-11-30 17:40:32.000000 N/ADisabled
2584760dllhost.exe0xa98dcc1ec80010-0False2020-11-30 17:40:32.000000 N/ADisabled
2772760msdtc.exe0xa98dccbf08009-0False2020-11-30 17:40:33.000000 N/ADisabled
3360608sihost.exe0xa98dca6125c07-1False2020-11-30 17:41:11.000000 N/ADisabled
3376760svchost.exe0xa98dca6468005-1False2020-11-30 17:41:11.000000 N/ADisabled
3444608taskhostw.exe0xa98dca66780012-1False2020-11-30 17:41:11.000000 N/ADisabled
3596744userinit.exe0xa98dca6be8000-1False2020-11-30 17:41:11.000000 2020-11-30 17:41:32.000000 Disabled
36163596explorer.exe0xa98dca6d348038-1False2020-11-30 17:41:11.000000 N/ADisabled
3680856RuntimeBroker.0xa98dca6e080011-1False2020-11-30 17:41:11.000000 N/ADisabled
3944856ShellExperienc0xa98dca7a008026-1False2020-11-30 17:41:12.000000 N/ADisabled
43403616vmtoolsd.exe0xa98dc9e6f5807-1False2020-11-30 17:41:27.000000 N/ADisabled
1728856SkypeHost.exe0xa98dca1e308010-1False2020-11-30 17:42:37.000000 N/ADisabled
41603616chrome.exe0xa98dc9c8e80030-1False2020-11-30 17:42:39.000000 N/ADisabled
7884160chrome.exe0xa98dca52e0805-1False2020-11-30 17:42:42.000000 N/ADisabled
42644160chrome.exe0xa98dc9d8b0802-1False2020-11-30 17:42:43.000000 N/ADisabled
36084160chrome.exe0xa98dca5830804-1False2020-11-30 17:42:43.000000 N/ADisabled
46684160chrome.exe0xa98dccc268008-1False2020-11-30 17:43:02.000000 N/ADisabled
54523616TrustMe.exe0xa98dc93078001-1True2020-11-30 17:43:17.000000 N/ADisabled
55285452cmd.exe0xa98dca6bd0801-1True2020-11-30 17:43:27.000000 N/ADisabled
55365528conhost.exe0xa98dca6ba0803-1False2020-11-30 17:43:27.000000 N/ADisabled
59845528net.exe0xa98dcc17a0800-1True2020-11-30 17:44:38.000000 2020-11-30 17:44:38.000000 Disabled
58483616cmd.exe0xa98dcaa2e0801-1False2020-11-30 17:54:17.000000 N/ADisabled
57085848conhost.exe0xa98dca65b8003-1False2020-11-30 17:54:17.000000 N/ADisabled
3228856dllhost.exe0xa98dc9edb0802-1False2020-11-30 18:25:05.000000 N/ADisabled
3728856ApplicationFra0xa98dca6f40803-1False2020-11-30 18:25:10.000000 N/ADisabled
4592856SystemSettings0xa98dca1b250010-1False2020-11-30 18:25:11.000000 N/ADisabled
1124856SearchUI.exe0xa98dca71e08032-1False2020-11-30 18:40:37.000000 N/ADisabled
                                                                                                                                                              
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# python3 vol.py -f ./memdump.vmem windows.pstree
Volatility 3 Framework 1.0.0
Progress:  100.00PDB scanning finished                     
PIDPPIDImageFileNameOffset(V)ThreadsHandlesSessionIdWow64CreateTimeExitTime

40System0xa98dca71e08085-N/AFalse2020-11-30 17:40:26.000000 N/A
* 5124smss.exe0xa98dca71e0802-N/AFalse2020-11-30 17:40:26.000000 N/A
** 656512smss.exe0xa98dca71e0800-1False2020-11-30 17:40:27.000000 2020-11-30 17:40:27.000000 
*** 672656csrss.exe0xa98dca71e08011-1False2020-11-30 17:40:27.000000 N/A
*** 744656winlogon.exe0xa98dca71e0802-1False2020-11-30 17:40:27.000000 N/A
**** 988744dwm.exe0xa98dca71e08011-1False2020-11-30 17:40:28.000000 N/A
**** 3596744userinit.exe0xa98dca71e0800-1False2020-11-30 17:41:11.000000 2020-11-30 17:41:32.000000 
***** 36163596explorer.exe0xa98dca71e08038-1False2020-11-30 17:41:11.000000 N/A
****** 41603616chrome.exe0xa98dca71e08030-1False2020-11-30 17:42:39.000000 N/A
******* 42644160chrome.exe0xa98dca71e0802-1False2020-11-30 17:42:43.000000 N/A
******* 36084160chrome.exe0xa98dca71e0804-1False2020-11-30 17:42:43.000000 N/A
******* 7884160chrome.exe0xa98dca71e0805-1False2020-11-30 17:42:42.000000 N/A
******* 46684160chrome.exe0xa98dca71e0808-1False2020-11-30 17:43:02.000000 N/A
****** 58483616cmd.exe0xa98dca71e0801-1False2020-11-30 17:54:17.000000 N/A
******* 57085848conhost.exe0xa98dca71e0803-1False2020-11-30 17:54:17.000000 N/A
****** 43403616vmtoolsd.exe0xa98dca71e0807-1False2020-11-30 17:41:27.000000 N/A
****** 54523616TrustMe.exe0xa98dca71e0801-1True2020-11-30 17:43:17.000000 N/A
******* 55285452cmd.exe0xa98dca71e0801-1True2020-11-30 17:43:27.000000 N/A
******** 55365528conhost.exe0xa98dca71e0803-1False2020-11-30 17:43:27.000000 N/A
******** 59845528net.exe0xa98dca71e0800-1True2020-11-30 17:44:38.000000 2020-11-30 17:44:38.000000 
588580csrss.exe0xa98dca71e0809-0False2020-11-30 17:40:27.000000 N/A
664580wininit.exe0xa98dca71e0801-0False2020-11-30 17:40:27.000000 N/A
* 760664services.exe0xa98dca71e0804-0False2020-11-30 17:40:27.000000 N/A
** 896760svchost.exe0xa98dca71e08010-0False2020-11-30 17:40:28.000000 N/A
** 1792760svchost.exe0xa98dca71e08012-0False2020-11-30 17:40:30.000000 N/A
** 1928760VGAuthService.0xa98dca71e0802-0False2020-11-30 17:40:31.000000 N/A
** 1420760svchost.exe0xa98dca71e0805-0False2020-11-30 17:40:29.000000 N/A
** 2584760dllhost.exe0xa98dca71e08010-0False2020-11-30 17:40:32.000000 N/A
** 1052760svchost.exe0xa98dca71e08011-0False2020-11-30 17:40:31.000000 N/A
** 1180760svchost.exe0xa98dca71e08019-0False2020-11-30 17:40:29.000000 N/A
** 1952760svchost.exe0xa98dca71e0804-0False2020-11-30 17:40:30.000000 N/A
** 1320760svchost.exe0xa98dca71e08024-0False2020-11-30 17:40:29.000000 N/A
** 3376760svchost.exe0xa98dca71e0805-1False2020-11-30 17:41:11.000000 N/A
** 1204760vmacthlp.exe0xa98dca71e0801-0False2020-11-30 17:40:29.000000 N/A
** 1472760svchost.exe0xa98dca71e0809-0False2020-11-30 17:40:29.000000 N/A
** 1600760svchost.exe0xa98dca71e0802-0False2020-11-30 17:40:31.000000 N/A
** 976760svchost.exe0xa98dca71e08013-0False2020-11-30 17:40:28.000000 N/A
*** 2372976dasHost.exe0xa98dca71e0803-0False2020-11-30 17:40:32.000000 N/A
** 2772760msdtc.exe0xa98dca71e0809-0False2020-11-30 17:40:33.000000 N/A
** 856760svchost.exe0xa98dca71e08016-0False2020-11-30 17:40:28.000000 N/A
*** 3680856RuntimeBroker.0xa98dca71e08011-1False2020-11-30 17:41:11.000000 N/A
*** 1728856SkypeHost.exe0xa98dca71e08010-1False2020-11-30 17:42:37.000000 N/A
*** 1124856SearchUI.exe0xa98dca71e08032-1False2020-11-30 18:40:37.000000 N/A
*** 3944856ShellExperienc0xa98dca71e08026-1False2020-11-30 17:41:12.000000 N/A
*** 2416856WmiPrvSE.exe0xa98dca71e0809-0False2020-11-30 17:40:32.000000 N/A
*** 3728856ApplicationFra0xa98dca71e0803-1False2020-11-30 18:25:10.000000 N/A
*** 4592856SystemSettings0xa98dca71e08010-1False2020-11-30 18:25:11.000000 N/A
*** 3228856dllhost.exe0xa98dca71e0802-1False2020-11-30 18:25:05.000000 N/A
** 2136760svchost.exe0xa98dca71e0804-0False2020-11-30 17:40:31.000000 N/A
** 1372760svchost.exe0xa98dca71e0805-0False2020-11-30 17:40:31.000000 N/A
** 608760svchost.exe0xa98dca71e08056-0False2020-11-30 17:40:28.000000 N/A
*** 3360608sihost.exe0xa98dca71e0807-1False2020-11-30 17:41:11.000000 N/A
*** 3444608taskhostw.exe0xa98dca71e08012-1False2020-11-30 17:41:11.000000 N/A
** 872760svchost.exe0xa98dca71e08018-0False2020-11-30 17:40:28.000000 N/A
** 756760svchost.exe0xa98dca71e08023-0False2020-11-30 17:40:28.000000 N/A
** 1784760vmtoolsd.exe0xa98dca71e0809-0False2020-11-30 17:40:31.000000 N/A
* 768664lsass.exe0xa98dca71e0807-0False2020-11-30 17:40:27.000000 N/A
                                                                                                                                                              
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# python3 vol.py -f ./memdump.vmem windows.dll --pid 5452
Volatility 3 Framework 1.0.0
Progress:  100.00PDB scanning finished                     
PIDProcessBaseSizeNamePathLoadTimeFile output

5452TrustMe.exe0x4000000x16000TrustMe.exeC:\Users\Sec504\Downloads\TrustMe.exe2020-11-30 17:43:17.000000 Disabled
5452TrustMe.exe0x7ffaf62900000x1d1000--2020-11-30 17:43:17.000000 Disabled
5452TrustMe.exe0x594e00000x52000wow64.dllC:\Windows\System32\wow64.dll2020-11-30 17:43:17.000000 Disabled
5452TrustMe.exe0x595400000x77000wow64win.dllC:\Windows\System32\wow64win.dll2020-11-30 17:43:17.000000 Disabled
5452TrustMe.exe0x594d00000xa000wow64cpu.dllC:\Windows\System32\wow64cpu.dll2020-11-30 17:43:17.000000 Disabled
                                                                                                                                                              
┌──(root㉿kali)-[/opt/volatility3-1.0.0]
└─# 
```

