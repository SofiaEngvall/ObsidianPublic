
feroxbuster on real assessment
fire and forget, it works alone
use like gobuster but recursive!

gobuster dir ...

cms = content management system - easy way to make websites

wpscan --url  http:address... -e u ,vp
vpvuln plugins
ap all plugins

easy to get list of usernames

look for usernames
plugins

start brute force of users since it takes time
wpscan --url ... -U user  -p 

google  plugins

google wordpress social warfare exploit
found RCE with python script 2019-
RFI remote file inclusion

make file
host file
load with special link  from rce

find bash  tcp  rev shell cheat sheet

start ncat

connect yay

upg shell

-
db stuff,  I missed a bit, making food for laban
-

mariadb wp users  table

john with  data

meanwhile looking at dirs
found rsa key for max
chmod and then ssh

ssh -i max_rsa  max@ip

sudo -l

look at running service

gtfobins.github.io/gtfobins/service/#shell

sudo the service /bin/sh

got to steven

sudo -l again

/opt/tools/server-health.sh

make  script

#!/bin/bash
mkdir /root/
cp /home/max/.ssh... /root/.ssh/....

or /bin/bash -p

chmod

-------

moneybox

missed a bit making food
ftp
image

sudo apt install  steghide

steghide --help

steghide extract -sf try.jpg
binwalk
exiftool
strings

check website
gobuster

found webpage from gobuster
link to other
found key to steghide
data put in txt file
username renu has bad passwd

hydra renu, got passwd 987654321

ssh

sudo -l
no sudo stuff

bash hist
lily use the same ssh key as renu

ssh as lily
sudo -l
can run perl!!
look in gtfobins

root shell











