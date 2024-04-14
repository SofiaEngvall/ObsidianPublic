
```sh
┌──(kali㉿kali)-[~/shells]
└─$ feroxbuster -u http://jewel.uploadvulns.thm/ -E   

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://jewel.uploadvulns.thm/
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💰  Collect Extensions    │ true
 💸  Ignored Extensions    │ [Images, Movies, Audio, etc...]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       20l       58w      844c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
301      GET       10l       16w      181c http://jewel.uploadvulns.thm/modules => http://jewel.uploadvulns.thm/modules/
200      GET       21l       70w     1579c http://jewel.uploadvulns.thm/assets/js/upload.js
200      GET       48l       78w     6019c http://jewel.uploadvulns.thm/assets/title.svg
200      GET        1l       35w     1404c http://jewel.uploadvulns.thm/assets/css/style.css
200      GET       11l       54w     2568c http://jewel.uploadvulns.thm/assets/favicon.ico
200      GET        1l        8w      880c http://jewel.uploadvulns.thm/assets/js/backgrounds.js
200      GET        1l        1w      101c http://jewel.uploadvulns.thm/assets/css/exo.css
200      GET        1l        1w      217c http://jewel.uploadvulns.thm/assets/css/cinzel.css
200      GET        1l        9w      657c http://jewel.uploadvulns.thm/assets/css/icons.css
200      GET        3l       91w     7047c http://jewel.uploadvulns.thm/assets/js/jquery.colour-2.2.0.min.js
301      GET       10l       16w      181c http://jewel.uploadvulns.thm/content => http://jewel.uploadvulns.thm/content/
200      GET        1l       10w      932c http://jewel.uploadvulns.thm/assets/css/backend.css
200      GET        1l       18w      478c http://jewel.uploadvulns.thm/assets/js/parseurl.js
200      GET       29l       87w     1238c http://jewel.uploadvulns.thm/admin
301      GET       10l       16w      179c http://jewel.uploadvulns.thm/assets => http://jewel.uploadvulns.thm/assets/
200      GET        2l     1297w    89476c http://jewel.uploadvulns.thm/assets/js/jquery-3.5.1.min.js
200      GET       30l      107w     1514c http://jewel.uploadvulns.thm/
200      GET       29l       87w     1238c http://jewel.uploadvulns.thm/Admin
301      GET       10l       16w      185c http://jewel.uploadvulns.thm/assets/js => http://jewel.uploadvulns.thm/assets/js/
301      GET       10l       16w      193c http://jewel.uploadvulns.thm/assets/images => http://jewel.uploadvulns.thm/assets/images/
301      GET       10l       16w      187c http://jewel.uploadvulns.thm/assets/css => http://jewel.uploadvulns.thm/assets/css/
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/css/stats
301      GET       10l       16w      191c http://jewel.uploadvulns.thm/assets/fonts => http://jewel.uploadvulns.thm/assets/fonts/
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/js/pics.js
200      GET       29l       87w     1238c http://jewel.uploadvulns.thm/ADMIN
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/css/_tempalbums
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/images/tracker
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/fonts/webadmin
...
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/fonts/disallowed.js
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/newImages
404      GET        0l        0w      844c http://jewel.uploadvulns.thm/assets/css/prepare_data
[####################] - 25m   480009/480009  0s      found:122     errors:198635 
[##########>---------] - 12m    30000/59970   40/s    http://jewel.uploadvulns.thm/ 
[##########>---------] - 24m    30000/60000   20/s    http://jewel.uploadvulns.thm/modules/ 
[####################] - 24m    30000/30000   21/s    http://jewel.uploadvulns.thm/content/ 
[####################] - 24m    30000/30000   21/s    http://jewel.uploadvulns.thm/assets/ 
[####################] - 24m    30000/30000   21/s    http://jewel.uploadvulns.thm/assets/js/ 
[####################] - 24m    30000/30000   21/s    http://jewel.uploadvulns.thm/assets/css/ 
[####################] - 24m    30000/30000   21/s    http://jewel.uploadvulns.thm/assets/images/ 
[####################] - 22m    30000/30000   22/s    http://jewel.uploadvulns.thm/assets/fonts/                                                                                                                                       
```


before second upload
```sh
┌──(kali㉿kali)-[~/shells]
└─$ feroxbuster -u http://jewel.uploadvulns.thm/content/ -w 3letters.txt -x jpg

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://jewel.uploadvulns.thm/content/
 🚀  Threads               │ 50
 📖  Wordlist              │ 3letters.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💲  Extensions            │ [jpg]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       20l       58w      844c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
200      GET     1854l    10634w   798455c http://jewel.uploadvulns.thm/content/LKQ.jpg
200      GET      853l     5271w   446639c http://jewel.uploadvulns.thm/content/SAD.jpg
200      GET     1694l     8202w   611152c http://jewel.uploadvulns.thm/content/UAD.jpg
200      GET       13l       35w      395c http://jewel.uploadvulns.thm/content/UKD.jpg
200      GET       12l       34w      382c http://jewel.uploadvulns.thm/content/XBE.jpg
[####################] - 2m     15634/15634   0s      found:5       errors:23     
[####################] - 2m     15626/15626   131/s   http://jewel.uploadvulns.thm/content/                                                                                                                                                                 
┌──(kali㉿kali)-[~/shells]
└─$ feroxbuster -u http://jewel.uploadvulns.thm/content/ -w 3letters.txt -x jpg
```

After upload
```
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://jewel.uploadvulns.thm/content/
 🚀  Threads               │ 50
 📖  Wordlist              │ 3letters.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💲  Extensions            │ [jpg]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       20l       58w      844c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
200      GET       12l       34w      382c http://jewel.uploadvulns.thm/content/LBB.jpg
200      GET     1854l    10634w   798455c http://jewel.uploadvulns.thm/content/LKQ.jpg
200      GET      853l     5271w   446639c http://jewel.uploadvulns.thm/content/SAD.jpg
200      GET     1694l     8202w   611152c http://jewel.uploadvulns.thm/content/UAD.jpg
200      GET       13l       35w      395c http://jewel.uploadvulns.thm/content/UKD.jpg
200      GET       12l       34w      382c http://jewel.uploadvulns.thm/content/XBE.jpg
[####################] - 6m     15634/15634   0s      found:6       errors:0      
[####################] - 6m     15626/15626   43/s    http://jewel.uploadvulns.thm/content/ 
```
