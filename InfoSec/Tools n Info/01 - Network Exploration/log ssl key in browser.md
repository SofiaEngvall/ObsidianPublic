
https://tryhackme.com/r/room/networkingsecureprotocols

set the browser to log the session’s TLS keys so we can take a closer look at the traffic using Wireshark. This logging was achieved by adding an extra option to the browser shortcut. Executing `chromium --ssl-key-log-file=~/ssl-key.log` dumps the TLS keys to the `ssl-key.log` file.

capture traffic with wireshark

