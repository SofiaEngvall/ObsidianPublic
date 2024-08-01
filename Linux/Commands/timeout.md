
`timeout [OPTIONS] DURATION COMMAND [ARG]…`

suffix:
`s` - seconds (default)
`m` - minutes
`h` - hours
`d` - days

`timeout 5 ping 8.8.8.8` (default 5s)
`timeout 5m ping 8.8.8.8`

`timeout 1m ./pspy64`

Sending Specific Signal
`sudo timeout -s SIGKILL ping 8.8.8.8`
`sudo timeout -s 9 ping 8.8.8.8`
list signals with `kill -l`

