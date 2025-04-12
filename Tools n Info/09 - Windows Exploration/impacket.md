
https://www.kali.org/tools/impacket/
https://www.kali.org/tools/impacket-scripts/

smbserver - create share for upload to our machine
`sudo impacket-smbserver -smb2support -username THMBackup -password CopyMaster555 myshare ../dirname`




### Set up virtual environment for impacket

```shell-session
user@attackbox$ python3 -m venv impacketEnv
user@attackbox$ source impacketEnv/bin/activate
user@attackbox$ python3 -m pip install --upgrade pip
user@attackbox$ python3 -m pip install impacket
```

