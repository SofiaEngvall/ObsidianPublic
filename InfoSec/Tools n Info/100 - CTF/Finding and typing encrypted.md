
`find ./files -type f -exec sh -c 'file "$1" | grep -i -E "openssl|whatever"' sh {} \;`

```sh
find ./files -type f -exec sh -c '
    result=$(file "$1" | grep -i -E "openssl|whatever")
    if [ -n "$result" ]; then
        echo "Processing: $1"
        # Replace the echo below with any command you want to run on $1
        openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$1" -k picoCTF
    fi
' sh {} \;
```

`openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF; `

```sh
find ./files -type f -exec sh -c 'result=$(file "$1" | grep -i -E "openssl|whatever") && [ -n "$result" ] && openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$1" -k picoCTF' sh {} \;
```
