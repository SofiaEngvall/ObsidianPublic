
https://tryhackme.com/r/room/adventofcyber2024 day 19

```sh
ubuntu@tryhackme:~$ ls -la
total 144
drwxr-xr-x 23 ubuntu ubuntu  4096 Dec 29 18:14 .
drwxr-xr-x  3 root   root    4096 Feb 27  2022 ..
-rw-------  1 ubuntu ubuntu   774 Dec 29 18:14 .Xauthority
lrwxrwxrwx  1 ubuntu ubuntu     9 Feb 27  2022 .bash_history -> /dev/null
-rw-r--r--  1 ubuntu ubuntu   220 Feb 25  2020 .bash_logout
-rw-r--r--  1 ubuntu ubuntu  3771 Feb 25  2020 .bashrc
drwx------ 19 ubuntu ubuntu  4096 Dec 29 18:14 .cache
drwx------ 27 ubuntu ubuntu  4096 Dec 19 07:23 .config
drwx------  3 ubuntu ubuntu  4096 Feb 27  2022 .dbus
drwx------  3 ubuntu ubuntu  4096 Feb 27  2022 .gnupg
drwxrwxr-x  2 ubuntu ubuntu  4096 Feb 27  2022 .icons
-rw-------  1 ubuntu ubuntu    36 Nov 27 18:27 .lesshst
drwx------  7 ubuntu ubuntu  4096 Oct 15 16:02 .local
drwx------  4 ubuntu ubuntu  4096 Feb 27  2022 .mozilla
drwx------  3 ubuntu ubuntu  4096 Oct 31 19:36 .pki
-rw-r--r--  1 ubuntu ubuntu   807 Feb 25  2020 .profile
-rw-rw-r--  1 ubuntu ubuntu    66 Feb 27  2022 .selected_editor
drwx------  2 ubuntu ubuntu  4096 Feb 27  2022 .ssh
-rw-r--r--  1 ubuntu ubuntu     0 Feb 27  2022 .sudo_as_admin_successful
drwxrwxr-x  2 ubuntu ubuntu  4096 Feb 27  2022 .themes
-rw-------  1 ubuntu ubuntu 14229 Dec 19 08:00 .viminfo
drwxr-xr-x  2 ubuntu ubuntu  4096 Dec 29 18:14 .vnc
drwxr-xr-x  4 ubuntu ubuntu  4096 Oct 31 19:36 .vscode
-rw-rw-r--  1 ubuntu ubuntu   161 Feb 27  2022 .wget-hsts
-rw-------  1 ubuntu ubuntu  5833 Feb 27  2022 .xsession-errors
drwxr-xr-x  3 ubuntu ubuntu  4096 Dec 19 08:08 Desktop
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Documents
drwxr-xr-x  2 ubuntu ubuntu  4096 Nov 27 16:52 Downloads
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Music
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Pictures
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Public
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Templates
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Videos
drwx------  3 ubuntu ubuntu  4096 Oct 31 19:36 snap
ubuntu@tryhackme:~$ cd Desktop/
ubuntu@tryhackme:~/Desktop$ ls -la
total 352
drwxr-xr-x  3 ubuntu ubuntu   4096 Dec 19 08:08 .
drwxr-xr-x 23 ubuntu ubuntu   4096 Dec 29 18:14 ..
-rw-r--r--  1 ubuntu ubuntu 344064 Dec 19 08:02 .aocgame.cpp.swp
drwxr-xr-x  4 ubuntu ubuntu   4096 Nov 28 17:00 TryUnlockMe
-rwxrwxr-x  1 ubuntu ubuntu    166 Feb 27  2022 mate-terminal.desktop
ubuntu@tryhackme:~/Desktop$ cd TryUnlockMe/
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ ls -la
total 420
drwxr-xr-x 4 ubuntu ubuntu   4096 Nov 28 17:00 .
drwxr-xr-x 3 ubuntu ubuntu   4096 Dec 19 08:08 ..
-rwxr-xr-x 1 ubuntu ubuntu 412640 Dec 19 08:06 TryUnlockMe
drwxr-xr-x 3 ubuntu ubuntu   4096 Nov 28 17:00 __handlers__
drwxr-xr-x 2 ubuntu ubuntu   4096 Nov 28 14:55 assets
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ cd assets/
ubuntu@tryhackme:~/Desktop/TryUnlockMe/assets$ ls -la
total 1268
drwxr-xr-x 2 ubuntu ubuntu    4096 Nov 28 14:55 .
drwxr-xr-x 4 ubuntu ubuntu    4096 Nov 28 17:00 ..
-rw-rw-r-- 1 ubuntu ubuntu    8668 Nov 27 21:17 1.png
-rw-r--r-- 1 ubuntu ubuntu   10088 Oct 15 01:25 2.png
-rw-rw-r-- 1 ubuntu ubuntu    8673 Nov 27 21:17 3.png
-rw-r--r-- 1 ubuntu ubuntu 1027192 Oct 15 01:25 arial.ttf
-rw-r--r-- 1 ubuntu ubuntu     269 Oct 15 01:25 arrows.png
-rw-r--r-- 1 ubuntu ubuntu     182 Oct 15 01:25 bkspc.png
-rw-r--r-- 1 ubuntu ubuntu   10088 Oct 15 01:25 coin.png
-rw-r--r-- 1 ubuntu ubuntu    2315 Oct 15 01:25 computer_anims.png
-rw-r--r-- 1 ubuntu ubuntu   24886 Nov 22 07:26 controls.png
-rw-r--r-- 1 ubuntu ubuntu    1086 Oct 15 01:25 gocp_anims.png
-rw-r--r-- 1 ubuntu ubuntu   94446 Nov 28 13:52 menu_bg.png
-rw-r--r-- 1 ubuntu ubuntu    3078 Nov 21 15:57 penguin1_anims.png
-rw-r--r-- 1 ubuntu ubuntu    3098 Nov 21 15:57 penguin2_anims.png
-rw-r--r-- 1 ubuntu ubuntu    3150 Nov 21 15:57 penguin3_anims.png
-rw-r--r-- 1 ubuntu ubuntu     980 Nov 22 07:26 player_anims.png
-rw-r--r-- 1 ubuntu ubuntu   10602 Oct 15 01:25 plus1coin.png
-rw-r--r-- 1 ubuntu ubuntu    2829 Oct 15 01:25 return.png
-rw-r--r-- 1 ubuntu ubuntu    8138 Oct 15 01:25 sold.png
-rw-r--r-- 1 ubuntu ubuntu    3004 Oct 15 01:25 space.png
-rw-r--r-- 1 ubuntu ubuntu     153 Oct 15 01:25 tab.png
-rw-r--r-- 1 ubuntu ubuntu    9198 Nov  8 03:28 terrain_ss.png
-rw-r--r-- 1 ubuntu ubuntu    3035 Oct 15 01:25 tree.png
-rw-r--r-- 1 ubuntu ubuntu     528 Oct 15 01:25 yeti_anims.png
ubuntu@tryhackme:~/Desktop/TryUnlockMe/assets$ cd ..
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ ls -la
total 420
drwxr-xr-x 4 ubuntu ubuntu   4096 Nov 28 17:00 .
drwxr-xr-x 3 ubuntu ubuntu   4096 Dec 19 08:08 ..
-rwxr-xr-x 1 ubuntu ubuntu 412640 Dec 19 08:06 TryUnlockMe
drwxr-xr-x 3 ubuntu ubuntu   4096 Nov 28 17:00 __handlers__
drwxr-xr-x 2 ubuntu ubuntu   4096 Nov 28 14:55 assets
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ cd __handlers__/
ubuntu@tryhackme:~/Desktop/TryUnlockMe/__handlers__$ ls -la
total 12
drwxr-xr-x 3 ubuntu ubuntu 4096 Nov 28 17:00 .
drwxr-xr-x 4 ubuntu ubuntu 4096 Nov 28 17:00 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 Nov 28 17:00 libaocgame.so
ubuntu@tryhackme:~/Desktop/TryUnlockMe/__handlers__$ cd libaocgame.so/
ubuntu@tryhackme:~/Desktop/TryUnlockMe/__handlers__/libaocgame.so$ ls -la
total 20
drwxr-xr-x 2 ubuntu ubuntu 4096 Nov 28 17:00 .
drwxr-xr-x 3 ubuntu ubuntu 4096 Nov 28 17:00 ..
-rw-r--r-- 1 ubuntu ubuntu  375 Nov 28 17:00 _Z16check_biometricsPKc.js
-rw-r--r-- 1 ubuntu ubuntu  377 Nov 28 17:00 _Z17validate_purchaseiii.js
-rw-r--r-- 1 ubuntu ubuntu  351 Nov 28 17:00 _Z7set_otpi.js
ubuntu@tryhackme:~/Desktop/TryUnlockMe/__handlers__/libaocgame.so$ cd ..
ubuntu@tryhackme:~/Desktop/TryUnlockMe/__handlers__$ cd ..
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ ls -la
total 420
drwxr-xr-x 4 ubuntu ubuntu   4096 Nov 28 17:00 .
drwxr-xr-x 3 ubuntu ubuntu   4096 Dec 19 08:08 ..
-rwxr-xr-x 1 ubuntu ubuntu 412640 Dec 19 08:06 TryUnlockMe
drwxr-xr-x 3 ubuntu ubuntu   4096 Nov 28 17:00 __handlers__
drwxr-xr-x 2 ubuntu ubuntu   4096 Nov 28 14:55 assets
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ frida-trace ./TryUnlockMe -i 'libaocgame.so!*'
Instrumenting...                                                        
_Z17validate_purchaseiii: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z17validate_purchaseiii.js"
_Z7set_otpi: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z7set_otpi.js"
_Z14create_keycardPKc: Auto-generated handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z14create_keycardPKc.js"
_Z16check_biometricsPKc: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z16check_biometricsPKc.js"
Started tracing 4 functions. Web UI available at http://localhost:1337/ 
           /* TID 0x7d4 */
 40131 ms  _Z7set_otpi()
494422 ms  _Z7set_otpi()
494422 ms  Parameter:415828
539085 ms  _Z7set_otpi()
539085 ms  Parameter:720407
745968 ms  _Z17validate_purchaseiii()
831618 ms  _Z17validate_purchaseiii()
973490 ms  _Z17validate_purchaseiii()
973490 ms  Parameter1:3
973490 ms  Parameter2:1000000
973490 ms  Parameter3:16
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
Warning: Skipping "_Z17validate_purchaseiii": could not parse '/handlers/_Z17validate_purchaseiii.js' line 607: invalid assignment left-hand side
1374468 ms  _Z17validate_purchaseiii()
1374468 ms  Parameter1:2
1374468 ms  Parameter2:10
1374468 ms  Parameter3:16
1403747 ms  _Z17validate_purchaseiii()
1403747 ms  Parameter1:-48
1403747 ms  Parameter2:5
1403747 ms  Parameter3:6
1513853 ms  _Z17validate_purchaseiii()
1655840 ms  _Z16check_biometricsPKc()
1671680 ms  _Z16check_biometricsPKc()
1776167 ms  _Z16check_biometricsPKc()
1776167 ms  Parameter:0x3eb741e0
1831518 ms  _Z16check_biometricsPKc()
1831518 ms  Parameter:0x3ea63ce0
{'type': 'error', 'description': 'TypeError: not a function', 'stack': 'TypeError: not a function\n    at onEnter (/handlers/_Z16check_biometricsPKc.js:11)\n    at call (native)\n    at invokeNativeHandler (agent.ts:541)\n    at onEnter (agent.ts:491)', 'fileName': '/handlers/_Z16check_biometricsPKc.js', 'lineNumber': 11, 'columnNumber': 1}
1960526 ms  _Z16check_biometricsPKc()
2009917 ms  _Z16check_biometricsPKc()
2009917 ms  Parameter:vbjAzlhcamdKf8t75NeHoWlAg8RrzZIsA027jhkJSLb7TSCWprldNXn1dCscl9Ut
2048602 ms  _Z16check_biometricsPKc()
2048602 ms  Parameter:7U1qAj7c4ihXAu3zjpa4KM6xYwXK3zDARCybv5DzlvUtnWsWJRadneYLb3dc2pnR
2157438 ms  _Z16check_biometricsPKc()
2157438 ms  Parameter:1j3vpGuY9NSwtISCj3nUfJqGMRrMGenGNoBA33jCQB7JRZTBaGfGXTUrvLD9xzPJ
2157438 ms  ret val=0x0
2252847 ms  _Z16check_biometricsPKc()
2252847 ms  Parameter:naRqcA12J8KlfnuE2ZSX1uPwEa5BZTSL1u9d28gKGy3ujx6jUWHVQgPeGToowE7x
2252847 ms  ret val=0x0
2252847 ms  new ret val=0x1
2372081 ms  _Z16check_biometricsPKc()
2372081 ms  Parameter:8Gb9PFTdBWVuRbcv7tPWXo8lFuZB9g7FvgOIvpt4JPwiyYe4P1Ywngi3bFEiuLxn
2372081 ms  ret val=0x0
2372081 ms  new ret val=0x1
2423092 ms  _Z7set_otpi()
2423092 ms  Parameter:982091
Process terminated
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ frida-trace ./TryUnlockMe -i 'libaocgame.so!*'
Instrumenting...                                                        
_Z17validate_purchaseiii: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z17validate_purchaseiii.js"
_Z7set_otpi: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z7set_otpi.js"
_Z14create_keycardPKc: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z14create_keycardPKc.js"
_Z16check_biometricsPKc: Loaded handler at "/home/ubuntu/Desktop/TryUnlockMe/__handlers__/libaocgame.so/_Z16check_biometricsPKc.js"
Started tracing 4 functions. Web UI available at http://localhost:1337/ 
           /* TID 0xa52 */
 42692 ms  _Z7set_otpi()
 42692 ms  Parameter:959994
107207 ms  _Z17validate_purchaseiii()
123413 ms  _Z17validate_purchaseiii()
133602 ms  _Z17validate_purchaseiii()
225760 ms  _Z17validate_purchaseiii()
225760 ms  Parameter:3
225760 ms  Parameter:1000000
225760 ms  Parameter:0
Process terminated
ubuntu@tryhackme:~/Desktop/TryUnlockMe$ 
```

read an integer argument value for a function in a library
```js
/*
 * Auto-generated by Frida. Please modify to match the signature of _Z7set_otpi.
 * This stub is currently auto-generated from manpages when available.
 *
 * For full API reference, see: https://frida.re/docs/javascript-api/
 */

defineHandler({
  onEnter(log, args, state) {
    log('_Z7set_otpi()');
    log("Parameter:" + args[0].toInt32());
  },

  onLeave(log, retval, state) {
  }
});
```

edit an integer argument value for a function in a library
```js
/*
 * Auto-generated by Frida. Please modify to match the signature of _Z17validate_purchaseiii.
 * This stub is currently auto-generated from manpages when available.
 *
 * For full API reference, see: https://frida.re/docs/javascript-api/
 */

defineHandler({
  onEnter(log, args, state) {
    log('_Z17validate_purchaseiii()');
    log("Parameter:" + args[0].toInt32());
    log("Parameter:" + args[1].toInt32());
    log("Parameter:" + args[2].toInt32());
    args[2]=ptr(1000000)
    //args[1] = ptr(0)
  },

  onLeave(log, retval, state) {
  }
});
```

read string argument and edit a boolean return value
```js
/*
 * Auto-generated by Frida. Please modify to match the signature of _Z16check_biometricsPKc.
 * This stub is currently auto-generated from manpages when available.
 *
 * For full API reference, see: https://frida.re/docs/javascript-api/
 */

defineHandler({
  onEnter(log, args, state) {
    log('_Z16check_biometricsPKc()');
    log("Parameter:" + Memory.readCString(args[0]));
  },

  onLeave(log, retval, state) {
    log("ret val="+retval);
    retval.replace(ptr(1))
    log("new ret val="+retval);
  }
});

```

