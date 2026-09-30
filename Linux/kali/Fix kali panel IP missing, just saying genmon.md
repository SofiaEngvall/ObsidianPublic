
Right click the text or if you can't find it at all, right click the panel, select `Panel`, `Panel Preferences`, `Items` and double click `Generic Monitor`. This is where the command that's run to get the ip is located. (Earlier removing the checkmark by Label helped too.)

The default command should be running `/usr/share/kali-themes/xfce4-panel-genmon-vpnip.sh`.

Edit this file or replace it in a way that updates at boot - so it's not reset when updating kali.

Let's make it easy to redo this by butting a script with the fix in our user folder that we can run if the ip disappears:

fix-panel-ip.sh
```sh
#!/bin/bash
sudo sh -c "cat > /usr/share/kali-themes/xfce4-panel-genmon-vpnip.sh" << 'EOF'
#!/bin/bash
IP=$(ip addr show tun0 2>/dev/null | grep -oP "(?<=inet )[0-9.]+")
if [ -z "$IP" ]; then
    IP=$(ip route get 1.1.1.1 2>/dev/null | awk '{print $7}')
fi
if [ -n "$IP" ]; then
    echo "<txt>$IP</txt>"
else
    echo "<txt>No Net</txt>"
fi
EOF
```

don't forget to run `chmod +x` on the file

Old file contents 2026-09-25:
```sh
#!/bin/sh

interface="$1"

[ -z "$interface" ] && interface="$(ip tuntap show | cut -d : -f1 | head -n 1)"
ip="$(ip addr show "${interface}" 2>/dev/null \
        | grep -o -P '(?<=inet )[0-9]{1,3}(\.[0-9]{1,3}){3}')"

if [ "${ip}" != "" ]; then
  printf "<icon>network-vpn-symbolic</icon>"
  printf "<txt>${ip}</txt>"
  if command -v xclip; then
    printf "<iconclick>sh -c 'printf ${ip} | xclip -selection clipboard'</iconclick>"
    printf "<txtclick>sh -c 'printf ${ip} | xclip -selection clipboard'</txtclick>"
    printf "<tool>VPN IP (click to copy)</tool>"
  else
    printf "<tool>VPN IP (install xclip to copy to clipboard)</tool>"
  fi
else
  printf "<txt></txt>"
fi

```
