
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"
  
else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi


if this is in a script, or just typed in terminal, it makes a file
```sh
cat > /tmp/test.txt << EOF
some text
EOF
```

`<<EOF` can in other words be used to start multiline input to something. You end it with `EOF` on a line alone