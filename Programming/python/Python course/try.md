
```python
try:
  print("try")
except StopIteration as e:
  print("StopIteration exception:")
  print(e.value)
  print(e.with_traceback)
except Exception as e:
  print("Unknown error occured")
  print(e.with_traceback)
else:
  print("try finished without failing")
finally:
  pass
```