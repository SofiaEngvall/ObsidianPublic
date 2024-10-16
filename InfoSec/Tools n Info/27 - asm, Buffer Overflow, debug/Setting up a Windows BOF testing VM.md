
**Clone the base Win 10 VM**

**Set to Dark Mode**
- `Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize` AppsUseLightTheme REG_DWORD 0

Install firefox
Install Windows Updates

**Install[[x64dbg (and x32dbg)]]
- Install [x64dbg](https://github.com/x64dbg/x64dbg)
- Install the plugin [ERC.Xdbg](https://github.com/Andy53/ERC.Xdbg)???

**Disable DEP (Data Execution Prevention)**:
- Buffer overflow exploration may require DEP to be turned off.
- Run `bcdedit /set nx AlwaysOff` in an elevated command prompt and reboot.

```sh
C:\Windows\system32>bcdedit /set nx AlwaysOff
The operation completed successfully.
```

**Turn off ASLR (Address Space Layout Randomization)**:
- Disable ASLR to ensure memory addresses remain static, which helps with buffer overflow testing.
- Modify registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management` by setting `MoveImages` to 0.

**Disable Windows Defender**:
- For testing malicious code, temporarily disabling antivirus might be necessary to avoid interference.
- **Temporarily Disable Windows Defender**: Go to Windows Security > Virus & threat protection > Manage settings, and turn off real-time protection.
- **Create Exclusions**: Add your work folder or specific tools as exclusions in Windows Defender to prevent them from being flagged.

