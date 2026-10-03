
### Why?

I'm going to try running kali as a dual-boot daily driver. Why?
- Win10 is dying and my computer is too old for Win11 (I could bypass but I don't want Win11!)
- I've run kali on so many vm:s and laptops and I'm very comfy with it. I run debian for servers.
- As I want the kali tools and a debian base, why not try?


#### Dual-boot Win10
- Use WSL2 to access ext4 partition


### What do I need?

- Kali tools
- Firefox and Thunderbird - what I use now on Win10
- LibreOffice - what I use now on Win10
- vlc  `sudo apt install vlc`

#### Tools for streaming

- OBS, native `sudo apt install obs-studio`, flatpak or from source
  since I don't want uncontrolled updates I'll do from source
  https://github.com/obsproject/obs-studio/wiki/Build-Instructions-For-Linux
- Streamer.bot, wine
- Speaker.bot, wine
- SAMMI, wine? is there a linux version
- Iriun, native (https://iriun.com/)
- Chrome or Chromium from the repo for http://tts.bot


#### Other tools

- Balena etcher - https://github.com/balena-io/etcher#debian-and-ubuntu-based-package-repository-gnulinux-x86x64
- Obsidian, preinstalled
- 3d printing - https://www.reddit.com/r/AnycubicKobraS1/comments/1izhcfm/linux_options/
- inkscape - sudo apt install inkscape
- Gimp, Pinta or some other gfx tools, Paint.net doesn't have a linux ver
- yt-dlp, to dl yt vids

#### Problems?

- DaVinci Resolve, only supported for Rocky Linux (red hat) + even if you get it running it will lack codecs -> Dual boot win? vm with pass through gfx?

#### Other stuff

- bluetooth
  `sudo apt install bluetooth bluez blueman`
  `rfkill list` check for software and hardware blocks
  `sudo rfkill unblock bluetooth` remove software block
  `systemctl status bluetooth` ("Active: inactive (dead)" means the service is installed but not active)
  `sudo systemctl enable bluetooth`
  `sudo systemctl start bluetooth`
  in the gui, search for devices
- screenshots - [[../../Obsidian/Grab shreenshots in Kali Linux|Grab shreenshots in Kali Linux]]

#### Play games with the kids

- Steam, native + proton (or flatpak)
  `sudo dpkg --add-architecture i386`
  `sudo apt update`
  `sudo apt install steam`
- Roblox, flatpak only due to android emulation
- minecraft
  sudo apt update
  Download minecraft .deb file from mojang
  For older versions
  sudo apt install -y openjdk-17-jre openjdk-21-jre
  java8..
- epic
  `flatpak install flathub com.heroicgameslauncher.hgl`
- hytale - native, https://hytale.com/download

#### wine

To run streamer.bot and other streaming tools

`sudo dpkg --add-architecture i386`
`sudo apt update`
`sudo apt install wine wine32 wine64 libwine libwine:i386`

#### flatpak

To run Roblox

`sudo apt install flatpak`
`flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`
`flatpak install flathub org.vinegarhq.Sober` (Roblox)
`flatpak run org.vinegarhq.Sober`

- nvidia drivers
  `sudo apt install -y nvidia-driver nvidia-cuda-toolkit`
  `sudo apt install libgl1-nvidia-glx:i386 libglx-nvidia0:i386 nvidia-vulkan-icd:i386`

sudo apt install nvidia-driver nvidia-vulkan-icd nvidia-vulkan-icd:i386


### Detailed installations

#### Obs

build system
`sudo apt install cmake extra-cmake-modules ninja-build pkg-config clang clang-format build-essential curl ccache git zsh`

obs code dependencies
`sudo apt install libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev libx264-dev libcurl4-openssl-dev libmbedtls-dev libgl1-mesa-dev libjansson-dev libluajit-5.1-dev python3-dev libx11-dev libxcb-randr0-dev libxcb-shm0-dev libxcb-xinerama0-dev libxcb-composite0-dev libxcomposite-dev libxinerama-dev libxcb1-dev libx11-xcb-dev libxcb-xfixes0-dev swig libcmocka-dev libxss-dev libglvnd-dev libgles2-mesa-dev libwayland-dev librist-dev libsrt-openssl-dev libpci-dev libpipewire-0.3-dev libqrcodegencpp-dev uthash-dev libsimde-dev`

ui deps
`sudo apt install qt6-base-dev qt6-base-private-dev qt6-svg-dev qt6-wayland qt6-image-formats-plugins`

plugin deps
`sudo apt install libasound2-dev libfdk-aac-dev libfontconfig-dev libfreetype6-dev libjack-jackd2-dev libpulse-dev libsndio-dev libspeexdsp-dev libudev-dev libv4l-dev libva-dev libvlc-dev libvpl-dev libdrm-dev nlohmann-json3-dev libwebsocketpp-dev libasio-dev`

download the pre-built obs-browser CEF framework - https://cdn-fastly.obsproject.com/downloads/cef_binary_6533_linux_x86_64_v6.tar.xz

grab the files
`git clone --recursive https://github.com/obsproject/obs-studio.git`




### Debugging

#### Minecraft broken .deb fix

```sh
# 1. Download the file and make a temporary folder
mkdir minecraft-fix
dpkg-deb -R Minecraft.deb minecraft-fix

# 2. Open the dependency list file in an editor
nano minecraft-fix/DEBIAN/control

# 3. Find the text "libgdk-pixbuf2.0-0" and fix it to match modern Kali:
# Change it to: libgdk-pixbuf-2.0-0

# 4. Save (Ctrl+O, Enter), Exit (Ctrl+X) and rebuild the package
dpkg-deb -b minecraft-fix Minecraft-patched.deb

# 5. Install it natively via apt
sudo apt install ./Minecraft-patched.deb
```


#### Roblox - Sober Crash `eglCreateContext`

`flatpak update`
`sudo apt update`
`sudo apt upgrade`
reboot

#### Roblox - Sober mousepad fix

Edit the config file
```sh
nano ~/.var/app/org.vinegarhq.Sober/config/sober/config.json
```

Set touch-mode to fake-off
```json
"touch_mode": "fake-off"
```

