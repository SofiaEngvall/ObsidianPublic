
autodetect compression and extract to current dir
```sh
tar -xvf archive.tar.gz
```

to spec location
```sh
tar -xvf archive.tar.gz -C /home/kali/program
```

list files (-t or --list)
```sh
tar -tf archive.tar.gz
```

extract only spec file/s
```sh
tar -xf archive.tar.gz file1 file2
tar -xf archive.tar.gz --wildcards '*.js'
```

with pipe, specify gzip type (postman ex)
```sh
sudo wget -c https://dl.pstmn.io/download/latest/linux_64 -O - | sudo tar -xzv -C /opt
```
