

lists
```python
list1 = ["a", "b", "c"] #["a", "b", "c"]
list2 = [x for x in list1]  #["a", "b", "c"]
list3 = [x for x in list1 if x == "a"]  #["a"]
list4 = [x for x in range(5)]  #[0, 1, 2, 3, 4]
list5 = [hex(x) for x in range(5)]  #["0x0", "0x1", "0x2, "0x3", "0x4"]
list6 = [hex(x) for x if x>0 else "X" in range(5)]  #["X", "0x1", "0x2, "0x3", "0x4"]
list7 = [x*x for x in range(5)]  #["0", "1", "4, "9", "16"]
list8 = [x for x in range(5) if x==0 or x==1]  #["0", "1"]
list9 = [[1, 2, 3][4, 5, 6][7, 8, 9]]
list10 = [y for x in list9 for y in x] #[1, 2, 3, 4, 5, 6, 7, 8, 9]
list11 = [c for c in "my string!"] #["m", "y", " ", "s", "t", "r", "i", "n", "g", "!"]
print("".join(list11)) #my string
print("-".join(list11)) #m-y- -s-t-r-i-n-g

#long form explanation
list12 = {}
for c in "my string":
  list12.append(c)
```

sets
```python
set1 = {x+x for x in range(5)}

```