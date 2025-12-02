
### Using the Terminal

Under `/usr/share/desktop-base/kali-theme/login/` is a symbolic link named `background`. Update it with your desired image path.

Sample Command:  
`sudo ln -s <image_path> /usr/share/desktop-base/kali-theme/login/background`

### Using the GUI

1. Click _Menu_ > _Settings_ > _LightDM GTK+ Greeter settings_
2. Authenticate if necessary
3. In the _Appearance_ tab of the window, select an image/color under _Background_
4. Click _Save_

### config login bg to be the desktop bg

still to solve:

sets it to the kali default - right now the blue cubes 3d one
`sudo ln -sf /usr/share/images/desktop-base/desktop-background /usr/share/desktop-base/kali-theme/login/background`

?
`sudo ln -sf /etc/alternatives/desktop-background /usr/share/desktop-base/kali-theme/login/background`

?
`sudo ln -sf /usr/share/backgrounds/kali-16x9/default /usr/share/desktop-base/kali-theme/login/background`




