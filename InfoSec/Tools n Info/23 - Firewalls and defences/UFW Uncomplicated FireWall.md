
### help
```sh
vantwinkle@ip-10-10-241-43:~$ ufw --help

Usage: ufw COMMAND

Commands:
 enable                          enables the firewall
 disable                         disables the firewall
 default ARG                     set default policy
 logging LEVEL                   set logging to LEVEL
 allow ARGS                      add allow rule
 deny ARGS                       add deny rule
 reject ARGS                     add reject rule
 limit ARGS                      add limit rule
 delete RULE|NUM                 delete RULE
 insert NUM RULE                 insert RULE at NUM
 route RULE                      add route RULE
 route delete RULE|NUM           delete route RULE
 route insert NUM RULE           insert route RULE at NUM
 reload                          reload firewall
 reset                           reset firewall
 status                          show firewall status
 status numbered                 show firewall status as numbered list of RULES
 status verbose                  show verbose firewall status
 show ARG                        show firewall report
 version                         display version information

Application profile commands:
 app list                        list application profiles
 app info PROFILE                show information on PROFILE
 app update PROFILE              update PROFILE
 app default ARG                 set default application policy
```

### whatever

`sudo ufw status`

`sudo ufw default allow outgoing`

`sudo ufw default deny incoming`

```sh
vantwinkle@ip-10-10-241-43:~$ sudo ufw status
[sudo] password for vantwinkle: 
Status: inactive
vantwinkle@ip-10-10-241-43:~$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
vantwinkle@ip-10-10-241-43:~$ sudo ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
vantwinkle@ip-10-10-241-43:~$ 
```

example rules
`sudo ufw allow 22/tcp`
`sudo ufw deny from 192.168.100.25`
`sudo ufw deny in on eth0 from 192.168.100.26`

Enabling
`sudo ufw enable`

`sudo ufw status verbose`


