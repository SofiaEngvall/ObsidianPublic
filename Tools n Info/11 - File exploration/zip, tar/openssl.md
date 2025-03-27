
https://stackoverflow.com/questions/16056135/how-to-use-openssl-to-encrypt-decrypt-files

ex:
```
tar -zcvf /tmp/backup.tgz /home/victim
openssl enc -aes256 -k P3NT35T3RL48 -in /tmp/backup.tgz -out /tmp/backup.tgz.enc
rm /tmp/backup.tgz
```

```
openssl enc -d -aes256 -k P3NT35T3RL48 -in /tmp/backup.tgz.enc -out /tmp/backup.tgz
```
