
```python
print(hexdump(read('/dev/urandom',32))) # 32 bytes from the "file" /dev/random
```

```sh
00000000  c9 c6 03 c5  de 07 f1 60  cf cb eb d2  6b cb fc 1a  │····│···`│····│k···│
00000010  9b ee bc d7  32 29 71 f4  e5 c1 90 32  3c b8 b3 65  │····│2)q·│···2│<··e│
00000020
```


```python
e = ELF(file_name) #will print stuff about the elf

#print("e.symbols")
#pprint(e.symbols) #lists all known symbols, including those below. Preference is given the PLT entries over GOT entries.
#print("e.got")
#pprint(e.got) #only contains GOT entries
#print("e.plt")
#pprint(e.plt) #only contains PLT entries
print("e.functions")
pprint(e.functions) #only contains functions (requires DWARF symbols)
```

```python
print("Functions:")
for function in e.functions.values():
  if(not function.name[:1] == "_"):
    print("%#x %s" % (function.address,function.name))
```

