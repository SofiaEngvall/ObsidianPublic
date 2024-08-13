
10.10.115.97
10.10.178.241
10.10.23.44

22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))

Gobuster found:
Wordpress on: http://internal.thm/blog
phpmyadmin logon at: http://internal.thm/phpmyadmin
wp admin logon at: http://internal.thm/blog/wp-admin

wpscan found no vulns, no plugins installed..

on the web page we found an article written by "admin"

wpscan password bruteforce of admin found
Username: admin, Password: my2boys

on webpage when logged in:
william:arnold147

we got shell by changing one of the theme php files
http://internal.thm/blog/wp-admin/theme-editor.php?file=index.php&theme=twentyseventeen
http://internal.thm/blog/wp-content/themes/twentyseventeen/index.php

in /opt/wp-save.txt we found
aubreanna:bubb13guM!@#123

Internal Jenkins service is running on 172.17.0.2:8080

in /opt/note.txt
root:tr0ub13guM!@#123

we had to stabilize the shell with python, not python3

THM{d0ck3r_d3str0y3r}