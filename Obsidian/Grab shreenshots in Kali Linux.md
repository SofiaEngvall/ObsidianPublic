
For my Obsidian notes, I need to grab parts of the screen and paste into obsidian. Here's how to do it.

### Flameshot

`sudo apt install flameshot`

##### Make keyboard shortcut

Settings → Keyboard → Shortcuts
Add shortcut
Command `flameshot gui -c`
Then click the button you want to bind. I use F4

![[Images/Pasted image 20250430142139.png]]

There's an annoying greyout and infomessage though, and a menu when dragging.

### main + xclip

`sudo apt install maim xclip`

test with `maim -s | xclip -selection clipboard -t image/png -i`

![[Images/Pasted image 20250430143158.png]]

This grabs a screenshot, but it doesn't freeze the screen as sharex does.

to add freeze and include cursor when taking screenshots:
`sudo apt install slop feh`

make screenshot.sh -  works 2026-10-01
```sh
#!/bin/bash
tmpimg="/tmp/maim_frozen.png"

# 1. Grab a full screen snapshot instantly to freeze the state
/usr/bin/maim "$tmpimg"

# 2. Open the image in a borderless fullscreen window on top of your video
/usr/bin/feh -F -N -Y "$tmpimg" & display_pid=$!
/usr/bin/sleep 0.1

# 3. Run your exact working selection line over the static image window
/usr/bin/maim -s | /usr/bin/xclip -selection clipboard -t image/png -i

# 4. Tear down the freeze window and clean up the temporary snapshot file
kill "$display_pid"
rm "$tmpimg"
```

`chmod +x screenshot.sh`

This works great for one screen

##### Make keyboard shortcut

Settings → Keyboard → Shortcuts
Add shortcut
Command `~/screenshot.sh` or `bash -c "/usr/bin/maim -s | /usr/bin/xclip -selection clipboard -t image/png -i"`
Then click the button you want to bind. I use F4

![[Images/Pasted image 20261006134402.png]]

