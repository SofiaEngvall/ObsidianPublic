
example that just echos output
```python
for line in sys.stdin:
  if line.strip() == "exit":
    break
  sys.stdout.write("{}".format(line))
```

