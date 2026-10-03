build system
`sudo apt install cmake extra-cmake-modules ninja-build pkg-config clang clang-format build-essential curl ccache git zsh`

obs code dependencies
`sudo apt install libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev libx264-dev libcurl4-openssl-dev libmbedtls-dev libgl1-mesa-dev libjansson-dev libluajit-5.1-dev python3-dev libx11-dev libxcb-randr0-dev libxcb-shm0-dev libxcb-xinerama0-dev libxcb-composite0-dev libxcomposite-dev libxinerama-dev libxcb1-dev libx11-xcb-dev libxcb-xfixes0-dev swig libcmocka-dev libxss-dev libglvnd-dev libgles2-mesa-dev libwayland-dev librist-dev libsrt-openssl-dev libpci-dev libpipewire-0.3-dev libqrcodegencpp-dev uthash-dev libsimde-dev`

ui deps
`sudo apt install qt6-base-dev qt6-base-private-dev qt6-svg-dev qt6-wayland qt6-image-formats-plugins`

plugin deps
`sudo apt install libasound2-dev libfdk-aac-dev libfontconfig-dev libfreetype6-dev libjack-jackd2-dev libpulse-dev libsndio-dev libspeexdsp-dev libudev-dev libv4l-dev libva-dev libvlc-dev libvpl-dev libdrm-dev nlohmann-json3-dev libwebsocketpp-dev libasio-dev`

download the pre-built obs-browser CEF framework - https://cdn-fastly.obsproject.com/downloads/cef_binary_6533_linux_x86_64_v6.tar.xz
extract it
`tar -xf cef_binary_6533_linux_x86_64_v6.tar.xz`

grab the files
`git clone --recursive https://github.com/obsproject/obs-studio.git`
`cd /home/fixit42/Downloads/obs-build/obs-studio`
`git checkout 32.2.2`
`git submodule update --init --recursive`

make a preset file - calling it /home/fixit42/Downloads/obs-build/obs-studio/CMakeUserPresets.json
```json
{
  "version": 3,
  "configurePresets": [
    {
      "name": "kali-portable",
      "binaryDir": "/home/fixit42/Downloads/obs-build/build",
      "cacheVariables": {
      
        "ENABLE_RELOCATABLE": true,
        "ENABLE_PORTABLE_CONFIG": true,
        "CMAKE_INSTALL_PREFIX": {"type": "STRING", "value": "/opt/obs"},

        "ENABLE_BROWSER" : true,
        "CEF_ROOT_DIR": {"type": "STRING", "value": "/home/fixit42/Downloads/obs-build/cef_binary_6533_linux_x86_64"},

        "OBS_COMPILE_DEPRECATION_AS_WARNING": true,

        "ENABLE_NVENC": false,
        "ENABLE_FFMPEG_NVENC": false,

        "ENABLE_AJA": false
      }
    }
  ]
}
```
change both NVENC lines to true for use with a nvidia card

I found a missing dependency while running the config - let's add it:
```sh
sudo apt install libxcb-xinput-dev libdatachannel-dev

git clone --recursive https://github.com/paullouisageneau/libdatachannel.git /home/fixit42/Downloads/obs-build/libdatachannel
cmake -S /home/fixit42/Downloads/obs-build/libdatachannel -B /home/fixit42/Downloads/obs-build/libdatachannel/build -DUSE_GNUTLS=0 -DUSE_NICE=0 -DCMAKE_BUILD_TYPE=Release
cmake --build /home/fixit42/Downloads/obs-build/libdatachannel/build --parallel $(nproc)
sudo cmake --install /home/fixit42/Downloads/obs-build/libdatachannel/build
```
TODO! Change the version of libdatachannel

configure the build project using our file with
```sh
cmake -S /home/fixit42/Downloads/obs-build/obs-studio --preset=kali-portable -Wno-dev
```

build it with 
```sh
cmake --build /home/fixit42/Downloads/obs-build/build --parallel $(nproc)
```

install it with
```sh
sudo cmake --install /home/fixit42/Downloads/obs-build/build
```

launch obs with
```sh
cd /opt/obs/bin && ./obs -p
```

