
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

###### useful commands

```sh
ssh ubnt@192.168.0.1
```

ssh tunneling
![[ssh-tunneling.png]]
then web go to localhost:8080



ssh sau@10.10.11.214 -L 8000:127.0.0.1:8000

ssh sau@10.10.11.214 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
