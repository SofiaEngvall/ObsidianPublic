
![[Images/Pasted image 20250105152616.png]]

On admin cmd: `sfc /scannow`

Example output:
```sh
C:\WINDOWS\system32>sfc /scannow

Beginning system scan.  This process will take some time.

Beginning verification phase of system scan.
Verification 100% complete.

Windows Resource Protection found corrupt files and successfully repaired them.
For online repairs, details are included in the CBS log file located at
windir\Logs\CBS\CBS.log. For example C:\Windows\Logs\CBS\CBS.log. For offline
repairs, details are included in the log file provided by the /OFFLOGFILE flag.
```

If this didn't work, try:
`DISM.exe /Online /Cleanup-image /Scanhealth`  
`DISM.exe /Online /Cleanup-image /Restorehealth`

This will use windows update to fix bad files

Example output:
```sh
C:\WINDOWS\system32>DISM.exe /Online /Cleanup-image /Scanhealth

Deployment Image Servicing and Management tool
Version: 10.0.19041.3636

Image Version: 10.0.19045.5247

[==========================100.0%==========================] No component store corruption detected.
The operation completed successfully.
```

