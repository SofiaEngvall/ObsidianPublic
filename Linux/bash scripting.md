
```sh
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
```


if this is in a script, or just typed in terminal, it makes a file
```sh
cat > /tmp/test.txt << EOF
some text
EOF
```

`<<EOF` can in other words be used to start multiline input to something. You end it with `EOF` on a line alone

variables
```sh
#!/bin/bash
echo "Hey, what’s your name?"
read name
echo "Welcome, $name"
```

loop
```sh
#!/bin/bash
for i in {1..10};
do
echo $i
done
```
the same:
```sh
#!/bin/bash
for i in {1..10}; do
  echo $i
done
```

if
```sh
#!/bin/bash
echo "Please enter your name first:"
read name
if [ "$name" = "Stewart" ]; then
        echo "Welcome Stewart! Here is the secret: THM_Script"
else
        echo "Sorry! You are not authorized to access the secret."
fi
```

