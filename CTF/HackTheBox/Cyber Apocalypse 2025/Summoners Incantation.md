
## The Summoner's Incantation

✧

Deep within the ancient halls lies the secret of the Dragon's Heart—a power that can only be unlocked by combining magical tokens in just the right way. The tokens are delicate: if you combine two adjacent tokens, their energy dissipates into the void.

Your quest is to determine the maximum amount of energy that can be harnessed by selecting tokens such that no two selected tokens are adjacent. This challenge is equivalent to finding the maximum sum of non-adjacent numbers from a list.

---

## 🔥 Your Quest

### Input Format:

- A single line containing a Python-style list of integers representing token energies.  
    _Example: [3, 2, 5, 10, 7]_

### Output Format:

- A single integer that is the maximum energy obtainable by summing non-adjacent tokens.

## 🔥 Example 1

### Input:

[3, 2, 5, 10, 7]

### Output:

15

Explanation: The optimal selection is to pick tokens 3, 5, and 7 (non-adjacent), yielding a sum of 3 + 5 + 7 = 15.

## 🔥 Example 2

### Input:

[10, 18, 4, 7]

### Output:

25

Explanation: The best choice is to select 18 and 7 (tokens at positions 2 and 4) for a total of 18 + 7 = 25.

## 🔥 Ancient Wisdom

- Examine each token's energy value carefully.
- If you combine adjacent tokens, their magical energy is lost!
- Find the optimal combination that maximizes the total energy while ensuring no two tokens are adjacent.

---

```python
# make a list of the string
nums = list(map(int,input().strip("[]").split(",")))

# set sums to 0
n = len(nums)
sums = [0] * n

# every sum is the max one, up to that position in the list

#the first sum is the first num
sums[0] = nums[0]

#the second sum is the highest of the first the numbers
sums[1] = max(nums[0], nums[1])

# for the rest we need to compare the old sums with the existing
for i in range(2, n):
    sums[i] = max(sums[i - 1], sums[i - 2] + nums[i])

# print the max sum for the last index
print(sums[-1])
```

`HTB{SUMM0N3RS_INC4NT4T10N_R3S0LV3D_a9e12a15dac309437ec2fb12d5247b90}`