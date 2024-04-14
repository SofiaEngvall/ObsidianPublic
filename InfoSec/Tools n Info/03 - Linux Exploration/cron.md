
users cron jobs files `/var/spool/cron/crontabs`
system-wide jobs `/etc/crontab` file or `/etc/cron.*`
system daemons and applications `/etc/cron.d/`


`crontab -l` lists jobs for active user
`cat /etc/crontab` list system wide jobs


scripts can be placed in dirs to be auto run
`/etc/cron.hourly/`
`/etc/cron.daily/`
`/etc/cron.weekly/`
`/etc/cron.monthly/`


`sudo crontab -l -u username` list crontab for other user
`ls /var/spool/cron/crontabs/` lists user crontab files


`ls -l /etc/cron.d/` contains files with crontab format added by software


`/etc/cron.allow` and `/etc/cron.deny` limits user access to cron jobs


`at` is similar to cron but a job is just run once.
`atq` checks at jobs

`systemctl list-timers` list timers and cron jobs managed by systemd

`/var/log/crno.log` and other logfiles like syslog and secure can be checked to see if jobs have logged their activity

email reports?

search for scripts containing cron jobs:
```bash
find /etc -type f -name "*.sh" -exec grep -i "cron" {} \;
```

files mentioning cron
```bash
grep -r "cron" /path/to/search
```

