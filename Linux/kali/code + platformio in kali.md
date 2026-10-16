
code oss is preinstalled
add the extension PlatformIO

Find our ESP32
```sh
┌──(fixit42㉿asus)-[~]
└─$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 093a:2510 Pixart Imaging, Inc. Optical Mouse
Bus 001 Device 003: ID 0c45:7603 Microdia USB Keyboard
Bus 001 Device 004: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
Bus 001 Device 005: ID 1e71:170e NZXT Kraken X
Bus 001 Device 006: ID 0d8c:0005 C-Media Electronics, Inc. Blue Snowball
Bus 001 Device 007: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
Bus 001 Device 008: ID 534d:2109 MacroSilicon USB Video
Bus 001 Device 009: ID 0bda:a728 Realtek Semiconductor Corp. Bluetooth 5.4 Radio
Bus 001 Device 010: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

Bus 001 Device 010: ID 10c4:ea60 Silicon Labs CP210x UART Bridge


### Switching to MS extensions

it won't build so I'm debugging - vs code from ms for linux should exist so we might install it instead, but first let's try replacing the  extensions gallery

First I uninstalled both extensions

then I edited /usr/lib/code-oss/resources/app/product.json

`sudo nano /usr/lib/code-oss/resources/app/product.json`

and replaced
```sh
        "extensionsGallery": {
                "serviceUrl": "https://open-vsx.org/vscode/gallery",
                "itemUrl": "https://open-vsx.org/vscode/item"
```

with
```sh
        "extensionsGallery": {
                "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
                "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index", "itemUrl": "https://marketplace.visualstudio.com/items"
```

When starting code I instantly got the 
![[Images/Pasted image 20261016020154.png]]
as the project was open, looking good!!

but then I could not install C/C++
![[Images/Pasted image 20261016021249.png]]

This will probably keep being a problem so let's try full VS Code from MS


