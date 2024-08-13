
For forensic VM

`dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

```sh
C:\Windows\system32>dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Deployment Image Servicing and Management tool
Version: 10.0.19041.3636

Image Version: 10.0.19045.4717

Enabling feature(s)
[==========================100.0%==========================]
The operation completed successfully.
```

`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all`

Downloaded and run:
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
(from https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

Restarted

```sh
C:\Windows\system32>wsl --set-default-version 2
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
The operation completed successfully.
```

Dowloading and running:
https://apps.microsoft.com/store/detail/kali-linux/9PKR34TNCV07

```sh
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x80370102
Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
For information please visit https://aka.ms/enablevirtualization
Press any key to continue...
```

```sh
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x80370102
Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
For information please visit https://aka.ms/enablevirtualization
Press any key to continue...
```