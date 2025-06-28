

Start install — when it says “This PC can’t run Windows 11”
- Press `Shift + F10` → command prompt opens
- Type: `regedit` → hit Enter

In regedit
- Go to: `HKEY_LOCAL_MACHINE\SYSTEM\Setup`  
- Right-click `Setup` → `New > Key` → name it: `LabConfig`
- Inside `LabConfig` key, create 3 new DWORD (32-bit) values:
```
BypassTPMCheck      = 1  
BypassSecureBootCheck = 1  
BypassRAMCheck      = 1
```

Click back, then Next — install proceeds