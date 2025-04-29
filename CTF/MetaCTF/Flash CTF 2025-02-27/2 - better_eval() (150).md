(solved by 279 teams)

I just want to let people run python code, but they keep trying to read flag.txt. So, I made a better eval that has filters to stop this!

Download the code [here](https://metaproblems.com/03a5325c8cd91ea302f15cc447900a91/better_eval.py) and connect to the remote instance with `nc kubenode.mctf.io 30019`

In the event that remote instance goes down, you can also use `nc host5.metaproblems.com 5110`. These two are identical, this is just the backup.

---

google: file open
https://www.w3schools.com/python/python_file_open.asp
```python
f = open("demofile.txt", "r")  
print(f.read())
```

google: python string concatenation not using +
https://stackoverflow.com/questions/18842779/string-concatenation-without-operator
```python
string1 = 'Hello'   'World'  #1 works fine
string2 = 'Hello' + 'World'  #2 also works fine
```

solution
```python
f = open("fl" "ag.txt", "r")  
print(f.read())
```

MetaCTF{f1l73rs_d0_n0t_s3cur3_u}
