
```sh
┌──(kali㉿kali)-[~]
└─$ crunch 3 3 0123456789ABCDEF -o 3digits.txt
Crunch will now generate the following amount of data: 16384 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 4096 

crunch: 100% completed generating output
```

`crunch 3 3 0123456789ABCDEF -o 3digits.txt`

The command above specifies the following:

- `3` the first number is the minimum length of the generated password
- `3` the second number is the maximum length of the generated password
- `0123456789ABCDEF` is the character set to use to generate the passwords
- `-o 3digits.txt` saves the output to the `3digits.txt` file

crunch also lets us specify a character set using the -t option to combine words of our choice. Here are some of the other options that could be used to help create different combinations of your choice:  

@ - lower case alpha characters

, - upper case alpha characters

% - numeric characters

^ - special characters including space

```shell-session
crunch 6 6 -t pass%%
```

