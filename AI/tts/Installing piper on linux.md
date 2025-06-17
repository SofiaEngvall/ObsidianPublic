
Download from releases: https://github.com/rhasspy/piper/releases

```sh
┌──(kali㉿proxli)-[/opt]
└─$ sudo tar -xvf ~/Downloads/piper_linux_x86_64.tar.gz
piper/
piper/espeak-ng
piper/libpiper_phonemize.so.1.2.0
...
```

```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ sudo mv ~/Downloads/en_US-amy-low.onnx* .
```

```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ ls -la
total 95424
drwxr-xr-x 4 root root     4096 May 31 00:52 .
drwxr-xr-x 9 root root     4096 May 30 23:01 ..
-rw-rw-r-- 1 kali kali 63104526 May 31 00:49 en_US-amy-low.onnx
-rw-rw-r-- 1 kali kali     4164 May 31 00:50 en_US-amy-low.onnx.json
-rw-r--r-- 1 root root    32776 Nov 14  2023 espeak-ng
drwxr-xr-x 4 root root     4096 Nov 14  2023 espeak-ng-data
lrwxrwxrwx 1 root root       17 Nov 14  2023 libespeak-ng.so -> libespeak-ng.so.1
lrwxrwxrwx 1 root root       24 Nov 14  2023 libespeak-ng.so.1 -> libespeak-ng.so.1.52.0.1
-rw-r--r-- 1 root root   580648 Nov 14  2023 libespeak-ng.so.1.52.0.1
lrwxrwxrwx 1 root root       24 Nov 14  2023 libonnxruntime.so -> libonnxruntime.so.1.14.1
-rw-r--r-- 1 root root 16324080 Nov 14  2023 libonnxruntime.so.1.14.1
lrwxrwxrwx 1 root root       23 Nov 14  2023 libpiper_phonemize.so -> libpiper_phonemize.so.1
lrwxrwxrwx 1 root root       27 Nov 14  2023 libpiper_phonemize.so.1 -> libpiper_phonemize.so.1.2.0
-rw-r--r-- 1 root root  1244560 Nov 14  2023 libpiper_phonemize.so.1.2.0
-rw-r--r-- 1 root root 10261536 Nov 14  2023 libtashkeel_model.ort
-rwxr-xr-x 1 root root  4999768 Nov 14  2023 piper
-rwxr-xr-x 1 root root  1121952 Nov 14  2023 piper_phonemize
drwxr-xr-x 2 root root     4096 Nov 14  2023 pkgconfig
```

Downloaded and added the two `en_US-amy-low` files

```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ echo 'Welcome to the world of speech synthesis!' | \
  sudo ./piper --model en_US-amy-low.onnx --output_file welcome.wav
[2025-05-31 00:54:02.488] [piper] [info] Loaded voice in 0.352967142 second(s)
[2025-05-31 00:54:02.489] [piper] [info] Initialized piper
welcome.wav
[2025-05-31 00:54:02.801] [piper] [info] Real-time factor: 0.10610252269553072 (infer=0.303877625 sec, audio=2.864 sec)
[2025-05-31 00:54:02.801] [piper] [info] Terminated piper
```
Created a file

To play it:
```sh
──(kali㉿proxli)-[/opt/piper]
└─$ echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --output_raw | aplay -r 17000 -f S16_LE -t raw -
Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 17000 Hz, Mono
[2025-05-31 00:59:25.625] [piper] [info] Loaded voice in 0.326168612 second(s)
[2025-05-31 00:59:25.626] [piper] [info] Initialized piper
[2025-05-31 00:59:26.469] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 00:59:32.740] [piper] [info] Real-time factor: 0.09280827894973069 (infer=0.827107382 sec, audio=8.912 sec)
[2025-05-31 00:59:32.740] [piper] [info] Terminated piper
```

We added sox to control speed more
```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | sox -q -t raw -r 17000 -e signed -b 16 -c 1 - -t raw - tempo 1.4 | aplay -N -r 17000 -f S16_LE -t raw -
Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 17000 Hz, Mono
[2025-05-31 01:16:12.127] [piper] [info] Loaded voice in 0.354678241 second(s)
[2025-05-31 01:16:12.128] [piper] [info] Initialized piper
[2025-05-31 01:16:12.834] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 01:16:12.837] [piper] [info] Real-time factor: 0.14837406980240547 (infer=0.690829669 sec, audio=4.656000000000001 sec)
[2025-05-31 01:16:12.837] [piper] [info] Terminated piper
```

the end was cut off so we tried ffmpeg and then we might as well play it with ffplay:
```

```

We also downloaded more voices:
```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ ls -la
total 403900
drwxr-xr-x 4 root root     4096 May 31 02:44 .
drwxr-xr-x 9 root root     4096 May 30 23:01 ..
-rw-rw-r-- 1 kali kali 63104526 May 31 00:49 en_US-amy-low.onnx
-rw-rw-r-- 1 kali kali     4164 May 31 00:50 en_US-amy-low.onnx.json
-rw-rw-r-- 1 kali kali 63201294 May 31 02:43 en_US-amy-medium.onnx
-rw-rw-r-- 1 kali kali     4882 May 31 02:43 en_US-amy-medium.onnx.json
-rw-rw-r-- 1 kali kali 63104526 May 31 02:41 en_US-danny-low.onnx
-rw-rw-r-- 1 kali kali     4166 May 31 02:41 en_US-danny-low.onnx.json
-rw-rw-r-- 1 kali kali 63104526 May 31 02:38 en_US-kathleen-low.onnx
-rw-rw-r-- 1 kali kali     4169 May 31 02:38 en_US-kathleen-low.onnx.json
-rw-rw-r-- 1 kali kali 63201294 May 31 02:42 en_US-lessac-low.onnx
-rw-rw-r-- 1 kali kali     4882 May 31 02:42 en_US-lessac-low.onnx.json
-rw-rw-r-- 1 kali kali 63104526 May 31 02:42 en_US-ryan-low.onnx
-rw-rw-r-- 1 kali kali     4165 May 31 02:42 en_US-ryan-low.onnx.json
...
-rw-r--r-- 1 root root    97580 May 31 00:54 welcome.wav
```

And tested longer texts:
```sh
┌──(kali㉿proxli)-[/opt/piper]
└─$ echo "Title: CISO Stature Rises, but Security Budgets Remain Tight                                         
Published: 2025-05-30
Link: https://www.darkreading.com/cybersecurity-operations/ciso-stature-rises-budgets-tight
Word count: 926
Generating summary (approximate length 300)...                         

Cybersecurity professionals, particularly Chief Information Security Officers (CISOs), are facing challenges despite receiving high salaries and expanding responsibilities. A recent survey by IANS Research found that the average CISO at large US companies earns $532,000, including bonuses and equity benefits. However, CISOs continue to struggle with securing budget approval, with many being unable to 
justify their expenses beyond mitigating risk.

The Ernst & Young survey revealed that 58% of CISOs face challenges communicating their value beyond risk mitigation. The industry is also seeing a shift towards tying security expenditures to business 
growth initiatives, allowing CISOs to secure budget approvals for initiatives directly tied to business expansion.

Despite the growing importance of cybersecurity, many CISOs are not consulted in major business strategy decisions, with nearly 60% saying they are not involved or involved too late. To address this, experts recommend that CISOs focus on simplification and automation, embracing a unified technology platform approach, and working closely with other business units to drive innovation.

To create value for the enterprise, CISOs should prioritize proactive adoption of AI and align their strategy with business goals. By connecting cybersecurity to enterprise-wide growth initiatives and quantifying its contribution, CISOs can unlock a larger share of the organization's value creation agenda. The security team should lead in AI adoption, driving efficiency and tackling security issues before other groups deploy the technology. 

Overall, while CISOs are doing well in terms of compensation, they continue to face challenges in securing budget approvals and communicating their value to organizations. By adopting a proactive and collaborative approach, CISOs can drive business growth and create value for their enterprises." | sudo ./piper --model en_US-ryan-low.onnx --length_scale 0.1 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 16000 -ac 1 -i pipe: -af "speechnorm=e=6:r=0.0001:l=1,atempo=1.0" -fflags +flush_packets -bufsize 1M -f wav - | ffplay -hide_banner -loglevel error -autoexit -infbuf -nodisp -
[2025-05-31 03:06:41.269] [piper] [info] Loaded voice in 0.410376377 second(s)
[2025-05-31 03:06:41.270] [piper] [info] Initialized piper
[2025-05-31 03:06:41.566] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:41.570] [piper] [info] Real-time factor: 0.11987862709731545 (infer=0.285790647 sec, audio=2.384 sec)
[2025-05-31 03:06:41.824] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:41.824] [piper] [info] Real-time factor: 0.11576687326989618 (infer=0.535306022 sec, audio=4.6240000000000006 sec)
[2025-05-31 03:06:42.517] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:42.526] [piper] [info] Real-time factor: 0.11479108345921447 (infer=1.2158671559999998 sec, audio=10.592 sec)
[2025-05-31 03:06:42.676] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:42.678] [piper] [info] Real-time factor: 0.11408657220548861 (infer=1.363562711 sec, audio=11.952 sec)
[2025-05-31 03:06:42.889] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:42.891] [piper] [info] Real-time factor: 0.11417818232808857 (infer=1.567438087 sec, audio=13.728 sec)
[2025-05-31 03:06:42.892] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:42.893] [piper] [info] Real-time factor: 0.11417818232808857 (infer=1.567438087 sec, audio=13.728 sec)
[2025-05-31 03:06:45.515] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:45.516] [piper] [info] Real-time factor: 0.14518221670626047 (infer=4.1556957709999995 sec, audio=28.624 sec)
[2025-05-31 03:06:45.693] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:45.694] [piper] [info] Real-time factor: 0.14230022845394738 (infer=4.325926945 sec, audio=30.4 sec)
[2025-05-31 03:06:45.696] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:45.697] [piper] [info] Real-time factor: 0.14230022845394738 (infer=4.325926945 sec, audio=30.4 sec)
[2025-05-31 03:06:46.498] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:46.500] [piper] [info] Real-time factor: 0.1343465056197479 (infer=5.115914934 sec, audio=38.08 sec)
[2025-05-31 03:06:46.898] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:46.902] [piper] [info] Real-time factor: 0.13086486644161277 (infer=5.504699742 sec, audio=42.064 sec)
[2025-05-31 03:06:46.903] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:46.904] [piper] [info] Real-time factor: 0.13086486644161277 (infer=5.504699742 sec, audio=42.064 sec)
[2025-05-31 03:06:48.591] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:48.598] [piper] [info] Real-time factor: 0.12763176939655174 (infer=7.165758061 sec, audio=56.144 sec)
[2025-05-31 03:06:48.599] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:48.599] [piper] [info] Real-time factor: 0.12763176939655174 (infer=7.165758061 sec, audio=56.144 sec)
[2025-05-31 03:06:50.244] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:50.247] [piper] [info] Real-time factor: 0.12217086294493881 (infer=8.786528463 sec, audio=71.92 sec)
[2025-05-31 03:06:50.248] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:50.249] [piper] [info] Real-time factor: 0.12217086294493881 (infer=8.786528463 sec, audio=71.92 sec)
[2025-05-31 03:06:51.516] [piper] [info] Waiting for audio to finish playing...
[2025-05-31 03:06:51.518] [piper] [info] Real-time factor: 0.12164972980937133 (infer=10.031723319 sec, audio=82.46400000000001 sec)
[2025-05-31 03:06:51.518] [piper] [info] Terminated piper
```
### Commands

##### Tests

The examples using aplay uses `sudo apt install alsa-utils`

```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken. This is another sentence just to get some more words to test with.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | sox -q -t raw -r 17000 -e signed -b 16 -c 1 - -t raw - tempo 1.4 | aplay -N -r 17000 -f S16_LE -t raw -
(cuts last word in half)
```

```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -f s16le -ar 17000 -ac 1 -i pipe: -af "atempo=1.0" -f wav - | ffplay -autoexit -nodisp -
```


```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -f s16le -ar 17000 -ac 1 -i pipe: -af "aresample=resampler=soxr:precision=28,atempo=2.0" -f wav - | ffplay -autoexit -nodisp -
```

```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 17000 -ac 1 -i pipe: -af "aresample=resampler=soxr:precision=28,atempo=2.0" -f wav - | ffplay -hide_banner -loglevel error -autoexit -nodisp -
```

```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 17000 -ac 1 -i pipe: -af "aresample=resampler=soxr:precision=28,atempo=2.0" -fflags +flush_packets -bufsize 1M -f wav - | ffplay -hide_banner -loglevel error -autoexit -infbuf -nodisp -
```

##### To use for rss-read-aloud? (or python version)

###### Low speed:
```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.5 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 17000 -ac 1 -i pipe: -af "speechnorm=e=6:r=0.0001:l=1,atempo=1.0" -fflags +flush_packets -bufsize 1M -f wav - | ffplay -hide_banner -loglevel error -autoexit -infbuf -nodisp -
```

###### Mid Speed:
```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 17000 -ac 1 -i pipe: -af "speechnorm=e=6:r=0.0001:l=1,atempo=1.0" -fflags +flush_packets -bufsize 1M -f wav - | ffplay -hide_banner -loglevel error -autoexit -infbuf -nodisp -
```

###### Max speed:
```sh
echo 'Welcome to the world of speech synthesis! This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | sudo ./piper --model en_US-amy-low.onnx --length_scale 0.1 --output_raw | ffmpeg -hide_banner -loglevel error -f s16le -ar 17000 -ac 1 -i pipe: -af "speechnorm=e=6:r=0.0001:l=1,atempo=1.6" -fflags +flush_packets -bufsize 1M -f wav - | ffplay -hide_banner -loglevel error -autoexit -infbuf -nodisp -
```

##### Voices

Download voice models: https://github.com/rhasspy/piper/blob/master/VOICES.md

###### female voice amy
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/low/en_US-amy-low.onnx?download=true
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/low/en_US-amy-low.onnx.json?download=true.json

###### male voice ryan
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx?download=true
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx.json?download=true.json






