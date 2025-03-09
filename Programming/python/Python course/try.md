
catch errors
```python
try:
  print("try")
except StopIteration as e:
  print("StopIteration exception:")
  print(e.value)
  print(e.with_traceback)
except FileNotFoundError:
  print("The file doean't exist!")
except Exception as e:
  print("Unknown error occured")
  print(e.with_traceback)
else:
  print("try finished without failing")
finally:
  print("Printing this however it goes!")
```

raise errors
```python
name=input("Name: ")
if name=""
  raise Exception("Name can't be nothing!")
```

Produce Assertion error
```python
name=input("Name: ")
assert(name!="")
```
