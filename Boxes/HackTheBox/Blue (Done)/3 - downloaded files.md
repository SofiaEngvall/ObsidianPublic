
```sh
┌──(kali㉿proxli)-[~/boxes/htb/blue]
└─$ ls -laR *
-rw-r--r--  1 kali kali  174 May  6 16:14 desktop.ini

Default:
total 1584
drwxrwxr-x 12 kali kali   4096 May  6 16:14  .
drwxrwxr-x  4 kali kali   4096 May  6 16:14  ..
drwxrwxr-x  4 kali kali   4096 May  6 16:14  AppData
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Desktop
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Documents
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Downloads
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Favorites
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Links
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Music
-rw-r--r--  1 kali kali 262144 May  6 16:14  NTUSER.DAT
-rw-r--r--  1 kali kali  65536 May  6 16:14  NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
-rw-r--r--  1 kali kali 524288 May  6 16:14  NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
-rw-r--r--  1 kali kali 524288 May  6 16:14  NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
-rw-r--r--  1 kali kali   1024 May  6 16:14  NTUSER.DAT.LOG
-rw-r--r--  1 kali kali 189440 May  6 16:14  NTUSER.DAT.LOG1
-rw-r--r--  1 kali kali      0 May  6 16:14  NTUSER.DAT.LOG2
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Pictures
drwxrwxr-x  2 kali kali   4096 May  6 16:14 'Saved Games'
drwxrwxr-x  2 kali kali   4096 May  6 16:14  Videos

Default/AppData:
total 16
drwxrwxr-x  4 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..
drwxrwxr-x  4 kali kali 4096 May  6 16:14 Local
drwxrwxr-x  4 kali kali 4096 May  6 16:14 Roaming

Default/AppData/Local:
total 16
drwxrwxr-x 4 kali kali 4096 May  6 16:14 .
drwxrwxr-x 4 kali kali 4096 May  6 16:14 ..
drwxrwxr-x 3 kali kali 4096 May  6 16:14 Microsoft
drwxrwxr-x 2 kali kali 4096 May  6 16:14 Temp

Default/AppData/Local/Microsoft:
total 12
drwxrwxr-x 3 kali kali 4096 May  6 16:14 .
drwxrwxr-x 4 kali kali 4096 May  6 16:14 ..
drwxrwxr-x 5 kali kali 4096 May  6 16:14 Windows

Default/AppData/Local/Microsoft/Windows:
total 20
drwxrwxr-x 5 kali kali 4096 May  6 16:14  .
drwxrwxr-x 3 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 2 kali kali 4096 May  6 16:14  GameExplorer
drwxrwxr-x 2 kali kali 4096 May  6 16:14  History
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'Temporary Internet Files'

Default/AppData/Local/Microsoft/Windows/GameExplorer:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 5 kali kali 4096 May  6 16:14 ..

Default/AppData/Local/Microsoft/Windows/History:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 5 kali kali 4096 May  6 16:14 ..

'Default/AppData/Local/Microsoft/Windows/Temporary Internet Files':
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 5 kali kali 4096 May  6 16:14 ..

Default/AppData/Local/Temp:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 4 kali kali 4096 May  6 16:14 ..

Default/AppData/Roaming:
total 16
drwxrwxr-x 4 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'Media Center Programs'
drwxrwxr-x 4 kali kali 4096 May  6 16:14  Microsoft

'Default/AppData/Roaming/Media Center Programs':
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 4 kali kali 4096 May  6 16:14 ..

Default/AppData/Roaming/Microsoft:
total 16
drwxrwxr-x 4 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 3 kali kali 4096 May  6 16:14 'Internet Explorer'
drwxrwxr-x 9 kali kali 4096 May  6 16:14  Windows

'Default/AppData/Roaming/Microsoft/Internet Explorer':
total 12
drwxrwxr-x 3 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'Quick Launch'

'Default/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch':
total 20
drwxrwxr-x 2 kali kali 4096 May  6 16:14  .
drwxrwxr-x 3 kali kali 4096 May  6 16:14  ..
-rw-r--r-- 1 kali kali  146 May  6 16:14  desktop.ini
-rw-r--r-- 1 kali kali  290 May  6 16:14 'Shows Desktop.lnk'
-rw-r--r-- 1 kali kali  272 May  6 16:14 'Window Switcher.lnk'

Default/AppData/Roaming/Microsoft/Windows:
total 36
drwxrwxr-x 9 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 2 kali kali 4096 May  6 16:14  Cookies
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'Network Shortcuts'
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'Printer Shortcuts'
drwxrwxr-x 2 kali kali 4096 May  6 16:14  Recent
drwxrwxr-x 2 kali kali 4096 May  6 16:14  SendTo
drwxrwxr-x 3 kali kali 4096 May  6 16:14 'Start Menu'
drwxrwxr-x 2 kali kali 4096 May  6 16:14  Templates

Default/AppData/Roaming/Microsoft/Windows/Cookies:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..

'Default/AppData/Roaming/Microsoft/Windows/Network Shortcuts':
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..

'Default/AppData/Roaming/Microsoft/Windows/Printer Shortcuts':
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..

Default/AppData/Roaming/Microsoft/Windows/Recent:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..

Default/AppData/Roaming/Microsoft/Windows/SendTo:
total 28
drwxrwxr-x 2 kali kali 4096 May  6 16:14  .
drwxrwxr-x 9 kali kali 4096 May  6 16:14  ..
-rw-r--r-- 1 kali kali    3 May  6 16:14 'Compressed (zipped) Folder.ZFSendToTarget'
-rw-r--r-- 1 kali kali    7 May  6 16:14 'Desktop (create shortcut).DeskLink'
-rw-r--r-- 1 kali kali  558 May  6 16:14  Desktop.ini
-rw-r--r-- 1 kali kali 1238 May  6 16:14 'Fax Recipient.lnk'
-rw-r--r-- 1 kali kali    4 May  6 16:14 'Mail Recipient.MAPIMail'

'Default/AppData/Roaming/Microsoft/Windows/Start Menu':
total 12
drwxrwxr-x 3 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..
drwxrwxr-x 4 kali kali 4096 May  6 16:14 Programs

'Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs':
total 16
drwxrwxr-x 4 kali kali 4096 May  6 16:14 .
drwxrwxr-x 3 kali kali 4096 May  6 16:14 ..
drwxrwxr-x 4 kali kali 4096 May  6 16:14 Accessories
drwxrwxr-x 2 kali kali 4096 May  6 16:14 Maintenance

'Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories':
total 36
drwxrwxr-x 4 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
drwxrwxr-x 2 kali kali 4096 May  6 16:14  Accessibility
-rw-r--r-- 1 kali kali 1280 May  6 16:14 'Command Prompt.lnk'
-rw-r--r-- 1 kali kali  678 May  6 16:14  Desktop.ini
-rw-r--r-- 1 kali kali 1304 May  6 16:14  Notepad.lnk
-rw-r--r-- 1 kali kali  262 May  6 16:14  Run.lnk
drwxrwxr-x 2 kali kali 4096 May  6 16:14 'System Tools'
-rw-r--r-- 1 kali kali 1228 May  6 16:14 'Windows Explorer.lnk'

'Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Accessibility':
total 28
drwxrwxr-x 2 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
-rw-r--r-- 1 kali kali  704 May  6 16:14  Desktop.ini
-rw-r--r-- 1 kali kali 1358 May  6 16:14 'Ease of Access.lnk'
-rw-r--r-- 1 kali kali 1258 May  6 16:14  Magnify.lnk
-rw-r--r-- 1 kali kali 1262 May  6 16:14  Narrator.lnk
-rw-r--r-- 1 kali kali 1250 May  6 16:14 'On-Screen Keyboard.lnk'

'Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/System Tools':
total 24
drwxrwxr-x 2 kali kali 4096 May  6 16:14  .
drwxrwxr-x 4 kali kali 4096 May  6 16:14  ..
-rw-r--r-- 1 kali kali  262 May  6 16:14  computer.lnk
-rw-r--r-- 1 kali kali  262 May  6 16:14 'Control Panel.lnk'
-rw-r--r-- 1 kali kali  592 May  6 16:14  Desktop.ini
-rw-r--r-- 1 kali kali 1306 May  6 16:14 'Private Character Editor.lnk'

'Default/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Maintenance':
total 16
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 4 kali kali 4096 May  6 16:14 ..
-rw-r--r-- 1 kali kali  318 May  6 16:14 Desktop.ini
-rw-r--r-- 1 kali kali  262 May  6 16:14 Help.lnk

Default/AppData/Roaming/Microsoft/Windows/Templates:
total 8
drwxrwxr-x 2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 9 kali kali 4096 May  6 16:14 ..

Default/Desktop:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Documents:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Downloads:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Favorites:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Links:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Music:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Pictures:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

'Default/Saved Games':
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Default/Videos:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 12 kali kali 4096 May  6 16:14 ..

Public:
total 44
drwxrwxr-x 10 kali kali 4096 May  6 16:14  .
drwxrwxr-x  4 kali kali 4096 May  6 16:14  ..
-rw-r--r--  1 kali kali  174 May  6 16:14  desktop.ini
drwxrwxr-x  2 kali kali 4096 May  6 16:14  Documents
drwxrwxr-x  2 kali kali 4096 May  6 16:14  Downloads
drwxrwxr-x  2 kali kali 4096 May  6 16:05  Favorites
drwxrwxr-x  2 kali kali 4096 May  6 16:14  Libraries
drwxrwxr-x  3 kali kali 4096 May  6 16:14  Music
drwxrwxr-x  3 kali kali 4096 May  6 16:14  Pictures
drwxrwxr-x  3 kali kali 4096 May  6 16:14 'Recorded TV'
drwxrwxr-x  3 kali kali 4096 May  6 16:14  Videos

Public/Documents:
total 12
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 10 kali kali 4096 May  6 16:14 ..
-rw-r--r--  1 kali kali  278 May  6 16:14 desktop.ini

Public/Downloads:
total 12
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 10 kali kali 4096 May  6 16:14 ..
-rw-r--r--  1 kali kali  174 May  6 16:14 desktop.ini

Public/Favorites:
total 8
drwxrwxr-x  2 kali kali 4096 May  6 16:05 .
drwxrwxr-x 10 kali kali 4096 May  6 16:14 ..

Public/Libraries:
total 16
drwxrwxr-x  2 kali kali 4096 May  6 16:14 .
drwxrwxr-x 10 kali kali 4096 May  6 16:14 ..
-rw-r--r--  1 kali kali   88 May  6 16:14 desktop.ini
-rw-r--r--  1 kali kali  876 May  6 16:14 RecordedTV.library-ms

Public/Music:
total 16
drwxrwxr-x  3 kali kali 4096 May  6 16:14  .
drwxrwxr-x 10 kali kali 4096 May  6 16:14  ..
-rw-r--r--  1 kali kali  380 May  6 16:14  desktop.ini
drwxrwxr-x  2 kali kali 4096 May  6 16:14 'Sample Music'

'Public/Music/Sample Music':
total 16984
drwxrwxr-x 2 kali kali    4096 May  6 16:14  .
drwxrwxr-x 3 kali kali    4096 May  6 16:14  ..
-rw-r--r-- 1 kali kali     586 May  6 16:14  desktop.ini
-rw-r--r-- 1 kali kali 8414449 May  6 16:14  Kalimba.mp3
-rw-r--r-- 1 kali kali 4113874 May  6 16:14 'Maid with the Flaxen Hair.mp3'
-rw-r--r-- 1 kali kali 4842585 May  6 16:14 'Sleep Away.mp3'

Public/Pictures:
total 16
drwxrwxr-x  3 kali kali 4096 May  6 16:14  .
drwxrwxr-x 10 kali kali 4096 May  6 16:14  ..
-rw-r--r--  1 kali kali  380 May  6 16:14  desktop.ini
drwxrwxr-x  2 kali kali 4096 May  6 16:14 'Sample Pictures'

'Public/Pictures/Sample Pictures':
total 5728
drwxrwxr-x 2 kali kali   4096 May  6 16:14 .
drwxrwxr-x 3 kali kali   4096 May  6 16:14 ..
-rw-r--r-- 1 kali kali 879394 May  6 16:14 Chrysanthemum.jpg
-rw-r--r-- 1 kali kali 845941 May  6 16:14 Desert.jpg
-rw-r--r-- 1 kali kali   1120 May  6 16:14 desktop.ini
-rw-r--r-- 1 kali kali 595284 May  6 16:14 Hydrangeas.jpg
-rw-r--r-- 1 kali kali 775702 May  6 16:14 Jellyfish.jpg
-rw-r--r-- 1 kali kali 780831 May  6 16:14 Koala.jpg
-rw-r--r-- 1 kali kali 561276 May  6 16:14 Lighthouse.jpg
-rw-r--r-- 1 kali kali 777835 May  6 16:14 Penguins.jpg
-rw-r--r-- 1 kali kali 620888 May  6 16:14 Tulips.jpg

'Public/Recorded TV':
total 16
drwxrwxr-x  3 kali kali 4096 May  6 16:14  .
drwxrwxr-x 10 kali kali 4096 May  6 16:14  ..
-rw-r--r--  1 kali kali   80 May  6 16:14  desktop.ini
drwxrwxr-x  2 kali kali 4096 May  6 16:14 'Sample Media'

'Public/Recorded TV/Sample Media':
total 9484
drwxrwxr-x 2 kali kali    4096 May  6 16:14 .
drwxrwxr-x 3 kali kali    4096 May  6 16:14 ..
-rw-r--r-- 1 kali kali     171 May  6 16:14 desktop.ini
-rw-r--r-- 1 kali kali 9699328 May  6 16:14 win7_scenic-demoshort_raw.wtv

Public/Videos:
total 16
drwxrwxr-x  3 kali kali 4096 May  6 16:14  .
drwxrwxr-x 10 kali kali 4096 May  6 16:14  ..
-rw-r--r--  1 kali kali  380 May  6 16:14  desktop.ini
drwxrwxr-x  2 kali kali 4096 May  6 16:14 'Sample Videos'

'Public/Videos/Sample Videos':
total 25644
drwxrwxr-x 2 kali kali     4096 May  6 16:14 .
drwxrwxr-x 3 kali kali     4096 May  6 16:14 ..
-rw-r--r-- 1 kali kali      326 May  6 16:14 desktop.ini
-rw-r--r-- 1 kali kali 26246026 May  6 16:14 Wildlife.wmv

```