
cmd windows
```
c:\r2w32\bin>r2 -d -A c:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper\gatekeeper.exe
INFO: Spawned new process with pid 7572, tid = 2376
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze imports (af@@@i)
INFO: Analyze entrypoint (af@ entry0)
INFO: Analyze symbols (af@@@s)
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Analyzing methods (af @@ method.*)
INFO: Recovering local variables (afva@@@F)
INFO: Skipping type matching analysis in debugger mode (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Use -AA or aaaa to perform additional experimental analysis
[0x77d255b0]> afl
0x08041a48   21    329 entry0
0x08041230   16    564 main
[0x77d255b0]> dc
(7572) loading library at 0x77CB0000 (C:\Windows\SysWOW64\ntdll.dll) ntdll.dll
(7572) loading library at 0x761F0000 (C:\Windows\SysWOW64\kernel32.dll) kernel32.dll
(7572) loading library at 0x764E0000 (C:\Windows\SysWOW64\KernelBase.dll) KernelBase.dll
(7572) loading library at 0x773D0000 (C:\Windows\SysWOW64\ws2_32.dll) ws2_32.dll
(7572) loading library at 0x77980000 (C:\Windows\SysWOW64\rpcrt4.dll) rpcrt4.dll
(7572) loading library at 0x762E0000 (C:\Windows\SysWOW64\ucrtbase.dll) ucrtbase.dll
(7572) loading library at 0x74D50000 (C:\Windows\SysWOW64\vcruntime140.dll) vcruntime140.dll
[0x77d61b03]> db
[0x77d61b03]> dc
(7572) Created thread 5136 (start @ 77CE5990) (teb @ 00373000)
(7572) Created thread 1824 (start @ 77CE5990) (teb @ 00376000)
(7572) loading library at 0x73690000 (C:\Windows\SysWOW64\mswsock.dll) mswsock.dll
(7572) Finished thread 1824 Exit code 0
(7572) Finished thread 5136 Exit code 0
(7572) Created thread 3032 (start @ 7632C570) (teb @ 00379000)
(7572) loading library at 0x75070000 (C:\Windows\SysWOW64\kernel.appcore.dll) kernel.appcore.dll
(7572) loading library at 0x76FB0000 (C:\Windows\SysWOW64\msvcrt.dll) msvcrt.dll
(7572) Created thread 8240 (start @ 77CE5990) (teb @ 0037C000)
(7572) Fatal Exception C0000005 (EXCEPTION_ACCESS_VIOLATION) in thread 3032
Hint: Use 'dce' continue into exception handler
[0x08041695]> dr
edi = 0x00650390
esi = 0x08041470
ebx = 0x00650390
edx = 0x763f0334
ecx = 0x3a11dd2e
eax = 0x00000000
ebp = 0x00000a21
eip = 0x08041695
eflags = 0x00010202
esp = 0x008319ec
[0x08041695]> dce
(7572) Fatal Exception C0000005 (EXCEPTION_ACCESS_VIOLATION) in thread 3032
Second-chance exception!!!
[0x08041695]> dr
edi = 0x00650390
esi = 0x08041470
ebx = 0x00650390
edx = 0x763f0334
ecx = 0x3a11dd2e
eax = 0x00000000
ebp = 0x00000a21
eip = 0x08041695
eflags = 0x00010202
esp = 0x008319ec
[0x08041695]> dce
(7572) Finished thread 3032 Exit code 3221225477
(7572) Finished thread 2376 Exit code 3221225477
[0x77d22ffc]> dr
edi = 0x00000000
esi = 0x00000000
ebx = 0x00650348
edx = 0x00000000
ecx = 0x00000000
eax = 0x00000000
ebp = 0x0019fae0
eip = 0x77d22ffc
eflags = 0x00000206
esp = 0x0019fa88
[0x77d22ffc]> pd 10 @ 0x08041695
        :   0x08041695      8b55d8         mov edx, dword [ebp - 0x28]
        :   0x08041698      83c201         add edx, 1
        :   0x0804169b      8955f4         mov dword [ebp - 0xc], edx
        `=< 0x0804169e      e9fafeffff     jmp 0x804159d
            0x080416a3      8b45f4         mov eax, dword [ebp - 0xc]
            0x080416a6      8d8db41affff   lea ecx, [ebp - 0xe54c]
            0x080416ac      2bc1           sub eax, ecx
            0x080416ae      8b55fc         mov edx, dword [ebp - 4]
            0x080416b1      2bd0           sub edx, eax
            0x080416b3      8955fc         mov dword [ebp - 4], edx
[0x77d22ffc]> px 64 @esp
- offset -  8889 8A8B 8C8D 8E8F 9091 9293 9495 9697  89ABCDEF01234567
0x0019fa88  c5a9 6973 1001 0000 0100 0000 0000 0000  ..is............
0x0019fa98  c807 6500 4803 6500 0000 0000 0072 cf00  ..e.H.e......r..
0x0019faa8  0000 0000 0000 0000 c807 6500 0000 0000  ..........e.....
0x0019fab8  0000 0000 1801 0000 0000 0000 1001 0000  ................
[0x77d22ffc]> px 300 @esp
- offset -  8889 8A8B 8C8D 8E8F 9091 9293 9495 9697  89ABCDEF01234567
0x0019fa88  c5a9 6973 1001 0000 0100 0000 0000 0000  ..is............
0x0019fa98  c807 6500 4803 6500 0000 0000 0072 cf00  ..e.H.e......r..
0x0019faa8  0000 0000 0000 0000 c807 6500 0000 0000  ..........e.....
0x0019fab8  0000 0000 1801 0000 0000 0000 1001 0000  ................
0x0019fac8  6079 feff ffff ffff 0000 0000 0000 0000  `y..............
0x0019fad8  44fb 1900 0c20 0100 fcfc 1900 624f 6a73  D.... ......bOjs
0x0019fae8  0200 0000 0400 0000 02a6 71a6 b801 6500  ..........q...e.
0x0019faf8  804c 6a73 0000 0000 0300 0100 0800 0000  .Ljs............
0x0019fb08  c8fa 1900 0000 0000 0400 0100 0400 0000  ................
0x0019fb18  d4fa 1900 0000 0000 0000 0000 4720 0100  ............G ..
0x0019fb28  0000 0000 ffff ffff 0000 0000 0000 0000  ................
0x0019fb38  30fd 1900 0100 0000 1800 6500 2001 00c0  0.........e. ...
0x0019fb48  0000 0000 00fb 1900 0100 0000 1401 0000  ................
0x0019fb58  0000 0000 0000 0000 0000 0000 c0fc 1900  ................
0x0019fb68  1000 0000 1000 0000 c807 6500 1800 6500  ..........e...e.
0x0019fb78  0000 6400 0000 0000 0000 0000 a8fc 1900  ..d.............
0x0019fb88  0000 0000 4803 6500 0000 0000 1801 0000  ....H.e.........
0x0019fb98  1801 0000 1001 0000 0000 0000 0000 0000  ................
0x0019fba8  e0fb 1900 4720 0100 e8fb 1900            ....G ......
[0x77d22ffc]> dmesg
[0x77d22ffc]> dc
INFO: ==> Process finished
[0x08041695]> ood
INFO: Spawned new process with pid 8312, tid = 8244
INFO: File dbg://C:\\Users\\Windows10x64VMUser\\Desktop\\thm-gatekeeper\\gatekeeper.exe reopened in read-write mode
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
ERROR: Unable to find file descriptor 3
ERROR: Unable to find file descriptor 3
8312
[0x77d255b0]> dc
(8312) loading library at 0x77CB0000 (C:\Windows\SysWOW64\ntdll.dll) ntdll.dll
(8312) loading library at 0x761F0000 (C:\Windows\SysWOW64\kernel32.dll) kernel32.dll
(8312) loading library at 0x764E0000 (C:\Windows\SysWOW64\KernelBase.dll) KernelBase.dll
(8312) loading library at 0x773D0000 (C:\Windows\SysWOW64\ws2_32.dll) ws2_32.dll
(8312) loading library at 0x77980000 (C:\Windows\SysWOW64\rpcrt4.dll) rpcrt4.dll
(8312) loading library at 0x762E0000 (C:\Windows\SysWOW64\ucrtbase.dll) ucrtbase.dll
(8312) Created thread 2824 (start @ 77CE5990) (teb @ 00374000)
(8312) loading library at 0x74D50000 (C:\Windows\SysWOW64\vcruntime140.dll) vcruntime140.dll
[0x77d61b03]> dc
(8312) Created thread 8368 (start @ 77CE5990) (teb @ 00377000)
(8312) loading library at 0x73690000 (C:\Windows\SysWOW64\mswsock.dll) mswsock.dll
(8312) Created thread 2552 (start @ 7632C570) (teb @ 0037A000)
(8312) loading library at 0x75070000 (C:\Windows\SysWOW64\kernel.appcore.dll) kernel.appcore.dll
(8312) loading library at 0x76FB0000 (C:\Windows\SysWOW64\msvcrt.dll) msvcrt.dll
(8312) Finished thread 2552 Exit code 0
(8312) Finished thread 2824 Exit code 0
(8312) Finished thread 8368 Exit code 0
(8312) Created thread 512 (start @ 7632C570) (teb @ 0037D000)
(8312) Fatal Exception C0000005 (EXCEPTION_ACCESS_VIOLATION) in thread 512
Hint: Use 'dce' continue into exception handler
[0x08041695]> dr
edi = 0x006125f8
esi = 0x08041470
ebx = 0x006125f8
edx = 0x763f0334
ecx = 0x1fa5151f
eax = 0x00000000
ebp = 0x00000a21
eip = 0x08041695
eflags = 0x00010202
esp = 0x007f19ec
[0x08041695]> pdf @eip
ERROR: Cannot find function at 0x08041695
[0x08041695]> pd 10 @ 0x08041695
        :   ;-- eip:
        :   0x08041695      8b55d8         mov edx, dword [ebp - 0x28]
        :   0x08041698      83c201         add edx, 1
        :   0x0804169b      8955f4         mov dword [ebp - 0xc], edx
        `=< 0x0804169e      e9fafeffff     jmp 0x804159d
            0x080416a3      8b45f4         mov eax, dword [ebp - 0xc]
            0x080416a6      8d8db41affff   lea ecx, [ebp - 0xe54c]
            0x080416ac      2bc1           sub eax, ecx
            0x080416ae      8b55fc         mov edx, dword [ebp - 4]
            0x080416b1      2bd0           sub edx, eax
            0x080416b3      8955fc         mov dword [ebp - 4], edx
[0x08041695]> ood
(8312) Created thread 7300 (start @ 77CE5990) (teb @ 00380000)
(8312) Finished thread 8244 Exit code 1
(8312) Finished thread 512 Exit code 1
INFO: ==> Process finished
INFO: Spawned new process with pid 2088, tid = 6852
INFO: File dbg://C:\\Users\\Windows10x64VMUser\\Desktop\\thm-gatekeeper\\gatekeeper.exe reopened in read-write mode
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
ERROR: Unable to find file descriptor 3
ERROR: Unable to find file descriptor 4
ERROR: Unable to find file descriptor 3
ERROR: Unable to find file descriptor 4
2088
[0x77d255b0]> dc
(2088) loading library at 0x77CB0000 (C:\Windows\SysWOW64\ntdll.dll) ntdll.dll
(2088) loading library at 0x761F0000 (C:\Windows\SysWOW64\kernel32.dll) kernel32.dll
(2088) loading library at 0x764E0000 (C:\Windows\SysWOW64\KernelBase.dll) KernelBase.dll
(2088) loading library at 0x773D0000 (C:\Windows\SysWOW64\ws2_32.dll) ws2_32.dll
(2088) loading library at 0x77980000 (C:\Windows\SysWOW64\rpcrt4.dll) rpcrt4.dll
(2088) loading library at 0x762E0000 (C:\Windows\SysWOW64\ucrtbase.dll) ucrtbase.dll
(2088) loading library at 0x74D50000 (C:\Windows\SysWOW64\vcruntime140.dll) vcruntime140.dll
(2088) Created thread 3800 (start @ 77CE5990) (teb @ 002B3000)
[0x77d61b03]> dc
(2088) Created thread 4764 (start @ 77CE5990) (teb @ 002B6000)
(2088) loading library at 0x73690000 (C:\Windows\SysWOW64\mswsock.dll) mswsock.dll
(2088) Created thread 2356 (start @ 7632C570) (teb @ 002B9000)
(2088) loading library at 0x75070000 (C:\Windows\SysWOW64\kernel.appcore.dll) kernel.appcore.dll
(2088) loading library at 0x76FB0000 (C:\Windows\SysWOW64\msvcrt.dll) msvcrt.dll
(2088) Fatal Exception C0000005 (EXCEPTION_ACCESS_VIOLATION) in thread 2356
Hint: Use 'dce' continue into exception handler
[0x39654138]> dr
edi = 0x0061fff8
esi = 0x08041470
ebx = 0x0061fff8
edx = 0x00000000
ecx = 0x105279e4
eax = 0xffffffff
ebp = 0x65413765
eip = 0x39654138
eflags = 0x00010286
esp = 0x00a019e4
[0x39654138]> q
Do you want to quit? (Y/n)
Do you want to kill the process? (Y/n)
c:\r2w32\bin>
```

After a lot of debugging this, first with x32dbg, then installing immunity debugger, setting more options in windows to lower defences and installing r2 for windows and running the above I uploaded the exe to the https://tryhackme.com/r/room/bufferoverflowprep vm and got the same result! I had though there might be options missing in my machine...

```sh
C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper>python fuzzer.py
Fuzzing with 110 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad
Recv: b'Hello Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad!!!\n'
Fuzzing with 120 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9
Recv: b'Hello Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9!!\x82\x00'
Fuzzing with 130 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2A
Recv: b'Hello Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae\x87\x00\x00\x00I\x19\x7f'
Fuzzing with 140 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae
Recv: b'Hello Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae\x87\x00\x00\x00I\x19\x7f'
Fuzzing with 150 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9
Fuzzing crashed: timed out

C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper>python fuzzer.py
Fuzzing with 100 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
Recv: b'Hello Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A!!!\n'
Fuzzing with 200 bytes.
Send: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
Fuzzing crashed: timed out
```

When found the problem was that I got a different crash here that I got when making bigger steps (100 chars instead of 10) and that the crash I got at 200 chars - This one actually overwriting EIP. I added a section in the Buffer overflow notes on Fuzzing and the importance of testing both smaller and bigger amounts of data!

