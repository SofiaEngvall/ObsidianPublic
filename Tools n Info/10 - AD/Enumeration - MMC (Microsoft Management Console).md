
### Connecting to a remote computers ad MMCs

We need the snap-ins for ad:
install # Remote Server Administration Tools for Windows 10
https://www.microsoft.com/en-us/download/details.aspx?id=45520

Might be the same for Windows 11

`runas.exe /netonly /user:domain.name\username mmc`

Click `File`, `Add/Remove Snap-in...` and select the three AD ones at the top

