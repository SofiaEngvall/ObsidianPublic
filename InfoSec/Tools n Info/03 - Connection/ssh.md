

`ssh user@10.10.147.146`
`ssh -oHostKeyAlgorithms=+ssh-rsa user@10.10.147.146`
`ssh -i key-filename root@10.10.221.227`

If we find a ssh key on a box, after saving it locally, do:
`chmod 600 filename`

if the key is old you might need options:
`ssh -i key-filename -oPubkeyAcceptedKeyTypes=+ssh-rsa -oHostKeyAlgorithms=+ssh-rsa root@10.10.221.227`

### ssh tunneling

`ssh -L 9000:imgur.com:80 user@example.com`

-L is a local tunnel (YOU <-- CLIENT)
-R is a remote tunnel (YOU --> CLIENT)

if a port (10000) is blocked (in firewall..) we can access it through a ssh tunnel
`ssh -L 10000:localhost:10000 <username>@<ip>`


![[images/ssh-tunneling.png]]
then web go to localhost:8080



ssh sau@10.10.11.214 -L 8000:127.0.0.1:8000

ssh sau@10.10.11.214 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null

###### ssh usage

```sh
┌──(kali㉿kali)-[~]
└─$ ssh   
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command [argument ...]]

```

