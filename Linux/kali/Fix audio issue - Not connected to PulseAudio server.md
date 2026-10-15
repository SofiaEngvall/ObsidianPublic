
![[Images/Pasted image 20261013203817.png]]

![[Images/Pasted image 20261013203732.png]]

Kali Linux recently shifted its default audio framework from **PulseAudio to PipeWire**


debug
```
┌──(fixit42㉿x1)-[~]
└─$ wpctl status
Could not connect to PipeWire

┌──(fixit42㉿x1)-[~]
└─$ wpctl reset --all 
The following files will be removed:
  /home/fixit42/.local/state/wireplumber/default-routes
  /home/fixit42/.local/state/wireplumber/stream-properties
  /home/fixit42/.local/state/wireplumber

WARNING: this action is not reversible.
Proceed? [y/N] y

┌──(fixit42㉿x1)-[~]
└─$ wpctl status     
PipeWire 'pipewire-0' [1.6.9, fixit42@x1, cookie:2806495923]
 └─ Clients:
        34. xdg-desktop-portal                  [1.6.9, fixit42@x1, pid:1644]
        35. WirePlumber                         [1.6.9, fixit42@x1, pid:16766]
        36. WirePlumber [client]                [1.6.9, fixit42@x1, pid:16766]
        37. wpctl                               [1.6.9, fixit42@x1, pid:16812]

Audio
 ├─ Devices:
 │      45. Built-in Audio                      [alsa]
 │  
 ├─ Sinks:
 │  *   54. Built-in Audio Analog Stereo        [vol: 0.40]
 │  
 ├─ Sources:
 │      32. Iriun Mic                           [vol: 1.00]
 │  *   55. Built-in Audio Analog Stereo        [vol: 1.00]
 │  
 ├─ Filters:
 │  
 └─ Streams:

Video
 ├─ Devices:
 │      56. Integrated Camera                   [v4l2]
 │      57. Integrated Camera                   [v4l2]
 │      58. Iriun Webcam                        [v4l2]
 │  
 ├─ Sinks:
 │  
 ├─ Sources:
 │  *   65. Integrated Camera (V4L2)           
 │  
 ├─ Filters:
 │  
 └─ Streams:

Settings
 └─ Default Configured Devices:
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user restart pipewire pipewire-pulse wireplumber
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%+                         
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%+
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%+
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%-
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%-
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl set-volume @DEFAULT_SINK@ 5%-
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ 

```
it works now but reboot stops it again

the actual fix - kalis apt update seems to have forgotten to enable
`systemctl --user enable pipewire pipewire-pulse wireplumber`

```
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user enable pipewire pipewire-pulse wireplumber
Created symlink '/home/fixit42/.config/systemd/user/default.target.wants/pipewire.service' → '/usr/lib/systemd/user/pipewire.service'.
Created symlink '/home/fixit42/.config/systemd/user/sockets.target.wants/pipewire.socket' → '/usr/lib/systemd/user/pipewire.socket'.
Created symlink '/home/fixit42/.config/systemd/user/default.target.wants/pipewire-pulse.service' → '/usr/lib/systemd/user/pipewire-pulse.service'.
Created symlink '/home/fixit42/.config/systemd/user/sockets.target.wants/pipewire-pulse.socket' → '/usr/lib/systemd/user/pipewire-pulse.socket'.
```

nope, still problems after reboot

systemctl --user stop pulseaudio pulseaudio.socket
systemctl --user disable pulseaudio pulseaudio.socket
systemctl --user mask pulseaudio pulseaudio.socket

┌──(fixit42㉿x1)-[~]
└─$ systemctl --user stop pulseaudio pulseaudio.socket
systemctl --user disable pulseaudio pulseaudio.socket
systemctl --user mask pulseaudio pulseaudio.socket
Failed to enqueue jobs: Unit pulseaudio.service not loaded.
Failed to disable unit: Unit pulseaudio.service does not exist
Unit pulseaudio.service does not exist, proceeding anyway.
Unit pulseaudio.socket does not exist, proceeding anyway.
Created symlink '/home/fixit42/.config/systemd/user/pulseaudio.service' → '/dev/null'.
Created symlink '/home/fixit42/.config/systemd/user/pulseaudio.socket' → '/dev/null'.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl status                                      
Could not connect to PipeWire
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl reset --all 
The following files will be removed:
  /home/fixit42/.local/state/wireplumber/stream-properties
  /home/fixit42/.local/state/wireplumber/default-routes
  /home/fixit42/.local/state/wireplumber

WARNING: this action is not reversible.
Proceed? [y/N] y
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ wpctl status     
PipeWire 'pipewire-0' [1.6.9, fixit42@x1, cookie:1072721757]
 └─ Clients:
        34. xdg-desktop-portal                  [1.6.9, fixit42@x1, pid:1629]
        35. WirePlumber                         [1.6.9, fixit42@x1, pid:12441]
        36. WirePlumber [client]                [1.6.9, fixit42@x1, pid:12441]
        37. wpctl                               [1.6.9, fixit42@x1, pid:12545]

Audio
 ├─ Devices:
 │      45. Built-in Audio                      [alsa]
 │  
 ├─ Sinks:
 │  *   54. Built-in Audio Analog Stereo        [vol: 0.40]
 │  
 ├─ Sources:
 │      32. Iriun Mic                           [vol: 1.00]
 │  *   55. Built-in Audio Analog Stereo        [vol: 1.00]
 │  
 ├─ Filters:
 │  
 └─ Streams:

Video
 ├─ Devices:
 │      56. Integrated Camera                   [v4l2]
 │      57. Integrated Camera                   [v4l2]
 │      58. Iriun Webcam                        [v4l2]
 │  
 ├─ Sinks:
 │  
 ├─ Sources:
 │  *   65. Integrated Camera (V4L2)           
 │  
 ├─ Filters:
 │  
 └─ Streams:

Settings
 └─ Default Configured Devices:
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user restart pipewire                           
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user restart pipewire-pulse             
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ this one did it, testing a restart


----

final lap

confirmed that
systemctl --user restart pipewire-pulse 
fixes the problem fully = starting it later might do it

systemctl --user edit pipewire-pulse.service

[Unit]
After=graphical-session.target

---

nope, no change

trying
systemctl --user status pipewire-pulse.service

```sh
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.service

○ pipewire-pulse.service - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.service; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.service.d
             └─kali.conf
             /home/fixit42/.config/systemd/user/pipewire-pulse.service.d
             └─override.conf
     Active: inactive (dead) since Tue 2026-10-13 23:14:07 CEST; 3min 31s ago
   Duration: 30ms
 Invocation: c5a29f49d9534d46b5457b032607cc60
TriggeredBy: × pipewire-pulse.socket
    Process: 1437 ExecStart=/usr/bin/pipewire-pulse (code=exited, status=0/SUCCESS)
   Main PID: 1437 (code=exited, status=0/SUCCESS)
   Mem peak: 2.5M
        CPU: 30ms

Oct 13 23:14:09 x1 systemd[1407]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:14:09 x1 systemd[1407]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:14:09 x1 systemd[1407]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:14:09 x1 systemd[1407]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:14:09 x1 systemd[1407]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.socket
× pipewire-pulse.socket - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.socket; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.socket.d
             └─kali.conf
     Active: failed (Result: trigger-limit-hit) since Tue 2026-10-13 23:14:09 CEST; 5min ago
   Duration: 1.985s
 Invocation: 17f3e2d15ab94d9f844e2f29d77676c6
   Triggers: ● pipewire-pulse.service
     Listen: /run/user/1000/pulse/native (Stream)

Oct 13 23:14:07 x1 systemd[1407]: Listening on pipewire-pulse.socket - PipeWire PulseAudio.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.socket: Trigger limit hit, refusing further activation.
Oct 13 23:14:09 x1 systemd[1407]: pipewire-pulse.socket: Failed with result 'trigger-limit-hit'.

```


such a mess!

---

remove experiments
rm -rf ~/.config/systemd/user/pipewire-pulse.service.d/
rm -rf ~/.config/systemd/user/pipewire-pulse.socket.d/

remove old configs
rm -rf ~/.config/pulse ~/.local/state/wireplumber ~/.config/wireplumber

reinstall
sudo apt install --reinstall -o Dpkg::Options::="--force-confmiss" -o Dpkg::Options::="--force-confnew" pipewire pipewire-pulse wireplumber pavucontrol

make sure to enable them
systemctl --user enable pipewire.socket pipewire-pulse.socket wireplumber.service

reboot

log:
```sh
┌──(fixit42㉿x1)-[~]
└─$ rm -rf ~/.config/systemd/user/pipewire-pulse.service.d/
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ rm -rf ~/.config/systemd/user/pipewire-pulse.socket.d/
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ rm -rf ~/.config/pulse ~/.local/state/wireplumber ~/.config/wireplumber
                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ sudo apt install --reinstall -o Dpkg::Options::="--force-confmiss" -o Dpkg::Options::="--force-confnew" pipewire pipewire-pulse wireplumber pavucontrol
The following packages were automatically installed and are no longer required:
  libavcodec62:i386  libavfilter11     libboost-python1.90.0  libswresample6:i386
  libavdevice62      libavutil60:i386  libobjc-15-dev         ruby-http-parser.rb
Use 'sudo apt autoremove' to remove them.

Summary:
  Upgrading: 0, Installing: 0, Reinstalling: 4, Removing: 0, Not Upgrading: 2
  Download size: 476 kB
  Space needed: 0 B / 146 GB available

Get:1 http://kali.download/kali kali-rolling/main amd64 pavucontrol amd64 6.1-1 [199 kB]
Get:3 http://kali.download/kali kali-rolling/main amd64 pipewire-pulse amd64 1.6.9-2 [15.4 kB]
Get:2 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 pipewire amd64 1.6.9-2 [117 kB]
Get:4 http://mirrors.dotsrc.org/kali kali-rolling/main amd64 wireplumber amd64 0.5.17-1 [144 kB]
Fetched 476 kB in 1s (626 kB/s)      
(Reading database… 851893 files and directories currently installed.)
Preparing to unpack …/pavucontrol_6.1-1_amd64.deb…
Unpacking pavucontrol (6.1-1) over (6.1-1)…
Preparing to unpack …/pipewire_1.6.9-2_amd64.deb…
Unpacking pipewire:amd64 (1.6.9-2) over (1.6.9-2)…
Preparing to unpack …/pipewire-pulse_1.6.9-2_amd64.deb…
Unpacking pipewire-pulse (1.6.9-2) over (1.6.9-2)…
Preparing to unpack …/wireplumber_0.5.17-1_amd64.deb…
Unpacking wireplumber (0.5.17-1) over (0.5.17-1)…
Setting up pavucontrol (6.1-1)…
Setting up pipewire:amd64 (1.6.9-2)…
Setting up wireplumber (0.5.17-1)…
Setting up pipewire-pulse (1.6.9-2)…
Processing triggers for kali-menu (2026.3.4)…
Processing triggers for desktop-file-utils (0.28-1)…
Processing triggers for man-db (2.13.1-1)…
Processing triggers for libglib2.0-0t64:amd64 (2.90.0-1)…
Processing triggers for libglib2.0-0t64:i386 (2.90.0-1)…
Processing triggers for mailcap (3.77)…
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
└─$ systemctl --user enable pipewire.socket pipewire-pulse.socket wireplumber.service

                                                                                                                                                 
┌──(fixit42㉿x1)-[~]
└─$ 

```

still no success

---


```sh
┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.service
○ pipewire-pulse.service - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.service; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.service.d
             └─kali.conf
     Active: inactive (dead) since Tue 2026-10-13 23:42:09 CEST; 35min ago
   Duration: 15ms
 Invocation: 38d001f468dc435bbd017e27505f249a
TriggeredBy: × pipewire-pulse.socket
    Process: 1487 ExecStart=/usr/bin/pipewire-pulse (code=killed, signal=TERM)
   Main PID: 1487 (code=killed, signal=TERM)
   Mem peak: 2.2M
        CPU: 15ms

Oct 13 23:42:11 x1 systemd[1457]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:42:11 x1 systemd[1457]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:42:11 x1 systemd[1457]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:42:11 x1 systemd[1457]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.
Oct 13 23:42:11 x1 systemd[1457]: Dependency failed for pipewire-pulse.service - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.service: Job pipewire-pulse.service/start failed with result 'dependency'.

┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.socket
× pipewire-pulse.socket - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.socket; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.socket.d
             └─kali.conf
     Active: failed (Result: trigger-limit-hit) since Tue 2026-10-13 23:42:11 CEST; 35min ago
   Duration: 2.047s
 Invocation: b41b52f12bc540b094b25559a20452a6
   Triggers: ● pipewire-pulse.service
     Listen: /run/user/1000/pulse/native (Stream)

Oct 13 23:42:09 x1 systemd[1457]: Listening on pipewire-pulse.socket - PipeWire PulseAudio.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.socket: Trigger limit hit, refusing further activation.
Oct 13 23:42:11 x1 systemd[1457]: pipewire-pulse.socket: Failed with result 'trigger-limit-hit'.

┌──(fixit42㉿x1)-[~]
└─$ systemctl --user restart pipewire-pulse      

┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.service
● pipewire-pulse.service - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.service; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.service.d
             └─kali.conf
     Active: active (running) since Wed 2026-10-14 00:25:51 CEST; 11s ago
 Invocation: a7d5b31b816d4e1092c257d6e742ab45
TriggeredBy: ● pipewire-pulse.socket
   Main PID: 35965 (pipewire-pulse)
      Tasks: 3 (limit: 8988)
     Memory: 2M (peak: 2.6M)
        CPU: 34ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/session.slice/pipewire-pulse.service
             └─35965 /usr/bin/pipewire-pulse

Oct 14 00:25:51 x1 systemd[1457]: Started pipewire-pulse.service - PipeWire PulseAudio.

┌──(fixit42㉿x1)-[~]
└─$ systemctl --user status pipewire-pulse.socket 
● pipewire-pulse.socket - PipeWire PulseAudio
     Loaded: loaded (/usr/lib/systemd/user/pipewire-pulse.socket; enabled; preset: enabled)
    Drop-In: /usr/lib/systemd/user/pipewire-pulse.socket.d
             └─kali.conf
     Active: active (running) since Wed 2026-10-14 00:25:51 CEST; 20s ago
 Invocation: 6a91cf2caa304f38ab99259c749adcff
   Triggers: ● pipewire-pulse.service
     Listen: /run/user/1000/pulse/native (Stream)

Oct 14 00:25:51 x1 systemd[1457]: Listening on pipewire-pulse.socket - PipeWire PulseAudio.
```
