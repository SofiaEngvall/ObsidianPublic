
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir -r -u http://monitorsthree.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -e 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://monitorsthree.htb
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://monitorsthree.htb/images               (Status: 403) [Size: 162]
http://monitorsthree.htb/admin                (Status: 403) [Size: 162]
http://monitorsthree.htb/css                  (Status: 403) [Size: 162]
http://monitorsthree.htb/js                   (Status: 403) [Size: 162]
http://monitorsthree.htb/fonts                (Status: 403) [Size: 162]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ feroxbuster -u http://monitorsthree.htb -E                           
                                                                                                                              
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.4
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://monitorsthree.htb
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.4
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💰  Collect Extensions    │ true
 💸  Ignored Extensions    │ [Images, Movies, Audio, etc...]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        7l       12w      162c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                     
301      GET        7l       12w      178c http://monitorsthree.htb/images => http://monitorsthree.htb/images/
301      GET        7l       12w      178c http://monitorsthree.htb/admin => http://monitorsthree.htb/admin/
301      GET        7l       12w      178c http://monitorsthree.htb/css => http://monitorsthree.htb/css/
301      GET        7l       12w      178c http://monitorsthree.htb/js => http://monitorsthree.htb/js/
301      GET        7l       12w      178c http://monitorsthree.htb/images/blog => http://monitorsthree.htb/images/blog/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets => http://monitorsthree.htb/admin/assets/
301      GET        7l       12w      178c http://monitorsthree.htb/fonts => http://monitorsthree.htb/fonts/
301      GET        7l       12w      178c http://monitorsthree.htb/images/services => http://monitorsthree.htb/images/services/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/images => http://monitorsthree.htb/admin/assets/images/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/css => http://monitorsthree.htb/admin/assets/css/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js => http://monitorsthree.htb/admin/assets/js/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js/plugins => http://monitorsthree.htb/admin/assets/js/plugins/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/swf => http://monitorsthree.htb/admin/assets/swf/
200      GET       71l      130w     1872c http://monitorsthree.htb/js/custom.js
200      GET        9l       43w     3028c http://monitorsthree.htb/images/services/03.png
200      GET       38l      117w     2813c http://monitorsthree.htb/js/plugins.js
200      GET       11l       15w      188c http://monitorsthree.htb/css/plugins.css
200      GET        5l       30w     1616c http://monitorsthree.htb/images/services/01.png
200      GET        6l       34w     2166c http://monitorsthree.htb/images/services/02.png
200      GET       19l       62w     3695c http://monitorsthree.htb/images/services/04.png
200      GET       24l       99w      770c http://monitorsthree.htb/js/smoothscroll.js
200      GET        1l      235w    12063c http://monitorsthree.htb/images/review.svg
200      GET        5l      369w    21003c http://monitorsthree.htb/js/popper.min.js
200      GET      935l     1752w    15174c http://monitorsthree.htb/css/style.css
200      GET      109l      619w    13655c http://monitorsthree.htb/images/service.svg
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js/pages => http://monitorsthree.htb/admin/assets/js/pages/
200      GET        1l      359w    22207c http://monitorsthree.htb/images/banner.svg
200      GET        7l      277w    44342c http://monitorsthree.htb/js/owl.carousel.min.js
200      GET        4l     1293w    86709c http://monitorsthree.htb/js/jquery-min.js
200      GET        1l      393w    15974c http://monitorsthree.htb/images/about-us.svg
200      GET       87l     1326w   157954c http://monitorsthree.htb/admin/assets/images/logo.ico
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js/core => http://monitorsthree.htb/admin/assets/js/core/
200      GET        7l      683w    60010c http://monitorsthree.htb/js/bootstrap.min.js
200      GET      175l     1248w    89112c http://monitorsthree.htb/admin/assets/images/logo.png
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/css/extras => http://monitorsthree.htb/admin/assets/css/extras/
200      GET       96l      239w     4252c http://monitorsthree.htb/login.php
200      GET      338l      982w    13560c http://monitorsthree.htb/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/css/icons => http://monitorsthree.htb/admin/assets/css/icons/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js/maps => http://monitorsthree.htb/admin/assets/js/maps/
302      GET        0l        0w        0c http://monitorsthree.htb/admin/dashboard.php => http://monitorsthree.htb/login.php
200      GET       20l       36w      303c http://monitorsthree.htb/admin/footer.php
302      GET        0l        0w        0c http://monitorsthree.htb/admin/customers.php => http://monitorsthree.htb/login.php
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/js/charts => http://monitorsthree.htb/admin/assets/js/charts/
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/images/flags => http://monitorsthree.htb/admin/assets/images/flags/
302      GET        0l        0w        0c http://monitorsthree.htb/admin/invoices.php => http://monitorsthree.htb/login.php
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/images/ui => http://monitorsthree.htb/admin/assets/images/ui/
302      GET        0l        0w        0c http://monitorsthree.htb/admin/tasks.php => http://monitorsthree.htb/login.php
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/images/backgrounds => http://monitorsthree.htb/admin/assets/images/backgrounds/
200      GET      306l      960w    11647c http://monitorsthree.htb/css/css2
301      GET        7l       12w      178c http://monitorsthree.htb/admin/assets/locales => http://monitorsthree.htb/admin/assets/locales/
200      GET      607l     1130w    16986c http://monitorsthree.htb/admin/assets/js/core/app.js
200      GET        2l      210w    12507c http://monitorsthree.htb/admin/assets/js/plugins/loaders/pace.min.js
200      GET        1l        1w    37820c http://monitorsthree.htb/admin/assets/css/minified/colors.min.css
200      GET        6l      184w     9227c http://monitorsthree.htb/admin/assets/js/plugins/loaders/blockui.min.js
200      GET        1l     5059w   256503c http://monitorsthree.htb/admin/assets/css/minified/components.min.css
200      GET        7l      430w    36816c http://monitorsthree.htb/admin/assets/js/core/libraries/bootstrap.min.js
200      GET        1l     1399w   107850c http://monitorsthree.htb/admin/assets/css/minified/core.min.css
200      GET        4l     1305w    84345c http://monitorsthree.htb/admin/assets/js/core/libraries/jquery.min.js
200      GET     1190l     1226w    47483c http://monitorsthree.htb/admin/assets/css/icons/icomoon/styles.css
200      GET        1l     1733w   122310c http://monitorsthree.htb/admin/assets/css/minified/bootstrap.min.css
200      GET       85l      212w     3030c http://monitorsthree.htb/forgot_password.php
200      GET      328l      984w     8383c http://monitorsthree.htb/admin/assets/js/plugins/visualization/d3/d3_tooltip.js
200      GET        7l      820w    35415c http://monitorsthree.htb/admin/assets/js/plugins/ui/moment/moment.min.js
200      GET        1l      313w    24437c http://monitorsthree.htb/admin/assets/js/plugins/forms/styling/switchery.min.js
200      GET        7l       36w      547c http://monitorsthree.htb/admin/assets/js/plugins/ui/headroom/headroom_jquery.min.js
200      GET       80l      166w     2101c http://monitorsthree.htb/admin/assets/js/pages/datatables_basic.js
200      GET       38l       98w     1167c http://monitorsthree.htb/admin/assets/js/pages/layout_navbar_hideable_sidebar.js
200      GET       98l      179w     2428c http://monitorsthree.htb/admin/assets/js/pages/layout_fixed_custom.js
200      GET        7l       78w     4317c http://monitorsthree.htb/admin/assets/js/plugins/ui/headroom/headroom.min.js
200      GET        1l      140w     8308c http://monitorsthree.htb/admin/assets/js/plugins/forms/styling/uniform.min.js
200      GET        5l     2891w   151143c http://monitorsthree.htb/admin/assets/js/plugins/visualization/d3/d3.min.js
200      GET       22l      743w    64569c http://monitorsthree.htb/admin/assets/js/plugins/forms/selects/select2.min.js
200      GET      118l      550w    60168c http://monitorsthree.htb/admin/assets/js/plugins/ui/nicescroll.min.js
200      GET     1416l     3843w    54619c http://monitorsthree.htb/admin/assets/js/plugins/forms/selects/bootstrap_multiselect.js
200      GET     1443l     4515w    60257c http://monitorsthree.htb/admin/assets/js/plugins/pickers/daterangepicker.js
200      GET      163l     1141w    80864c http://monitorsthree.htb/admin/assets/js/plugins/tables/datatables/datatables.min.js
200      GET      144l      370w     6248c http://monitorsthree.htb/admin/navbar.php
302      GET        0l        0w        0c http://monitorsthree.htb/admin/changelog.php => http://monitorsthree.htb/login.php
[####################] - 4m   1639749/1639749 0s      found:78      errors:36     
[####################] - 4m    118343/118343  545/s   http://monitorsthree.htb/ 
[####################] - 4m    118717/118717  557/s   http://monitorsthree.htb/images/ 
[####################] - 4m    118623/118623  557/s   http://monitorsthree.htb/admin/ 
[####################] - 4m    119336/119336  554/s   http://monitorsthree.htb/css/ 
[####################] - 4m    118765/118765  551/s   http://monitorsthree.htb/js/ 
[####################] - 4m    119210/119210  553/s   http://monitorsthree.htb/images/blog/ 
[####################] - 4m    119234/119234  553/s   http://monitorsthree.htb/admin/assets/ 
[####################] - 4m    119408/119408  555/s   http://monitorsthree.htb/fonts/ 
[####################] - 4m    119474/119474  553/s   http://monitorsthree.htb/images/services/ 
[####################] - 4m    119442/119442  552/s   http://monitorsthree.htb/admin/assets/images/ 
[####################] - 4m    119578/119578  555/s   http://monitorsthree.htb/admin/assets/css/ 
[####################] - 4m    119560/119560  553/s   http://monitorsthree.htb/admin/assets/js/ 
[####################] - 4m    119860/119860  556/s   http://monitorsthree.htb/admin/assets/swf/ 
[####################] - 3m     60000/60000   287/s   http://monitorsthree.htb/admin/assets/locales/                          
```