
## Create a ssh key pair

in normal ps window or linux terminal:
```powershell
PS C:\Users\sofia\.ssh> ssh-keygen -t ed25519 -C "sofia@fixit42.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\sofia/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\sofia/.ssh/id_ed25519.
Your public key has been saved in C:\Users\sofia/.ssh/id_ed25519.pub.
The key fingerprint is:
...
```

## Start using it in windows

in admin ps window:
```powershell
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
```

in normal ps window:
```powershell
PS C:\Users\sofia\.ssh> ssh-add .\id_ed25519
Identity added: .\id_ed25519 (sofia@babythings.se)
```

## Start using it in linux

TO DO paste from history of asus kali laptop!
```sh
ssh-add ~/.ssh/id_ed25519
```

Might be different, check out https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux

## Add it to github
 
in github:
Settings, SSH and GPG keys, New SSH key, paste the contents of the id_ed25519.pub file.

