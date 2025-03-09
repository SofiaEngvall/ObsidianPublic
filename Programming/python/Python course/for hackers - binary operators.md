
```python
x=13
y=5
print(bin(x)) #0b1101
print(bin(x)[2:].rjust(4,"0")) #0b1101 (removing 0b)
print(bin(y)[2:].rjust(4,"0")) #0b0101

print(bin(x & y)[2:].rjust(4,"0")) #bitwise and 0b0101
print(x&y) #5

print(bin(x | y)[2:].rjust(4,"0")) #bitwise or 0b1101
print(x&y) #5

print(bin(x >> 1)[2:].rjust(4,"0")) #shift 1 step right 0b0110
print(bin(x >> 2)[2:].rjust(4,"0")) #shift 2 steps right 0b0011

x=13
print(bin(x >> 1)[2:].rjust(4,"0")) #shift 1 step left 0b011010

```

