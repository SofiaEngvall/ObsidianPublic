
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

##### Make keyboard shortcut

Settings → Keyboard → Shortcuts
Add shortcut
Command `maim -s | xclip -selection clipboard -t image/png -i`
Then click the button you want to bind. I use F4

bash -c "/usr/bin/maim -s | /usr/bin/xclip -selection clipboard -t image/png -i"

![[Images/Pasted image 20250430144438.png]]

This grabs a screenshot, but it doesn't freeze the screen as sharex does.

For freeze:

```sh
#!/bin/bash
tmpimg="/tmp/maim_frozen.png"

# Take a full-screen screenshot (frozen state)
maim "$tmpimg"

# Let user select region from the frozen image
maim -i "$tmpimg" -s | xclip -selection clipboard -t image/png -i

# Optional: clean up
rm "$tmpimg"

```

bash -c 'maim /tmp/frozen.png && sleep 0.5 && maim -i /tmp/frozen.png -s | xclip -selection clipboard -t image/png -i && rm /tmp/frozen.png'

