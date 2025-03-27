
## The Enchanted Cipher

The Grand Arcane Codex has been corrupted, altering historical records. Each entry has been encoded with an **enchanted shifting cipher** that encrypts a plaintext composed of 3–7 randomly generated words.

The cipher operates as follows:

- Alphabetical characters are processed in groups of 5 (ignoring non-alphabetical characters).
- For each group, a random shift between 1 and 25 is chosen and applied to every letter in that group.
- After the encoded message, an additional line indicates the total number of shift groups, followed by another line listing the random shift values used for each group.

Your quest is to decode the given input and restore the original plaintext.

## Example

### Input

ibeqtsl
2
[4, 7]

### Output

example

---

```python
# Input the text as a single string
cipher = input()
shift_groups = input()
shift_values = list(map(int,input().strip("[]").split(",")))

alpha_num_chars = 0
decoded = ""

#loop through all chars
for i in range(len(cipher)):

#print(alpha_num_chars//5) #,end="")
char = ord(cipher[i])
steps = shift_values[alpha_num_chars//5]

if 'A' <= cipher[i] <= 'Z':  # Uppercase letters
    decoded += chr(((char - 65 - steps) % 26) + 65)
    alpha_num_chars += 1
elif 'a' <= cipher[i] <= 'z':  # Lowercase letters
    decoded += chr(((char - 97 - steps) % 26) + 97)
    alpha_num_chars += 1
else:
    decoded += cipher[i]

print(decoded)
```

`HTB{3NCH4NT3D_C1PH3R_D3C0D3D_b440f47b1c721ccdc61092b53ee42ec2}`

