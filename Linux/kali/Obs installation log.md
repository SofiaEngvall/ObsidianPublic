
```sh
┌──(fixit42㉿x1)-[~]
└─$ sudo apt install cmake extra-cmake-modules ninja-build pkg-config clang clang-format build-essential curl ccache git zsh
[sudo] password for fixit42: 
clang is already the newest version (1:21.1.6-71+b1).
clang set to manually installed.
build-essential is already the newest version (12.12).
build-essential set to manually installed.
curl is already the newest version (8.21.0-2).
curl set to manually installed.
git is already the newest version (1:2.53.0-1).
git set to manually installed.
zsh is already the newest version (5.9.2-1+b1).
zsh set to manually installed.
Installing:                 
  ccache  clang-format  cmake  extra-cmake-modules  ninja-build  pkg-config

Installing dependencies:
  clang-format-21  librhash1

Suggested packages:
  distcc  | icecc  cmake-doc  cmake-format  elpa-cmake-mode  qt6-base-dev

Summary:
  Upgrading: 0, Installing: 8, Removing: 0, Not Upgrading: 1
  Download size: 17.7 MB
  Space needed: 65.5 MB / 155 GB available

Continue? [Y/n] y
Get:1 http://kali.download/kali kali-rolling/main amd64 ccache amd64 4.13.6-1 [849 kB]
Get:2 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 clang-format-21 amd64 1:21.1.8-10 [71.3 kB]
Get:3 http://http.kali.org/kali kali-rolling/main amd64 clang-format amd64 1:21.1.6-71+b1 [4,372 B]
Get:4 http://http.kali.org/kali kali-rolling/main amd64 librhash1 amd64 1.4.6-1.1+b1 [135 kB]
Get:5 http://kali.download/kali kali-rolling/main amd64 cmake amd64 4.3.4-1 [16.2 MB]
Get:7 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 ninja-build amd64 1.13.2-1 [163 kB]
Get:8 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 pkg-config amd64 2.5.1-4 [18.1 kB]
Get:6 http://kali.download/kali kali-rolling/main amd64 extra-cmake-modules amd64 6.30.0-1 [222 kB]
Fetched 17.7 MB in 3s (6,104 kB/s)           
Selecting previously unselected package ccache.
(Reading database… 816940 files and directories currently installed.)
Preparing to unpack …/0-ccache_4.13.6-1_amd64.deb…
Unpacking ccache (4.13.6-1)…
Selecting previously unselected package clang-format-21.
Preparing to unpack …/1-clang-format-21_1%3a21.1.8-10_amd64.deb…
Unpacking clang-format-21 (1:21.1.8-10)…
Selecting previously unselected package clang-format:amd64.
Preparing to unpack …/2-clang-format_1%3a21.1.6-71+b1_amd64.deb…
Unpacking clang-format:amd64 (1:21.1.6-71+b1)…
Selecting previously unselected package librhash1:amd64.
Preparing to unpack …/3-librhash1_1.4.6-1.1+b1_amd64.deb…
Unpacking librhash1:amd64 (1.4.6-1.1+b1)…
Selecting previously unselected package cmake.
Preparing to unpack …/4-cmake_4.3.4-1_amd64.deb…
Unpacking cmake (4.3.4-1)…
Selecting previously unselected package extra-cmake-modules.
Preparing to unpack …/5-extra-cmake-modules_6.30.0-1_amd64.deb…
Unpacking extra-cmake-modules (6.30.0-1)…
Selecting previously unselected package ninja-build.
Preparing to unpack …/6-ninja-build_1.13.2-1_amd64.deb…
Unpacking ninja-build (1.13.2-1)…
Selecting previously unselected package pkg-config:amd64.
Preparing to unpack …/7-pkg-config_2.5.1-4_amd64.deb…
Unpacking pkg-config:amd64 (2.5.1-4)…
Setting up extra-cmake-modules (6.30.0-1)…
Setting up ccache (4.13.6-1)…
Updating symlinks in /usr/lib/ccache ...
Setting up ninja-build (1.13.2-1)…
Setting up pkg-config:amd64 (2.5.1-4)…
Setting up clang-format-21 (1:21.1.8-10)…
Setting up librhash1:amd64 (1.4.6-1.1+b1)…
Setting up clang-format:amd64 (1:21.1.6-71+b1)…
Setting up cmake (4.3.4-1)…
Processing triggers for doc-base (0.11.2)…
Processing 2 added doc-base files...
Processing triggers for libc-bin (2.43-4)…
Processing triggers for man-db (2.13.1-1)…
Processing triggers for kali-menu (2026.3.4)…
Scanning processes...                                                                                                                            
Scanning processor microcode...                                                                                                                  
Scanning linux images...                                                                                                                         

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ sudo apt install libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev libx264-dev libcurl4-openssl-dev libmbedtls-dev libgl1-mesa-dev libjansson-dev libluajit-5.1-dev python3-dev libx11-dev libxcb-randr0-dev libxcb-shm0-dev libxcb-xinerama0-dev libxcb-composite0-dev libxcomposite-dev libxinerama-dev libxcb1-dev libx11-xcb-dev libxcb-xfixes0-dev swig libcmocka-dev libxss-dev libglvnd-dev libgles2-mesa-dev libwayland-dev librist-dev libsrt-openssl-dev libpci-dev libpipewire-0.3-dev libqrcodegencpp-dev uthash-dev libsimde-dev   
python3-dev is already the newest version (3.14.7-3).
python3-dev set to manually installed.
libx11-dev is already the newest version (2:1.8.13-1).
libx11-dev set to manually installed.
libxcb1-dev is already the newest version (1.17.0-2+b2).
libxcb1-dev set to manually installed.
Installing:                 
  libavcodec-dev   libcurl4-openssl-dev  libmbedtls-dev       libsrt-openssl-dev  libxcb-composite0-dev  libxinerama-dev
  libavdevice-dev  libgl1-mesa-dev       libpci-dev           libswresample-dev   libxcb-randr0-dev      libxss-dev                              
  libavfilter-dev  libgles2-mesa-dev     libpipewire-0.3-dev  libswscale-dev      libxcb-shm0-dev        swig                                    
  libavformat-dev  libglvnd-dev          libqrcodegencpp-dev  libwayland-dev      libxcb-xfixes0-dev     uthash-dev                              
  libavutil-dev    libjansson-dev        librist-dev          libx11-xcb-dev      libxcb-xinerama0-dev                                           
  libcmocka-dev    libluajit-5.1-dev     libsimde-dev         libx264-dev         libxcomposite-dev                                              
                                                                                                                                                 
Installing dependencies:
  cmocka-doc           libegl-dev         libldap-dev                libngtcp2-dev     libsrt1.5-openssl  libunistring-dev    nettle-dev
  doxygen-awesome-css  libgles-dev        libmbedtls21               libp11-kit-dev    libssh2-1-dev      libwayland-bin                         
  libavdevice62        libgles1           libmbedx509-7              libpsl-dev        libssl-dev         libxcb-render0-dev                     
  libbrotli-dev        libglvnd-core-dev  libnghttp2-dev             libqrcodegencpp1  libtasn1-6-dev     libxcb-shape0-dev                      
  libcjson-dev         libgnutls28-dev    libnghttp3-dev             librtmp-dev       libtasn1-doc       libxfixes-dev                          
  libcmocka0           libidn2-dev        libngtcp2-crypto-ossl-dev  libspa-0.2-dev    libudev-dev        libzstd-dev                            
                                                                                                                                                 
Suggested packages:
  libcurl4-doc  gnutls-doc      libnghttp2-doc  pipewire-doc  libssl-doc      swig-doc
  libidn-dev    libmbedtls-doc  p11-kit-doc     libsrt-doc    libwayland-doc  swig-examples

Summary:
  Upgrading: 0, Installing: 71, Removing: 0, Not Upgrading: 1
  Download size: 29.8 MB
  Space needed: 128 MB / 155 GB available

Continue? [Y/n] y
Get:1 http://kali.download/kali kali-rolling/main amd64 doxygen-awesome-css all 2.4.2-2 [19.1 kB]
Get:5 http://http.kali.org/kali kali-rolling/main amd64 libavcodec-dev amd64 7:8.1.2-2+b3 [7,513 kB]            
Get:10 http://http.kali.org/kali kali-rolling/main amd64 libavdevice-dev amd64 7:8.1.2-2+b3 [117 kB]       
Get:20 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libngtcp2-dev amd64 1.24.0-1 [204 kB]             
Get:22 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libpsl-dev amd64 0.23.3-1 [30.1 kB]               
Get:2 http://kali.download/kali kali-rolling/main amd64 cmocka-doc all 2.0.2-1 [151 kB]                                    
Get:26 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libgnutls28-dev amd64 3.8.13-1 [1,479 kB]    
Get:3 http://http.kali.org/kali kali-rolling/main amd64 libavutil-dev amd64 7:8.1.2-2+b3 [628 kB]                                            
Get:12 http://http.kali.org/kali kali-rolling/main amd64 libcjson-dev amd64 1.7.19-2+b1 [29.2 kB]                                              
Get:27 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 librtmp-dev amd64 2.6-1 [69.7 kB]                                  
Get:28 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libssl-dev amd64 3.6.4-1 [3,156 kB]                           
Get:34 http://http.kali.org/kali kali-rolling/main amd64 libgles1 amd64 1.7.0-3+b1 [11.4 kB]                                           
Get:36 http://http.kali.org/kali kali-rolling/main amd64 libglvnd-dev amd64 1.7.0-3+b1 [4,336 B]                                   
Get:47 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libpipewire-0.3-dev amd64 1.6.8-1 [65.3 kB]                              
Get:49 http://http.kali.org/kali kali-rolling/main amd64 libqrcodegencpp-dev amd64 1.8.0-1.2+b3 [29.4 kB]                                      
Get:4 http://http.kali.org/kali kali-rolling/main amd64 libswresample-dev amd64 7:8.1.2-2+b3 [125 kB]                                         
Get:6 http://http.kali.org/kali kali-rolling/main amd64 libavdevice62 amd64 7:8.1.2-2+b3 [108 kB]     
Get:70 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 swig amd64 4.5.1-2 [1,597 kB]       
Get:7 http://http.kali.org/kali kali-rolling/main amd64 libavformat-dev amd64 7:8.1.2-2+b3 [1,571 kB]     
Get:30 http://http.kali.org/kali kali-rolling/main amd64 libzstd-dev amd64 1.5.7+dfsg-4 [371 kB]               
Get:46 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libspa-0.2-dev amd64 1.6.8-1 [122 kB]
Get:8 http://http.kali.org/kali kali-rolling/main amd64 libswscale-dev amd64 7:8.1.2-2+b3 [561 kB]
Get:9 http://http.kali.org/kali kali-rolling/main amd64 libavfilter-dev amd64 7:8.1.2-2+b3 [2,570 kB]
Get:11 http://http.kali.org/kali kali-rolling/main amd64 libbrotli-dev amd64 1.2.0-4+b1 [324 kB]
Get:13 http://http.kali.org/kali kali-rolling/main amd64 libcmocka0 amd64 2.0.2-1+b1 [31.9 kB]
Get:14 http://http.kali.org/kali kali-rolling/main amd64 libcmocka-dev amd64 2.0.2-1+b1 [39.0 kB]
Get:15 http://kali.download/kali kali-rolling/main amd64 libidn2-dev amd64 2.3.8-5 [102 kB]
Get:16 http://http.kali.org/kali kali-rolling/main amd64 libldap-dev amd64 2.6.14+dfsg-2 [321 kB]
Get:17 http://kali.download/kali kali-rolling/main amd64 libnghttp2-dev amd64 1.70.0-1 [131 kB]
Get:18 http://kali.download/kali kali-rolling/main amd64 libnghttp3-dev amd64 1.17.0-1 [96.3 kB]
Get:19 http://kali.download/kali kali-rolling/main amd64 libngtcp2-crypto-ossl-dev amd64 1.24.0-1 [27.5 kB]
Get:21 http://kali.download/kali kali-rolling/main amd64 libunistring-dev amd64 1.4.2-1 [651 kB]
Get:23 http://kali.download/kali kali-rolling/main amd64 libp11-kit-dev amd64 0.26.5-1 [226 kB]
Get:24 http://http.kali.org/kali kali-rolling/main amd64 libtasn1-6-dev amd64 4.21.0-2+b1 [98.6 kB]
Get:25 http://http.kali.org/kali kali-rolling/main amd64 nettle-dev amd64 3.10.2-1+b1 [1,321 kB]
Get:50 http://http.kali.org/kali kali-rolling/main amd64 librist-dev amd64 0.2.20+dfsg-1 [68.3 kB]
Get:29 http://kali.download/kali kali-rolling/main amd64 libssh2-1-dev amd64 1.11.1-6 [402 kB]
Get:31 http://kali.download/kali kali-rolling/main amd64 libcurl4-openssl-dev amd64 8.21.0-2 [550 kB]                                           
Get:32 http://http.kali.org/kali kali-rolling/main amd64 libegl-dev amd64 1.7.0-3+b1 [18.7 kB]                                                  
Get:33 http://http.kali.org/kali kali-rolling/main amd64 libglvnd-core-dev amd64 1.7.0-3+b1 [12.6 kB]                                           
Get:35 http://http.kali.org/kali kali-rolling/main amd64 libgles-dev amd64 1.7.0-3+b1 [50.0 kB]                                                 
Get:37 http://kali.download/kali kali-rolling/main amd64 libgl1-mesa-dev amd64 26.1.6-1 [15.4 kB]                                               
Get:38 http://kali.download/kali kali-rolling/main amd64 libgles2-mesa-dev amd64 26.1.6-1 [15.4 kB]                                             
Get:39 http://kali.download/kali kali-rolling/main amd64 libjansson-dev amd64 2.15.1-1 [75.8 kB]                                                
Get:40 http://http.kali.org/kali kali-rolling/main amd64 libluajit-5.1-dev amd64 2.1.0+openresty20251030-1+b2 [288 kB]                          
Get:41 http://kali.download/kali kali-rolling/main amd64 libmbedx509-7 amd64 3.6.7-3 [157 kB]                                                   
Get:42 http://kali.download/kali kali-rolling/main amd64 libmbedtls21 amd64 3.6.7-3 [250 kB]                                                    
Get:43 http://kali.download/kali kali-rolling/main amd64 libmbedtls-dev amd64 3.6.7-3 [849 kB]                                                  
Get:44 http://kali.download/kali kali-rolling/main amd64 libudev-dev amd64 261.2-1 [54.0 kB]                                                    
Get:45 http://kali.download/kali kali-rolling/main amd64 libpci-dev amd64 1:3.15.0-2 [70.8 kB]                                                  
Get:48 http://http.kali.org/kali kali-rolling/main amd64 libqrcodegencpp1 amd64 1.8.0-1.2+b3 [25.6 kB]                                          
Get:53 http://kali.download/kali kali-rolling/main amd64 libsrt-openssl-dev amd64 1.5.7-1 [398 kB]                                              
Get:54 http://kali.download/kali kali-rolling/main amd64 libtasn1-doc all 4.21.0-2 [321 kB]                                                     
Get:55 http://kali.download/kali kali-rolling/main amd64 libwayland-bin amd64 1.26.0-1 [21.7 kB]                                                
Get:57 http://kali.download/kali kali-rolling/main amd64 libx11-xcb-dev amd64 2:1.8.13-1 [252 kB]                                               
Get:58 http://http.kali.org/kali kali-rolling/main amd64 libx264-dev amd64 2:0.165.3223+git20250910.0480cb0-1 [19.0 kB]                         
Get:59 http://http.kali.org/kali kali-rolling/main amd64 libxcb-render0-dev amd64 1.17.0-2+b2 [118 kB]                                          
Get:60 http://http.kali.org/kali kali-rolling/main amd64 libxcb-shape0-dev amd64 1.17.0-2+b2 [107 kB]                                           
Get:61 http://http.kali.org/kali kali-rolling/main amd64 libxcb-xfixes0-dev amd64 1.17.0-2+b2 [112 kB]                                          
Get:62 http://http.kali.org/kali kali-rolling/main amd64 libxcb-composite0-dev amd64 1.17.0-2+b2 [106 kB]                                       
Get:63 http://http.kali.org/kali kali-rolling/main amd64 libxcb-randr0-dev amd64 1.17.0-2+b2 [120 kB]                                           
Get:64 http://http.kali.org/kali kali-rolling/main amd64 libxcb-shm0-dev amd64 1.17.0-2+b2 [108 kB]                                             
Get:65 http://http.kali.org/kali kali-rolling/main amd64 libxcb-xinerama0-dev amd64 1.17.0-2+b2 [106 kB]                                        
Get:66 http://http.kali.org/kali kali-rolling/main amd64 libxfixes-dev amd64 1:6.0.0-2+b5 [22.4 kB]                                             
Get:67 http://http.kali.org/kali kali-rolling/main amd64 libxcomposite-dev amd64 1:0.4.6-1+b2 [20.4 kB]                                         
Get:68 http://http.kali.org/kali kali-rolling/main amd64 libxinerama-dev amd64 2:1.1.4-3+b5 [18.4 kB]                                           
Get:69 http://http.kali.org/kali kali-rolling/main amd64 libxss-dev amd64 1:1.2.3-1+b4 [22.8 kB]                                                
Get:71 http://http.kali.org/kali kali-rolling/main amd64 uthash-dev amd64 2.3.0-2+b1 [197 kB]                                                   
Get:51 http://http.kali.org/kali kali-rolling/main amd64 libsimde-dev all 0.8.4~rc3-5 [500 kB]                                                  
Get:52 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libsrt1.5-openssl amd64 1.5.7-1 [357 kB]                             
Get:56 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libwayland-dev amd64 1.26.0-1 [78.1 kB]                              
Fetched 29.8 MB in 8s (3,803 kB/s)                                                                                                              
Extracting templates from packages: 100%
Selecting previously unselected package doxygen-awesome-css.
(Reading database… 821292 files and directories currently installed.)
Preparing to unpack …/00-doxygen-awesome-css_2.4.2-2_all.deb…
Unpacking doxygen-awesome-css (2.4.2-2)…
Selecting previously unselected package cmocka-doc.
Preparing to unpack …/01-cmocka-doc_2.0.2-1_all.deb…
Unpacking cmocka-doc (2.0.2-1)…
Selecting previously unselected package libavutil-dev:amd64.
Preparing to unpack …/02-libavutil-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavutil-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libswresample-dev:amd64.
Preparing to unpack …/03-libswresample-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libswresample-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libavcodec-dev:amd64.
Preparing to unpack …/04-libavcodec-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavcodec-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libavdevice62:amd64.
Preparing to unpack …/05-libavdevice62_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavdevice62:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libavformat-dev:amd64.
Preparing to unpack …/06-libavformat-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavformat-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libswscale-dev:amd64.
Preparing to unpack …/07-libswscale-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libswscale-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libavfilter-dev:amd64.
Preparing to unpack …/08-libavfilter-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavfilter-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libavdevice-dev:amd64.
Preparing to unpack …/09-libavdevice-dev_7%3a8.1.2-2+b3_amd64.deb…
Unpacking libavdevice-dev:amd64 (7:8.1.2-2+b3)…
Selecting previously unselected package libbrotli-dev:amd64.
Preparing to unpack …/10-libbrotli-dev_1.2.0-4+b1_amd64.deb…
Unpacking libbrotli-dev:amd64 (1.2.0-4+b1)…
Selecting previously unselected package libcjson-dev:amd64.
Preparing to unpack …/11-libcjson-dev_1.7.19-2+b1_amd64.deb…
Unpacking libcjson-dev:amd64 (1.7.19-2+b1)…
Selecting previously unselected package libcmocka0:amd64.
Preparing to unpack …/12-libcmocka0_2.0.2-1+b1_amd64.deb…
Unpacking libcmocka0:amd64 (2.0.2-1+b1)…
Selecting previously unselected package libcmocka-dev:amd64.
Preparing to unpack …/13-libcmocka-dev_2.0.2-1+b1_amd64.deb…
Unpacking libcmocka-dev:amd64 (2.0.2-1+b1)…
Selecting previously unselected package libidn2-dev:amd64.
Preparing to unpack …/14-libidn2-dev_2.3.8-5_amd64.deb…
Unpacking libidn2-dev:amd64 (2.3.8-5)…
Selecting previously unselected package libldap-dev:amd64.
Preparing to unpack …/15-libldap-dev_2.6.14+dfsg-2_amd64.deb…
Unpacking libldap-dev:amd64 (2.6.14+dfsg-2)…
Selecting previously unselected package libnghttp2-dev:amd64.
Preparing to unpack …/16-libnghttp2-dev_1.70.0-1_amd64.deb…
Unpacking libnghttp2-dev:amd64 (1.70.0-1)…
Selecting previously unselected package libnghttp3-dev:amd64.
Preparing to unpack …/17-libnghttp3-dev_1.17.0-1_amd64.deb…
Unpacking libnghttp3-dev:amd64 (1.17.0-1)…
Selecting previously unselected package libngtcp2-crypto-ossl-dev:amd64.
Preparing to unpack …/18-libngtcp2-crypto-ossl-dev_1.24.0-1_amd64.deb…
Unpacking libngtcp2-crypto-ossl-dev:amd64 (1.24.0-1)…
Selecting previously unselected package libngtcp2-dev:amd64.
Preparing to unpack …/19-libngtcp2-dev_1.24.0-1_amd64.deb…
Unpacking libngtcp2-dev:amd64 (1.24.0-1)…
Selecting previously unselected package libunistring-dev:amd64.
Preparing to unpack …/20-libunistring-dev_1.4.2-1_amd64.deb…
Unpacking libunistring-dev:amd64 (1.4.2-1)…
Selecting previously unselected package libpsl-dev:amd64.
Preparing to unpack …/21-libpsl-dev_0.23.3-1_amd64.deb…
Unpacking libpsl-dev:amd64 (0.23.3-1)…
Selecting previously unselected package libp11-kit-dev:amd64.
Preparing to unpack …/22-libp11-kit-dev_0.26.5-1_amd64.deb…
Unpacking libp11-kit-dev:amd64 (0.26.5-1)…
Selecting previously unselected package libtasn1-6-dev:amd64.
Preparing to unpack …/23-libtasn1-6-dev_4.21.0-2+b1_amd64.deb…
Unpacking libtasn1-6-dev:amd64 (4.21.0-2+b1)…
Selecting previously unselected package nettle-dev:amd64.
Preparing to unpack …/24-nettle-dev_3.10.2-1+b1_amd64.deb…
Unpacking nettle-dev:amd64 (3.10.2-1+b1)…
Selecting previously unselected package libgnutls28-dev:amd64.
Preparing to unpack …/25-libgnutls28-dev_3.8.13-1_amd64.deb…
Unpacking libgnutls28-dev:amd64 (3.8.13-1)…
Selecting previously unselected package librtmp-dev:amd64.
Preparing to unpack …/26-librtmp-dev_2.6-1_amd64.deb…
Unpacking librtmp-dev:amd64 (2.6-1)…
Selecting previously unselected package libssl-dev:amd64.
Preparing to unpack …/27-libssl-dev_3.6.4-1_amd64.deb…
Unpacking libssl-dev:amd64 (3.6.4-1)…
Selecting previously unselected package libssh2-1-dev:amd64.
Preparing to unpack …/28-libssh2-1-dev_1.11.1-6_amd64.deb…
Unpacking libssh2-1-dev:amd64 (1.11.1-6)…
Selecting previously unselected package libzstd-dev:amd64.
Preparing to unpack …/29-libzstd-dev_1.5.7+dfsg-4_amd64.deb…
Unpacking libzstd-dev:amd64 (1.5.7+dfsg-4)…
Selecting previously unselected package libcurl4-openssl-dev:amd64.
Preparing to unpack …/30-libcurl4-openssl-dev_8.21.0-2_amd64.deb…
Unpacking libcurl4-openssl-dev:amd64 (8.21.0-2)…
Selecting previously unselected package libegl-dev:amd64.
Preparing to unpack …/31-libegl-dev_1.7.0-3+b1_amd64.deb…
Unpacking libegl-dev:amd64 (1.7.0-3+b1)…
Selecting previously unselected package libglvnd-core-dev:amd64.
Preparing to unpack …/32-libglvnd-core-dev_1.7.0-3+b1_amd64.deb…
Unpacking libglvnd-core-dev:amd64 (1.7.0-3+b1)…
Selecting previously unselected package libgles1:amd64.
Preparing to unpack …/33-libgles1_1.7.0-3+b1_amd64.deb…
Unpacking libgles1:amd64 (1.7.0-3+b1)…
Selecting previously unselected package libgles-dev:amd64.
Preparing to unpack …/34-libgles-dev_1.7.0-3+b1_amd64.deb…
Unpacking libgles-dev:amd64 (1.7.0-3+b1)…
Selecting previously unselected package libglvnd-dev:amd64.
Preparing to unpack …/35-libglvnd-dev_1.7.0-3+b1_amd64.deb…
Unpacking libglvnd-dev:amd64 (1.7.0-3+b1)…
Selecting previously unselected package libgl1-mesa-dev:amd64.
Preparing to unpack …/36-libgl1-mesa-dev_26.1.6-1_amd64.deb…
Unpacking libgl1-mesa-dev:amd64 (26.1.6-1)…
Selecting previously unselected package libgles2-mesa-dev:amd64.
Preparing to unpack …/37-libgles2-mesa-dev_26.1.6-1_amd64.deb…
Unpacking libgles2-mesa-dev:amd64 (26.1.6-1)…
Selecting previously unselected package libjansson-dev:amd64.
Preparing to unpack …/38-libjansson-dev_2.15.1-1_amd64.deb…
Unpacking libjansson-dev:amd64 (2.15.1-1)…
Selecting previously unselected package libluajit-5.1-dev:amd64.
Preparing to unpack …/39-libluajit-5.1-dev_2.1.0+openresty20251030-1+b2_amd64.deb…
Unpacking libluajit-5.1-dev:amd64 (2.1.0+openresty20251030-1+b2)…
Selecting previously unselected package libmbedx509-7:amd64.
Preparing to unpack …/40-libmbedx509-7_3.6.7-3_amd64.deb…
Unpacking libmbedx509-7:amd64 (3.6.7-3)…
Selecting previously unselected package libmbedtls21:amd64.
Preparing to unpack …/41-libmbedtls21_3.6.7-3_amd64.deb…
Unpacking libmbedtls21:amd64 (3.6.7-3)…
Selecting previously unselected package libmbedtls-dev:amd64.
Preparing to unpack …/42-libmbedtls-dev_3.6.7-3_amd64.deb…
Unpacking libmbedtls-dev:amd64 (3.6.7-3)…
Selecting previously unselected package libudev-dev:amd64.
Preparing to unpack …/43-libudev-dev_261.2-1_amd64.deb…
Unpacking libudev-dev:amd64 (261.2-1)…
Selecting previously unselected package libpci-dev:amd64.
Preparing to unpack …/44-libpci-dev_1%3a3.15.0-2_amd64.deb…
Unpacking libpci-dev:amd64 (1:3.15.0-2)…
Selecting previously unselected package libspa-0.2-dev:amd64.
Preparing to unpack …/45-libspa-0.2-dev_1.6.8-1_amd64.deb…
Unpacking libspa-0.2-dev:amd64 (1.6.8-1)…
Selecting previously unselected package libpipewire-0.3-dev:amd64.
Preparing to unpack …/46-libpipewire-0.3-dev_1.6.8-1_amd64.deb…
Unpacking libpipewire-0.3-dev:amd64 (1.6.8-1)…
Selecting previously unselected package libqrcodegencpp1:amd64.
Preparing to unpack …/47-libqrcodegencpp1_1.8.0-1.2+b3_amd64.deb…
Unpacking libqrcodegencpp1:amd64 (1.8.0-1.2+b3)…
Selecting previously unselected package libqrcodegencpp-dev:amd64.
Preparing to unpack …/48-libqrcodegencpp-dev_1.8.0-1.2+b3_amd64.deb…
Unpacking libqrcodegencpp-dev:amd64 (1.8.0-1.2+b3)…
Selecting previously unselected package librist-dev:amd64.
Preparing to unpack …/49-librist-dev_0.2.20+dfsg-1_amd64.deb…
Unpacking librist-dev:amd64 (0.2.20+dfsg-1)…
Selecting previously unselected package libsimde-dev.
Preparing to unpack …/50-libsimde-dev_0.8.4~rc3-5_all.deb…
Unpacking libsimde-dev (0.8.4~rc3-5)…
Selecting previously unselected package libsrt1.5-openssl:amd64.
Preparing to unpack …/51-libsrt1.5-openssl_1.5.7-1_amd64.deb…
Unpacking libsrt1.5-openssl:amd64 (1.5.7-1)…
Selecting previously unselected package libsrt-openssl-dev:amd64.
Preparing to unpack …/52-libsrt-openssl-dev_1.5.7-1_amd64.deb…
Unpacking libsrt-openssl-dev:amd64 (1.5.7-1)…
Selecting previously unselected package libtasn1-doc.
Preparing to unpack …/53-libtasn1-doc_4.21.0-2_all.deb…
Unpacking libtasn1-doc (4.21.0-2)…
Selecting previously unselected package libwayland-bin.
Preparing to unpack …/54-libwayland-bin_1.26.0-1_amd64.deb…
Unpacking libwayland-bin (1.26.0-1)…
Selecting previously unselected package libwayland-dev:amd64.
Preparing to unpack …/55-libwayland-dev_1.26.0-1_amd64.deb…
Unpacking libwayland-dev:amd64 (1.26.0-1)…
Selecting previously unselected package libx11-xcb-dev:amd64.
Preparing to unpack …/56-libx11-xcb-dev_2%3a1.8.13-1_amd64.deb…
Unpacking libx11-xcb-dev:amd64 (2:1.8.13-1)…
Selecting previously unselected package libx264-dev:amd64.
Preparing to unpack …/57-libx264-dev_2%3a0.165.3223+git20250910.0480cb0-1_amd64.deb…
Unpacking libx264-dev:amd64 (2:0.165.3223+git20250910.0480cb0-1)…
Selecting previously unselected package libxcb-render0-dev:amd64.
Preparing to unpack …/58-libxcb-render0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-render0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-shape0-dev:amd64.
Preparing to unpack …/59-libxcb-shape0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-shape0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-xfixes0-dev:amd64.
Preparing to unpack …/60-libxcb-xfixes0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-xfixes0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-composite0-dev:amd64.
Preparing to unpack …/61-libxcb-composite0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-composite0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-randr0-dev:amd64.
Preparing to unpack …/62-libxcb-randr0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-randr0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-shm0-dev:amd64.
Preparing to unpack …/63-libxcb-shm0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-shm0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxcb-xinerama0-dev:amd64.
Preparing to unpack …/64-libxcb-xinerama0-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-xinerama0-dev:amd64 (1.17.0-2+b2)…
Selecting previously unselected package libxfixes-dev:amd64.
Preparing to unpack …/65-libxfixes-dev_1%3a6.0.0-2+b5_amd64.deb…
Unpacking libxfixes-dev:amd64 (1:6.0.0-2+b5)…
Selecting previously unselected package libxcomposite-dev:amd64.
Preparing to unpack …/66-libxcomposite-dev_1%3a0.4.6-1+b2_amd64.deb…
Unpacking libxcomposite-dev:amd64 (1:0.4.6-1+b2)…
Selecting previously unselected package libxinerama-dev:amd64.
Preparing to unpack …/67-libxinerama-dev_2%3a1.1.4-3+b5_amd64.deb…
Unpacking libxinerama-dev:amd64 (2:1.1.4-3+b5)…
Selecting previously unselected package libxss-dev:amd64.
Preparing to unpack …/68-libxss-dev_1%3a1.2.3-1+b4_amd64.deb…
Unpacking libxss-dev:amd64 (1:1.2.3-1+b4)…
Selecting previously unselected package swig.
Preparing to unpack …/69-swig_4.5.1-2_amd64.deb…
Unpacking swig (4.5.1-2)…
Selecting previously unselected package uthash-dev:amd64.
Preparing to unpack …/70-uthash-dev_2.3.0-2+b1_amd64.deb…
Unpacking uthash-dev:amd64 (2.3.0-2+b1)…
Setting up libunistring-dev:amd64 (1.4.2-1)…
Setting up libavutil-dev:amd64 (7:8.1.2-2+b3)…
Setting up libsimde-dev (0.8.4~rc3-5)…
Setting up libnghttp2-dev:amd64 (1.70.0-1)…
Setting up libx11-xcb-dev:amd64 (2:1.8.13-1)…
Setting up libqrcodegencpp1:amd64 (1.8.0-1.2+b3)…
Setting up libcjson-dev:amd64 (1.7.19-2+b1)…
Setting up swig (4.5.1-2)…
Setting up uthash-dev:amd64 (2.3.0-2+b1)…
Setting up libzstd-dev:amd64 (1.5.7+dfsg-4)…
Setting up libglvnd-core-dev:amd64 (1.7.0-3+b1)…
Setting up nettle-dev:amd64 (3.10.2-1+b1)…
Setting up libegl-dev:amd64 (1.7.0-3+b1)…
Setting up libswresample-dev:amd64 (7:8.1.2-2+b3)…
Setting up libavcodec-dev:amd64 (7:8.1.2-2+b3)…
Setting up libtasn1-doc (4.21.0-2)…
Setting up libxcb-xinerama0-dev:amd64 (1.17.0-2+b2)…
Setting up libavformat-dev:amd64 (7:8.1.2-2+b3)…
Setting up libngtcp2-dev:amd64 (1.24.0-1)…
Setting up libxss-dev:amd64 (1:1.2.3-1+b4)…
Setting up libx264-dev:amd64 (2:0.165.3223+git20250910.0480cb0-1)…
Setting up doxygen-awesome-css (2.4.2-2)…
Setting up libcmocka0:amd64 (2.0.2-1+b1)…
Setting up libavdevice62:amd64 (7:8.1.2-2+b3)…
Setting up libxfixes-dev:amd64 (1:6.0.0-2+b5)…
Setting up libqrcodegencpp-dev:amd64 (1.8.0-1.2+b3)…
Setting up libsrt1.5-openssl:amd64 (1.5.7-1)…
Setting up libxcb-shm0-dev:amd64 (1.17.0-2+b2)…
Setting up libwayland-bin (1.26.0-1)…
Setting up libmbedx509-7:amd64 (3.6.7-3)…
Setting up libldap-dev:amd64 (2.6.14+dfsg-2)…
Setting up libgles1:amd64 (1.7.0-3+b1)…
Setting up libswscale-dev:amd64 (7:8.1.2-2+b3)…
Setting up libssl-dev:amd64 (3.6.4-1)…
Setting up libudev-dev:amd64 (261.2-1)…
Setting up libxinerama-dev:amd64 (2:1.1.4-3+b5)…
Setting up libsrt-openssl-dev:amd64 (1.5.7-1)…
Setting up libxcb-render0-dev:amd64 (1.17.0-2+b2)…
Setting up libcmocka-dev:amd64 (2.0.2-1+b1)…
Setting up libssh2-1-dev:amd64 (1.11.1-6)…
Setting up libidn2-dev:amd64 (2.3.8-5)…
Setting up libluajit-5.1-dev:amd64 (2.1.0+openresty20251030-1+b2)…
Setting up libxcb-shape0-dev:amd64 (1.17.0-2+b2)…
Setting up libmbedtls21:amd64 (3.6.7-3)…
Setting up cmocka-doc (2.0.2-1)…
Setting up libnghttp3-dev:amd64 (1.17.0-1)…
Setting up libngtcp2-crypto-ossl-dev:amd64 (1.24.0-1)…
Setting up libxcb-xfixes0-dev:amd64 (1.17.0-2+b2)…
Setting up libgles-dev:amd64 (1.7.0-3+b1)…
Setting up libspa-0.2-dev:amd64 (1.6.8-1)…
Setting up libtasn1-6-dev:amd64 (4.21.0-2+b1)…
Setting up libjansson-dev:amd64 (2.15.1-1)…
Setting up libbrotli-dev:amd64 (1.2.0-4+b1)…
Setting up libp11-kit-dev:amd64 (0.26.5-1)…
Setting up libpci-dev:amd64 (1:3.15.0-2)…
Setting up libgnutls28-dev:amd64 (3.8.13-1)…
Setting up librist-dev:amd64 (0.2.20+dfsg-1)…
Setting up libxcb-composite0-dev:amd64 (1.17.0-2+b2)…
Setting up libxcomposite-dev:amd64 (1:0.4.6-1+b2)…
Setting up libavfilter-dev:amd64 (7:8.1.2-2+b3)…
Setting up libglvnd-dev:amd64 (1.7.0-3+b1)…
Setting up libmbedtls-dev:amd64 (3.6.7-3)…
Setting up libwayland-dev:amd64 (1.26.0-1)…
Setting up libpsl-dev:amd64 (0.23.3-1)…
Setting up libxcb-randr0-dev:amd64 (1.17.0-2+b2)…
Setting up librtmp-dev:amd64 (2.6-1)…
Setting up libpipewire-0.3-dev:amd64 (1.6.8-1)…
Setting up libgl1-mesa-dev:amd64 (26.1.6-1)…
Setting up libavdevice-dev:amd64 (7:8.1.2-2+b3)…
Setting up libgles2-mesa-dev:amd64 (26.1.6-1)…
Setting up libcurl4-openssl-dev:amd64 (8.21.0-2)…
Processing triggers for doc-base (0.11.2)…
Processing 5 added doc-base files...
Processing triggers for libc-bin (2.43-4)…
Processing triggers for man-db (2.13.1-1)…
Processing triggers for kali-menu (2026.3.4)…
Scanning processes...                                                                                                                            
Scanning processor microcode...                                                                                                                  
Scanning linux images...                                                                                                                         

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ sudo apt install qt6-base-dev qt6-base-private-dev qt6-svg-dev qt6-wayland qt6-image-formats-plugins  
qt6-wayland is already the newest version (6.10.2-5).
qt6-wayland set to manually installed.
Installing:                 
  qt6-base-dev  qt6-base-private-dev  qt6-image-formats-plugins  qt6-svg-dev
                                                                                                                                                 
Installing dependencies:
  bzip2-doc            libbz2-dev         libgio-2.0-dev-bin  libmng2       libpng-tools              libvulkan-dev     qtpaths6
  gir1.2-glib-2.0-dev  libevdev-dev       libglib2.0-dev      libmount-dev  libqt6concurrent6         libwacom-dev      qtpaths6-bin             
  gir1.2-gudev-1.0     libfontconfig-dev  libglib2.0-dev-bin  libmtdev-dev  libselinux-dev            libxkbcommon-dev                           
  girepository-tools   libfreetype-dev    libgudev-1.0-dev    libpcre2-dev  libsepol-dev              qmake6                                     
  libblkid-dev         libgio-2.0-dev     libinput-dev        libpng-dev    libsysprof-capture-4-dev  qmake6-bin                                 
                                                                                                                                                 
Suggested packages:
  libevdev-doc  freetype2-doc  libglib2.0-doc  libgdk-pixbuf2.0-bin

Summary:
  Upgrading: 0, Installing: 36, Removing: 0, Not Upgrading: 1
  Download size: 13.2 MB
  Space needed: 114 MB / 154 GB available

Continue? [Y/n] y
Get:1 http://kali.download/kali kali-rolling/main amd64 bzip2-doc all 1.0.8-6 [505 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 gir1.2-glib-2.0-dev amd64 2.90.0-1 [908 kB]
Get:3 http://http.kali.org/kali kali-rolling/main amd64 gir1.2-gudev-1.0 amd64 238-7+b2 [5,048 B]                           
Get:4 http://kali.download/kali kali-rolling/main amd64 girepository-tools amd64 2.90.0-1 [138 kB]                                              
Get:7 http://http.kali.org/kali kali-rolling/main amd64 libevdev-dev amd64 1.13.7+dfsg-1 [50.9 kB]                                              
Get:5 http://kali.download/kali kali-rolling/main amd64 libblkid-dev amd64 2.42.3-1 [224 kB]                                                    
Get:6 http://http.kali.org/kali kali-rolling/main amd64 libbz2-dev amd64 1.0.8-6+b2 [33.6 kB]                                                   
Get:8 http://kali.download/kali kali-rolling/main amd64 libpng-dev amd64 1.6.58-1 [372 kB]                             
Get:9 http://http.kali.org/kali kali-rolling/main amd64 libfreetype-dev amd64 2.14.3+dfsg-2 [663 kB]                 
Get:10 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libfontconfig-dev amd64 2.17.1-5 [155 kB]                   
Get:12 http://kali.download/kali kali-rolling/main amd64 libpcre2-dev amd64 10.48-2 [880 kB]                                                 
Get:13 http://kali.download/kali kali-rolling/main amd64 libselinux-dev amd64 3.11-2 [173 kB]                                              
Get:17 http://kali.download/kali kali-rolling/main amd64 libgio-2.0-dev-bin amd64 2.90.0-1 [152 kB]                            
Get:18 http://kali.download/kali kali-rolling/main amd64 libglib2.0-dev-bin amd64 2.90.0-1 [38.6 kB]                                
Get:20 http://http.kali.org/kali kali-rolling/main amd64 libgudev-1.0-dev amd64 238-7+b2 [28.8 kB]                                   
Get:14 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libmount-dev amd64 2.42.3-1 [26.9 kB]                   
Get:16 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libgio-2.0-dev amd64 2.90.0-1 [1,779 kB]                             
Get:21 http://http.kali.org/kali kali-rolling/main amd64 libmtdev-dev amd64 1.1.7-1+b2 [24.0 kB]                                 
Get:22 http://kali.download/kali kali-rolling/main amd64 libwacom-dev amd64 2.20.0-1 [10.2 kB]                                              
Get:23 http://kali.download/kali kali-rolling/main amd64 libinput-dev amd64 1.31.3-1 [36.9 kB]                          
Get:24 http://http.kali.org/kali kali-rolling/main amd64 libmng2 amd64 2.0.3+dfsg-5+b1 [192 kB]                              
Get:25 http://kali.download/kali kali-rolling/main amd64 libpng-tools amd64 1.6.58-1 [132 kB]                         
Get:26 http://http.kali.org/kali kali-rolling/main amd64 libqt6concurrent6 amd64 6.10.2+dfsg-16 [38.2 kB]              
Get:29 http://http.kali.org/kali kali-rolling/main amd64 qmake6-bin amd64 6.10.2+dfsg-16 [709 kB]                                 
Get:11 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libsepol-dev amd64 3.11-1 [378 kB]                         
Get:30 http://http.kali.org/kali kali-rolling/main amd64 qtpaths6-bin amd64 6.10.2+dfsg-16 [58.4 kB]                                   
Get:31 http://http.kali.org/kali kali-rolling/main amd64 qtpaths6 amd64 6.10.2+dfsg-16 [31.7 kB]                                            
Get:15 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libsysprof-capture-4-dev amd64 50.0-3 [47.8 kB]      
Get:19 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libglib2.0-dev amd64 2.90.0-1 [39.3 kB]               
Get:35 http://kali.download/kali kali-rolling/main amd64 qt6-image-formats-plugins amd64 6.10.2-3 [52.7 kB]
Get:27 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libvulkan-dev amd64 1.4.357.0-1 [1,910 kB]                                
Get:36 http://kali.download/kali kali-rolling/main amd64 qt6-svg-dev amd64 6.10.2-9 [23.2 kB]             
Get:28 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 libxkbcommon-dev amd64 1.13.1-1 [60.1 kB]     
Get:32 http://http.kali.org/kali kali-rolling/main amd64 qmake6 amd64 6.10.2+dfsg-16 [146 kB]
Get:33 http://http.kali.org/kali kali-rolling/main amd64 qt6-base-dev amd64 6.10.2+dfsg-16 [2,283 kB]
Get:34 http://http.kali.org/kali kali-rolling/main amd64 qt6-base-private-dev amd64 6.10.2+dfsg-16 [892 kB]
Fetched 13.2 MB in 3s (4,810 kB/s)                                                    
Extracting templates from packages: 100%
Selecting previously unselected package bzip2-doc.
(Reading database… 825187 files and directories currently installed.)
Preparing to unpack …/00-bzip2-doc_1.0.8-6_all.deb…
Unpacking bzip2-doc (1.0.8-6)…
Selecting previously unselected package gir1.2-glib-2.0-dev:amd64.
Preparing to unpack …/01-gir1.2-glib-2.0-dev_2.90.0-1_amd64.deb…
Unpacking gir1.2-glib-2.0-dev:amd64 (2.90.0-1)…
Selecting previously unselected package gir1.2-gudev-1.0:amd64.
Preparing to unpack …/02-gir1.2-gudev-1.0_238-7+b2_amd64.deb…
Unpacking gir1.2-gudev-1.0:amd64 (238-7+b2)…
Selecting previously unselected package girepository-tools:amd64.
Preparing to unpack …/03-girepository-tools_2.90.0-1_amd64.deb…
Unpacking girepository-tools:amd64 (2.90.0-1)…
Selecting previously unselected package libblkid-dev:amd64.
Preparing to unpack …/04-libblkid-dev_2.42.3-1_amd64.deb…
Unpacking libblkid-dev:amd64 (2.42.3-1)…
Selecting previously unselected package libbz2-dev:amd64.
Preparing to unpack …/05-libbz2-dev_1.0.8-6+b2_amd64.deb…
Unpacking libbz2-dev:amd64 (1.0.8-6+b2)…
Selecting previously unselected package libevdev-dev:amd64.
Preparing to unpack …/06-libevdev-dev_1.13.7+dfsg-1_amd64.deb…
Unpacking libevdev-dev:amd64 (1.13.7+dfsg-1)…
Selecting previously unselected package libpng-dev:amd64.
Preparing to unpack …/07-libpng-dev_1.6.58-1_amd64.deb…
Unpacking libpng-dev:amd64 (1.6.58-1)…
Selecting previously unselected package libfreetype-dev:amd64.
Preparing to unpack …/08-libfreetype-dev_2.14.3+dfsg-2_amd64.deb…
Unpacking libfreetype-dev:amd64 (2.14.3+dfsg-2)…
Selecting previously unselected package libfontconfig-dev:amd64.
Preparing to unpack …/09-libfontconfig-dev_2.17.1-5_amd64.deb…
Unpacking libfontconfig-dev:amd64 (2.17.1-5)…
Selecting previously unselected package libsepol-dev:amd64.
Preparing to unpack …/10-libsepol-dev_3.11-1_amd64.deb…
Unpacking libsepol-dev:amd64 (3.11-1)…
Selecting previously unselected package libpcre2-dev:amd64.
Preparing to unpack …/11-libpcre2-dev_10.48-2_amd64.deb…
Unpacking libpcre2-dev:amd64 (10.48-2)…
Selecting previously unselected package libselinux-dev:amd64.
Preparing to unpack …/12-libselinux-dev_3.11-2_amd64.deb…
Unpacking libselinux-dev:amd64 (3.11-2)…
Selecting previously unselected package libmount-dev:amd64.
Preparing to unpack …/13-libmount-dev_2.42.3-1_amd64.deb…
Unpacking libmount-dev:amd64 (2.42.3-1)…
Selecting previously unselected package libsysprof-capture-4-dev:amd64.
Preparing to unpack …/14-libsysprof-capture-4-dev_50.0-3_amd64.deb…
Unpacking libsysprof-capture-4-dev:amd64 (50.0-3)…
Selecting previously unselected package libgio-2.0-dev:amd64.
Preparing to unpack …/15-libgio-2.0-dev_2.90.0-1_amd64.deb…
Unpacking libgio-2.0-dev:amd64 (2.90.0-1)…
Selecting previously unselected package libgio-2.0-dev-bin.
Preparing to unpack …/16-libgio-2.0-dev-bin_2.90.0-1_amd64.deb…
Unpacking libgio-2.0-dev-bin (2.90.0-1)…
Selecting previously unselected package libglib2.0-dev-bin.
Preparing to unpack …/17-libglib2.0-dev-bin_2.90.0-1_amd64.deb…
Unpacking libglib2.0-dev-bin (2.90.0-1)…
Selecting previously unselected package libglib2.0-dev:amd64.
Preparing to unpack …/18-libglib2.0-dev_2.90.0-1_amd64.deb…
Unpacking libglib2.0-dev:amd64 (2.90.0-1)…
Selecting previously unselected package libgudev-1.0-dev:amd64.
Preparing to unpack …/19-libgudev-1.0-dev_238-7+b2_amd64.deb…
Unpacking libgudev-1.0-dev:amd64 (238-7+b2)…
Selecting previously unselected package libmtdev-dev:amd64.
Preparing to unpack …/20-libmtdev-dev_1.1.7-1+b2_amd64.deb…
Unpacking libmtdev-dev:amd64 (1.1.7-1+b2)…
Selecting previously unselected package libwacom-dev:amd64.
Preparing to unpack …/21-libwacom-dev_2.20.0-1_amd64.deb…
Unpacking libwacom-dev:amd64 (2.20.0-1)…
Selecting previously unselected package libinput-dev:amd64.
Preparing to unpack …/22-libinput-dev_1.31.3-1_amd64.deb…
Unpacking libinput-dev:amd64 (1.31.3-1)…
Selecting previously unselected package libmng2:amd64.
Preparing to unpack …/23-libmng2_2.0.3+dfsg-5+b1_amd64.deb…
Unpacking libmng2:amd64 (2.0.3+dfsg-5+b1)…
Selecting previously unselected package libpng-tools.
Preparing to unpack …/24-libpng-tools_1.6.58-1_amd64.deb…
Unpacking libpng-tools (1.6.58-1)…
Selecting previously unselected package libqt6concurrent6:amd64.
Preparing to unpack …/25-libqt6concurrent6_6.10.2+dfsg-16_amd64.deb…
Unpacking libqt6concurrent6:amd64 (6.10.2+dfsg-16)…
Selecting previously unselected package libvulkan-dev:amd64.
Preparing to unpack …/26-libvulkan-dev_1.4.357.0-1_amd64.deb…
Unpacking libvulkan-dev:amd64 (1.4.357.0-1)…
Selecting previously unselected package libxkbcommon-dev:amd64.
Preparing to unpack …/27-libxkbcommon-dev_1.13.1-1_amd64.deb…
Unpacking libxkbcommon-dev:amd64 (1.13.1-1)…
Selecting previously unselected package qmake6-bin.
Preparing to unpack …/28-qmake6-bin_6.10.2+dfsg-16_amd64.deb…
Unpacking qmake6-bin (6.10.2+dfsg-16)…
Selecting previously unselected package qtpaths6-bin.
Preparing to unpack …/29-qtpaths6-bin_6.10.2+dfsg-16_amd64.deb…
Unpacking qtpaths6-bin (6.10.2+dfsg-16)…
Selecting previously unselected package qtpaths6:amd64.
Preparing to unpack …/30-qtpaths6_6.10.2+dfsg-16_amd64.deb…
Unpacking qtpaths6:amd64 (6.10.2+dfsg-16)…
Selecting previously unselected package qmake6:amd64.
Preparing to unpack …/31-qmake6_6.10.2+dfsg-16_amd64.deb…
Unpacking qmake6:amd64 (6.10.2+dfsg-16)…
Selecting previously unselected package qt6-base-dev:amd64.
Preparing to unpack …/32-qt6-base-dev_6.10.2+dfsg-16_amd64.deb…
Unpacking qt6-base-dev:amd64 (6.10.2+dfsg-16)…
Selecting previously unselected package qt6-base-private-dev:amd64.
Preparing to unpack …/33-qt6-base-private-dev_6.10.2+dfsg-16_amd64.deb…
Unpacking qt6-base-private-dev:amd64 (6.10.2+dfsg-16)…
Selecting previously unselected package qt6-image-formats-plugins.
Preparing to unpack …/34-qt6-image-formats-plugins_6.10.2-3_amd64.deb…
Unpacking qt6-image-formats-plugins (6.10.2-3)…
Selecting previously unselected package qt6-svg-dev:amd64.
Preparing to unpack …/35-qt6-svg-dev_6.10.2-9_amd64.deb…
Unpacking qt6-svg-dev:amd64 (6.10.2-9)…
Setting up libqt6concurrent6:amd64 (6.10.2+dfsg-16)…
Setting up libblkid-dev:amd64 (2.42.3-1)…
Setting up bzip2-doc (1.0.8-6)…
Setting up libmng2:amd64 (2.0.3+dfsg-5+b1)…
Setting up libgio-2.0-dev-bin (2.90.0-1)…
Setting up libvulkan-dev:amd64 (1.4.357.0-1)…
Setting up girepository-tools:amd64 (2.90.0-1)…
Setting up libpcre2-dev:amd64 (10.48-2)…
Setting up qt6-image-formats-plugins (6.10.2-3)…
Setting up libpng-tools (1.6.58-1)…
Setting up libevdev-dev:amd64 (1.13.7+dfsg-1)…
Setting up libmtdev-dev:amd64 (1.1.7-1+b2)…
Setting up libxkbcommon-dev:amd64 (1.13.1-1)…
Setting up libpng-dev:amd64 (1.6.58-1)…
Setting up libsysprof-capture-4-dev:amd64 (50.0-3)…
Setting up qt6-svg-dev:amd64 (6.10.2-9)…
Setting up gir1.2-gudev-1.0:amd64 (238-7+b2)…
Setting up libsepol-dev:amd64 (3.11-1)…
Setting up qtpaths6-bin (6.10.2+dfsg-16)…
Setting up qmake6-bin (6.10.2+dfsg-16)…
Setting up gir1.2-glib-2.0-dev:amd64 (2.90.0-1)…
Setting up qtpaths6:amd64 (6.10.2+dfsg-16)…
Setting up libselinux-dev:amd64 (3.11-2)…
Setting up libmount-dev:amd64 (2.42.3-1)…
Setting up libbz2-dev:amd64 (1.0.8-6+b2)…
Setting up libglib2.0-dev-bin (2.90.0-1)…
Setting up libgio-2.0-dev:amd64 (2.90.0-1)…
Setting up qmake6:amd64 (6.10.2+dfsg-16)…
Setting up libfreetype-dev:amd64 (2.14.3+dfsg-2)…
Setting up qt6-base-dev:amd64 (6.10.2+dfsg-16)…
Setting up libfontconfig-dev:amd64 (2.17.1-5)…
Processing triggers for man-db (2.13.1-1)…
Processing triggers for libglib2.0-0t64:i386 (2.90.0-1)…
Processing triggers for libglib2.0-0t64:amd64 (2.90.0-1)…
Setting up libglib2.0-dev:amd64 (2.90.0-1)…
Processing triggers for kali-menu (2026.3.4)…
Processing triggers for doc-base (0.11.2)…
Processing 1 added doc-base file...
Processing triggers for libc-bin (2.43-4)…
Setting up libgudev-1.0-dev:amd64 (238-7+b2)…
Setting up libwacom-dev:amd64 (2.20.0-1)…
Setting up libinput-dev:amd64 (1.31.3-1)…
Setting up qt6-base-private-dev:amd64 (6.10.2+dfsg-16)…
Scanning processes...                                                                                                                            
Scanning processor microcode...                                                                                                                  
Scanning linux images...                                                                                                                         

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ sudo apt install libasound2-dev libfdk-aac-dev libfontconfig-dev libfreetype6-dev libjack-jackd2-dev libpulse-dev libsndio-dev libspeexdsp-dev libudev-dev libv4l-dev libva-dev libvlc-dev libvpl-dev libdrm-dev nlohmann-json3-dev libwebsocketpp-dev libasio-dev
Note, selecting 'libfreetype-dev' instead of 'libfreetype6-dev'
libfontconfig-dev is already the newest version (2.17.1-5).
libfontconfig-dev set to manually installed.
libfreetype-dev is already the newest version (2.14.3+dfsg-2).
libfreetype-dev set to manually installed.
libudev-dev is already the newest version (261.2-1).
libudev-dev set to manually installed.
Installing:                 
  libasio-dev     libdrm-dev      libjack-jackd2-dev  libsndio-dev     libv4l-dev  libvlc-dev  libwebsocketpp-dev
  libasound2-dev  libfdk-aac-dev  libpulse-dev        libspeexdsp-dev  libva-dev   libvpl-dev  nlohmann-json3-dev                                
                                                                                                                                                 
Installing dependencies:
  libboost-date-time-dev  libboost-regex-dev  libfdk-aac2t64  libjpeg62-turbo-dev  libset-scalar-perl  libv4l2rds0t64
  libboost-dev            libdrm-freedreno1   libjpeg-dev     libpciaccess-dev     libsndio7.0                                                   
                                                                                                                                                 
Suggested packages:
  libasound2-doc  libboost-doc  sndiod  libspeex-dev  speex-doc

Summary:
  Upgrading: 0, Installing: 25, Removing: 0, Not Upgrading: 1
  Download size: 4,026 kB
  Space needed: 19.7 MB / 154 GB available

Continue? [Y/n] y
Get:1 http://kali.download/kali kali-rolling/main amd64 libasio-dev all 1:1.36.0-1 [412 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 libasound2-dev amd64 1.2.16.1-1 [119 kB]
Get:4 http://http.kali.org/kali kali-rolling/main amd64 libboost-dev amd64 1.90.0.2+nmu1 [3,200 B]
Get:3 http://http.kali.org/kali kali-rolling/main amd64 libboost-date-time-dev amd64 1.90.0.2+nmu1 [2,988 B]          
Get:6 http://kali.download/kali kali-rolling/main amd64 libdrm-freedreno1 amd64 2.4.134-3 [21.2 kB]                         
Get:7 http://kali.download/kali kali-rolling/main amd64 libpciaccess-dev amd64 0.19-2 [21.9 kB]
Get:5 http://http.kali.org/kali kali-rolling/main amd64 libboost-regex-dev amd64 1.90.0.2+nmu1 [3,260 B]
Get:8 http://kali.download/kali kali-rolling/main amd64 libdrm-dev amd64 2.4.134-3 [323 kB]
Get:9 http://kali.download/kali kali-rolling/non-free amd64 libfdk-aac2t64 amd64 2.0.3-1 [656 kB]
Get:11 http://http.kali.org/kali kali-rolling/main amd64 libjack-jackd2-dev amd64 1.9.22~dfsg-6 [58.2 kB]
Get:12 http://kali.download/kali kali-rolling/main amd64 libjpeg62-turbo-dev amd64 1:3.1.3-4 [356 kB]
Get:13 http://kali.download/kali kali-rolling/main amd64 libjpeg-dev amd64 1:3.1.3-4 [78.8 kB]
Get:10 http://mirrors.dotsrc.org/kali kali-rolling/non-free amd64 libfdk-aac-dev amd64 2.0.3-1 [781 kB]
Get:16 http://http.kali.org/kali kali-rolling/main amd64 libsndio7.0 amd64 1.10.0-0.2+b2 [27.7 kB]
Get:18 http://kali.download/kali kali-rolling/main amd64 libspeexdsp-dev amd64 1.2.1-4 [53.1 kB]
Get:19 http://kali.download/kali kali-rolling/main amd64 libv4l2rds0t64 amd64 1.32.0-5 [88.2 kB]   
Get:20 http://kali.download/kali kali-rolling/main amd64 libv4l-dev amd64 1.32.0-5 [111 kB]       
Get:14 http://http.kali.org/kali kali-rolling/main amd64 libpulse-dev amd64 17.0+dfsg1-3 [86.1 kB]
Get:15 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libset-scalar-perl all 1.29-3 [32.1 kB]
Get:21 http://kali.download/kali kali-rolling/main amd64 libva-dev amd64 2.24.1-2 [130 kB] 
Get:17 http://http.kali.org/kali kali-rolling/main amd64 libsndio-dev amd64 1.10.0-0.2+b2 [24.9 kB]    
Get:22 http://http.kali.org/kali kali-rolling/main amd64 libvlc-dev amd64 3.0.23-3+b4 [133 kB]
Get:23 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 libvpl-dev amd64 1:2.17.0-1 [104 kB]
Get:25 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 nlohmann-json3-dev all 3.12.0.really.3.12.0.really.3.11.3-3 [263 kB]
Get:24 http://http.kali.org/kali kali-rolling/main amd64 libwebsocketpp-dev amd64 0.8.2+git20250909-3 [135 kB]
Fetched 4,026 kB in 3s (1,434 kB/s)                                                    
Selecting previously unselected package libasio-dev.
(Reading database… 831282 files and directories currently installed.)
Preparing to unpack …/00-libasio-dev_1%3a1.36.0-1_all.deb…
Unpacking libasio-dev (1:1.36.0-1)…
Selecting previously unselected package libasound2-dev:amd64.
Preparing to unpack …/01-libasound2-dev_1.2.16.1-1_amd64.deb…
Unpacking libasound2-dev:amd64 (1.2.16.1-1)…
Selecting previously unselected package libboost-date-time-dev:amd64.
Preparing to unpack …/02-libboost-date-time-dev_1.90.0.2+nmu1_amd64.deb…
Unpacking libboost-date-time-dev:amd64 (1.90.0.2+nmu1)…
Selecting previously unselected package libboost-dev:amd64.
Preparing to unpack …/03-libboost-dev_1.90.0.2+nmu1_amd64.deb…
Unpacking libboost-dev:amd64 (1.90.0.2+nmu1)…
Selecting previously unselected package libboost-regex-dev:amd64.
Preparing to unpack …/04-libboost-regex-dev_1.90.0.2+nmu1_amd64.deb…
Unpacking libboost-regex-dev:amd64 (1.90.0.2+nmu1)…
Selecting previously unselected package libdrm-freedreno1:amd64.
Preparing to unpack …/05-libdrm-freedreno1_2.4.134-3_amd64.deb…
Unpacking libdrm-freedreno1:amd64 (2.4.134-3)…
Selecting previously unselected package libpciaccess-dev:amd64.
Preparing to unpack …/06-libpciaccess-dev_0.19-2_amd64.deb…
Unpacking libpciaccess-dev:amd64 (0.19-2)…
Selecting previously unselected package libdrm-dev:amd64.
Preparing to unpack …/07-libdrm-dev_2.4.134-3_amd64.deb…
Unpacking libdrm-dev:amd64 (2.4.134-3)…
Selecting previously unselected package libfdk-aac2t64:amd64.
Preparing to unpack …/08-libfdk-aac2t64_2.0.3-1_amd64.deb…
Unpacking libfdk-aac2t64:amd64 (2.0.3-1)…
Selecting previously unselected package libfdk-aac-dev:amd64.
Preparing to unpack …/09-libfdk-aac-dev_2.0.3-1_amd64.deb…
Unpacking libfdk-aac-dev:amd64 (2.0.3-1)…
Selecting previously unselected package libjack-jackd2-dev:amd64.
Preparing to unpack …/10-libjack-jackd2-dev_1.9.22~dfsg-6_amd64.deb…
Unpacking libjack-jackd2-dev:amd64 (1.9.22~dfsg-6)…
Selecting previously unselected package libjpeg62-turbo-dev:amd64.
Preparing to unpack …/11-libjpeg62-turbo-dev_1%3a3.1.3-4_amd64.deb…
Unpacking libjpeg62-turbo-dev:amd64 (1:3.1.3-4)…
Selecting previously unselected package libjpeg-dev:amd64.
Preparing to unpack …/12-libjpeg-dev_1%3a3.1.3-4_amd64.deb…
Unpacking libjpeg-dev:amd64 (1:3.1.3-4)…
Selecting previously unselected package libpulse-dev:amd64.
Preparing to unpack …/13-libpulse-dev_17.0+dfsg1-3_amd64.deb…
Unpacking libpulse-dev:amd64 (17.0+dfsg1-3)…
Selecting previously unselected package libset-scalar-perl.
Preparing to unpack …/14-libset-scalar-perl_1.29-3_all.deb…
Unpacking libset-scalar-perl (1.29-3)…
Selecting previously unselected package libsndio7.0:amd64.
Preparing to unpack …/15-libsndio7.0_1.10.0-0.2+b2_amd64.deb…
Unpacking libsndio7.0:amd64 (1.10.0-0.2+b2)…
Selecting previously unselected package libsndio-dev:amd64.
Preparing to unpack …/16-libsndio-dev_1.10.0-0.2+b2_amd64.deb…
Unpacking libsndio-dev:amd64 (1.10.0-0.2+b2)…
Selecting previously unselected package libspeexdsp-dev:amd64.
Preparing to unpack …/17-libspeexdsp-dev_1.2.1-4_amd64.deb…
Unpacking libspeexdsp-dev:amd64 (1.2.1-4)…
Selecting previously unselected package libv4l2rds0t64:amd64.
Preparing to unpack …/18-libv4l2rds0t64_1.32.0-5_amd64.deb…
Unpacking libv4l2rds0t64:amd64 (1.32.0-5)…
Selecting previously unselected package libv4l-dev:amd64.
Preparing to unpack …/19-libv4l-dev_1.32.0-5_amd64.deb…
Unpacking libv4l-dev:amd64 (1.32.0-5)…
Selecting previously unselected package libva-dev:amd64.
Preparing to unpack …/20-libva-dev_2.24.1-2_amd64.deb…
Unpacking libva-dev:amd64 (2.24.1-2)…
Selecting previously unselected package libvlc-dev:amd64.
Preparing to unpack …/21-libvlc-dev_3.0.23-3+b4_amd64.deb…
Unpacking libvlc-dev:amd64 (3.0.23-3+b4)…
Selecting previously unselected package libvpl-dev.
Preparing to unpack …/22-libvpl-dev_1%3a2.17.0-1_amd64.deb…
Unpacking libvpl-dev (1:2.17.0-1)…
Selecting previously unselected package libwebsocketpp-dev:amd64.
Preparing to unpack …/23-libwebsocketpp-dev_0.8.2+git20250909-3_amd64.deb…
Unpacking libwebsocketpp-dev:amd64 (0.8.2+git20250909-3)…
Selecting previously unselected package nlohmann-json3-dev.
Preparing to unpack …/24-nlohmann-json3-dev_3.12.0.really.3.12.0.really.3.11.3-3_all.deb…
Unpacking nlohmann-json3-dev (3.12.0.really.3.12.0.really.3.11.3-3)…
Setting up libpciaccess-dev:amd64 (0.19-2)…
Setting up libspeexdsp-dev:amd64 (1.2.1-4)…
Setting up libjack-jackd2-dev:amd64 (1.9.22~dfsg-6)…
Setting up libjpeg62-turbo-dev:amd64 (1:3.1.3-4)…
Setting up libdrm-freedreno1:amd64 (2.4.134-3)…
Setting up libboost-date-time-dev:amd64 (1.90.0.2+nmu1)…
Setting up libpulse-dev:amd64 (17.0+dfsg1-3)…
Setting up libset-scalar-perl (1.29-3)…
Setting up libsndio7.0:amd64 (1.10.0-0.2+b2)…
Setting up libwebsocketpp-dev:amd64 (0.8.2+git20250909-3)…
Setting up libv4l2rds0t64:amd64 (1.32.0-5)…
Setting up libboost-dev:amd64 (1.90.0.2+nmu1)…
Setting up libasio-dev (1:1.36.0-1)…
Setting up nlohmann-json3-dev (3.12.0.really.3.12.0.really.3.11.3-3)…
Setting up libasound2-dev:amd64 (1.2.16.1-1)…
Setting up libboost-regex-dev:amd64 (1.90.0.2+nmu1)…
Setting up libvpl-dev (1:2.17.0-1)…
Setting up libfdk-aac2t64:amd64 (2.0.3-1)…
Setting up libvlc-dev:amd64 (3.0.23-3+b4)…
Setting up libdrm-dev:amd64 (2.4.134-3)…
Setting up libsndio-dev:amd64 (1.10.0-0.2+b2)…
Setting up libjpeg-dev:amd64 (1:3.1.3-4)…
Setting up libv4l-dev:amd64 (1.32.0-5)…
Setting up libfdk-aac-dev:amd64 (2.0.3-1)…
Setting up libva-dev:amd64 (2.24.1-2)…
Processing triggers for libc-bin (2.43-4)…
Processing triggers for man-db (2.13.1-1)…
Processing triggers for kali-menu (2026.3.4)…
Scanning processes...                                                                                                                            
Scanning processor microcode...                                                                                                                  
Scanning linux images...                                                                                                                         

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ cd Downloads
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads]
└─$ ls -la
total 319720
drwxr-xr-x  2 fixit42 fixit42      4096 Oct  1 19:08 .
drwx------ 33 fixit42 fixit42      4096 Oct  1 18:59 ..
-rw-rw-r--  1 fixit42 fixit42 325417128 Oct  1 19:08 cef_binary_6533_linux_x86_64_v6.tar.xz
-rw-rw-r--  1 fixit42 fixit42    469837 Sep 17 16:08 event-flyer-2.jpg
-rw-rw-r--  1 fixit42 fixit42   1012280 Sep 17 16:08 event-flyer-3.jpg
-rw-rw-r--  1 fixit42 fixit42     16013 Sep 17 16:04 htb_highres_527246589.avif
-rw-rw-r--  1 fixit42 fixit42    456111 Sep 17 16:14 Screenshot_2026-09-17_16_14_24.png
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads]
└─$ mkdir obs-git      
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads]
└─$ cd obs-git  
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git]
└─$ ls -la
total 8
drwxrwxr-x 2 fixit42 fixit42 4096 Oct  1 19:12 .
drwxr-xr-x 3 fixit42 fixit42 4096 Oct  1 19:12 ..
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git]
└─$ git clone --recursive https://github.com/obsproject/obs-studio.git
Cloning into 'obs-studio'...
remote: Enumerating objects: 127900, done.
remote: Counting objects: 100% (164/164), done.
remote: Compressing objects: 100% (110/110), done.
remote: Total 127900 (delta 91), reused 54 (delta 54), pack-reused 127736 (from 4)
Receiving objects: 100% (127900/127900), 80.98 MiB | 8.04 MiB/s, done.
Resolving deltas: 100% (91249/91249), done.
Submodule 'plugins/win-dshow/libdshowcapture' (https://github.com/obsproject/libdshowcapture.git) registered for path 'deps/libdshowcapture/src'
Submodule 'plugins/obs-browser' (https://github.com/obsproject/obs-browser.git) registered for path 'plugins/obs-browser'
Submodule 'plugins/obs-websocket' (https://github.com/obsproject/obs-websocket.git) registered for path 'plugins/obs-websocket'
Cloning into '/home/fixit42/Downloads/obs-git/obs-studio/deps/libdshowcapture/src'...
remote: Enumerating objects: 1050, done.        
remote: Counting objects: 100% (626/626), done.        
remote: Compressing objects: 100% (107/107), done.        
remote: Total 1050 (delta 556), reused 519 (delta 519), pack-reused 424 (from 2)        
Receiving objects: 100% (1050/1050), 324.86 KiB | 1.96 MiB/s, done.
Resolving deltas: 100% (735/735), done.
Cloning into '/home/fixit42/Downloads/obs-git/obs-studio/plugins/obs-browser'...
remote: Enumerating objects: 4160, done.        
remote: Counting objects: 100% (1905/1905), done.        
remote: Compressing objects: 100% (448/448), done.        
remote: Total 4160 (delta 1597), reused 1459 (delta 1457), pack-reused 2255 (from 3)        
Receiving objects: 100% (4160/4160), 1.16 MiB | 3.32 MiB/s, done.
Resolving deltas: 100% (2842/2842), done.
Cloning into '/home/fixit42/Downloads/obs-git/obs-studio/plugins/obs-websocket'...
remote: Enumerating objects: 13999, done.        
remote: Counting objects: 100% (1341/1341), done.        
remote: Compressing objects: 100% (316/316), done.        
remote: Total 13999 (delta 1108), reused 1026 (delta 1024), pack-reused 12658 (from 3)        
Receiving objects: 100% (13999/13999), 3.92 MiB | 2.00 MiB/s, done.
Resolving deltas: 100% (9740/9740), done.
Submodule path 'deps/libdshowcapture/src': checked out '8878638324393815512f802640b0d5ce940161f1'
Submodule 'external/capture-device-support' (https://github.com/elgatosf/capture-device-support) registered for path 'deps/libdshowcapture/src/external/capture-device-support'
Cloning into '/home/fixit42/Downloads/obs-git/obs-studio/deps/libdshowcapture/src/external/capture-device-support'...
remote: Enumerating objects: 60, done.        
remote: Counting objects: 100% (60/60), done.        
remote: Compressing objects: 100% (42/42), done.        
remote: Total 60 (delta 30), reused 41 (delta 18), pack-reused 0 (from 0)        
Receiving objects: 100% (60/60), 34.48 KiB | 6.89 MiB/s, done.
Resolving deltas: 100% (30/30), done.
Submodule path 'deps/libdshowcapture/src/external/capture-device-support': checked out 'fe9630974d47f51bf54826e72fb8b654e620aa93'
Submodule path 'plugins/obs-browser': checked out 'a1624431ae60cd89560d3d12c8143b1b926b410a'
Submodule path 'plugins/obs-websocket': checked out '1ef34bf48110c2a18184e50e41cd0b1a855e2147'
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git]
└─$ ls -la
total 12
drwxrwxr-x  3 fixit42 fixit42 4096 Oct  1 19:12 .
drwxr-xr-x  3 fixit42 fixit42 4096 Oct  1 19:12 ..
drwxrwxr-x 18 fixit42 fixit42 4096 Oct  1 19:13 obs-studio
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git]
└─$ cd obs-studio
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ ls -la
total 284
drwxrwxr-x 18 fixit42 fixit42  4096 Oct  1 19:13 .
drwxrwxr-x  3 fixit42 fixit42  4096 Oct  1 19:12 ..
drwxrwxr-x 16 fixit42 fixit42  4096 Oct  1 19:13 additional_install_files
-rw-rw-r--  1 fixit42 fixit42 55826 Oct  1 19:13 AUTHORS
drwxrwxr-x  4 fixit42 fixit42  4096 Oct  1 19:13 build-aux
-rw-rw-r--  1 fixit42 fixit42   708 Oct  1 19:13 .cirrus.yml
-rw-rw-r--  1 fixit42 fixit42  5972 Oct  1 19:13 .clang-format
drwxrwxr-x  8 fixit42 fixit42  4096 Oct  1 19:13 cmake
-rw-rw-r--  1 fixit42 fixit42   944 Oct  1 19:13 CMakeLists.txt
-rw-rw-r--  1 fixit42 fixit42  9148 Oct  1 19:13 CMakePresets.json
-rw-rw-r--  1 fixit42 fixit42  6648 Oct  1 19:13 COC.rst
-rw-rw-r--  1 fixit42 fixit42 32687 Oct  1 19:13 CODESTYLE.md
-rw-rw-r--  1 fixit42 fixit42  2092 Oct  1 19:13 COMMITMENT
-rw-rw-r--  1 fixit42 fixit42 11921 Oct  1 19:13 CONTRIBUTING.md
-rw-rw-r--  1 fixit42 fixit42 18092 Oct  1 19:13 COPYING
drwxrwxr-x  8 fixit42 fixit42  4096 Oct  1 19:13 deps
drwxrwxr-x  3 fixit42 fixit42  4096 Oct  1 19:13 docs
-rw-rw-r--  1 fixit42 fixit42  1238 Oct  1 19:13 .editorconfig
drwxrwxr-x 19 fixit42 fixit42  4096 Oct  1 19:13 frontend
-rw-rw-r--  1 fixit42 fixit42   252 Oct  1 19:13 .gersemirc
drwxrwxr-x  8 fixit42 fixit42  4096 Oct  1 19:13 .git
-rw-rw-r--  1 fixit42 fixit42   220 Oct  1 19:13 .gitattributes
-rw-rw-r--  1 fixit42 fixit42   583 Oct  1 19:13 .git-blame-ignore-revs
drwxrwxr-x  5 fixit42 fixit42  4096 Oct  1 19:13 .github
-rw-rw-r--  1 fixit42 fixit42   765 Oct  1 19:13 .gitignore
-rw-rw-r--  1 fixit42 fixit42   374 Oct  1 19:13 .gitmodules
-rw-rw-r--  1 fixit42 fixit42   105 Oct  1 19:13 INSTALL
drwxrwxr-x 10 fixit42 fixit42  4096 Oct  1 19:13 libobs
drwxrwxr-x  3 fixit42 fixit42  4096 Oct  1 19:13 libobs-d3d11
drwxrwxr-x  2 fixit42 fixit42  4096 Oct  1 19:13 libobs-metal
drwxrwxr-x  3 fixit42 fixit42  4096 Oct  1 19:13 libobs-opengl
drwxrwxr-x  2 fixit42 fixit42  4096 Oct  1 19:13 libobs-winrt
-rw-rw-r--  1 fixit42 fixit42  4460 Oct  1 19:13 .mailmap
drwxrwxr-x 43 fixit42 fixit42  4096 Oct  1 19:13 plugins
-rw-rw-r--  1 fixit42 fixit42  3139 Oct  1 19:13 README.rst
-rw-rw-r--  1 fixit42 fixit42  5117 Oct  1 19:13 SECURITY.md
drwxrwxr-x 16 fixit42 fixit42  4096 Oct  1 19:13 shared
-rw-rw-r--  1 fixit42 fixit42   853 Oct  1 19:13 .swift-format
drwxrwxr-x  6 fixit42 fixit42  4096 Oct  1 19:13 test
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ 

```

```sh
┌──(fixit42㉿x1)-[~]
└─$ nano obs-cmake-presets.json
```


```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ cmake -S /home/fixit42/Downloads/obs-build/obs-studio --preset=kali-portable                                                    
CMake Warning (dev) at cmake/common/versionconfig.cmake:66 (message):
                                                                                                                                                 
  ******************************************************************************                                                                 
                                                                                                                                                 
    + OBS-Studio - Beta detected, OBS_VERSION is now: 33.0.0-beta5                                                                               
                                                                                                                                                 
                                                                                                                                                 
  ******************************************************************************                                                                 
Call Stack (most recent call first):                                                                                                             
  cmake/common/bootstrap.cmake:60 (include)                                                                                                      
  CMakeLists.txt:3 (include)                                                                                                                     
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- The C compiler identification is GNU 16.2.0
-- The CXX compiler identification is GNU 16.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Checking for interprocedural optimization support
-- Checking for interprocedural optimization support - available
-- Checking for interprocedural optimization support - enabled [Release, MinSizeRel]
-- Found SIMDe: /usr/include (found version "0.8.4")
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libswresample.so;/usr/lib/x86_64-linux-gnu/libavcodec.so (found suitable version "8.1", minimum required is "6.1") found components: avformat avutil swscale swresample avcodec
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.3.2")
-- Found Uthash: /usr/include (found version "2.3.0")
-- Found jansson: /usr/lib/x86_64-linux-gnu/libjansson.so (found version "2.15.1")
-- Found LibUUID: /usr/lib/x86_64-linux-gnu/libuuid.so (found version "2.42.3")
-- Found X11: /usr/include
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- Found X11_XCB: /usr/lib/x86_64-linux-gnu/libX11-xcb.so (found version "1.8.13")
-- Found XCB_XCB: /usr/lib/x86_64-linux-gnu/libxcb.so (found version "1.17.0")
-- Could NOT find XCB_XINPUT (missing: XCB_XINPUT_LIBRARY XCB_XINPUT_INCLUDE_DIR) (found version "")
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so (found version "1.17.0") found components: XCB missing components: XINPUT
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found version "2.90.0")
-- Performing Test HAVE_MATH_IN_STD_LIB
-- Performing Test HAVE_MATH_IN_STD_LIB - Failed
-- Performing Test HAVE_UUID_HEADER
-- Performing Test HAVE_UUID_HEADER - Success
-- Found PulseAudio: /usr/include (found version "17.0")
-- Found Wayland_Client: /usr/lib/x86_64-linux-gnu/libwayland-client.so (found version "1.26.0")
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so (found version "1.26.0") found components: Client
-- Found Xkbcommon: /usr/lib/x86_64-linux-gnu/libxkbcommon.so (found version "1.13.1")
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so
-- Found Libdrm: /usr/lib/x86_64-linux-gnu/libdrm.so (found version "2.4.134")
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so (found version "1.17.0") found components: XCB
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so  found components: EGL
-- Found Wayland_Server: /usr/lib/x86_64-linux-gnu/libwayland-server.so (found version "1.26.0")
-- Found Wayland_Cursor: /usr/lib/x86_64-linux-gnu/libwayland-cursor.so (found version "1.26.0")
-- Found Wayland_Egl: /usr/lib/x86_64-linux-gnu/libwayland-egl.so (found version "18.1.0")
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so;/usr/lib/x86_64-linux-gnu/libwayland-server.so;/usr/lib/x86_64-linux-gnu/libwayland-cursor.so;/usr/lib/x86_64-linux-gnu/libwayland-egl.so (found version "1.26.0")
-- Performing Test HAVE_STDATOMIC
-- Performing Test HAVE_STDATOMIC - Success
-- Found WrapAtomic: TRUE
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so
-- Found WrapOpenGL: TRUE
-- Found WrapVulkanHeaders: /usr/include
-- Found SWIG: /usr/bin/swig (found suitable version "4.5.1", minimum required is "4")
-- Found Luajit: /usr/lib/x86_64-linux-gnu/libluajit-5.1.so (found version "2.1.1761786044")
CMake Warning (dev) at shared/obs-scripting/cmake/lua.cmake:8 (add_custom_command):
  The following keywords are not supported when using                                                                                            
  add_custom_command(OUTPUT): PRE_BUILD.                                                                                                         
                                                                                                                                                 
  Policy CMP0175 is not set: add_custom_command() rejects invalid arguments.                                                                     
  Run "cmake --help-policy CMP0175" for policy details.  Use the cmake_policy                                                                    
  command to set the policy and suppress this warning.                                                                                           
Call Stack (most recent call first):                                                                                                             
  shared/obs-scripting/CMakeLists.txt:15 (include)                                                                                               
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- Found Python: /usr/bin/python3 (found suitable version "3.14.7", minimum required is "3.8") found components: Interpreter Development Development.Module Development.Embed
CMake Warning (dev) at shared/obs-scripting/cmake/python.cmake:14 (add_custom_command):
  The following keywords are not supported when using                                                                                            
  add_custom_command(OUTPUT): PRE_BUILD.                                                                                                         
                                                                                                                                                 
  Policy CMP0175 is not set: add_custom_command() rejects invalid arguments.                                                                     
  Run "cmake --help-policy CMP0175" for policy details.  Use the cmake_policy                                                                    
  command to set the policy and suppress this warning.                                                                                           
Call Stack (most recent call first):                                                                                                             
  shared/obs-scripting/CMakeLists.txt:16 (include)                                                                                               
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.2.16.1")
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- Found XCB_RENDER: /usr/lib/x86_64-linux-gnu/libxcb-render.so (found version "1.17.0")
-- Found XCB_SHAPE: /usr/lib/x86_64-linux-gnu/libxcb-shape.so (found version "1.17.0")
-- Found XCB_XFIXES: /usr/lib/x86_64-linux-gnu/libxcb-xfixes.so (found version "1.17.0")
-- Found XCB_SHM: /usr/lib/x86_64-linux-gnu/libxcb-shm.so (found version "1.17.0")
-- Found XCB_COMPOSITE: /usr/lib/x86_64-linux-gnu/libxcb-composite.so (found version "1.17.0")
-- Found XCB_RANDR: /usr/lib/x86_64-linux-gnu/libxcb-randr.so (found version "1.17.0")
-- Found XCB_XINERAMA: /usr/lib/x86_64-linux-gnu/libxcb-xinerama.so (found version "1.17.0")
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so;/usr/lib/x86_64-linux-gnu/libxcb-render.so;/usr/lib/x86_64-linux-gnu/libxcb-shape.so;/usr/lib/x86_64-linux-gnu/libxcb-xfixes.so;/usr/lib/x86_64-linux-gnu/libxcb-shm.so;/usr/lib/x86_64-linux-gnu/libxcb-composite.so;/usr/lib/x86_64-linux-gnu/libxcb-randr.so;/usr/lib/x86_64-linux-gnu/libxcb-xinerama.so (found version "1.17.0") found components: XCB XFIXES RANDR SHM XINERAMA COMPOSITE
-- Found PipeWire: /usr/lib/x86_64-linux-gnu/libpipewire-0.3.so (found suitable version "1.6.8", minimum required is "0.3.33")
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found suitable version "2.90.0", minimum required is "2.76")
-- Found Libv4l2: /usr/lib/x86_64-linux-gnu/libv4l2.so (found version "1.32.0")
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libavformat.so (found version "8.1") found components: avcodec avutil avformat
-- Performing Test HAVE_VIDEODEV2_HEADER
-- Performing Test HAVE_VIDEODEV2_HEADER - Success
-- Found Libudev: /usr/lib/x86_64-linux-gnu/libudev.so (found version "261")
-- Found CEF: /home/fixit42/Downloads/obs-build/cef_binary_6533_linux_x86_64/Release/libcef.so (found suitable version "127.0.0", minimum required is "95")
-- Found nlohmann_json: /usr/share/cmake/nlohmann_json/nlohmann_jsonConfig.cmake (found suitable version "3.11.3", minimum required is "3.11")
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found suitable version "8.1", minimum required is "6.1") found components: avcodec avfilter avdevice avutil swscale avformat swresample
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avdevice avutil avformat
-- Found Libva: /usr/lib/x86_64-linux-gnu/libva.so (found version "1.24.0")
-- Found Libpci: /usr/lib/x86_64-linux-gnu/libpci.so (found version "3.15.0")
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avutil avformat
-- Found Libspeexdsp: /usr/lib/x86_64-linux-gnu/libspeexdsp.so (found version "1.2.1")
CMake Warning (dev) at cmake/finders/FindLibrnnoise.cmake:87 (message):
  Failed to find Librnnoise version.                                                                                                             
Call Stack (most recent call first):                                                                                                             
  plugins/obs-filters/cmake/rnnoise.cmake:7 (find_package)                                                                                       
  plugins/obs-filters/CMakeLists.txt:36 (include)                                                                                                
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- Could NOT find Librnnoise (missing: Librnnoise_LIBRARY Librnnoise_INCLUDE_DIR) (found version "0.0.0")
    Reason given by package: Ensure librnnoise libraries are available in local libary paths.

CMake Warning at plugins/obs-filters/cmake/rnnoise.cmake:10 (message):
  No RNNoise library found.  Using internal RNNoise version instead.                                                                             
Call Stack (most recent call first):                                                                                                             
  plugins/obs-filters/CMakeLists.txt:36 (include)                                                                                                
                                                                                                                                                 
                                                                                                                                                 
-- Found VPL: /usr/lib/x86_64-linux-gnu/libvpl.so (Required is at least version "2.9")
CMake Error at plugins/obs-webrtc/CMakeLists.txt:8 (find_package):
  By not providing "FindLibDataChannel.cmake" in CMAKE_MODULE_PATH this                                                                          
  project has asked CMake to find a package configuration file provided by                                                                       
  "LibDataChannel", but CMake did not find one.                                                                                                  
                                                                                                                                                 
  Could not find a package configuration file provided by "LibDataChannel"                                                                       
  (requested version 0.20) with any of the following names:                                                                                      
                                                                                                                                                 
    LibDataChannel.cps                                                                                                                           
    libdatachannel.cps                                                                                                                           
    LibDataChannelConfig.cmake                                                                                                                   
    libdatachannel-config.cmake                                                                                                                  
                                                                                                                                                 
  Add the installation prefix of "LibDataChannel" to CMAKE_PREFIX_PATH or set                                                                    
  "LibDataChannel_DIR" to a directory containing one of the above files.  If                                                                     
  "LibDataChannel" provides a separate development package or SDK, be sure it                                                                    
  has been installed.                                                                                                                            
                                                                                                                                                 
                                                                                                                                                 
-- Configuring incomplete, errors occurred!


```


```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ sudo apt install libxcb-xinput-dev
[sudo] password for fixit42: 
Installing:                     
  libxcb-xinput-dev
                                                                                                                                                 
Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 6
  Download size: 143 kB
  Space needed: 611 kB / 152 GB available

Get:1 http://http.kali.org/kali kali-rolling/main amd64 libxcb-xinput-dev amd64 1.17.0-2+b2 [143 kB]
Fetched 143 kB in 1s (275 kB/s)           
Selecting previously unselected package libxcb-xinput-dev:amd64.
(Reading database… 833555 files and directories currently installed.)
Preparing to unpack …/libxcb-xinput-dev_1.17.0-2+b2_amd64.deb…
Unpacking libxcb-xinput-dev:amd64 (1.17.0-2+b2)…
Setting up libxcb-xinput-dev:amd64 (1.17.0-2+b2)…
Scanning processes...                                                                                                                            
Scanning processor microcode...                                                                                                                  
Scanning linux images...                                                                                                                         

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.

```

```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ cmake -S /home/fixit42/Downloads/obs-build/obs-studio --preset=kali-portable
CMake Warning (dev) at cmake/common/versionconfig.cmake:66 (message):
                                                                                                                                                 
  ******************************************************************************                                                                 
                                                                                                                                                 
    + OBS-Studio - Beta detected, OBS_VERSION is now: 33.0.0-beta5                                                                               
                                                                                                                                                 
                                                                                                                                                 
  ******************************************************************************                                                                 
Call Stack (most recent call first):                                                                                                             
  cmake/common/bootstrap.cmake:60 (include)                                                                                                      
  CMakeLists.txt:3 (include)                                                                                                                     
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- Checking for interprocedural optimization support
-- Checking for interprocedural optimization support - enabled [Release, MinSizeRel]
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libswresample.so;/usr/lib/x86_64-linux-gnu/libavcodec.so (found suitable version "8.1", minimum required is "6.1") found components: avformat avutil swscale swresample avcodec
-- Found XCB_XINPUT: /usr/lib/x86_64-linux-gnu/libxcb-xinput.so (found version "1.17.0")
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so;/usr/lib/x86_64-linux-gnu/libxcb-xinput.so (found version "1.17.0") found components: XCB XINPUT
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found version "2.90.0")
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so (found version "1.26.0") found components: Client
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so (found version "1.17.0") found components: XCB
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so  found components: EGL
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so;/usr/lib/x86_64-linux-gnu/libwayland-server.so;/usr/lib/x86_64-linux-gnu/libwayland-cursor.so;/usr/lib/x86_64-linux-gnu/libwayland-egl.so (found version "1.26.0")
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so
CMake Warning (dev) at shared/obs-scripting/cmake/lua.cmake:8 (add_custom_command):
  The following keywords are not supported when using                                                                                            
  add_custom_command(OUTPUT): PRE_BUILD.                                                                                                         
                                                                                                                                                 
  Policy CMP0175 is not set: add_custom_command() rejects invalid arguments.                                                                     
  Run "cmake --help-policy CMP0175" for policy details.  Use the cmake_policy                                                                    
  command to set the policy and suppress this warning.                                                                                           
Call Stack (most recent call first):                                                                                                             
  shared/obs-scripting/CMakeLists.txt:15 (include)                                                                                               
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
CMake Warning (dev) at shared/obs-scripting/cmake/python.cmake:14 (add_custom_command):
  The following keywords are not supported when using                                                                                            
  add_custom_command(OUTPUT): PRE_BUILD.                                                                                                         
                                                                                                                                                 
  Policy CMP0175 is not set: add_custom_command() rejects invalid arguments.                                                                     
  Run "cmake --help-policy CMP0175" for policy details.  Use the cmake_policy                                                                    
  command to set the policy and suppress this warning.                                                                                           
Call Stack (most recent call first):                                                                                                             
  shared/obs-scripting/CMakeLists.txt:16 (include)                                                                                               
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so;/usr/lib/x86_64-linux-gnu/libxcb-render.so;/usr/lib/x86_64-linux-gnu/libxcb-shape.so;/usr/lib/x86_64-linux-gnu/libxcb-xfixes.so;/usr/lib/x86_64-linux-gnu/libxcb-shm.so;/usr/lib/x86_64-linux-gnu/libxcb-composite.so;/usr/lib/x86_64-linux-gnu/libxcb-randr.so;/usr/lib/x86_64-linux-gnu/libxcb-xinerama.so (found version "1.17.0") found components: XCB XFIXES RANDR SHM XINERAMA COMPOSITE
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found suitable version "2.90.0", minimum required is "2.76")
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libavformat.so (found version "8.1") found components: avcodec avutil avformat
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found suitable version "8.1", minimum required is "6.1") found components: avcodec avfilter avdevice avutil swscale avformat swresample
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avdevice avutil avformat
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avutil avformat
CMake Warning (dev) at cmake/finders/FindLibrnnoise.cmake:87 (message):
  Failed to find Librnnoise version.                                                                                                             
Call Stack (most recent call first):                                                                                                             
  plugins/obs-filters/cmake/rnnoise.cmake:7 (find_package)                                                                                       
  plugins/obs-filters/CMakeLists.txt:36 (include)                                                                                                
This warning is for project developers.  Use -Wno-dev to suppress it.                                                                            
                                                                                                                                                 
-- Could NOT find Librnnoise (missing: Librnnoise_LIBRARY Librnnoise_INCLUDE_DIR) (found version "0.0.0")
    Reason given by package: Ensure librnnoise libraries are available in local libary paths.

CMake Warning at plugins/obs-filters/cmake/rnnoise.cmake:10 (message):
  No RNNoise library found.  Using internal RNNoise version instead.                                                                             
Call Stack (most recent call first):                                                                                                             
  plugins/obs-filters/CMakeLists.txt:36 (include)                                                                                                
                                                                                                                                                 
                                                                                                                                                 
CMake Error at plugins/obs-webrtc/CMakeLists.txt:8 (find_package):
  By not providing "FindLibDataChannel.cmake" in CMAKE_MODULE_PATH this                                                                          
  project has asked CMake to find a package configuration file provided by                                                                       
  "LibDataChannel", but CMake did not find one.                                                                                                  
                                                                                                                                                 
  Could not find a package configuration file provided by "LibDataChannel"                                                                       
  (requested version 0.20) with any of the following names:                                                                                      
                                                                                                                                                 
    LibDataChannel.cps                                                                                                                           
    libdatachannel.cps                                                                                                                           
    LibDataChannelConfig.cmake                                                                                                                   
    libdatachannel-config.cmake                                                                                                                  
                                                                                                                                                 
  Add the installation prefix of "LibDataChannel" to CMAKE_PREFIX_PATH or set                                                                    
  "LibDataChannel_DIR" to a directory containing one of the above files.  If                                                                     
  "LibDataChannel" provides a separate development package or SDK, be sure it                                                                    
  has been installed.                                                                                                                            
                                                                                                                                                 
                                                                                                                                                 
-- Configuring incomplete, errors occurred!

```

```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ sudo apt install libdatachannel-dev
Error: Unable to locate package libdatachannel-dev
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ git clone --recursive https://github.com/paullouisageneau/libdatachannel.git /home/fixit42/Downloads/obs-build/libdatachannel
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel'...
remote: Enumerating objects: 21178, done.
remote: Counting objects: 100% (506/506), done.
remote: Compressing objects: 100% (217/217), done.
remote: Total 21178 (delta 408), reused 299 (delta 286), pack-reused 20672 (from 3)
Receiving objects: 100% (21178/21178), 54.59 MiB | 10.69 MiB/s, done.
Resolving deltas: 100% (13303/13303), done.
Submodule 'deps/json' (https://github.com/nlohmann/json.git) registered for path 'deps/json'
Submodule 'deps/libjuice' (https://github.com/paullouisageneau/libjuice.git) registered for path 'deps/libjuice'
Submodule 'deps/libsrtp' (https://github.com/cisco/libsrtp.git) registered for path 'deps/libsrtp'
Submodule 'deps/plog' (https://github.com/SergiusTheBest/plog.git) registered for path 'deps/plog'
Submodule 'deps/usrsctp' (https://github.com/paullouisageneau/usrsctp.git) registered for path 'deps/usrsctp'
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel/deps/json'...
remote: Enumerating objects: 13264, done.        
remote: Counting objects: 100% (13264/13264), done.        
remote: Compressing objects: 100% (8097/8097), done.        
remote: Total 13264 (delta 7814), reused 8853 (delta 4058), pack-reused 0 (from 0)        
Receiving objects: 100% (13264/13264), 170.99 MiB | 10.54 MiB/s, done.
Resolving deltas: 100% (7814/7814), done.
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel/deps/libjuice'...
remote: Enumerating objects: 4246, done.        
remote: Counting objects: 100% (1852/1852), done.        
remote: Compressing objects: 100% (130/130), done.        
remote: Total 4246 (delta 1755), reused 1731 (delta 1722), pack-reused 2394 (from 2)        
Receiving objects: 100% (4246/4246), 946.99 KiB | 9.47 MiB/s, done.
Resolving deltas: 100% (2919/2919), done.
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel/deps/libsrtp'...
remote: Enumerating objects: 3675, done.        
remote: Counting objects: 100% (3675/3675), done.        
remote: Compressing objects: 100% (3055/3055), done.        
remote: Total 3675 (delta 1053), reused 2950 (delta 477), pack-reused 0 (from 0)        
Receiving objects: 100% (3675/3675), 3.23 MiB | 9.07 MiB/s, done.
Resolving deltas: 100% (1053/1053), done.
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel/deps/plog'...
remote: Enumerating objects: 1051, done.        
remote: Counting objects: 100% (1051/1051), done.        
remote: Compressing objects: 100% (668/668), done.        
remote: Total 1051 (delta 527), reused 668 (delta 256), pack-reused 0 (from 0)        
Receiving objects: 100% (1051/1051), 347.14 KiB | 6.94 MiB/s, done.
Resolving deltas: 100% (527/527), done.
Cloning into '/home/fixit42/Downloads/obs-build/libdatachannel/deps/usrsctp'...
remote: Enumerating objects: 273, done.        
remote: Counting objects: 100% (273/273), done.        
remote: Compressing objects: 100% (178/178), done.        
remote: Total 273 (delta 67), reused 165 (delta 30), pack-reused 0 (from 0)        
Receiving objects: 100% (273/273), 787.69 KiB | 7.96 MiB/s, done.
Resolving deltas: 100% (67/67), done.
Submodule path 'deps/json': checked out '55f93686c01528224f448c19128836e7df245f72'
Submodule path 'deps/libjuice': checked out 'b89c792e3612faf2f12cf35bcc56857313a06be3'
Submodule path 'deps/libsrtp': checked out 'd33b8ffb1491a0b4b58a206889f09800cf7310ab'
remote: Enumerating objects: 196, done.
remote: Counting objects: 100% (170/170), done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 70 (delta 39), reused 45 (delta 22), pack-reused 0 (from 0)
Unpacking objects: 100% (70/70), 10.67 KiB | 575.00 KiB/s, done.
From https://github.com/SergiusTheBest/plog
 * branch            94899e0b926ac1b0f4750bfbd495167b4a6ae9ef -> FETCH_HEAD
Submodule path 'deps/plog': checked out '94899e0b926ac1b0f4750bfbd495167b4a6ae9ef'
Submodule path 'deps/usrsctp': checked out 'fec583d54493f879d2ae44a743423bf8a04371ab'
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ cmake -S /home/fixit42/Downloads/obs-build/libdatachannel -B /home/fixit42/Downloads/obs-build/libdatachannel/build -
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ cmake -S /home/fixit42/Downloads/obs-build/libdatachannel -B /home/fixit42/Downloads/obs-build/libdatachannel/build -DUSE_GNUTLS=0 -DUSE_NICE=0 -DCMAKE_BUILD_TYPE=Release
-- The CXX compiler identification is GNU 16.2.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- The C compiler identification is GNU 16.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for include file sys/queue.h
-- Looking for include file sys/queue.h - found
-- Looking for include files sys/socket.h, linux/if_addr.h
-- Looking for include files sys/socket.h, linux/if_addr.h - found
-- Looking for include files sys/socket.h, linux/rtnetlink.h
-- Looking for include files sys/socket.h, linux/rtnetlink.h - found
-- Looking for 4 include files sys/types.h, ..., netinet/ip_icmp.h
-- Looking for 4 include files sys/types.h, ..., netinet/ip_icmp.h - found
-- Looking for 3 include files sys/types.h, ..., net/route.h
-- Looking for 3 include files sys/types.h, ..., net/route.h - found
-- Looking for include file stdatomic.h
-- Looking for include file stdatomic.h - found
-- Looking for usrsctp.h
-- Looking for usrsctp.h - found
-- Performing Test have_sa_len
-- Performing Test have_sa_len - Failed
-- Performing Test have_sin_len
-- Performing Test have_sin_len - Failed
-- Performing Test have_sin6_len
-- Performing Test have_sin6_len - Failed
-- Performing Test have_sconn_len
-- Performing Test have_sconn_len - Failed
-- Performing Test has_wfloat_equal
-- Performing Test has_wfloat_equal - Success
-- Performing Test has_wshadow
-- Performing Test has_wshadow - Success
-- Performing Test has_wpointer_aritih
-- Performing Test has_wpointer_aritih - Success
-- Performing Test has_wunreachable_code
-- Performing Test has_wunreachable_code - Success
-- Performing Test has_winit_self
-- Performing Test has_winit_self - Success
-- Performing Test has_wno_unused_function
-- Performing Test has_wno_unused_function - Success
-- Performing Test has_wno_unused_parameter
-- Performing Test has_wno_unused_parameter - Success
-- Performing Test has_wno_unreachable_code
-- Performing Test has_wno_unreachable_code - Success
-- Performing Test has_wstrict_prototypes
-- Performing Test has_wstrict_prototypes - Success
-- Compiler flags (CMAKE_C_FLAGS):  -std=c99 -pedantic -Wall -Wextra -Wfloat-equal -Wshadow -Wpointer-arith -Wunreachable-code -Winit-self -Wno-unused-function -Wno-unused-parameter -Wno-unreachable-code -Wstrict-prototypes
-- Performing Test has_wno_address_of_packed_member
-- Performing Test has_wno_address_of_packed_member - Success
-- Performing Test has_wno_deprecated_declarations
-- Performing Test has_wno_deprecated_declarations - Success
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for byteswap.h
-- Looking for byteswap.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for machine/types.h
-- Looking for machine/types.h - not found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for sys/int_types.h
-- Looking for sys/int_types.h - not found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for windows.h
-- Looking for windows.h - not found
-- Looking for winsock2.h
-- Looking for winsock2.h - not found
-- Looking for sigaction
-- Looking for sigaction - found
-- Looking for inet_aton
-- Looking for inet_aton - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of uint8_t
-- Check size of uint8_t - done
-- Check size of uint16_t
-- Check size of uint16_t - done
-- Check size of uint32_t
-- Check size of uint32_t - done
-- Check size of uint64_t
-- Check size of uint64_t - done
-- Check size of int32_t
-- Check size of int32_t - done
-- Check size of unsigned long
-- Check size of unsigned long - done
-- Check size of unsigned long long
-- Check size of unsigned long long - done
-- Performing Test HAVE_INLINE
-- Performing Test HAVE_INLINE - Success
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found suitable version "3.6.4", minimum required is "1.1.0")
-- Warnings Active for: srtp2
-- Warnings as Errors: ON
-- Found PCAP: pcap
-- Warnings Active for: datatypes_driver
-- Warnings as Errors: ON
-- Warnings Active for: cipher_driver
-- Warnings as Errors: ON
-- Warnings Active for: kernel_driver
-- Warnings as Errors: ON
-- Warnings Active for: rdbx_driver
-- Warnings as Errors: ON
-- Warnings Active for: replay_driver
-- Warnings as Errors: ON
-- Warnings Active for: roc_driver
-- Warnings as Errors: ON
-- Warnings Active for: srtp_driver
-- Warnings as Errors: ON
-- Warnings Active for: test_srtp
-- Warnings as Errors: ON
-- Warnings Active for: rtpw
-- Warnings as Errors: ON
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "3.6.4")
-- Using the multi-header code from /home/fixit42/Downloads/obs-build/libdatachannel/deps/json/include/
-- Configuring done (5.7s)
-- Generating done (0.1s)
-- Build files have been written to: /home/fixit42/Downloads/obs-build/libdatachannel/build
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ cmake --build /home/fixit42/Downloads/obs-build/libdatachannel/build --parallel $(nproc)
[  3%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/agent.c.o
[  3%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/cipher/cipher.c.o
[  3%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/addr.c.o
[  3%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_asconf.c.o
[  3%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/cipher/cipher_test_cases.c.o
[  3%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_auth.c.o
[  5%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/srtp/srtp.c.o
[  5%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_bsd_addr.c.o
[  5%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/cipher/null_cipher.c.o
[  5%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/crc32.c.o
[  6%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/const_time.c.o
[  8%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/cipher/aes_icm_ossl.c.o
[  8%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/cipher/aes_gcm_ossl.c.o
[  8%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_callout.c.o
[  8%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/hash/auth.c.o
[ 10%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/hash/auth_test_cases.c.o
[ 10%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/conn.c.o
[ 12%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_cc_functions.c.o
[ 12%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/conn_poll.c.o
[ 12%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/hash/null_auth.c.o
[ 12%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/conn_thread.c.o
[ 12%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_crc32.c.o
[ 12%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/hash/hmac_ossl.c.o
[ 13%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/conn_mux.c.o
[ 15%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/kernel/alloc.c.o
[ 15%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_indata.c.o
[ 15%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/base64.c.o
[ 17%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_input.c.o
[ 17%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_output.c.o
[ 17%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/kernel/crypto_kernel.c.o
[ 17%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/hash.c.o
[ 17%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/kernel/err.c.o
[ 18%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/kernel/key.c.o
[ 18%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_pcb.c.o
[ 20%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_peeloff.c.o
[ 20%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/math/datatypes.c.o
[ 20%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/replay/rdb.c.o
[ 22%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/hmac.c.o
[ 22%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_sha1.c.o
[ 22%] Building C object deps/libsrtp/CMakeFiles/srtp2.dir/crypto/replay/rdbx.c.o
[ 22%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/ice.c.o
[ 24%] Linking C static library libsrtp2.a
[ 24%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_ss_functions.c.o
[ 24%] Built target srtp2
[ 24%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_sysctl.c.o
[ 24%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/juice.c.o
[ 25%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_timer.c.o
[ 25%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_userspace.c.o
[ 27%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/log.c.o
[ 27%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/random.c.o
[ 27%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/server.c.o
[ 27%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctp_usrreq.c.o
[ 29%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet/sctputil.c.o
/home/fixit42/Downloads/obs-build/libdatachannel/deps/usrsctp/usrsctplib/netinet/sctp_usrreq.c: In function ‘sctp_setopt’:
/home/fixit42/Downloads/obs-build/libdatachannel/deps/usrsctp/usrsctplib/netinet/sctp_usrreq.c:5571:29: warning: variable ‘cnt’ set but not used [-Wunused-but-set-variable=]
 5571 |                         int cnt;
      |                             ^~~
[ 29%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/netinet6/sctp6_usrreq.c.o
[ 29%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/stun.c.o
[ 29%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/user_environment.c.o
[ 31%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/timestamp.c.o
[ 32%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/user_mbuf.c.o
[ 32%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/tcp.c.o
[ 32%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/turn.c.o
[ 32%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/user_recv_thread.c.o
[ 32%] Building C object deps/usrsctp/usrsctplib/CMakeFiles/usrsctp.dir/user_socket.c.o
[ 34%] Building C object deps/libjuice/CMakeFiles/juice.dir/src/udp.c.o
[ 34%] Linking C static library libjuice.a
[ 34%] Built target juice
[ 36%] Linking C static library libusrsctp.a
[ 36%] Built target usrsctp
[ 37%] Building CXX object CMakeFiles/datachannel.dir/src/configuration.cpp.o
[ 37%] Building CXX object CMakeFiles/datachannel.dir/src/channel.cpp.o
[ 39%] Building CXX object CMakeFiles/datachannel.dir/src/candidate.cpp.o
[ 39%] Building CXX object CMakeFiles/datachannel.dir/src/datachannel.cpp.o
[ 39%] Building CXX object CMakeFiles/datachannel.dir/src/dependencydescriptor.cpp.o
[ 39%] Building CXX object CMakeFiles/datachannel.dir/src/description.cpp.o
[ 41%] Building CXX object CMakeFiles/datachannel.dir/src/iceudpmuxlistener.cpp.o
[ 41%] Building CXX object CMakeFiles/datachannel.dir/src/mediahandler.cpp.o
[ 41%] Building CXX object CMakeFiles/datachannel.dir/src/global.cpp.o
[ 41%] Building CXX object CMakeFiles/datachannel.dir/src/message.cpp.o
[ 43%] Building CXX object CMakeFiles/datachannel.dir/src/peerconnection.cpp.o
[ 43%] Building CXX object CMakeFiles/datachannel.dir/src/rtcpreceivingsession.cpp.o
[ 43%] Building CXX object CMakeFiles/datachannel.dir/src/track.cpp.o
[ 44%] Building CXX object CMakeFiles/datachannel.dir/src/websocket.cpp.o
[ 44%] Building CXX object CMakeFiles/datachannel.dir/src/websocketserver.cpp.o
[ 44%] Building CXX object CMakeFiles/datachannel.dir/src/rtppacketizationconfig.cpp.o
[ 46%] Building CXX object CMakeFiles/datachannel.dir/src/video_layers_allocation.cpp.o
[ 46%] Building CXX object CMakeFiles/datachannel.dir/src/rtcpsrreporter.cpp.o
[ 46%] Building CXX object CMakeFiles/datachannel.dir/src/rtppacketizer.cpp.o
[ 46%] Building CXX object CMakeFiles/datachannel.dir/src/rtpdepacketizer.cpp.o
[ 48%] Building CXX object CMakeFiles/datachannel.dir/src/h264rtppacketizer.cpp.o
[ 48%] Building CXX object CMakeFiles/datachannel.dir/src/h264rtpdepacketizer.cpp.o
[ 48%] Building CXX object CMakeFiles/datachannel.dir/src/nalunit.cpp.o
[ 50%] Building CXX object CMakeFiles/datachannel.dir/src/h265rtppacketizer.cpp.o
[ 50%] Building CXX object CMakeFiles/datachannel.dir/src/h265rtpdepacketizer.cpp.o
[ 50%] Building CXX object CMakeFiles/datachannel.dir/src/h265nalunit.cpp.o
[ 51%] Building CXX object CMakeFiles/datachannel.dir/src/av1rtppacketizer.cpp.o
[ 51%] Building CXX object CMakeFiles/datachannel.dir/src/av1rtpdepacketizer.cpp.o
[ 51%] Building CXX object CMakeFiles/datachannel.dir/src/vp8rtppacketizer.cpp.o
[ 51%] Building CXX object CMakeFiles/datachannel.dir/src/vp8rtpdepacketizer.cpp.o
[ 53%] Building CXX object CMakeFiles/datachannel.dir/src/vp9rtppacketizer.cpp.o
[ 53%] Building CXX object CMakeFiles/datachannel.dir/src/vp9rtpdepacketizer.cpp.o
[ 53%] Building CXX object CMakeFiles/datachannel.dir/src/rtcpnackresponder.cpp.o
[ 55%] Building CXX object CMakeFiles/datachannel.dir/src/rtp.cpp.o
[ 55%] Building CXX object CMakeFiles/datachannel.dir/src/capi.cpp.o
[ 55%] Building CXX object CMakeFiles/datachannel.dir/src/plihandler.cpp.o
[ 56%] Building CXX object CMakeFiles/datachannel.dir/src/pacinghandler.cpp.o
[ 56%] Building CXX object CMakeFiles/datachannel.dir/src/rembhandler.cpp.o
[ 56%] Building CXX object CMakeFiles/datachannel.dir/src/rtcpapphandler.cpp.o
[ 56%] Building CXX object CMakeFiles/datachannel.dir/src/impl/certificate.cpp.o
[ 58%] Building CXX object CMakeFiles/datachannel.dir/src/impl/channel.cpp.o
[ 58%] Building CXX object CMakeFiles/datachannel.dir/src/impl/datachannel.cpp.o
[ 58%] Building CXX object CMakeFiles/datachannel.dir/src/impl/dtlssrtptransport.cpp.o
[ 60%] Building CXX object CMakeFiles/datachannel.dir/src/impl/dtlstransport.cpp.o
[ 60%] Building CXX object CMakeFiles/datachannel.dir/src/impl/icetransport.cpp.o
[ 60%] Building CXX object CMakeFiles/datachannel.dir/src/impl/iceudpmuxlistener.cpp.o
[ 62%] Building CXX object CMakeFiles/datachannel.dir/src/impl/init.cpp.o
[ 62%] Building CXX object CMakeFiles/datachannel.dir/src/impl/peerconnection.cpp.o
[ 62%] Building CXX object CMakeFiles/datachannel.dir/src/impl/logcounter.cpp.o
[ 63%] Building CXX object CMakeFiles/datachannel.dir/src/impl/sctptransport.cpp.o
[ 63%] Building CXX object CMakeFiles/datachannel.dir/src/impl/threadpool.cpp.o
[ 63%] Building CXX object CMakeFiles/datachannel.dir/src/impl/tls.cpp.o
[ 63%] Building CXX object CMakeFiles/datachannel.dir/src/impl/track.cpp.o
[ 65%] Building CXX object CMakeFiles/datachannel.dir/src/impl/utils.cpp.o
[ 65%] Building CXX object CMakeFiles/datachannel.dir/src/impl/processor.cpp.o
[ 65%] Building CXX object CMakeFiles/datachannel.dir/src/impl/sha.cpp.o
[ 67%] Building CXX object CMakeFiles/datachannel.dir/src/impl/pollinterrupter.cpp.o
[ 67%] Building CXX object CMakeFiles/datachannel.dir/src/impl/pollservice.cpp.o
[ 67%] Building CXX object CMakeFiles/datachannel.dir/src/impl/http.cpp.o
[ 68%] Building CXX object CMakeFiles/datachannel.dir/src/impl/httpproxytransport.cpp.o
[ 68%] Building CXX object CMakeFiles/datachannel.dir/src/impl/tcpserver.cpp.o
[ 68%] Building CXX object CMakeFiles/datachannel.dir/src/impl/tcptransport.cpp.o
[ 68%] Building CXX object CMakeFiles/datachannel.dir/src/impl/tlstransport.cpp.o
[ 70%] Building CXX object CMakeFiles/datachannel.dir/src/impl/transport.cpp.o
[ 70%] Building CXX object CMakeFiles/datachannel.dir/src/impl/verifiedtlstransport.cpp.o
[ 70%] Building CXX object CMakeFiles/datachannel.dir/src/impl/websocket.cpp.o
[ 72%] Building CXX object CMakeFiles/datachannel.dir/src/impl/websocketserver.cpp.o
[ 72%] Building CXX object CMakeFiles/datachannel.dir/src/impl/wstransport.cpp.o
[ 72%] Building CXX object CMakeFiles/datachannel.dir/src/impl/wshandshake.cpp.o
[ 74%] Linking CXX shared library libdatachannel.so
[ 74%] Built target datachannel
[ 74%] Building CXX object CMakeFiles/datachannel-benchmark.dir/test/benchmark.cpp.o
[ 74%] Building CXX object examples/client/CMakeFiles/datachannel-client.dir/main.cpp.o
[ 77%] Building CXX object CMakeFiles/datachannel-tests.dir/test/main.cpp.o
[ 77%] Building CXX object examples/media-receiver/CMakeFiles/datachannel-media-receiver.dir/main.cpp.o
[ 77%] Building CXX object examples/client-benchmark/CMakeFiles/datachannel-client-benchmark.dir/main.cpp.o
[ 77%] Building CXX object examples/media-sender/CMakeFiles/datachannel-media-sender.dir/main.cpp.o
[ 77%] Building CXX object examples/media-sfu/CMakeFiles/datachannel-media-sfu.dir/main.cpp.o
[ 77%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/main.cpp.o
[ 77%] Building CXX object CMakeFiles/datachannel-tests.dir/test/connectivity.cpp.o
[ 77%] Linking CXX executable benchmark
[ 77%] Built target datachannel-benchmark
[ 79%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/dispatchqueue.cpp.o
[ 81%] Building CXX object examples/client/CMakeFiles/datachannel-client.dir/parse_cl.cpp.o
[ 82%] Building CXX object examples/client-benchmark/CMakeFiles/datachannel-client-benchmark.dir/parse_cl.cpp.o
[ 82%] Building CXX object CMakeFiles/datachannel-tests.dir/test/dtls.cpp.o
[ 82%] Building CXX object examples/copy-paste/CMakeFiles/datachannel-copy-paste-offerer.dir/offerer.cpp.o
[ 84%] Building CXX object CMakeFiles/datachannel-tests.dir/test/negotiated.cpp.o
[ 84%] Linking CXX executable media-receiver
[ 86%] Linking CXX executable media-sender
[ 86%] Built target datachannel-media-receiver
[ 86%] Built target datachannel-media-sender
[ 86%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/h264fileparser.cpp.o
[ 86%] Building CXX object CMakeFiles/datachannel-tests.dir/test/reliability.cpp.o
[ 86%] Linking CXX executable offerer
[ 86%] Built target datachannel-copy-paste-offerer
[ 86%] Building CXX object CMakeFiles/datachannel-tests.dir/test/simulcast_sdp_generation.cpp.o
[ 86%] Linking CXX executable media-sfu
[ 86%] Built target datachannel-media-sfu
[ 86%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/helpers.cpp.o
[ 86%] Building CXX object CMakeFiles/datachannel-tests.dir/test/simulcast_sdp_parsing.cpp.o
[ 86%] Linking CXX executable client
[ 86%] Built target datachannel-client
[ 86%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/opusfileparser.cpp.o
[ 87%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/fileparser.cpp.o
[ 87%] Building CXX object examples/copy-paste/CMakeFiles/datachannel-copy-paste-answerer.dir/answerer.cpp.o
[ 87%] Linking CXX executable client-benchmark
[ 87%] Built target datachannel-client-benchmark
[ 87%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/stream.cpp.o
[ 87%] Building C object examples/copy-paste-capi/CMakeFiles/datachannel-copy-paste-capi-offerer.dir/offerer.c.o
[ 89%] Linking C executable offerer-capi
[ 91%] Building CXX object CMakeFiles/datachannel-tests.dir/test/turn_connectivity.cpp.o
[ 91%] Building CXX object examples/streamer/CMakeFiles/streamer.dir/ArgParser.cpp.o
[ 91%] Built target datachannel-copy-paste-capi-offerer
[ 91%] Building CXX object CMakeFiles/datachannel-tests.dir/test/track.cpp.o
[ 91%] Building C object examples/copy-paste-capi/CMakeFiles/datachannel-copy-paste-capi-answerer.dir/answerer.c.o
[ 91%] Linking C executable answerer-capi
[ 91%] Building CXX object CMakeFiles/datachannel-tests.dir/test/video_layers_allocation.cpp.o
[ 91%] Built target datachannel-copy-paste-capi-answerer
[ 93%] Building CXX object CMakeFiles/datachannel-tests.dir/test/capi_connectivity.cpp.o
[ 93%] Building CXX object CMakeFiles/datachannel-tests.dir/test/capi_track.cpp.o
[ 93%] Building CXX object CMakeFiles/datachannel-tests.dir/test/websocket.cpp.o
[ 94%] Linking CXX executable streamer
[ 96%] Building CXX object CMakeFiles/datachannel-tests.dir/test/websocketserver.cpp.o
[ 96%] Building CXX object CMakeFiles/datachannel-tests.dir/test/capi_websocketserver.cpp.o
[ 96%] Built target streamer
[ 96%] Building CXX object CMakeFiles/datachannel-tests.dir/test/benchmark.cpp.o
[ 98%] Linking CXX executable answerer
[ 98%] Built target datachannel-copy-paste-answerer
[ 98%] Building CXX object CMakeFiles/datachannel-tests.dir/test/fir.cpp.o
[100%] Building CXX object CMakeFiles/datachannel-tests.dir/test/rtx.cpp.o
[100%] Building CXX object CMakeFiles/datachannel-tests.dir/test/rtcp_app.cpp.o
[100%] Linking CXX executable tests
[100%] Built target datachannel-tests
                                                                                                                                                 
┌──(fixit42㉿x1)-[~/Downloads/obs-build]
└─$ sudo cmake --install /home/fixit42/Downloads/obs-build/libdatachannel/build
-- Install configuration: "Release"
-- Installing: /usr/local/lib/libdatachannel.so.0.24.6
-- Installing: /usr/local/lib/libdatachannel.so.0.24
-- Installing: /usr/local/lib/libdatachannel.so
-- Installing: /usr/local/include/rtc/candidate.hpp
-- Installing: /usr/local/include/rtc/channel.hpp
-- Installing: /usr/local/include/rtc/configuration.hpp
-- Installing: /usr/local/include/rtc/datachannel.hpp
-- Installing: /usr/local/include/rtc/dependencydescriptor.hpp
-- Installing: /usr/local/include/rtc/description.hpp
-- Installing: /usr/local/include/rtc/iceudpmuxlistener.hpp
-- Installing: /usr/local/include/rtc/mediahandler.hpp
-- Installing: /usr/local/include/rtc/rtcpreceivingsession.hpp
-- Installing: /usr/local/include/rtc/common.hpp
-- Installing: /usr/local/include/rtc/global.hpp
-- Installing: /usr/local/include/rtc/message.hpp
-- Installing: /usr/local/include/rtc/frameinfo.hpp
-- Installing: /usr/local/include/rtc/peerconnection.hpp
-- Installing: /usr/local/include/rtc/reliability.hpp
-- Installing: /usr/local/include/rtc/rtc.h
-- Installing: /usr/local/include/rtc/rtc.hpp
-- Installing: /usr/local/include/rtc/rtp.hpp
-- Installing: /usr/local/include/rtc/track.hpp
-- Installing: /usr/local/include/rtc/websocket.hpp
-- Installing: /usr/local/include/rtc/websocketserver.hpp
-- Installing: /usr/local/include/rtc/rtppacketizationconfig.hpp
-- Installing: /usr/local/include/rtc/video_layers_allocation.hpp
-- Installing: /usr/local/include/rtc/rtcpsrreporter.hpp
-- Installing: /usr/local/include/rtc/rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/h264rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/h264rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/nalunit.hpp
-- Installing: /usr/local/include/rtc/h265rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/h265rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/h265nalunit.hpp
-- Installing: /usr/local/include/rtc/av1rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/av1rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/vp8rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/vp8rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/vp9rtppacketizer.hpp
-- Installing: /usr/local/include/rtc/vp9rtpdepacketizer.hpp
-- Installing: /usr/local/include/rtc/rtcpnackresponder.hpp
-- Installing: /usr/local/include/rtc/utils.hpp
-- Installing: /usr/local/include/rtc/plihandler.hpp
-- Installing: /usr/local/include/rtc/pacinghandler.hpp
-- Installing: /usr/local/include/rtc/rembhandler.hpp
-- Installing: /usr/local/include/rtc/rtcpapphandler.hpp
-- Installing: /usr/local/include/rtc/version.h
-- Installing: /usr/local/lib/cmake/LibDataChannel/LibDataChannelTargets.cmake
-- Installing: /usr/local/lib/cmake/LibDataChannel/LibDataChannelTargets-release.cmake
-- Installing: /usr/local/lib/cmake/LibDataChannel/LibDataChannelConfig.cmake
-- Installing: /usr/local/lib/cmake/LibDataChannel/LibDataChannelConfigVersion.cmake
```

```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build/obs-studio]
└─$ git checkout 32.2.2
M       plugins/obs-browser
Note: switching to '32.2.2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at ba2f32bdf libobs: Update version to 32.2.2

┌──(fixit42㉿x1)-[~/Downloads/obs-build/obs-studio]
└─$ git submodule update --init --recursive
Submodule path 'plugins/obs-browser': checked out '3f0a2cdf378939ebe3c6f9ab36d4ea100c25aac2'

┌──(fixit42㉿x1)-[~/Downloads/obs-build/obs-studio]
└─$ cmake -S /home/fixit42/Downloads/obs-build/obs-studio --preset=kali-portable -Wno-dev                                           
-- Checking for interprocedural optimization support
-- Checking for interprocedural optimization support - enabled [Release, MinSizeRel]
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libswresample.so;/usr/lib/x86_64-linux-gnu/libavcodec.so (found suitable version "8.1", minimum required is "6.1") found components: avformat avutil swscale swresample avcodec
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so;/usr/lib/x86_64-linux-gnu/libxcb-xinput.so (found version "1.17.0") found components: XCB XINPUT
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found version "2.90.0")
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so (found version "1.26.0") found components: Client
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so (found version "1.17.0") found components: XCB
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so  found components: EGL
-- Found Wayland: /usr/lib/x86_64-linux-gnu/libwayland-client.so;/usr/lib/x86_64-linux-gnu/libwayland-server.so;/usr/lib/x86_64-linux-gnu/libwayland-cursor.so;/usr/lib/x86_64-linux-gnu/libwayland-egl.so (found version "1.26.0")
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so
-- Found Python: /usr/bin/python3 (found suitable version "3.14.7", minimum required is "3.8") found components: Interpreter Development Development.Module Development.Embed
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- XCB: XFIXES requires XCB;RENDER;SHAPE
-- Found XCB: /usr/lib/x86_64-linux-gnu/libxcb.so;/usr/lib/x86_64-linux-gnu/libxcb-render.so;/usr/lib/x86_64-linux-gnu/libxcb-shape.so;/usr/lib/x86_64-linux-gnu/libxcb-xfixes.so;/usr/lib/x86_64-linux-gnu/libxcb-shm.so;/usr/lib/x86_64-linux-gnu/libxcb-composite.so;/usr/lib/x86_64-linux-gnu/libxcb-randr.so;/usr/lib/x86_64-linux-gnu/libxcb-xinerama.so (found version "1.17.0") found components: XCB XFIXES RANDR SHM XINERAMA COMPOSITE
-- Found Gio: /usr/lib/x86_64-linux-gnu/libgio-2.0.so (found suitable version "2.90.0", minimum required is "2.76")
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libavformat.so (found version "8.1") found components: avcodec avutil avformat
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found suitable version "8.1", minimum required is "6.1") found components: avcodec avfilter avdevice avutil swscale avformat swresample
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avdevice avutil avformat
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavfilter.so;/usr/lib/x86_64-linux-gnu/libavdevice.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libswscale.so;/usr/lib/x86_64-linux-gnu/libavformat.so;/usr/lib/x86_64-linux-gnu/libswresample.so (found version "8.1") found components: avcodec avutil avformat
-- Could NOT find Librnnoise (missing: Librnnoise_LIBRARY Librnnoise_INCLUDE_DIR) (found version "0.0.0")
    Reason given by package: Ensure librnnoise libraries are available in local libary paths.

CMake Warning at plugins/obs-filters/cmake/rnnoise.cmake:10 (message):
  No RNNoise library found.  Using internal RNNoise version instead.                                                                             
Call Stack (most recent call first):                                                                                                             
  plugins/obs-filters/CMakeLists.txt:36 (include)                                                                                                
                                                                                                                                                 
                                                                                                                                                 
-- Found FFmpeg: /usr/lib/x86_64-linux-gnu/libavcodec.so;/usr/lib/x86_64-linux-gnu/libavutil.so;/usr/lib/x86_64-linux-gnu/libavformat.so (found version "8.1") found components: avcodec avutil avformat
-- Found Python: /usr/bin/python3 (found version "3.14.7") found components: Interpreter Development Development.Module Development.Embed
                      _                   _             _ _       
                 ___ | |__  ___       ___| |_ _   _  __| (_) ___  
                / _ \| '_ \/ __|_____/ __| __| | | |/ _` | |/ _ \ 
               | (_) | |_) \__ \_____\__ \ |_| |_| | (_| | | (_) |
                \___/|_.__/|___/     |___/\__|\__,_|\__,_|_|\___/ 

OBS:  Application Version: 32.2.2 - Build Number: 5
==================================================================================


------------------------       Enabled Features           ------------------------
 - Browser panels
 - OpenGL renderer
 - PipeWire 0.3.60+ camera support
 - Plugin Support
 - PulseAudio audio monitoring (Linux)
 - RNNoise noise suppression
 - Scripting Support (Frontend)
 - Scripting support
 - SpeexDSP noise suppression
 - User Interface
 - Wayland compositor support (Linux)
 - What's New panel
------------------------       Disabled Features          ------------------------
 - Idian Playground
 - NVIDIA Hardware Encoder
 - Restream API connection
 - Twitch API connection
 - YouTube API connection
------------------------        Enabled Modules           ------------------------
 - decklink
 - decklink-captions
 - decklink-output-ui
 - frontend-tools
 - image-source
 - linux-alsa
 - linux-capture
 - linux-pipewire
 - linux-pulseaudio
 - linux-v4l2
 - obs-browser
 - obs-ffmpeg
 - obs-filters
 - obs-outputs
 - obs-qsv11
 - obs-transitions
 - obs-vst
 - obs-webrtc
 - obs-websocket
 - obs-x264
 - obslua
 - obspython
 - rtmp-services
 - text-freetype2
 - vlc-video
------------------------        Disabled Modules          ------------------------
 - aja
 - aja-output-ui
 - linux-jack
 - obs-libfdk
 - obs-nvenc
 - sndio
 - test-input
----------------------------------------------------------------------------------
-- Configuring done (2.5s)
-- Generating done (0.6s)
-- Build files have been written to: /home/fixit42/Downloads/obs-build/build

```

```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-build/obs-studio]
└─$ cmake --build /home/fixit42/Downloads/obs-build/build --parallel $(nproc)               
[  0%] Building C object libobs/CMakeFiles/libobs-version.dir/obsversion.c.o
[  1%] Building C object deps/glad/CMakeFiles/obsglad.dir/src/glad.c.o
[  1%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/caption.c.o
[  1%] Swig compile obslua.i for lua
[  1%] Building CXX object plugins/obs-browser/CMakeFiles/browser-helper.dir/browser-app.cpp.o
[  1%] Swig compile obspython.i for python
[  1%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/celt_lpc.c.o
[  1%] Building C object deps/blake2/CMakeFiles/blake2.dir/src/blake2b-ref.c.o
[  1%] Built target libobs-version
[  2%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/cea708.c.o
[  2%] Building CXX object plugins/obs-browser/CMakeFiles/browser-helper.dir/obs-browser-page/obs-browser-page-main.cpp.o
[  2%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/eia608.c.o
[  3%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/denoise.c.o
[  3%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/eia608_charmap.c.o
[  3%] Built target blake2
[  3%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/kiss_fft.c.o
[  3%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/eia608_from_utf8.c.o
[  3%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/mpeg.c.o
[  3%] Building C object deps/glad/CMakeFiles/obsglad.dir/src/glad_egl.c.o
[  3%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/scc.c.o
[  3%] Building CXX object frontend/json11/CMakeFiles/json11.dir/json11.cpp.o
[  3%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/pitch.c.o
[  4%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/srt.c.o
[  4%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/utf8.c.o
[  4%] Built target idian_autogen_timestamp_deps
[  4%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/rnn.c.o
[  4%] Building C object deps/libcaption/CMakeFiles/caption.dir/src/xds.c.o
[  4%] Linking C static library libcaption.a
[  4%] Built target obslua_swig_compilation
[  4%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/rnn_data.c.o
[  4%] Building C object plugins/obs-filters/CMakeFiles/obs-rnnoise.dir/rnnoise/src/rnn_reader.c.o
[  4%] Automatic MOC for target idian
[  4%] Built target caption
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-hevc.c.o
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-audio-controls.c.o
[  5%] Built target obs-rnnoise
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-audio.c.o
[  5%] Built target obsglad
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-av1.c.o
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-avc.c.o
[  5%] Building C object libobs/CMakeFiles/libobs.dir/obs-canvas.c.o
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-data.c.o
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-display.c.o
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-encoder.c.o
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-hotkey-name-map.c.o
[  6%] Built target idian_autogen
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-hotkey.c.o
[  6%] Building C object libobs/CMakeFiles/libobs.dir/obs-missing-files.c.o
[  6%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/idian_autogen/mocs_compilation.cpp.o
[  7%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/components/CheckBox.cpp.o
[  7%] Building C object libobs/CMakeFiles/libobs.dir/obs-module.c.o
[  7%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/components/ComboBox.cpp.o
[  8%] Building C object libobs/CMakeFiles/libobs.dir/obs-nal.c.o
[  8%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/components/DoubleSpinBox.cpp.o
[  8%] Built target json11
[  8%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/components/SpinBox.cpp.o
[  8%] Building C object libobs/CMakeFiles/libobs.dir/obs-output-delay.c.o
[  8%] Building C object libobs/CMakeFiles/libobs.dir/obs-output.c.o
[  8%] Built target obspython_swig_compilation
[  8%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/components/ToggleSwitch.cpp.o
[  8%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/include/Idian/StateEventFilter.cpp.o
[  8%] Building C object libobs/CMakeFiles/libobs.dir/obs-properties.c.o
[  9%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/include/Idian/Utils.cpp.o
[  9%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/widgets/Group.cpp.o
[  9%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/widgets/PropertiesList.cpp.o
[  9%] Building C object libobs/CMakeFiles/libobs.dir/obs-scene.c.o
[  9%] Building CXX object shared/qt/idian/CMakeFiles/idian.dir/widgets/Row.cpp.o
[  9%] Linking CXX executable obs-browser-page
Copy browser-helper to binary directory
[  9%] Built target browser-helper
[  9%] Building C object libobs/CMakeFiles/libobs.dir/obs-service.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-source-deinterlace.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-source-transition.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-source.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-video-gpu-encode.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-video.c.o
[ 10%] Building C object libobs/CMakeFiles/libobs.dir/obs-view.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/obs.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/util/array-serializer.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/util/base.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/util/bitstream.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/util/bmem.c.o
[ 11%] Building C object libobs/CMakeFiles/libobs.dir/util/buffered-file-serializer.c.o
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/cf-lexer.c.o
/home/fixit42/Downloads/obs-build/obs-studio/libobs/util/buffered-file-serializer.c: In function ‘io_thread’:
/home/fixit42/Downloads/obs-build/obs-studio/libobs/util/buffered-file-serializer.c:167:55: warning: ‘next_seek_position’ may be used uninitialized [-Wmaybe-uninitialized]
  167 |                                 current_seek_position = next_seek_position + chunk_used;
      |                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/libobs/util/buffered-file-serializer.c:83:18: note: ‘next_seek_position’ was declared here
   83 |         uint64_t next_seek_position;
      |                  ^~~~~~~~~~~~~~~~~~
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/cf-parser.c.o
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/config-file.c.o
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/crc32.c.o
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/dstr.c.o
[ 12%] Building C object libobs/CMakeFiles/libobs.dir/util/file-serializer.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/lexer.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/pipe.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/platform.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/profiler.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/source-profiler.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/task.c.o
[ 13%] Building C object libobs/CMakeFiles/libobs.dir/util/text-lookup.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/util/utf8.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/callback/calldata.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/callback/decl.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/callback/proc.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/callback/signal.c.o
[ 14%] Building C object libobs/CMakeFiles/libobs.dir/media-io/audio-io.c.o
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/audio-resampler-ffmpeg.c.o
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/format-conversion.c.o
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/media-remux.c.o
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/video-fourcc.c.o
[ 15%] Linking CXX static library libidian.a
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/video-frame.c.o
[ 15%] Building C object libobs/CMakeFiles/libobs.dir/media-io/video-io.c.o
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/media-io/video-matrices.c.o
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/media-io/video-scaler-ffmpeg.c.o
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/graphics/axisang.c.o
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/graphics/bounds.c.o
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/graphics/effect-parser.c.o
[ 16%] Built target idian
[ 16%] Building C object libobs/CMakeFiles/libobs.dir/graphics/effect.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/graphics-ffmpeg.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/graphics-imports.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/graphics.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/image-file.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/libnsgif/libnsgif.c.o
[ 17%] Building C object libobs/CMakeFiles/libobs.dir/graphics/math-extra.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/matrix3.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/matrix4.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/plane.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/quat.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/shader-parser.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/texture-render.c.o
[ 18%] Building C object libobs/CMakeFiles/libobs.dir/graphics/vec2.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/graphics/vec3.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/graphics/vec4.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/obs-nix-platform.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/obs-nix-x11.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/obs-nix.c.o
[ 19%] Building C object libobs/CMakeFiles/libobs.dir/util/pipe-posix.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/util/platform-nix.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/util/threading-posix.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/audio-monitoring/pulse/pulseaudio-enum-devices.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/audio-monitoring/pulse/pulseaudio-monitoring-available.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/audio-monitoring/pulse/pulseaudio-output.c.o
[ 20%] Building C object libobs/CMakeFiles/libobs.dir/audio-monitoring/pulse/pulseaudio-wrapper.c.o
[ 21%] Building C object libobs/CMakeFiles/libobs.dir/util/platform-nix-dbus.c.o
[ 21%] Building C object libobs/CMakeFiles/libobs.dir/util/platform-nix-portal.c.o
[ 21%] Building C object libobs/CMakeFiles/libobs.dir/obs-nix-wayland.c.o
[ 21%] Linking C shared library libobs.so
Copy libobs to library directory (lib)
Create symlink for legacy libobs
Copy libobs resources to data directory (share/obs/libobs)
[ 21%] Built target libobs
[ 21%] Building CXX object frontend/api/CMakeFiles/obs-frontend-api.dir/obs-frontend-api.cpp.o
[ 21%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-wayland-egl.c.o
[ 21%] Building C object plugins/linux-alsa/CMakeFiles/linux-alsa.dir/alsa-input.c.o
[ 21%] Building C object plugins/linux-capture/CMakeFiles/linux-capture.dir/linux-capture.c.o
[ 21%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/camera-portal.c.o
[ 21%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/linux/platform.cpp.o
[ 22%] Building C object plugins/image-source/CMakeFiles/image-source.dir/color-source.c.o
[ 23%] Building C object plugins/linux-pulseaudio/CMakeFiles/linux-pulseaudio.dir/linux-pulseaudio.c.o
[ 23%] Building C object plugins/linux-pulseaudio/CMakeFiles/linux-pulseaudio.dir/pulse-input.c.o
[ 24%] Building C object plugins/linux-capture/CMakeFiles/linux-capture.dir/xcomposite-input.c.o
[ 24%] Building C object plugins/image-source/CMakeFiles/image-source.dir/image-source.c.o
[ 24%] Building C object plugins/linux-alsa/CMakeFiles/linux-alsa.dir/linux-alsa.c.o
[ 24%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-egl-common.c.o
[ 24%] Building C object plugins/decklink/CMakeFiles/decklink.dir/audio-repack.c.o
[ 24%] Building C object plugins/linux-pulseaudio/CMakeFiles/linux-pulseaudio.dir/pulse-wrapper.c.o
[ 24%] Linking C shared module linux-alsa.so
[ 24%] Building C object plugins/image-source/CMakeFiles/image-source.dir/obs-slideshow.c.o
Copy linux-alsa to plugin directory (lib/obs-plugins)
[ 25%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-device-discovery.cpp.o
Copy linux-alsa resources to data directory (share/obs/obs-plugins/linux-alsa)
[ 25%] Built target linux-alsa
[ 25%] Building C object plugins/linux-capture/CMakeFiles/linux-capture.dir/xcursor-xcb.c.o
[ 25%] Linking C shared module linux-pulseaudio.so
Copy linux-pulseaudio to plugin directory (lib/obs-plugins)
[ 26%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-nix.c.o
Copy linux-pulseaudio resources to data directory (share/obs/obs-plugins/linux-pulseaudio)
[ 26%] Built target linux-pulseaudio
[ 26%] Building C object plugins/image-source/CMakeFiles/image-source.dir/obs-slideshow-mk2.c.o
[ 26%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-device-instance.cpp.o
[ 26%] Building C object plugins/linux-capture/CMakeFiles/linux-capture.dir/xhelpers.c.o
[ 26%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/linux-v4l2.c.o
[ 26%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-x11-egl.c.o
[ 26%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-controls.c.o
[ 26%] Building C object plugins/linux-capture/CMakeFiles/linux-capture.dir/xshm-input.c.o
[ 26%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-helpers.c.o
[ 27%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-decoder.c.o
[ 27%] Linking CXX shared library libobs-frontend-api.so
[ 27%] Linking C shared module linux-capture.so
Copy obs-frontend-api to library directory (lib)
[ 28%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/formats.c.o
Create symlink for legacy obs-frontend-api
[ 28%] Built target obs-frontend-api
[ 28%] Linking C shared module image-source.so
[ 28%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-helpers.c.o
[ 28%] Building C object shared/opts-parser/CMakeFiles/opts-parser.dir/opts-parser.c.o
Copy linux-capture to plugin directory (lib/obs-plugins)
Copy linux-capture resources to data directory (share/obs/obs-plugins/linux-capture)
Copy image-source to plugin directory (lib/obs-plugins)
Copy image-source resources to data directory (share/obs/obs-plugins/image-source)
[ 28%] Built target linux-capture
[ 28%] Built target opts-parser
[ 28%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-indexbuffer.c.o
[ 28%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/linux-pipewire.c.o
[ 28%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-device-mode.cpp.o
[ 28%] Built target image-source
[ 28%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-input.c.o
[ 28%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/pipewire.c.o
[ 28%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-shader.c.o
[ 29%] Building C object plugins/obs-ffmpeg/ffmpeg-mux/CMakeFiles/obs-ffmpeg-mux.dir/ffmpeg-mux.c.o
[ 29%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/async-delay-filter.c.o
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-ffmpeg/ffmpeg-mux/ffmpeg-mux.c: In function ‘ffmpeg_mux_io_thread’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-ffmpeg/ffmpeg-mux/ffmpeg-mux.c:771:55: warning: ‘next_seek_position’ may be used uninitialized [-Wmaybe-uninitialized]
  771 |                                 current_seek_position = next_seek_position + chunk_used;
      |                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-ffmpeg/ffmpeg-mux/ffmpeg-mux.c:687:18: note: ‘next_seek_position’ was declared here
  687 |         uint64_t next_seek_position;
      |                  ^~~~~~~~~~~~~~~~~~
[ 29%] Building C object plugins/obs-outputs/bpm/CMakeFiles/bpm.dir/bpm.c.o
[ 29%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/chroma-key-filter.c.o
[ 29%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-output.c.o
[ 29%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-device.cpp.o
[ 29%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/color-correction-filter.c.o
[ 29%] Linking C executable obs-ffmpeg-mux
[ 29%] Building C object plugins/linux-v4l2/CMakeFiles/linux-v4l2.dir/v4l2-udev.c.o
[ 29%] Built target bpm
[ 29%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-shaderparser.c.o
[ 29%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/color-grade-filter.c.o
[ 29%] Linking C shared module linux-v4l2.so
[ 29%] Building C object shared/happy-eyeballs/CMakeFiles/happy-eyeballs.dir/happy-eyeballs.c.o
[ 29%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-devices.cpp.o
Copy linux-v4l2 to plugin directory (lib/obs-plugins)
Copy linux-v4l2 resources to data directory (share/obs/obs-plugins/linux-v4l2)
[ 29%] Built target linux-v4l2
[ 29%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/portal.c.o
Copy obs-ffmpeg-mux to binary directory
[ 29%] Built target obs-ffmpeg-mux
[ 30%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-stagesurf.c.o
[ 30%] Built target happy-eyeballs
[ 31%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/color-key-filter.c.o
[ 31%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-output.cpp.o
[ 31%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-subsystem.c.o
[ 31%] Building CXX object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/common_utils_linux.cpp.o
[ 31%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/compressor-filter.c.o
[ 31%] Building C object plugins/linux-pipewire/CMakeFiles/linux-pipewire.dir/screencast-portal.c.o
[ 31%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/obs-transitions.c.o
[ 31%] Built target obs-vst_autogen_timestamp_deps
[ 31%] Building CXX object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/common_utils.cpp.o
[ 31%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-cut.c.o
[ 31%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/crop-filter.c.o
[ 31%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-texture2d.c.o
[ 31%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-fade-to-color.c.o
[ 32%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/decklink-source.cpp.o
[ 33%] Building C object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/obs-qsv11-plugin-main.c.o
[ 33%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/eq-filter.c.o
[ 33%] Building C object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/obs-qsv11.c.o
[ 33%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-fade.c.o
[ 33%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/expander-filter.c.o
[ 33%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-texture3d.c.o
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/obs-qsv11.c: In function ‘obs_qsv_create’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/obs-qsv11.c:777:17: warning: enumeration value ‘VIDEO_CS_DEFAULT’ not handled in switch [-Wswitch]
  777 |                 switch (voi->colorspace) {
      |                 ^~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/obs-qsv11.c:777:17: warning: enumeration value ‘VIDEO_CS_601’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/obs-qsv11.c:777:17: warning: enumeration value ‘VIDEO_CS_709’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/obs-qsv11.c:777:17: warning: enumeration value ‘VIDEO_CS_SRGB’ not handled in switch [-Wswitch]
[ 33%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-luma-wipe.c.o
[ 33%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/DecklinkBase.cpp.o
[ 33%] Building CXX object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/QSV_Encoder.cpp.o
[ 34%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-slide.c.o
[ 34%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-texturecube.c.o
[ 34%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/gain-filter.c.o
[ 34%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-stinger.c.o
[ 35%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/gpu-delay.c.o
[ 36%] Building CXX object plugins/obs-webrtc/CMakeFiles/obs-webrtc.dir/obs-webrtc.cpp.o
[ 36%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-vertexbuffer.c.o
[ 36%] Building CXX object plugins/obs-webrtc/CMakeFiles/obs-webrtc.dir/whip-output.cpp.o
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp: In function ‘qsv_t* qsv_encoder_open(qsv_param_t*, qsv_codec, bool)’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_NONE’ not handled in switch [-Wswitch]
   91 |                 switch (sts) {
      |                        ^
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_INCOMPATIBLE_VIDEO_PARAM’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_GPU_HANG’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_REALLOC_SURFACE’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_RESOURCE_MAPPED’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_NOT_IMPLEMENTED’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_MORE_EXTBUFFER’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_NONE_PARTIAL_OUTPUT’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_WRN_ALLOC_TIMEOUT_EXPIRED’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_TASK_DONE’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_TASK_WORKING’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_TASK_BUSY’ not handled in switch [-Wswitch]
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder.cpp:91:24: warning: enumeration value ‘MFX_ERR_MORE_DATA_SUBMIT_TASK’ not handled in switch [-Wswitch]
[ 36%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/hdr-tonemap-filter.c.o
[ 36%] Linking C shared module linux-pipewire.so
[ 36%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/DecklinkInput.cpp.o
[ 36%] Building C object plugins/obs-transitions/CMakeFiles/obs-transitions.dir/transition-swipe.c.o
Copy linux-pipewire to plugin directory (lib/obs-plugins)
Copy linux-pipewire resources to data directory (share/obs/obs-plugins/linux-pipewire)
[ 36%] Building C object libobs-opengl/CMakeFiles/libobs-opengl.dir/gl-zstencil.c.o
[ 36%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/invert-audio-polarity.c.o
[ 36%] Building CXX object plugins/obs-qsv11/CMakeFiles/obs-qsv11.dir/QSV_Encoder_Internal.cpp.o
[ 36%] Built target linux-pipewire
[ 36%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/DecklinkOutput.cpp.o
[ 36%] Linking C shared module obs-transitions.so
Copy obs-transitions to plugin directory (lib/obs-plugins)
[ 36%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/limiter-filter.c.o
Copy obs-transitions resources to data directory (share/obs/obs-plugins/obs-transitions)
[ 37%] Linking C shared library libobs-opengl.so
[ 37%] Built target obs-transitions
[ 37%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/OBSVideoFrame.cpp.o
Copy libobs-opengl to library directory (lib)
[ 37%] Built target libobs-opengl
[ 37%] Building CXX object plugins/obs-webrtc/CMakeFiles/obs-webrtc.dir/whip-service.cpp.o
[ 37%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/luma-key-filter.c.o
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp: In function ‘bool HasOptimizedBRCSupport(const mfxPlatform&, const mfxVersion&, mfxU16)’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:31: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                               ^~~~~~~~
In file included from /usr/include/vpl/mfxstructures.h:9,
                 from /home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.h:58,
                 from /home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:57:
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:31: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                               ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:31: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                               ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:43: warning: ‘MFX_PLATFORM_BATTLEMAGE’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                                           ^~~~~~~~~~~~~~~~~~~~~~~
In file included from /usr/include/vpl/mfxcommon.h:9:
/usr/include/vpl/mfxcommon.h:270:5: note: declared here
  270 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_BATTLEMAGE)     = 52, /*!< Code name Battlemage. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:79: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                                                                               ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:79: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                                                                               ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:79: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                                                                               ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:178:91: warning: ‘MFX_PLATFORM_ALDERLAKE_N’ is deprecated [-Wdeprecated-declarations]
  178 |                     (platform.CodeName >= MFX_PLATFORM_BATTLEMAGE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N)) {
      |                                                                                           ^~~~~~~~~~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:267:5: note: declared here
  267 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_ALDERLAKE_N)    = 55, /*!< Code name Alder Lake N. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp: In function ‘bool HasAV1ScreenContentSupport(const mfxPlatform&, const mfxVersion&)’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:42: warning: ‘MFX_PLATFORM_LUNARLAKE’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                                          ^~~~~~~~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:271:5: note: declared here
  271 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_LUNARLAKE)      = 53, /*!< Code name Lunar Lake. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:77: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                                                                             ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:77: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                                                                             ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:77: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                                                                             ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:194:89: warning: ‘MFX_PLATFORM_ALDERLAKE_N’ is deprecated [-Wdeprecated-declarations]
  194 |                 if (platform.CodeName >= MFX_PLATFORM_LUNARLAKE && platform.CodeName != MFX_PLATFORM_ALDERLAKE_N &&
      |                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:267:5: note: declared here
  267 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_ALDERLAKE_N)    = 55, /*!< Code name Alder Lake N. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:195:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  195 |                     platform.CodeName != MFX_PLATFORM_ARROWLAKE) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:195:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  195 |                     platform.CodeName != MFX_PLATFORM_ARROWLAKE) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:195:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  195 |                     platform.CodeName != MFX_PLATFORM_ARROWLAKE) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:195:42: warning: ‘MFX_PLATFORM_ARROWLAKE’ is deprecated [-Wdeprecated-declarations]
  195 |                     platform.CodeName != MFX_PLATFORM_ARROWLAKE) {
      |                                          ^~~~~~~~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:272:5: note: declared here
  272 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_ARROWLAKE)      = 54, /*!< Code name Arrow Lake. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp: In member function ‘mfxStatus QSV_Encoder_Internal::InitParams(qsv_param_t*, qsv_codec)’:
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:250:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  250 |                 if (platform.CodeName >= MFX_PLATFORM_DG2) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:250:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  250 |                 if (platform.CodeName >= MFX_PLATFORM_DG2) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:250:30: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  250 |                 if (platform.CodeName >= MFX_PLATFORM_DG2) {
      |                              ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:250:42: warning: ‘MFX_PLATFORM_DG2’ is deprecated [-Wdeprecated-declarations]
  250 |                 if (platform.CodeName >= MFX_PLATFORM_DG2) {
      |                                          ^~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:265:5: note: declared here
  265 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_DG2)            = 46, /*!< Code name DG2. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:312:22: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  312 |             platform.CodeName >= MFX_PLATFORM_ICELAKE) {
      |                      ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:312:22: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  312 |             platform.CodeName >= MFX_PLATFORM_ICELAKE) {
      |                      ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:312:22: warning: ‘mfxPlatform::CodeName’ is deprecated [-Wdeprecated-declarations]
  312 |             platform.CodeName >= MFX_PLATFORM_ICELAKE) {
      |                      ^~~~~~~~
/usr/include/vpl/mfxcommon.h:287:27: note: declared here
  287 |    MFX_DEPRECATED  mfxU16 CodeName;         /*!< Deprecated. */
      |                           ^~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-qsv11/QSV_Encoder_Internal.cpp:312:34: warning: ‘MFX_PLATFORM_ICELAKE’ is deprecated [-Wdeprecated-declarations]
  312 |             platform.CodeName >= MFX_PLATFORM_ICELAKE) {
      |                                  ^~~~~~~~~~~~~~~~~~~~
/usr/include/vpl/mfxcommon.h:256:5: note: declared here
  256 |     MFX_DEPRECATED_ENUM_FIELD_INSIDE(MFX_PLATFORM_ICELAKE)        = 30, /*!< Code name Ice Lake. */
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 37%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/mask-filter.c.o
[ 38%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/noise-gate-filter.c.o
[ 38%] Built target obs-websocket_autogen_timestamp_deps
[ 38%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/obs-filters.c.o
[ 38%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/scale-filter.c.o
[ 38%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/plugin-main.cpp.o
[ 38%] Linking CXX shared module obs-qsv11.so
[ 38%] Building C object plugins/obs-x264/CMakeFiles/obs-x264.dir/obs-x264.c.o
[ 38%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/scroll-filter.c.o
[ 39%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/util.cpp.o
[ 40%] Building C object plugins/obs-x264/CMakeFiles/obs-x264-test.dir/obs-x264-test.c.o
Copy obs-qsv11 to plugin directory (lib/obs-plugins)
Copy obs-qsv11 resources to data directory (share/obs/obs-plugins/obs-qsv11)
[ 40%] Built target obs-qsv11
[ 40%] Linking C executable obs-x264-test
[ 40%] Building C object plugins/obs-x264/CMakeFiles/obs-x264.dir/obs-x264-plugin-main.c.o
[ 40%] Building CXX object plugins/decklink/CMakeFiles/decklink.dir/linux/decklink-sdk/DeckLinkAPIDispatch.cpp.o
[ 40%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/sdr-on-hdr-filter.c.o
[ 40%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/sharpness-filter.c.o
[ 41%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/rtmp-common.c.o
[ 41%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/rtmp-custom.c.o
[ 41%] Built target obs-x264-test
[ 42%] Building C object plugins/obs-filters/CMakeFiles/obs-filters.dir/noise-suppress-filter.c.o
[ 42%] Building C object plugins/text-freetype2/CMakeFiles/text-freetype2.dir/find-font-unix.c.o
[ 42%] Linking C shared module obs-x264.so
[ 42%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/rtmp-services-main.c.o
Copy obs-x264 to plugin directory (lib/obs-plugins)
Copy obs-x264 resources to data directory (share/obs/obs-plugins/obs-x264)
[ 42%] Building C object plugins/vlc-video/CMakeFiles/vlc-video.dir/vlc-video-plugin.c.o
[ 42%] Built target obs-x264
[ 42%] Building C object plugins/vlc-video/CMakeFiles/vlc-video.dir/vlc-video-source.c.o
[ 43%] Building C object plugins/text-freetype2/CMakeFiles/text-freetype2.dir/obs-convenience.c.o
[ 43%] Building C object plugins/text-freetype2/CMakeFiles/text-freetype2.dir/text-freetype2.c.o
[ 43%] Linking CXX shared module decklink.so
[ 43%] Building C object plugins/text-freetype2/CMakeFiles/text-freetype2.dir/text-functionality.c.o
[ 43%] Linking C shared module obs-filters.so
[ 43%] Built target decklink-captions_autogen_timestamp_deps
[ 43%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/amazon-ivs.c.o
Copy decklink to plugin directory (lib/obs-plugins)
[ 43%] Built target decklink-output-ui_autogen_timestamp_deps
Copy obs-filters to plugin directory (lib/obs-plugins)
Copy decklink resources to data directory (share/obs/obs-plugins/decklink)
[ 43%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/dacast.c.o
Copy obs-filters resources to data directory (share/obs/obs-plugins/obs-filters)
[ 44%] obs-scripting - generating Python 3 SWIG interface headers
[ 44%] Built target decklink
[ 44%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/nimotv.c.o
[ 44%] obs-scripting - generating Luajit SWIG interface headers
[ 45%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/service-ingest.c.o
[ 45%] Built target obs-filters
[ 45%] Built target obs-browser_autogen_timestamp_deps
[ 45%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-lua-frontend.c.o
[ 45%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-lua-source.c.o
[ 45%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-mpegts.c.o
[ 45%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/showroom.c.o
[ 45%] Linking C shared module text-freetype2.so
[ 46%] Linking C shared module vlc-video.so
[ 46%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-vaapi.c.o
Copy text-freetype2 to plugin directory (lib/obs-plugins)
Copy text-freetype2 resources to data directory (share/obs/obs-plugins/text-freetype2)
Copy vlc-video to plugin directory (lib/obs-plugins)
Copy vlc-video resources to data directory (share/obs/obs-plugins/vlc-video)
[ 46%] Built target text-freetype2
[ 46%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/service-specific/twitch.c.o
[ 46%] Built target vlc-video
[ 46%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-lua.c.o
[ 46%] Building C object plugins/rtmp-services/CMakeFiles/rtmp-services.dir/__/__/shared/file-updater/file-updater/file-updater.c.o
[ 46%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/vaapi-utils.c.o
[ 46%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-audio-encoders.c.o
[ 46%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/rtmp-hevc.c.o
[ 47%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-av1.c.o
[ 47%] Linking C shared module rtmp-services.so
[ 47%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-python-frontend.c.o
Copy rtmp-services to plugin directory (lib/obs-plugins)
Copy rtmp-services resources to data directory (share/obs/obs-plugins/rtmp-services)
[ 47%] Built target rtmp-services
[ 47%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-python.c.o
[ 47%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/flv-mux.c.o
[ 47%] Automatic MOC and UIC for target obs-vst
/home/fixit42/Downloads/obs-build/obs-studio/shared/obs-scripting/obs-scripting-python.c: In function ‘obs_scripting_load_python’:
/home/fixit42/Downloads/obs-build/obs-studio/shared/obs-scripting/obs-scripting-python.c:1648:9: warning: ‘PySys_SetArgv’ is deprecated [-Wdeprecated-declarations]
 1648 |         PySys_SetArgv(argc, argv);
      |         ^~~~~~~~~~~~~
In file included from /usr/include/python3.14/Python.h:128,
                 from /home/fixit42/Downloads/obs-build/obs-studio/shared/obs-scripting/obs-scripting-python-import.h:39,
                 from /home/fixit42/Downloads/obs-build/obs-studio/shared/obs-scripting/obs-scripting-python.h:31,
                 from /home/fixit42/Downloads/obs-build/obs-studio/shared/obs-scripting/obs-scripting-python.c:19:
/usr/include/python3.14/sysmodule.h:10:38: note: declared here
   10 | Py_DEPRECATED(3.11) PyAPI_FUNC(void) PySys_SetArgv(int, wchar_t **);
      |                                      ^~~~~~~~~~~~~
[ 47%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-openh264.c.o
[ 47%] Automatic MOC and UIC for target obs-websocket
[ 47%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/flv-output.c.o
[ 47%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-hls-mux.c.o
[ 47%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-mux.c.o
[ 47%] Built target obs-vst_autogen
[ 47%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-output.c.o
[ 48%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/amf.c.o
[ 49%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting-logging.c.o
[ 49%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-source.c.o
[ 50%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg-video-encoders.c.o
[ 50%] Building C object shared/obs-scripting/CMakeFiles/obs-scripting.dir/obs-scripting.c.o
[ 50%] Built target obs-websocket_autogen
[ 50%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/cencode.c.o
[ 50%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/hashswf.c.o
[ 50%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/obs-ffmpeg.c.o
[ 50%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/log.c.o
[ 50%] Building CXX object shared/obs-scripting/CMakeFiles/obs-scripting.dir/cstrcache.cpp.o
[ 50%] Automatic MOC and UIC for target decklink-captions
[ 50%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/md5.c.o
[ 51%] Automatic MOC and UIC for target decklink-output-ui
[ 51%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/parseurl.c.o
[ 51%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/__/__/shared/media-playback/media-playback/cache.c.o
[ 51%] Automatic MOC and UIC for target obs-browser
[ 52%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/librtmp/rtmp.c.o
[ 52%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/obs-vst_autogen/mocs_compilation.cpp.o
AutoMoc: /home/fixit42/Downloads/obs-build/obs-studio/plugins/obs-browser/browser-app.hpp: note: No relevant classes found. No output generated.
[ 52%] Linking CXX shared library libobs-scripting.so
[ 52%] Built target decklink-captions_autogen
[ 52%] Automatic RCC for src/forms/resources.qrc
[ 52%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/__/__/shared/media-playback/media-playback/decode.c.o
[ 52%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/obs-websocket_autogen/mocs_compilation.cpp.o
Copy obs-scripting to library directory (lib)
[ 52%] Built target obs-browser_autogen
[ 52%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/Config.cpp.o
[ 52%] Built target obs-scripting
[ 53%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/forms/ConnectInfo.cpp.o
[ 53%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/__/__/shared/media-playback/media-playback/media-playback.c.o
[ 53%] Building C object plugins/obs-ffmpeg/CMakeFiles/obs-ffmpeg.dir/__/__/shared/media-playback/media-playback/media.c.o
[ 53%] Built target decklink-output-ui_autogen
[ 53%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/mp4-mux.c.o
[ 53%] Linking C shared module obs-ffmpeg.so
Copy obs-ffmpeg to plugin directory (lib/obs-plugins)
Copy obs-ffmpeg resources to data directory (share/obs/obs-plugins/obs-ffmpeg)
[ 53%] Built target obs-ffmpeg
[ 53%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/mp4-output.c.o
[ 53%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/linux/EditorWidget-linux.cpp.o
[ 53%] Linking CXX shared module obs-webrtc.so
Copy obs-webrtc to plugin directory (lib/obs-plugins)
Copy obs-webrtc resources to data directory (share/obs/obs-plugins/obs-webrtc)
[ 53%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/forms/SettingsDialog.cpp.o
[ 53%] Built target obs-webrtc
[ 53%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/obs-websocket.cpp.o
[ 53%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/net-if.c.o
[ 53%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/WebSocketApi.cpp.o
[ 53%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/null-output.c.o
[ 53%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/obs-outputs.c.o
[ 54%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/rtmp-av1.c.o
[ 55%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/linux/VSTPlugin-linux.cpp.o
[ 55%] Building CXX object plugins/decklink-captions/CMakeFiles/decklink-captions.dir/decklink-captions_autogen/mocs_compilation.cpp.o
[ 55%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/rtmp-stream.c.o
[ 55%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/EditorWidget.cpp.o
[ 55%] Building C object plugins/obs-outputs/CMakeFiles/obs-outputs.dir/rtmp-windows.c.o
[ 55%] Linking C shared module obs-outputs.so
Copy obs-outputs to plugin directory (lib/obs-plugins)
Copy obs-outputs resources to data directory (share/obs/obs-plugins/obs-outputs)
[ 55%] Built target obs-outputs
[ 55%] Building CXX object plugins/decklink-captions/CMakeFiles/decklink-captions.dir/decklink-captions.cpp.o
[ 55%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/websocketserver/WebSocketServer.cpp.o
[ 55%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/obs-vst.cpp.o
[ 55%] Building CXX object plugins/obs-vst/CMakeFiles/obs-vst.dir/VSTPlugin.cpp.o
[ 55%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/websocketserver/WebSocketServer_Protocol.cpp.o
[ 55%] Linking CXX shared module decklink-captions.so
Copy decklink-captions to plugin directory (lib/obs-plugins)
Copy decklink-captions resources to data directory (share/obs/obs-plugins/decklink-captions)
[ 55%] Built target decklink-captions
[ 56%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler.cpp.o
[ 57%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/decklink-output-ui_autogen/mocs_compilation.cpp.o
[ 57%] Built target frontend-tools_autogen_timestamp_deps
[ 57%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/DecklinkOutputUI.cpp.o
[ 57%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Canvases.cpp.o
[ 57%] Building C object shared/obs-scripting/obslua/CMakeFiles/obslua.dir/CMakeFiles/obslua.dir/obsluaLUA_wrap.c.o
[ 57%] Linking CXX shared module obs-vst.so
Copy obs-vst to plugin directory (lib/obs-plugins)
Copy obs-vst resources to data directory (share/obs/obs-plugins/obs-vst)
[ 57%] Built target obs-vst
[ 57%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/decklink-ui-main.cpp.o
[ 57%] Building CXX object shared/obs-scripting/obslua/CMakeFiles/obslua.dir/__/cstrcache.cpp.o
[ 57%] Building C object shared/obs-scripting/obspython/CMakeFiles/obspython.dir/CMakeFiles/obspython.dir/obspythonPYTHON_wrap.c.o
[ 57%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Config.cpp.o
[ 57%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/properties-view/double-slider.cpp.o
[ 57%] Building CXX object shared/obs-scripting/obspython/CMakeFiles/obspython.dir/__/cstrcache.cpp.o
[ 57%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/obs-browser_autogen/mocs_compilation.cpp.o
[ 57%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/properties-view/properties-view.cpp.o
[ 57%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Filters.cpp.o
[ 57%] Automatic MOC and UIC for target frontend-tools
[ 58%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/browser-app.cpp.o
[ 58%] Built target frontend-tools_autogen
[ 58%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/browser-client.cpp.o
[ 58%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/properties-view/spinbox-ignorewheel.cpp.o
[ 58%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/frontend-tools_autogen/mocs_compilation.cpp.o
[ 58%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/auto-scene-switcher-nix.cpp.o
[ 58%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/browser-scheme.cpp.o
[ 59%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/qt/wrappers/qt-wrappers.cpp.o
[ 59%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/auto-scene-switcher.cpp.o
[ 59%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/deps/base64/base64.cpp.o
[ 59%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_General.cpp.o
[ 59%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/deps/signal-restore.cpp.o
[ 59%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/qt/plain-text-edit/plain-text-edit.cpp.o
[ 59%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/deps/wide-string.cpp.o
[ 60%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/obs-browser-plugin.cpp.o
[ 60%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Inputs.cpp.o
[ 60%] Building C object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/frontend-tools.c.o
[ 60%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/qt/vertical-scroll-area/vertical-scroll-area.cpp.o                                                                                                                                           
[ 60%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/qt/slider-ignorewheel/slider-ignorewheel.cpp.o                                                                                                                                               
[ 60%] Building CXX object plugins/decklink-output-ui/CMakeFiles/decklink-output-ui.dir/__/__/shared/qt/icon-label/IconLabel.cpp.o
[ 60%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/obs-browser-source.cpp.o
[ 61%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_MediaInputs.cpp.o
[ 61%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/output-timer.cpp.o
[ 61%] Linking CXX shared module decklink-output-ui.so
Copy decklink-output-ui to plugin directory (lib/obs-plugins)
Copy decklink-output-ui resources to data directory (share/obs/obs-plugins/decklink-output-ui)
[ 61%] Built target decklink-output-ui
[ 61%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/drm-format.cpp.o
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/scripts.cpp.o
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/properties-view/double-slider.cpp.o
[ 62%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Outputs.cpp.o
[ 62%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/deps/ip-string-posix.cpp.o
[ 62%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_SceneItems.cpp.o
[ 62%] Linking CXX shared module _obspython.so
Copy obspython to plugin directory (lib/obs-scripting)
Add obspython import module
[ 62%] Built target obspython
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/properties-view/properties-view.cpp.o
[ 62%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Scenes.cpp.o
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/properties-view/spinbox-ignorewheel.cpp.o
[ 62%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/panel/browser-panel-client.cpp.o
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/qt/wrappers/qt-wrappers.cpp.o
[ 62%] Building CXX object plugins/obs-browser/CMakeFiles/obs-browser.dir/panel/browser-panel.cpp.o
[ 62%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/qt/plain-text-edit/plain-text-edit.cpp.o
[ 62%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Transitions.cpp.o
[ 63%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/qt/vertical-scroll-area/vertical-scroll-area.cpp.o
[ 63%] Linking CXX shared module obslua.so
Copy obslua to plugin directory (lib/obs-scripting)
[ 63%] Built target obslua
[ 63%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/qt/slider-ignorewheel/slider-ignorewheel.cpp.o
[ 63%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/eventhandler/EventHandler_Ui.cpp.o
[ 64%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestBatchHandler.cpp.o
[ 64%] Building CXX object plugins/frontend-tools/CMakeFiles/frontend-tools.dir/__/__/shared/qt/icon-label/IconLabel.cpp.o
[ 65%] Linking CXX shared module obs-browser.so
[ 65%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler.cpp.o
[ 65%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Canvases.cpp.o
Copy obs-browser to plugin directory (lib/obs-plugins)
Add Chromium Embedded Framework to library directory
[ 65%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Config.cpp.o
[ 65%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Filters.cpp.o
[ 65%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_General.cpp.o
[ 65%] Linking CXX shared module frontend-tools.so
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Inputs.cpp.o
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_MediaInputs.cpp.o
Copy frontend-tools to plugin directory (lib/obs-plugins)
Copy frontend-tools resources to data directory (share/obs/obs-plugins/frontend-tools)
[ 66%] Built target frontend-tools
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Outputs.cpp.o
Copy obs-browser resources to data directory (share/obs/obs-plugins/obs-browser)
[ 66%] Built target obs-browser
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Record.cpp.o
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_SceneItems.cpp.o
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Scenes.cpp.o
[ 66%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Sources.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Stream.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Transitions.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/RequestHandler_Ui.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/rpc/Request.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/rpc/RequestBatchRequest.cpp.o
[ 67%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/requesthandler/rpc/RequestResult.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Compat.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Crypto.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Json.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_ActionHelper.cpp.o
[ 68%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_ArrayHelper.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_NumberHelper.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_ObjectHelper.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_SearchHelper.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_StringHelper.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Obs_VolumeMeter.cpp.o
[ 69%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/src/utils/Platform.cpp.o
[ 70%] Building CXX object plugins/obs-websocket/CMakeFiles/obs-websocket.dir/obs-websocket_autogen/GYHPFG4CL2/qrc_resources.cpp.o
[ 70%] Linking CXX shared module obs-websocket.so
Copy obs-websocket to plugin directory (lib/obs-plugins)
Copy obs-websocket resources to data directory (share/obs/obs-plugins/obs-websocket)
[ 70%] Built target obs-websocket
[ 70%] Built target obs-studio_autogen_timestamp_deps
[ 71%] Automatic MOC and UIC for target obs-studio
[ 71%] Built target obs-studio_autogen
[ 71%] Automatic RCC for forms/obs.qrc
[ 71%] Building CXX object frontend/CMakeFiles/obs-studio.dir/obs-studio_autogen/mocs_compilation.cpp.o
[ 71%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/AccessibleAlignmentCell.cpp.o
[ 71%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/AccessibleAlignmentSelector.cpp.o
[ 72%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/AbsoluteSlider.cpp.o
[ 72%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/ApplicationAudioCaptureToolbar.cpp.o
[ 72%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/AlignmentSelector.cpp.o
[ 72%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/AudioCaptureToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/BrowserToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/ColorSourceToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/ComboSelectToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/DeviceCaptureToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/DisplayCaptureToolbar.cpp.o
[ 73%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/FlowFrame.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/FlowLayout.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/FocusList.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/GameCaptureToolbar.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/ImageSourceToolbar.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/MediaControls.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/MenuButton.cpp.o
[ 74%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/MenuCheckBox.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/Multiview.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/OBSAdvAudioCtrl.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/OBSPreviewScalingComboBox.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/OBSPreviewScalingLabel.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/OBSSourceLabel.cpp.o
[ 75%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SceneTree.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceSelectButton.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceToolbar.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceTree.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceTreeDelegate.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceTreeItem.cpp.o
[ 76%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/SourceTreeModel.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/TextSourceToolbar.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/UIValidation.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/UrlPushButton.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VisibilityItemDelegate.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VisibilityItemWidget.cpp.o
[ 77%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VolumeAccessibleInterface.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VolumeControl.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VolumeMeter.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VolumeName.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/VolumeSlider.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/components/WindowCaptureToolbar.cpp.o
[ 78%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/LogUploadDialog.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/NameDialog.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OAuthLogin.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSAbout.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicAdvAudio.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicFilters.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicInteraction.cpp.o
[ 79%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicProperties.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicSourceSelect.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicTransform.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSBasicVCamConfig.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSLogViewer.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSMissingFiles.cpp.o
[ 80%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSRemux.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSWhatsNew.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/docks/OBSDock.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importer/ImporterEntryPathItemDelegate.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importer/ImporterModel.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importer/OBSImporter.cpp.o
[ 81%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importers/classic.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importers/importers.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importers/sl.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importers/studio.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/importers/xsplit.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/plugin-manager/PluginManager.cpp.o
[ 82%] Building CXX object frontend/CMakeFiles/obs-studio.dir/plugin-manager/PluginManagerWindow.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/models/Rect.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/models/SceneCollection.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/oauth/Auth.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/oauth/AuthListener.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/oauth/OAuth.cpp.o
[ 83%] Building CXX object frontend/CMakeFiles/obs-studio.dir/dialogs/OBSExtraBrowsers.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/docks/BrowserDock.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ExtraBrowsersDelegate.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ExtraBrowsersModel.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSBasicSettings_A11y.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSBasicSettings_Appearance.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSBasicSettings_Stream.cpp.o
[ 84%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSBasicSettings.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSHotkeyEdit.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSHotkeyLabel.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/settings/OBSHotkeyWidget.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/AdvancedOutput.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/BasicOutputHandler.cpp.o
[ 85%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/CrashHandler.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/FFmpegCodec.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/FFmpegFormat.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/GoLiveAPI_CensoredJson.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/GoLiveAPI_Network.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/GoLiveAPI_PostData.cpp.o
[ 86%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/MissingFilesModel.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/MissingFilesPathItemDelegate.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/MultitrackVideoError.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/MultitrackVideoOutput.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/OBSCanvas.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/OBSProxyStyle.cpp.o
[ 87%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/OBSTranslator.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/PreviewProgramSizeObserver.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/QuickTransition.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/RemoteTextThread.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/RemuxEntryPathItemDelegate.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/RemuxQueueModel.cpp.o
[ 88%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/RemuxWorker.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/SceneRenameDelegate.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ScreenshotObj.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/SimpleOutput.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ThumbnailItem.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ThumbnailManager.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/ThumbnailView.cpp.o
[ 89%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/audio-encoders.cpp.o
[ 90%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/item-widget-helpers.cpp.o
[ 90%] Building C object frontend/CMakeFiles/obs-studio.dir/utility/obf.c.o
[ 90%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/undo_stack.cpp.o
[ 90%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/AudioMixer.cpp.o
[ 90%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/ColorSelect.cpp.o
[ 90%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Browser.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Canvases.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Clipboard.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_ContextToolbar.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Docks.cpp.o
[ 91%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Dropfiles.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Hotkeys.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Icons.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_MainControls.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_OutputHandler.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Preview.cpp.o
[ 92%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Profiles.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Projectors.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Recording.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_ReplayBuffer.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_SceneCollections.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_SceneItems.cpp.o
[ 93%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Scenes.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Screenshots.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Service.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_StatusBar.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Streaming.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_StudioMode.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_SysTray.cpp.o
[ 94%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Transitions.cpp.o
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_Updater.cpp.o
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_VirtualCam.cpp.o
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasic_YouTube.cpp.o
/home/fixit42/Downloads/obs-build/obs-studio/frontend/widgets/OBSBasic_SceneItems.cpp: In member function ‘void OBSBasic::CreateSourcePopupMenu(int, bool)’:
/home/fixit42/Downloads/obs-build/obs-studio/frontend/widgets/OBSBasic_SceneItems.cpp:689:33: warning: ‘source’ may be used uninitialized [-Wmaybe-uninitialized]
  689 |                 if (hasVideo && source) {
      |                                 ^~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/frontend/widgets/OBSBasic_SceneItems.cpp:588:23: note: ‘source’ was declared here
  588 |         obs_source_t *source;
      |                       ^~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/frontend/widgets/OBSBasic_SceneItems.cpp:753:17: warning: ‘flags’ may be used uninitialized [-Wmaybe-uninitialized]
  753 |                 if (flags && flags & OBS_SOURCE_INTERACTION) {
      |                 ^~
/home/fixit42/Downloads/obs-build/obs-studio/frontend/widgets/OBSBasic_SceneItems.cpp:589:18: note: ‘flags’ was declared here
  589 |         uint32_t flags;
      |                  ^~~~~
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasicControls.cpp.o
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasicPreview.cpp.o
[ 95%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasicStats.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSBasicStatusBar.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSProjector.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/OBSQTDisplay.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/widgets/StatusBarWidget.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/wizards/AutoConfig.cpp.o
[ 96%] Building CXX object frontend/CMakeFiles/obs-studio.dir/wizards/AutoConfigStartPage.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/wizards/AutoConfigStreamPage.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/wizards/AutoConfigTestPage.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/wizards/AutoConfigVideoPage.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/WhatsNewBrowserInitThread.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/WhatsNewInfoThread.cpp.o
[ 97%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/crypto-helpers-mbedtls.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/update-helpers.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/obs-main.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/OBSStudioAPI.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/OBSApp.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/OBSApp_Themes.cpp.o
[ 98%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/CrashHandler_Linux.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/NativeEventFilter.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/platform-x11.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/utility/system-info-posix.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/obs-studio_autogen/QM7UNKGVG2/qrc_obs.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/qt/slider-ignorewheel/slider-ignorewheel.cpp.o
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/properties-view/double-slider.cpp.o
/home/fixit42/Downloads/obs-build/obs-studio/frontend/OBSApp_Themes.cpp: In function ‘bool ParseMath(CFParser&, QStringList&, std::vector<OBSThemeVariable>&)’:
/home/fixit42/Downloads/obs-build/obs-studio/frontend/OBSApp_Themes.cpp:267:34: warning: ‘varType’ may be used uninitialized [-Wmaybe-uninitialized]
  267 |                         var.type = varType;
      |                         ~~~~~~~~~^~~~~~~~~
/home/fixit42/Downloads/obs-build/obs-studio/frontend/OBSApp_Themes.cpp:254:56: note: ‘varType’ was declared here
  254 |                         OBSThemeVariable::VariableType varType;
      |                                                        ^~~~~~~
[ 99%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/properties-view/properties-view.cpp.o
[100%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/properties-view/spinbox-ignorewheel.cpp.o
[100%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/qt/wrappers/qt-wrappers.cpp.o
[100%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/qt/plain-text-edit/plain-text-edit.cpp.o
[100%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/qt/vertical-scroll-area/vertical-scroll-area.cpp.o
[100%] Building CXX object frontend/CMakeFiles/obs-studio.dir/__/shared/qt/icon-label/IconLabel.cpp.o
[100%] Linking CXX executable obs
Copy obs-studio to binary directory
Copy obs-studio resource /home/fixit42/Downloads/obs-build/obs-studio/frontend/../AUTHORS to library directory (share/obs/obs-studio/authors)
Copy obs-studio resources to data directory (share/obs/obs-studio)
[100%] Built target obs-studio

```

```sh

┌──(fixit42㉿x1)-[~/Downloads/obs-build/obs-studio]
└─$ sudo cmake --install /home/fixit42/Downloads/obs-build/build               
[sudo] password for fixit42: 
-- Install configuration: "RelWithDebInfo"
-- Installing: /opt/obs/lib/libobs.so.30
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/libobs.so.30" to "$ORIGIN/"
-- Installing: /opt/obs/lib/libobs.so
-- Installing: /opt/obs/lib/libobs.so.0
-- Installing: /opt/obs/share/obs/libobs
-- Installing: /opt/obs/share/obs/libobs/repeat.effect
-- Installing: /opt/obs/share/obs/libobs/bilinear_lowres_scale.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_base.effect
-- Installing: /opt/obs/share/obs/libobs/color.effect
-- Installing: /opt/obs/share/obs/libobs/premultiplied_alpha.effect
-- Installing: /opt/obs/share/obs/libobs/lanczos_scale.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_discard.effect
-- Installing: /opt/obs/share/obs/libobs/bicubic_scale.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_blend.effect
-- Installing: /opt/obs/share/obs/libobs/opaque.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_linear_2x.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_linear.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_yadif.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_blend_2x.effect
-- Installing: /opt/obs/share/obs/libobs/format_conversion.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_discard_2x.effect
-- Installing: /opt/obs/share/obs/libobs/solid.effect
-- Installing: /opt/obs/share/obs/libobs/default.effect
-- Installing: /opt/obs/share/obs/libobs/default_rect.effect
-- Installing: /opt/obs/share/obs/libobs/area.effect
-- Installing: /opt/obs/share/obs/libobs/deinterlace_yadif_2x.effect
-- Up-to-date: /opt/obs/lib/libobs.so.30
-- Up-to-date: /opt/obs/lib/libobs.so
-- Installing: /opt/obs/include/obs/callback/calldata.h
-- Installing: /opt/obs/include/obs/callback/decl.h
-- Installing: /opt/obs/include/obs/callback/proc.h
-- Installing: /opt/obs/include/obs/callback/signal.h
-- Installing: /opt/obs/include/obs/graphics/axisang.h
-- Installing: /opt/obs/include/obs/graphics/bounds.h
-- Installing: /opt/obs/include/obs/graphics/effect-parser.h
-- Installing: /opt/obs/include/obs/graphics/effect.h
-- Installing: /opt/obs/include/obs/graphics/graphics.h
-- Installing: /opt/obs/include/obs/graphics/image-file.h
-- Installing: /opt/obs/include/obs/graphics/input.h
-- Installing: /opt/obs/include/obs/graphics/math-defs.h
-- Installing: /opt/obs/include/obs/graphics/math-extra.h
-- Installing: /opt/obs/include/obs/graphics/matrix3.h
-- Installing: /opt/obs/include/obs/graphics/matrix4.h
-- Installing: /opt/obs/include/obs/graphics/plane.h
-- Installing: /opt/obs/include/obs/graphics/quat.h
-- Installing: /opt/obs/include/obs/graphics/shader-parser.h
-- Installing: /opt/obs/include/obs/graphics/srgb.h
-- Installing: /opt/obs/include/obs/graphics/vec2.h
-- Installing: /opt/obs/include/obs/graphics/vec3.h
-- Installing: /opt/obs/include/obs/graphics/vec4.h
-- Installing: /opt/obs/include/obs/graphics/libnsgif/libnsgif.h
-- Installing: /opt/obs/include/obs/media-io/audio-io.h
-- Installing: /opt/obs/include/obs/media-io/audio-math.h
-- Installing: /opt/obs/include/obs/media-io/audio-resampler.h
-- Installing: /opt/obs/include/obs/media-io/format-conversion.h
-- Installing: /opt/obs/include/obs/media-io/frame-rate.h
-- Installing: /opt/obs/include/obs/media-io/media-io-defs.h
-- Installing: /opt/obs/include/obs/media-io/media-remux.h
-- Installing: /opt/obs/include/obs/media-io/video-frame.h
-- Installing: /opt/obs/include/obs/media-io/video-io.h
-- Installing: /opt/obs/include/obs/media-io/video-scaler.h
-- Installing: /opt/obs/include/obs/util/array-serializer.h
-- Installing: /opt/obs/include/obs/util/base.h
-- Installing: /opt/obs/include/obs/util/bitstream.h
-- Installing: /opt/obs/include/obs/util/bmem.h
-- Installing: /opt/obs/include/obs/util/c99defs.h
-- Installing: /opt/obs/include/obs/util/cf-lexer.h
-- Installing: /opt/obs/include/obs/util/cf-parser.h
-- Installing: /opt/obs/include/obs/util/config-file.h
-- Installing: /opt/obs/include/obs/util/crc32.h
-- Installing: /opt/obs/include/obs/util/darray.h
-- Installing: /opt/obs/include/obs/util/deque.h
-- Installing: /opt/obs/include/obs/util/dstr.h
-- Installing: /opt/obs/include/obs/util/dstr.hpp
-- Installing: /opt/obs/include/obs/util/file-serializer.h
-- Installing: /opt/obs/include/obs/util/lexer.h
-- Installing: /opt/obs/include/obs/util/pipe.h
-- Installing: /opt/obs/include/obs/util/platform.h
-- Installing: /opt/obs/include/obs/util/profiler.h
-- Installing: /opt/obs/include/obs/util/profiler.hpp
-- Installing: /opt/obs/include/obs/util/serializer.h
-- Installing: /opt/obs/include/obs/util/sse-intrin.h
-- Installing: /opt/obs/include/obs/util/task.h
-- Installing: /opt/obs/include/obs/util/text-lookup.h
-- Installing: /opt/obs/include/obs/util/threading-posix.h
-- Installing: /opt/obs/include/obs/util/threading.h
-- Installing: /opt/obs/include/obs/util/uthash.h
-- Installing: /opt/obs/include/obs/util/util.hpp
-- Installing: /opt/obs/include/obs/util/util_uint128.h
-- Installing: /opt/obs/include/obs/util/util_uint64.h
-- Installing: /opt/obs/include/obs/obs-audio-controls.h
-- Installing: /opt/obs/include/obs/obs-avc.h
-- Installing: /opt/obs/include/obs/obs-config.h
-- Installing: /opt/obs/include/obs/obs-data.h
-- Installing: /opt/obs/include/obs/obs-defs.h
-- Installing: /opt/obs/include/obs/obs-encoder.h
-- Installing: /opt/obs/include/obs/obs-hotkey.h
-- Installing: /opt/obs/include/obs/obs-hotkeys.h
-- Installing: /opt/obs/include/obs/obs-interaction.h
-- Installing: /opt/obs/include/obs/obs-missing-files.h
-- Installing: /opt/obs/include/obs/obs-module.h
-- Installing: /opt/obs/include/obs/obs-nal.h
-- Installing: /opt/obs/include/obs/obs-nix-platform.h
-- Installing: /opt/obs/include/obs/obs-output.h
-- Installing: /opt/obs/include/obs/obs-properties.h
-- Installing: /opt/obs/include/obs/obs-service.h
-- Installing: /opt/obs/include/obs/obs-source.h
-- Installing: /opt/obs/include/obs/obs.h
-- Installing: /opt/obs/include/obs/obs.hpp
-- Installing: /opt/obs/include/obs/obs-hevc.h
-- Installing: /opt/obs/include/obs/obsconfig.h
-- Installing: /opt/obs/lib/cmake/libobs/libobsTargets.cmake
-- Installing: /opt/obs/lib/cmake/libobs/libobsTargets-relwithdebinfo.cmake
-- Installing: /opt/obs/lib/cmake/libobs/libobsConfig.cmake
-- Installing: /opt/obs/lib/cmake/libobs/libobsConfigVersion.cmake
-- Installing: /opt/obs/lib/cmake/libobs/finders/FindSIMDe.cmake
-- Installing: /opt/obs/lib/pkgconfig/libobs.pc
-- Installing: /opt/obs/lib/libobs-opengl.so.30
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/libobs-opengl.so.30" to "$ORIGIN/"
-- Installing: /opt/obs/lib/libobs-opengl.so
-- Installing: /opt/obs/lib/obs-plugins/decklink.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/decklink.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/decklink
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/an-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/decklink/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/decklink-captions.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/decklink-captions.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/decklink-captions
-- Installing: /opt/obs/share/obs/obs-plugins/decklink-captions/.keepme
-- Installing: /opt/obs/lib/obs-plugins/decklink-output-ui.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/decklink-output-ui.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/decklink-output-ui
-- Installing: /opt/obs/share/obs/obs-plugins/decklink-output-ui/.keepme
-- Installing: /opt/obs/lib/obs-scripting/obslua.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-scripting/obslua.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/lib/obs-scripting/_obspython.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-scripting/_obspython.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/lib/obs-scripting/obspython.py
-- Installing: /opt/obs/lib/libobs-scripting.so.30
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/libobs-scripting.so.30" to "$ORIGIN/"
-- Installing: /opt/obs/lib/libobs-scripting.so
-- Installing: /opt/obs/lib/obs-plugins/frontend-tools.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/frontend-tools.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/countdown.lua
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/instant-replay.lua
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/pause-scene.lua
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source.lua
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source/dial.png
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source/second.png
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source/hour.png
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/clock-source/minute.png
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/scripts/url-text.py
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/frontend-tools/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/image-source.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/image-source.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/image-source
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/pa-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/image-source/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/linux-alsa.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/linux-alsa.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/lv-LV.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/an-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-alsa/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/linux-capture.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/linux-capture.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/lv-LV.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/te-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-capture/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/linux-pipewire.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/linux-pipewire.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/.gitkeep
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pipewire/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/linux-pulseaudio.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/linux-pulseaudio.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-pulseaudio/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/linux-v4l2.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/linux-v4l2.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/linux-v4l2/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-browser-page
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-browser-page" to "$ORIGIN/"
-- Installing: /opt/obs/lib/obs-plugins/obs-browser.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-browser.so" to "$ORIGIN/"
-- Installing: /opt/obs/lib/obs-plugins/libcef.so
-- Installing: /opt/obs/lib/obs-plugins/chrome-sandbox
-- Installing: /opt/obs/lib/obs-plugins/libEGL.so
-- Installing: /opt/obs/lib/obs-plugins/libGLESv2.so
-- Installing: /opt/obs/lib/obs-plugins/libvk_swiftshader.so
-- Installing: /opt/obs/lib/obs-plugins/libvulkan.so.1
-- Installing: /opt/obs/lib/obs-plugins/v8_context_snapshot.bin
-- Installing: /opt/obs/lib/obs-plugins/vk_swiftshader_icd.json
-- Installing: /opt/obs/lib/obs-plugins/chrome_100_percent.pak
-- Installing: /opt/obs/lib/obs-plugins/chrome_200_percent.pak
-- Installing: /opt/obs/lib/obs-plugins/icudtl.dat
-- Installing: /opt/obs/lib/obs-plugins/resources.pak
-- Installing: /opt/obs/lib/obs-plugins/locales
-- Installing: /opt/obs/lib/obs-plugins/locales/ja.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/zh-CN.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/th.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/fi.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/vi.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/pl.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/am.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/te.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/lt.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ca.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/et.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/nl.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/kn.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/uk.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/hi.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/af.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ro.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/mr.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/fil.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/tr.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/en-US.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/da.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/en-GB.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/sw.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/lv.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/sr.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/de.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/bn.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/gu.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ml.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/sl.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/hr.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/zh-TW.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/hu.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/cs.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ru.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ko.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/pt-PT.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ur.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/bg.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/fr.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/it.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/sv.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/he.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ms.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/fa.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/el.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ta.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/nb.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/es.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/ar.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/es-419.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/id.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/pt-BR.pak
-- Installing: /opt/obs/lib/obs-plugins/locales/sk.pak
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/error.html
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-browser/locale/sk-SK.ini
-- Installing: /opt/obs/bin/obs-ffmpeg-mux
-- Set non-toolchain portion of runtime path of "/opt/obs/bin/obs-ffmpeg-mux" to "$ORIGIN/:$ORIGIN/../lib"
-- Installing: /opt/obs/lib/obs-plugins/obs-ffmpeg.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-ffmpeg.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-ffmpeg/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-filters.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-filters.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/original.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/red_isolated.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/posterize.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/invert.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/original.cube
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/teal_lows_orange_highs.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/grayscale.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/black_and_white.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/LUTs/grayscale.cube
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/crop_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/mask_color_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/color_grade_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/color.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/sharpness.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/blend_sub_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/hdr_tonemap_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/luma_key_filter_v2.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/blend_add_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/luma_key_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/chroma_key_filter_v2.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/color_correction_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/chroma_key_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/mask_alpha_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/sdr_on_hdr_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/blend_mul_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/color_key_filter_v2.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/color_key_filter.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-filters/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-outputs.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-outputs.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-outputs/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-qsv11.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-qsv11.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-qsv11/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-transitions.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-transitions.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/swipe_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/slide_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/fade_to_color_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipe_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/fade_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/stinger_matte_transition.effect
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/barndoor-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/watercolor.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/iris.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/burst.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/barndoor-botleft.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/strips-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/barndoor-topleft.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/strips-v.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/fractal.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/parallel-zigzag-v.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/box-topright.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/circles.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/fan.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/box-topleft.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/wipes.json
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/spiral.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/cloud.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/curtain.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/box-botright.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/sinus9.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/clock.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/stripes.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/zigzag-v.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/zigzag-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/parallel-zigzag-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/blinds-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/squares.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/barndoor-v.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/linear-topleft.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/box-botleft.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/linear-topright.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/linear-v.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/square.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/checkerboard-small.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/luma_wipes/linear-h.png
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-transitions/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-vst.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-vst.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/an-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-vst/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-webrtc.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-webrtc.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-webrtc/locale/sk-SK.ini
-- Installing: /opt/obs/include/obs/obs-websocket-api.h
-- Installing: /opt/obs/lib/cmake/obs-websocket-api/obs-websocket-apiTargets.cmake
-- Installing: /opt/obs/lib/cmake/obs-websocket-api/obs-websocket-apiConfig.cmake
-- Installing: /opt/obs/lib/cmake/obs-websocket-api/obs-websocket-apiConfigVersion.cmake
-- Installing: /opt/obs/lib/obs-plugins/obs-websocket.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-websocket.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-websocket/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/obs-x264.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/obs-x264.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/lv-LV.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/obs-x264/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/rtmp-services.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/rtmp-services.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/services.json
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/schema
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/schema/service-schema-v5.json
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/schema/package-schema.json
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/package.json
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/rtmp-services/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/text-freetype2.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/text-freetype2.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/text_default.effect
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/lv-LV.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/text-freetype2/locale/sk-SK.ini
-- Installing: /opt/obs/lib/obs-plugins/vlc-video.so
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/obs-plugins/vlc-video.so" to "$ORIGIN/:$ORIGIN/.."
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-plugins/vlc-video/locale/sk-SK.ini
-- Installing: /opt/obs/lib/libobs-frontend-api.so.30
-- Set non-toolchain portion of runtime path of "/opt/obs/lib/libobs-frontend-api.so.30" to "$ORIGIN/"
-- Installing: /opt/obs/lib/libobs-frontend-api.so
-- Installing: /opt/obs/lib/libobs-frontend-api.so.0
-- Up-to-date: /opt/obs/lib/libobs-frontend-api.so.30
-- Up-to-date: /opt/obs/lib/libobs-frontend-api.so
-- Installing: /opt/obs/include/obs/obs-frontend-api.h
-- Installing: /opt/obs/lib/cmake/obs-frontend-api/obs-frontend-apiTargets.cmake
-- Installing: /opt/obs/lib/cmake/obs-frontend-api/obs-frontend-apiTargets-relwithdebinfo.cmake
-- Installing: /opt/obs/lib/cmake/obs-frontend-api/obs-frontend-apiConfig.cmake
-- Installing: /opt/obs/lib/cmake/obs-frontend-api/obs-frontend-apiConfigVersion.cmake
-- Installing: /opt/obs/lib/pkgconfig/obs-frontend-api.pc
-- Installing: /opt/obs/share/metainfo/com.obsproject.Studio.metainfo.xml
-- Installing: /opt/obs/share/applications/com.obsproject.Studio.desktop
-- Installing: /opt/obs/share/icons/hicolor/128x128/apps/com.obsproject.Studio.png
-- Installing: /opt/obs/share/icons/hicolor/256x256/apps/com.obsproject.Studio.png
-- Installing: /opt/obs/share/icons/hicolor/512x512/apps/com.obsproject.Studio.png
-- Installing: /opt/obs/share/icons/hicolor/scalable/apps/com.obsproject.Studio.svg
-- Installing: /opt/obs/bin/obs
-- Set non-toolchain portion of runtime path of "/opt/obs/bin/obs" to "$ORIGIN/:$ORIGIN/../lib"
-- Installing: /opt/obs/share/obs/obs-studio/authors/AUTHORS
-- Up-to-date: /opt/obs/share/obs/obs-studio
-- Installing: /opt/obs/share/obs/obs-studio/striped_line.effect
-- Installing: /opt/obs/share/obs/obs-studio/themes
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Classic.ovt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Light.ovt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Rachni.ovt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Grey.ovt
-- Installing: /opt/obs/share/obs/obs-studio/themes/System.obt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_checked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/down_arrow.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_checked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/sizegrip.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/down_arrow_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/left_arrow_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/up_arrow_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/right_arrow_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_checked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/right_arrow.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_unchecked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/left_arrow.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_unchecked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_checked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_unchecked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_checked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_checked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/radio_unchecked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_unchecked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/checkbox_unchecked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Rachni/up_arrow.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/no_sources.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/collapse.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/streaming-inactive.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/mute.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/updown.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/recording-inactive.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/up.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/audio.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/appearance.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/general.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/accessibility.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/stream.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/advanced.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/hotkeys.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/video.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/settings/output.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/interact.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/window.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/scene.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/brush.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/image.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/slideshow.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/text.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/windowaudio.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/camera.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/default.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/globe.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/microphone.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/group.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/gamepad.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/sources/media.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/network-inactive.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/network-disconnected.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/layout-horizontal.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/dots-vert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/unassigned.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/down.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/filter.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/refresh.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/entry-clear.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/dots.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/cogs.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/trash.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/left.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/close.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/save.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/headphones-off.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/recording-pause-inactive.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_stop.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_play.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_previous.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_restart.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_next.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media/media_pause.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/locked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/alert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/layout-vertical.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/visible.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/revert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/popout.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/media-pause.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/minus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/headphones.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/expand.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/plus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Dark/right.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/no_sources.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/collapse.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/mute.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/updown.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/up.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/audio.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/appearance.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/general.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/accessibility.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/stream.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/advanced.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/hotkeys.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/video.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/settings/output.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/interact.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/window.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/scene.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/brush.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/image.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/slideshow.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/text.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/windowaudio.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/camera.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/default.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/globe.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/microphone.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/group.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/gamepad.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/sources/media.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/layout-horizontal.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_checked_focus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/dots-vert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/down.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/filter.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_unchecked_focus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/refresh.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/entry-clear.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/dots.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/cogs.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/trash.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_unchecked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_unchecked_disabled.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/left.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/close.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/save.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/headphones-off.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_stop.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_play.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_previous.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_restart.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_next.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media/media_pause.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/locked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/alert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/layout-vertical.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/visible.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/revert.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/popout.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_checked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/media-pause.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/minus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/headphones.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/checkbox_checked_disabled.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/expand.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/plus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Light/right.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_checked_focus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_unchecked_focus.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_unchecked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_unchecked_disabled.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_checked.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami/checkbox_checked_disabled.svg
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Default.ovt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami.obt
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_checked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_checked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/sizegrip.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_checked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/bot_hook2.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_unchecked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_unchecked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_checked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_unchecked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_checked_disabled.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_checked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/radio_unchecked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_unchecked_focus.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/top_hook.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/bot_hook.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Acri/checkbox_unchecked.png
-- Installing: /opt/obs/share/obs/obs-studio/themes/Yami_Acri.ovt
-- Installing: /opt/obs/share/obs/obs-studio/license
-- Installing: /opt/obs/share/obs/obs-studio/license/gplv2.txt
-- Installing: /opt/obs/share/obs/obs-studio/images
-- Installing: /opt/obs/share/obs/obs-studio/images/overflow.png
-- Installing: /opt/obs/share/obs/obs-studio/OBSPublicRSAKey.pem
-- Installing: /opt/obs/share/obs/obs-studio/locale
-- Installing: /opt/obs/share/obs/obs-studio/locale/gd-GB.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/oc-FR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/zh-CN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/lv-LV.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ka-GE.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sr-CS.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/is-IS.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/kmr-TR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/zh-TW.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sl-SI.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/uz-UZ.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/en-US.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/fr-FR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/fi-FI.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/en-GB.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/af-ZA.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/nl-NL.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/val-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/pl-PL.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ro-RO.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ru-RU.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ja-JP.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/hr-HR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/si-LK.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/mn-MN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/bg-BG.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ar-SA.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/hi-IN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/eo-UY.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/it-IT.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/az-AZ.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/szl-PL.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/kab-KAB.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/cs-CZ.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ug-CN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/be-BY.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/lo-LA.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/fil-PH.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ur-PK.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ca-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/nb-NO.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sv-SE.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/pt-PT.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/hy-AM.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/de-DE.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sq-AL.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/th-TH.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/he-IL.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sr-SP.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/hu-HU.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/te-IN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/bn-BD.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/tr-TR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/da-DK.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/vi-VN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ko-KR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/uk-UA.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/es-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/el-GR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/tt-RU.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/et-EE.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/pa-IN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/an-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ms-MY.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/kaa.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/pt-BR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/fa-IR.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/eu-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/tl-PH.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/lt-LT.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/id-ID.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ba-RU.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/nn-NO.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/ta-IN.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/bem-ZM.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/gl-ES.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale/sk-SK.ini
-- Installing: /opt/obs/share/obs/obs-studio/locale.ini

```

```sh

```


