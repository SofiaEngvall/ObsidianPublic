
```sh
#!/bin/bash

port=1234

echo "Listening for bad guys on port $port"

while [ 1 ]; do

    ip=$(nc -nvlp $port 2>&1 | grep "Connection from" | awk -F " " '{print $3;}')

    echo Connection from ip: $ip

    iptables -A INPUT -p tcp -s $ip -j DROP
    if [ $? -eq 0 ]; then
        echo "$ip has been blocked"
    else
        echo "Failed to block $ip"
    fi

done

#clear with iptables -F
#list with iptables -L
```

