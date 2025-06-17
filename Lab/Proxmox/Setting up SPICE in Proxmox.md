
1. Click the VM you want to add SPICE to

2. Go to `Hardware`, double click `Display`
	- Set `Graphics Card` to `SPICE`
	- Set `Memory (MiB)` to `32` (optional)
   ![[Images/Pasted image 20250227145220.png]]

3. Go to **Options**, double click **Spice Enhancements**
   - Set **Video Streaming** to `all`
   - Enable `Folder sharing` if you want to
   ![[Images/Pasted image 20250227145348.png]]

4. OPTIONAL: Go to **Hardware**, click `Add`, `Audio Device`
   - Use default options, click `Add`
   ![[Images/Pasted image 20250227145451.png]]
   ![[Images/Pasted image 20250227145634.png]]

5. OPTIONAL: Go to `Hardware`, Add `USB Device`
   - Use default options, click `Add`
   ![[Images/Pasted image 20250227150419.png]]
   ![[Images/Pasted image 20250227150456.png]]

6. On the client (our PC) install the Spice client
	- Linux - sudo apt install virt-viewer
	- Windows - https://virt-manager.org/download (Win x64 MSI)
		- Go to options in your browser and temporarily enable `Ask wether to open or save files`
		- Click the `>_ Console` arrow down menu and select SPICE
		- Select to open the file and to open it with `remote-viewer.exe`
		- A file should be downloaded and opened so you can see the desktop...
	
7.  Install the Guest Tools for Windows (This enables copy, paste and stops the mouse from locking inside the app!)
   - Go to https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.266-1/
   - Download `virtio-win-guest-tools.exe`
   - (This did seem to crash the vm - might be a conflict with rdp as rdp closes now when we open spice?)
   - Alternative way: use the files in the D:\guest-agent\qemu-ga-x86_64.msi (the wirtio-win-iso)
   - (This didn't seem to work at all and we got a crash at reboot)
     
6. Install the Guest Tools for Linux (might be preinstalled)
   - Install `sudo apt install spice-vdagent`
   - Start/Enable `sudo systemctl start spice-vdagent` or `sudo systemctl enable spice-vdagent`
   - Check the status of the service: `sudo systemctl status spice-vdagent`
     
9. To enable file sharing we also need the WebDAV Daemon https://www.spice-space.org/download/windows/spice-webdavd/
   - Windows ^
   - Linux: [[Linux VM Spice]]

