
```sh
james@mnemonic:~$ ls -la ../condor
ls: cannot access '../condor/..': Permission denied
ls: cannot access '../condor/'\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\''': Permission denied
ls: cannot access '../condor/.gnupg': Permission denied
ls: cannot access '../condor/.bash_logout': Permission denied
ls: cannot access '../condor/.bashrc': Permission denied
ls: cannot access '../condor/.profile': Permission denied
ls: cannot access '../condor/.cache': Permission denied
ls: cannot access '../condor/.bash_history': Permission denied
ls: cannot access '../condor/.': Permission denied
ls: cannot access '../condor/aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==': Permission denied
total 0
d????????? ? ? ? ?            ?  .
d????????? ? ? ? ?            ?  ..
d????????? ? ? ? ?            ? 'aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw=='
l????????? ? ? ? ?            ?  .bash_history
-????????? ? ? ? ?            ?  .bash_logout
-????????? ? ? ? ?            ?  .bashrc
d????????? ? ? ? ?            ?  .cache
d????????? ? ? ? ?            ?  .gnupg
-????????? ? ? ? ?            ?  .profile
d????????? ? ? ? ?            ? ''\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\'''
```

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ echo "aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==" | base64 --decode
https://i.ytimg.com/vi/K-96JmC2AkE/maxresdefault.jpg

┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ echo "VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ==" | base64 --decode
THM{a5f82a00e2feee3465249b855be71c01}
```

