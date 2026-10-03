
┌──(fixit42㉿x1)-[/opt/obs/bin]
└─$ ./obs -p
error: Crash sentinel location '../config/obs-studio/.sentinel' does not exist and unable to create directory:
filesystem error: cannot create directory: No such file or directory [../config/obs-studio/.sentinel].
debug: Found portal inhibitor
qt.qpa.services: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")
error: Failed to create required user directories
error: Crash sentinel location '../config/obs-studio/.sentinel' does not exist
info: == Profiler Results =============================
info: run_program_init: 14988.1 ms
info:  ┗OBSApp::AppInit: 8676.99 ms
info: =================================================
info: == Profiler Time Between Calls ==================
info: =================================================
info: Number of memory leaks: 5
                                                                                                                                                 
┌──(fixit42㉿x1)-[/opt/obs/bin]
└─$ sudo ./obs -p
[sudo] password for fixit42: 
error: Crash sentinel location '../config/obs-studio/.sentinel' does not exist and unable to create directory:
filesystem error: cannot create directory: No such file or directory [../config/obs-studio/.sentinel].
debug: Found portal inhibitor
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/locale/en-US.ini
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/locale.ini
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/themes
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/themes/
error: Failed to rename basic scene collection file:
filesystem error: cannot rename: No such file or directory [../config/obs-studio/basic/scenes.json] [../config/obs-studio/basic/scenes/Untitled.json]
info: Command Line Arguments: -p
info: Using EGL/X11
info: CPU Name: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
info: CPU Speed: 2999.950MHz
info: Physical Cores: 4, Logical Cores: 8
info: Physical Memory: 7704MB Total, 997MB Free
info: Kernel Version: Linux 7.1.5+kali-amd64
info: Distribution: "Kali GNU/Linux" "2026.3"
info: Desktop Environment: XFCE
info: Window System: X11.0, Vendor: The X.Org Foundation, Version: 1.21.1
info: Current Date/Time: 2026-10-03, 02:11:51 AM
info: Browser Hardware Acceleration: true
info: Qt Version: 6.10.2 (runtime), 6.10.2 (compiled)
info: Portable mode: true
info: OBS 32.2.2 (linux)
info: ---------------------------------
info: ---------------------------------
info: audio settings reset:
        samples per sec: 48000
        speakers:        2
        max buffering:   960 milliseconds
        buffering type:  dynamically increasing
info: ---------------------------------
info: Initializing OpenGL...
info: Loading up OpenGL on adapter Intel Mesa Intel(R) UHD Graphics 620 (KBL GT2)
info: OpenGL loaded successfully, version 4.6 (Core Profile) Mesa 26.1.6-1, shading language 4.60
info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: Audio monitoring device:
        name: Default
        id: default
info: ---------------------------------
warning: Failed to load 'en-US' text for module: 'decklink-captions.so'
warning: Failed to load 'en-US' text for module: 'decklink-output-ui.so'
libDeckLinkAPI.so: cannot open shared object file: No such file or directory
warning: A DeckLink iterator could not be created.  The DeckLink drivers may not be installed
warning: Failed to initialize module 'decklink.so'
info: [pipewire] No capture sources available
warning: v4l2loopback not installed, virtual camera not registered
info: [obs-browser]: Version 2.26.9
info: [obs-browser]: CEF Version 127.0.6533.120 (runtime), 127.0.0-6533-fix-stutter-and-osr-extra-info.3042+g176b09c+chromium-127.0.6533.120 (compiled)
error: VAAPI: Failed to initialize display in vaapi_device_h264_supported
info: FFmpeg VAAPI H264 encoding not supported
error: VAAPI: Failed to initialize display in vaapi_device_av1_supported
info: FFmpeg VAAPI AV1 encoding not supported
error: VAAPI: Failed to initialize display in vaapi_device_hevc_supported
info: FFmpeg VAAPI HEVC encoding not supported
error: os_dlopen(/opt/obs/lib/obs-plugins/obs-webrtc.so->/opt/obs/lib/obs-plugins/obs-webrtc.so): libdatachannel.so.0.24: cannot open shared object file: No such file or directory

warning: Module '/opt/obs/lib/obs-plugins/obs-webrtc.so' not loaded
info: [obs-websocket] [obs_module_load] you can haz websockets (Version: 5.7.4 | RPC Version: 1)
info: [obs-websocket] [obs_module_load] Qt version (compile-time): 6.10.2 | Qt version (run-time): 6.10.2
info: [obs-websocket] [obs_module_load] Linked ASIO Version: 103600
info: [obs-websocket] [Config::Load] Existing configuration not found, using defaults.
info: [obs-websocket] [Config::Load] (FirstLoad) Generating new server password.
info: [obs-websocket] [obs_module_load] Module loaded.
info: [vlc-video]: VLC 3.0.23 Vetinari found, VLC video source enabled
info: ---------------------------------
info:   Loaded Modules:
info:     vlc-video.so
info:     text-freetype2.so
info:     rtmp-services.so
info:     obs-x264.so
info:     obs-websocket.so
info:     obs-vst.so
info:     obs-transitions.so
info:     obs-qsv11.so
info:     obs-outputs.so
info:     obs-filters.so
info:     obs-ffmpeg.so
info:     obs-browser.so
info:     linux-v4l2.so
info:     linux-pulseaudio.so
info:     linux-pipewire.so
info:     linux-capture.so
info:     linux-alsa.so
info:     image-source.so
info:     frontend-tools.so
info:     decklink-output-ui.so
info:     decklink-captions.so
info: ---------------------------------
info: ---------------------------------
info: Available Encoders:
info:   Video Encoders:
info:   - ffmpeg_svt_av1 (SVT-AV1)
info:   - ffmpeg_aom_av1 (AOM AV1)
info:   - obs_x264 (x264)
info:   Audio Encoders:
info:   - ffmpeg_aac (FFmpeg AAC)
info:   - ffmpeg_opus (FFmpeg Opus)
info:   - ffmpeg_pcm_s16le (FFmpeg PCM (16-bit))
info:   - ffmpeg_pcm_s24le (FFmpeg PCM (24-bit))
info:   - ffmpeg_pcm_f32le (FFmpeg PCM (32-bit float))
info:   - ffmpeg_alac (FFmpeg ALAC (24-bit))
info:   - ffmpeg_flac (FFmpeg FLAC (16-bit))
info: ==== Startup complete ===============================================
info: No scene file found, creating default scene
warning: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")
info: All scene data cleared
info: ------------------------------------------------
info: Switched to scene 'Scene'
info: Created scene collection 'Untitled' (clean, Untitled.json)
info: ------------------------------------------------
info: [rtmp-services plugin] Successfully updated file 'services.json' (version 293)
info: [rtmp-services plugin] Successfully updated package (version 293)
warning: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")
info: 
==== Auto-config wizard testing commencing ======

info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 128x128
        downscale filter:  Bicubic
        fps:               60/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        128
        height:       128
        keyint:       120

info: [x264 encoder: 'test_x264'] custom settings: 
        scenecut = 0
info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: [rtmp stream: 'test_stream'] Connecting to RTMP URL rtmp://ingest.global-contribute.live-video.net/app...
info: [rtmp stream: 'test_stream'] Connection to rtmp://ingest.global-contribute.live-video.net/app (35.55.40.58) successful
info: [rtmp stream: 'test_stream'] User stopped the stream
info: Output 'test_stream': stopping
info: Output 'test_stream': Total frames output: 751
info: Output 'test_stream': Total drawn frames: 992 (1003 attempted)
info: Output 'test_stream': Number of lagged frames due to rendering lag/stalls: 11 (1.1%)
[aac @ 0x7f7ec0045600] Qavg: 65432.348
[aac @ 0x7f7ec0045600] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        128
        height:       128
        keyint:       120

info: [x264 encoder: 'test_x264'] custom settings: 
        scenecut = 0
info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: [rtmp stream: 'test_stream'] Connecting to RTMP URL rtmp://eun10.contribute.live-video.net/app...
info: [rtmp stream: 'test_stream'] Connection to rtmp://eun10.contribute.live-video.net/app (35.55.40.3) successful
info: [rtmp stream: 'test_stream'] User stopped the stream
info: Output 'test_stream': stopping
info: Output 'test_stream': Total frames output: 751
info: Output 'test_stream': Total drawn frames: 844
[aac @ 0x7f7ec00482c0] Qavg: 65432.520
[aac @ 0x7f7ec00482c0] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        128
        height:       128
        keyint:       120

info: [x264 encoder: 'test_x264'] custom settings: 
        scenecut = 0
info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: [rtmp stream: 'test_stream'] Connecting to RTMP URL rtmp://euc10.contribute.live-video.net/app...
info: [rtmp stream: 'test_stream'] Connection to rtmp://euc10.contribute.live-video.net/app (35.55.18.12) successful
info: [rtmp stream: 'test_stream'] User stopped the stream
info: Output 'test_stream': stopping
info: Output 'test_stream': Total frames output: 751
info: Output 'test_stream': Total drawn frames: 834
[aac @ 0x7f7ec00aa040] Qavg: 65432.348
[aac @ 0x7f7ec00aa040] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1920x1080
        downscale filter:  Bicubic
        fps:               60/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
warning: Output 'null': Tried to use obs_output_set_media on an encoded output
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] profile: main
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        1920
        height:       1080
        keyint:       120

info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: Output 'null': stopping
info: Output 'null': Total frames output: 264
info: Output 'null': Total drawn frames: 300
info: Video stopped, number of skipped frames due to encoding lag: 146/305 (47.9%)
[aac @ 0x7f7ec0026e00] Qavg: 65286.652
[aac @ 0x7f7ec0026e00] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1920x1080
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
warning: Output 'null': Tried to use obs_output_set_media on an encoded output
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] profile: main
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      30
        fps_den:      1
        width:        1920
        height:       1080
        keyint:       60

info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: Output 'null': stopping
info: Output 'null': Total frames output: 122
info: Output 'null': Total drawn frames: 150
[aac @ 0x7f7ec1dffc40] Qavg: 65271.797
[aac @ 0x7f7ec1dffc40] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               60/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
warning: Output 'null': Tried to use obs_output_set_media on an encoded output
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] profile: main
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        1280
        height:       720
        keyint:       120

info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: Output 'null': stopping
info: Output 'null': Total frames output: 273
info: Output 'null': Total drawn frames: 300
[aac @ 0x7f7ec0027440] Qavg: 65270.668
[aac @ 0x7f7ec0027440] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
warning: Output 'null': Tried to use obs_output_set_media on an encoded output
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] profile: main
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      30
        fps_den:      1
        width:        1280
        height:       720
        keyint:       60

info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: Output 'null': stopping
info: Output 'null': Total frames output: 123
info: Output 'null': Total drawn frames: 150
[aac @ 0x7f7ec0027440] Qavg: 65269.527
[aac @ 0x7f7ec0027440] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
warning: QFormLayout::takeAt: Invalid index 0
info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 128x128
        downscale filter:  Bicubic
        fps:               60/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: ---------------------------------
info: [x264 encoder: 'test_x264'] preset: veryfast
info: [x264 encoder: 'test_x264'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      60
        fps_den:      1
        width:        128
        height:       128
        keyint:       120

info: [x264 encoder: 'test_x264'] custom settings: 
        scenecut = 0
info: ---------------------------------
info: [FFmpeg aac encoder: 'test_aac'] bitrate: 32, channels: 2, channel_layout: stereo, track: 1

info: [rtmp stream: 'test_stream'] Connecting to RTMP URL rtmp://ingest.global-contribute.live-video.net/app...
info: [rtmp stream: 'test_stream'] Connection to rtmp://ingest.global-contribute.live-video.net/app (35.55.42.18) successful
info: [rtmp stream: 'test_stream'] User stopped the stream
info: Output 'test_stream': stopping
info: Output 'test_stream': Total frames output: 54
info: Output 'test_stream': Total drawn frames: 136
[aac @ 0x7f7ec000d280] Qavg: 64386.227
[aac @ 0x7f7ec000d280] 2 frames left in the queue on closing
info: ---------------------------------                                                                                                          
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1280x720
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: 
==== Auto-config wizard testing stopping ========

info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1920x1080
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: Settings changed (general, stream 1, outputs, video)
info: ------------------------------------------------
info: User added scene 'Scene 2'
info: User switched to scene 'Scene 2'
info: User switched to scene 'Scene'
info: v4l2-input: Start capture from 
error: v4l2-input: Unable to open device
error: v4l2-input: Initialization failed, errno: No such file or directory
info: User added source 'Video Capture Device (V4L2)' (v4l2_input) to scene 'Scene'
info: v4l2-input: /dev/video1 seems to not support video capture
info: v4l2-input: Found device 'Integrated Camera: Integrated C' at /dev/video0
info: v4l2-input: Found input 'Camera 1' (Index 0)
info: v4l2-controls: setting default for Power Line Frequency to 1
info: v4l2-controls: setting default for Auto Exposure to 3
info: v4l2-input: Pixelformat: Motion-JPEG (available)
info: v4l2-input: Pixelformat: YUYV 4:2:2 (available)
info: v4l2-input: Pixelformat: RGB3 (Emulated) (unavailable)
info: v4l2-input: Pixelformat: BGR3 (Emulated) (available)
info: v4l2-input: Pixelformat: YU12 (Emulated) (available)
info: v4l2-input: Pixelformat: YV12 (Emulated) (available)
info: v4l2-input: Stepwise and Continuous framesizes are currently hardcoded
info: v4l2-input: Stepwise and Continuous framerates are currently hardcoded
info: v4l2-input: Start capture from /dev/video0
info: v4l2-input: Pixelformat: Motion-JPEG (available)
info: v4l2-input: Pixelformat: YUYV 4:2:2 (available)
info: v4l2-input: Pixelformat: RGB3 (Emulated) (unavailable)
info: v4l2-input: Pixelformat: BGR3 (Emulated) (available)
info: v4l2-input: Pixelformat: YU12 (Emulated) (available)
info: v4l2-input: Pixelformat: YV12 (Emulated) (available)
info: v4l2-input: Input: 0
info: v4l2-input: Resolution: 1280x720
info: v4l2-input: Pixelformat: MJPG
info: v4l2-input: Linesize: 0 Bytes
info: v4l2-input: Framerate: 30.00 fps
info: v4l2-input: Stepwise and Continuous framesizes are currently hardcoded
info: v4l2-input: /dev/video0: select timeout set to 166666 (5x frame periods)
error: v4l2-input: /dev/video0: select timed out
error: v4l2-input: /dev/video0: failed to log status
error: v4l2-input: /dev/video0: select timed out
error: v4l2-input: /dev/video0: failed to log status
info: User added source 'Browser' (browser_source) to scene 'Scene'
Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Could not open the default X display.
Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

ERR: DisplayVkXcb.cpp:58 (initialize): xcb_connect() failed, error 1
ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Not initialized.
Authorization required, but no authorization protocol specified

ERR: DisplayVkXcb.cpp:58 (initialize): xcb_connect() failed, error 1
ERR: Display.cpp:1083 (initialize): ANGLE Display::initialize error 12289: Not initialized.
Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

Authorization required, but no authorization protocol specified

[1003/022424.770468:FATAL:gpu_data_manager_impl_private.cc(454)] GPU process isn't usable. Goodbye.
zsh: trace trap  sudo ./obs -p

----------------------------------------------------------------------------------------------------------

┌──(fixit42㉿x1)-[~]
└─$ cd /opt/obs/bin && ./obs -p
debug: Found portal inhibitor
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/locale/en-US.ini
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/locale.ini
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/themes
debug: Attempted path: /opt/obs/bin/../share/obs/obs-studio/themes/
warning: Crash or unclean shutdown detected
qt.qpa.services: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")
warning: [Safe Mode] Normal launch selected, loading third-party plugins is enabled
info: Command Line Arguments: -p
info: Using EGL/X11
info: CPU Name: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
info: CPU Speed: 1714.785MHz
info: Physical Cores: 4, Logical Cores: 8
info: Physical Memory: 7704MB Total, 847MB Free
info: Kernel Version: Linux 7.1.5+kali-amd64
info: Distribution: "Kali GNU/Linux" "2026.3"
info: Desktop Environment: XFCE (lightdm-xsession)
info: Session Type: x11
info: Window System: X11.0, Vendor: The X.Org Foundation, Version: 1.21.1
info: Current Date/Time: 2026-10-03, 02:34:18 AM
info: Browser Hardware Acceleration: true
info: Qt Version: 6.10.2 (runtime), 6.10.2 (compiled)
info: Portable mode: true
info: OBS 32.2.2 (linux)
info: ---------------------------------
info: ---------------------------------
info: audio settings reset:
        samples per sec: 48000
        speakers:        2
        max buffering:   960 milliseconds
        buffering type:  dynamically increasing
info: ---------------------------------
info: Initializing OpenGL...
info: Loading up OpenGL on adapter Intel Mesa Intel(R) UHD Graphics 620 (KBL GT2)
info: OpenGL loaded successfully, version 4.6 (Core Profile) Mesa 26.1.6-1, shading language 4.60
info: ---------------------------------
info: video settings reset:
        base resolution:   1920x1080
        output resolution: 1920x1080
        downscale filter:  Bicubic
        fps:               30/1
        format:            NV12
        YUV mode:          Rec. 709/Partial
info: NV12 texture support enabled
info: P010 texture support not available
info: Audio monitoring device:
        name: Default
        id: default
info: ---------------------------------
warning: Failed to load 'en-US' text for module: 'decklink-captions.so'
warning: Failed to load 'en-US' text for module: 'decklink-output-ui.so'
libDeckLinkAPI.so: cannot open shared object file: No such file or directory
warning: A DeckLink iterator could not be created.  The DeckLink drivers may not be installed
warning: Failed to initialize module 'decklink.so'
info: [pipewire] No capture sources available
warning: v4l2loopback not installed, virtual camera not registered
info: [obs-browser]: Version 2.26.9
info: [obs-browser]: CEF Version 127.0.6533.120 (runtime), 127.0.0-6533-fix-stutter-and-osr-extra-info.3042+g176b09c+chromium-127.0.6533.120 (compiled)
error: VAAPI: Failed to initialize display in vaapi_device_h264_supported
info: FFmpeg VAAPI H264 encoding not supported
error: VAAPI: Failed to initialize display in vaapi_device_av1_supported
info: FFmpeg VAAPI AV1 encoding not supported
error: VAAPI: Failed to initialize display in vaapi_device_hevc_supported
info: FFmpeg VAAPI HEVC encoding not supported
error: os_dlopen(/opt/obs/lib/obs-plugins/obs-webrtc.so->/opt/obs/lib/obs-plugins/obs-webrtc.so): libdatachannel.so.0.24: cannot open shared object file: No such file or directory

warning: Module '/opt/obs/lib/obs-plugins/obs-webrtc.so' not loaded
info: [obs-websocket] [obs_module_load] you can haz websockets (Version: 5.7.4 | RPC Version: 1)
info: [obs-websocket] [obs_module_load] Qt version (compile-time): 6.10.2 | Qt version (run-time): 6.10.2
info: [obs-websocket] [obs_module_load] Linked ASIO Version: 103600
info: [obs-websocket] [obs_module_load] Module loaded.
info: [vlc-video]: VLC 3.0.23 Vetinari found, VLC video source enabled
info: ---------------------------------
info:   Loaded Modules:
info:     vlc-video.so
info:     text-freetype2.so
info:     rtmp-services.so
info:     obs-x264.so
info:     obs-websocket.so
info:     obs-vst.so
info:     obs-transitions.so
info:     obs-qsv11.so
info:     obs-outputs.so
info:     obs-filters.so
info:     obs-ffmpeg.so
info:     obs-browser.so
info:     linux-v4l2.so
info:     linux-pulseaudio.so
info:     linux-pipewire.so
info:     linux-capture.so
info:     linux-alsa.so
info:     image-source.so
info:     frontend-tools.so
info:     decklink-output-ui.so
info:     decklink-captions.so
info: ---------------------------------
info: ---------------------------------
info: Available Encoders:
info:   Video Encoders:
info:   - ffmpeg_svt_av1 (SVT-AV1)
info:   - ffmpeg_aom_av1 (AOM AV1)
info:   - obs_x264 (x264)
info:   Audio Encoders:
info:   - ffmpeg_aac (FFmpeg AAC)
info:   - ffmpeg_opus (FFmpeg Opus)
info:   - ffmpeg_pcm_s16le (FFmpeg PCM (16-bit))
info:   - ffmpeg_pcm_s24le (FFmpeg PCM (24-bit))
info:   - ffmpeg_pcm_f32le (FFmpeg PCM (32-bit float))
info:   - ffmpeg_alac (FFmpeg ALAC (24-bit))
info:   - ffmpeg_flac (FFmpeg FLAC (16-bit))
info: ==== Startup complete ===============================================
info: All scene data cleared
info: ------------------------------------------------
info: v4l2-input: Start capture from /dev/video0
info: v4l2-input: Input: 0
info: v4l2-input: Resolution: 1280x720
info: v4l2-input: Pixelformat: MJPG
info: v4l2-input: Linesize: 0 Bytes
info: v4l2-input: Framerate: 30.00 fps
info: v4l2-input: /dev/video0: select timeout set to 166666 (5x frame periods)
info: Switched to scene 'Scene'
info: ------------------------------------------------
info: Loaded scenes:
info: - scene 'Scene':
info:     - source: 'Video Capture Device (V4L2)' (v4l2_input)
info:     - source: 'Browser' (browser_source)
info: - scene 'Scene 2':
info: ------------------------------------------------
error: v4l2-input: /dev/video0: select timed out
error: v4l2-input: /dev/video0: failed to log status
error: v4l2-input: /dev/video0: select timed out
error: v4l2-input: /dev/video0: failed to log status
info: User added filter 'Color Correction' (color_filter_v2) to source 'Browser'
info: User switched to scene 'Scene 2'
info: User added source 'Display Capture (XSHM)' (xshm_input_v2) to scene 'Scene 2'
info: xshm-input: Geometry 1920x1080 @ 0,0
info: User switched to scene 'Scene'
info: User added source 'Browser 2' (browser_source) to scene 'Scene'
info: User added source 'Text (FreeType 2)' (text_ft2_source_v2) to scene 'Scene'
info: alsa-input: PCM 'default' rate set to 44100
info: alsa-input: PCM 'default' channels set to 2
info: User added source 'Audio Capture Device (ALSA)' (alsa_input_capture) to scene 'Scene'
info: adding 42 milliseconds of audio buffering, total audio buffering is now 42 milliseconds (source: Audio Capture Device (ALSA))

info: alsa-input: PCM 'front:CARD=PCH,DEV=0' rate set to 44100
info: alsa-input: PCM 'front:CARD=PCH,DEV=0' channels set to 2
info: adding 320 milliseconds of audio buffering, total audio buffering is now 362 milliseconds (source: Audio Capture Device (ALSA))

info: adding 21 milliseconds of audio buffering, total audio buffering is now 384 milliseconds (source: Audio Capture Device (ALSA))

info: User switched to scene 'Scene 2'
info: User switched to scene 'Scene'
info: User switched to scene 'Scene 2'
info: User added source 'Audio Capture Device (ALSA)' (alsa_input_capture) to scene 'Scene 2'
info: User switched to scene 'Scene'
info: User switched to scene 'Scene 2'
info: User added source 'Browser 2' (browser_source) to scene 'Scene 2'
info: User switched to scene 'Scene'
info: ---------------------------------
info: [x264 encoder: 'simple_video_stream'] preset: veryfast
info: [x264 encoder: 'simple_video_stream'] settings:
        rate_control: CBR
        bitrate:      6000
        buffer size:  6000
        crf:          23
        fps_num:      30
        fps_den:      1
        width:        1920
        height:       1080
        keyint:       60

info: [x264 encoder: 'simple_video_stream'] custom settings: 
        scenecut = 0
info: ---------------------------------
info: [FFmpeg aac encoder: 'simple_aac'] bitrate: 160, channels: 2, channel_layout: stereo, track: 1

info: [rtmp stream: 'simple_stream'] Connecting to RTMP URL rtmp://ingest.global-contribute.live-video.net/app...
info: [rtmp stream: 'simple_stream'] Connection to rtmp://ingest.global-contribute.live-video.net/app (35.55.42.17) successful
info: ==== Streaming Start ===============================================
info: User switched to scene 'Scene 2'
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: alsa-input: PCM 'default' rate set to 44100
info: alsa-input: PCM 'default' channels set to 2
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: User switched to scene 'Scene'
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: User switched to scene 'Scene 2'
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: User switched to scene 'Scene'
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: alsa-input: PCM 'front:CARD=PCH,DEV=0' rate set to 44100
info: alsa-input: PCM 'front:CARD=PCH,DEV=0' channels set to 2
info: User switched to scene 'Scene 2'
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
ALSA lib confmisc.c:1377:(snd_func_refer) [error.core] Unable to find definition 'cards.1.pcm.front.0:CARD=Snowball'
ALSA lib conf.c:5211:(_snd_config_evaluate) [error.core] function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5734:(snd_config_expand) [error.core] Evaluate error: No such file or directory
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) [error.pcm] Unknown PCM front:CARD=Snowball,DEV=0
error: alsa-input: Failed to open 'front:CARD=Snowball,DEV=0': No such file or directory
info: alsa-input: PCM 'front:CARD=PCH,DEV=0' rate set to 44100
info: alsa-input: PCM 'front:CARD=PCH,DEV=0' channels set to 2
info: User switched to scene 'Scene'
info: [rtmp stream: 'simple_stream'] User stopped the stream
info: Output 'simple_stream': stopping
info: Output 'simple_stream': Total frames output: 16133
info: Output 'simple_stream': Total drawn frames: 16195 (16199 attempted)
info: Output 'simple_stream': Number of lagged frames due to rendering lag/stalls: 4 (0.0%)
info: [rtmp stream: 'simple_stream'] Freeing 1 remaining packets
info: Video stopped, number of skipped frames due to encoding lag: 10/16160 (0.1%)
info: ==== Streaming Stop ================================================
[aac @ 0x55ea87460180] Qavg: 9038.410
[aac @ 0x55ea87460180] 2 frames left in the queue on closing
info: ==== Shutting down ==================================================                                                                      
info: v4l2-input: /dev/video0: Stopped capture after 42491 frames
info: All scene data cleared
info: ------------------------------------------------
error: Tried to call obs_frontend_remove_event_callback with no callbacks!
info: [obs-websocket] [obs_module_unload] Shutting down...
error: Tried to call obs_frontend_remove_event_callback with no callbacks!
info: [obs-websocket] [obs_module_unload] Finished shutting down.
info: [Scripting] Total detached callbacks: 0
info: Freeing OBS context data
info: == Profiler Results =============================
info: run_program_init: 144771 ms
info:  ┣OBSApp::AppInit: 61.498 ms
info:  ┃ ┗OBSApp::InitLocale: 0.961 ms
info:  ┗OBSApp::OBSInit: 136292 ms
info:    ┣obs_startup: 25.812 ms
info:    ┗OBSBasic::OBSInit: 136227 ms
info:      ┣OBSBasic::InitBasicConfig: 0.732 ms
info:      ┣OBSBasic::ResetAudio: 0.165 ms
info:      ┣OBSBasic::ResetVideo: 261.436 ms
info:      ┃ ┗obs_init_graphics: 257.095 ms
info:      ┃   ┗shader compilation: 153.529 ms
info:      ┣OBSBasic::InitOBSCallbacks: 0.003 ms
info:      ┣OBSBasic::InitHotkeys: 0.035 ms
info:      ┣obs_load_all_modules2: 219.734 ms
info:      ┃ ┣obs_init_module(decklink-captions.so): 0 ms
info:      ┃ ┣obs_init_module(decklink-output-ui.so): 0 ms
info:      ┃ ┣obs_init_module(decklink.so): 0.127 ms
info:      ┃ ┣obs_init_module(frontend-tools.so): 55.186 ms
info:      ┃ ┣obs_init_module(image-source.so): 0.007 ms
info:      ┃ ┣obs_init_module(linux-alsa.so): 0.001 ms
info:      ┃ ┣obs_init_module(linux-capture.so): 1.003 ms
info:      ┃ ┣obs_init_module(linux-pipewire.so): 21.749 ms
info:      ┃ ┣obs_init_module(linux-pulseaudio.so): 0.002 ms
info:      ┃ ┣obs_init_module(linux-v4l2.so): 2.599 ms
info:      ┃ ┣obs_init_module(obs-browser.so): 0.066 ms
info:      ┃ ┣obs_init_module(obs-ffmpeg.so): 0.756 ms
info:      ┃ ┣obs_init_module(obs-filters.so): 0.019 ms
info:      ┃ ┣obs_init_module(obs-outputs.so): 0.003 ms
info:      ┃ ┣obs_init_module(obs-qsv11.so): 1.034 ms
info:      ┃ ┣obs_init_module(obs-transitions.so): 0.007 ms
info:      ┃ ┣obs_init_module(obs-vst.so): 0.002 ms
info:      ┃ ┣obs_init_module(obs-websocket.so): 7.468 ms
info:      ┃ ┣obs_init_module(obs-x264.so): 0.001 ms
info:      ┃ ┣obs_init_module(rtmp-services.so): 0.416 ms
info:      ┃ ┣obs_init_module(text-freetype2.so): 0.009 ms
info:      ┃ ┗obs_init_module(vlc-video.so): 3.589 ms
info:      ┣OBSBasic::InitService: 5.046 ms
info:      ┣OBSBasic::ResetOutputs: 0.272 ms
info:      ┣OBSBasic::CreateHotkeys: 0.054 ms
info:      ┣OBSBasic::InitPrimitives: 0.14 ms
info:      ┗OBSBasic::Load: 210.644 ms
info: obs_hotkey_thread(25 ms): min=0.077 ms, median=0.516 ms, max=133.209 ms, 99th percentile=11.374 ms, 99.955% below 25 ms
info: audio_thread(Audio): min=0.008 ms, median=0.056 ms, max=131.389 ms, 99th percentile=5.261 ms
info:  ┗receive_audio: min=0.002 ms, median=1.173 ms, max=83.071 ms, 99th percentile=7.55 ms, 0.332333 calls per parent call
info:    ┣buffer_audio: min=0.001 ms, median=0.002 ms, max=1.272 ms, 99th percentile=0.01 ms
info:    ┗do_encode: min=0.026 ms, median=1.167 ms, max=83.064 ms, 99th percentile=7.541 ms
info:      ┣encode(simple_aac): min=0.022 ms, median=1.12 ms, max=83.016 ms, 99th percentile=7.145 ms
info:      ┗send_packet: min=0.001 ms, median=0.027 ms, max=22.337 ms, 99th percentile=2.764 ms
info: obs_graphics_thread(33.3333 ms): min=0.099 ms, median=3.721 ms, max=156.629 ms, 99th percentile=17.756 ms, 99.9054% below 33.333 ms
info:  ┣tick_sources: min=0 ms, median=0.023 ms, max=105.897 ms, 99th percentile=8.947 ms
info:  ┣output_frame: min=0.061 ms, median=1.16 ms, max=152.567 ms, 99th percentile=5.539 ms
info:  ┃ ┣gs_context(video->graphics): min=0.061 ms, median=1.001 ms, max=152.555 ms, 99th percentile=2.715 ms
info:  ┃ ┃ ┣render_video: min=0.013 ms, median=0.759 ms, max=151.522 ms, 99th percentile=2.091 ms
info:  ┃ ┃ ┃ ┣render_main_texture: min=0.011 ms, median=0.736 ms, max=151.511 ms, 99th percentile=1.998 ms
info:  ┃ ┃ ┃ ┣render_convert_texture: min=0.023 ms, median=0.049 ms, max=88.469 ms, 99th percentile=0.158 ms, 0.332394 calls per parent call
info:  ┃ ┃ ┃ ┗stage_output_texture: min=0.012 ms, median=0.025 ms, max=2.607 ms, 99th percentile=0.083 ms, 0.332394 calls per parent call
info:  ┃ ┃ ┣gs_flush: min=0.039 ms, median=0.157 ms, max=6.52 ms, 99th percentile=0.61 ms
info:  ┃ ┃ ┗download_frame: min=0 ms, median=0.125 ms, max=10.326 ms, 99th percentile=0.687 ms, 0.332394 calls per parent call
info:  ┃ ┗output_video_data: min=0.001 ms, median=0.612 ms, max=22.489 ms, 99th percentile=4.556 ms, 0.332373 calls per parent call
info:  ┗render_displays: min=0.003 ms, median=1.532 ms, max=66.867 ms, 99th percentile=13.111 ms
info: video_thread(video): min=1.597 ms, median=3.605 ms, max=181.226 ms, 99th percentile=27.004 ms
info:  ┗receive_video: min=1.595 ms, median=3.598 ms, max=181.225 ms, 99th percentile=25.495 ms
info:    ┗do_encode: min=1.594 ms, median=3.596 ms, max=181.224 ms, 99th percentile=25.494 ms
info:      ┣encode(simple_video_stream): min=1.569 ms, median=3.544 ms, max=180.25 ms, 99th percentile=25.324 ms
info:      ┗send_packet: min=0.003 ms, median=0.02 ms, max=12.148 ms, 99th percentile=0.676 ms
info: =================================================
info: == Profiler Time Between Calls ==================
info: obs_hotkey_thread(25 ms): min=25.109 ms, median=25.62 ms, max=158.259 ms, 35.1175% within ±2% of 25 ms (0% lower, 64.8825% higher)
info: obs_graphics_thread(33.3333 ms): min=5.463 ms, median=33.333 ms, max=156.64 ms, 96.2948% within ±2% of 33.333 ms (1.85981% lower, 1.84541% higher)
info: =================================================
info: Number of memory leaks: 0
