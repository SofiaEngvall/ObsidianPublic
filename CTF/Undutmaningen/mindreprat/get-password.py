# 'Enter the password: ' display.
# s := ([ stdin nextLine ] on: Error do: ['']) asByteArray.
# chars := 'abcdefghijklmnopqrstuvwxyz0123456789'.
# ok := (s size) == 16 and: [
#     (s allSatisfy: [ :c | chars includes: (c asCharacter)])
#         & (((s at: 6)  -       (s at: 4))  <  -4)
#         & (((s at: 12) -       (s at: 1))  == -5)
#         & (((s at: 5)  bitXor: (s at: 13)) == 2)
#         & (((s at: 14) bitXor: (s at: 2))  == 19)
#         & (((s at: 11) bitOr:  (s at: 2))  == 126)
#         & (((s at: 8)  bitOr:  (s at: 5))  == 108)
#         & (((s at: 16) bitXor: (s at: 7))  == 16)
#         & (((s at: 9)  bitXor: (s at: 10)) == 9)
#         & (((s at: 3)  +       (s at: 12)) == 226)
#         & (((s at: 15) -       (s at: 4))  == -5)
#         & (((s at: 9)  bitOr:  (s at: 8))  == 125)
#         & (((s at: 4)  +       (s at: 12)) <  226)
#         & (((s at: 6)  bitXor: (s at: 10)) == 8)
#         & (((s at: 12) bitOr:  (s at: 11)) == 111)
#         & (((s at: 2)  bitXor: (s at: 4))  == 2)
#         & (((s at: 13) bitXor: (s at: 3))  == 25)
#         & (((s at: 10) bitXor: (s at: 16)) == 26)
# ].
# '' displayNl.
# ans := ok
#     ifTrue:  [ ans := (FileStream open: 'flag.txt') nextLine ]
#     ifFalse: ['Incorrect!'].
# ans displayNl.

from z3 import *

# Initialize solver
solver = Solver()

# Password is 16 bytes (Smalltalk uses 1-based indexing; Python uses 0-based)
s = [BitVec(f's_{i}', 8) for i in range(16)]

# Constraint: Only lowercase letters and digits
valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
for c in s:
    solver.add(Or([c == ord(x) for x in valid_chars]))

# Add all constraints (converted to 0-based indexing)
solver.add(s[5] - s[3] < -4)                   # (s at:6) - (s at:4) < -4
solver.add(s[11] - s[0] == -5)                 # (s at:12) - (s at:1) == -5
solver.add(s[4] ^ s[12] == 2)                  # (s at:5) ^ (s at:13) == 2
solver.add(s[13] ^ s[1] == 19)                 # (s at:14) ^ (s at:2) == 19
solver.add(s[10] | s[1] == 126)                # (s at:11) | (s at:2) == 126
solver.add(s[7] | s[4] == 108)                 # (s at:8) | (s at:5) == 108
solver.add(s[15] ^ s[6] == 16)                 # (s at:16) ^ (s at:7) == 16
solver.add(s[8] ^ s[9] == 9)                   # (s at:9) ^ (s at:10) == 9
solver.add(s[2] + s[11] == 226)                # (s at:3) + (s at:12) == 226
solver.add(s[14] - s[3] == -5)                 # (s at:15) - (s at:4) == -5
solver.add(s[8] | s[7] == 125)                 # (s at:9) | (s at:8) == 125
solver.add(s[3] + s[11] < 226)                 # (s at:4) + (s at:12) < 226
solver.add(s[5] ^ s[9] == 8)                   # (s at:6) ^ (s at:10) == 8
solver.add(s[11] | s[10] == 111)               # (s at:12) | (s at:11) == 111
solver.add(s[1] ^ s[3] == 2)                   # (s at:2) ^ (s at:4) == 2
solver.add(s[12] ^ s[2] == 25)                 # (s at:13) ^ (s at:3) == 25
solver.add(s[9] ^ s[15] == 26)                 # (s at:10) ^ (s at:16) == 26

# Solve and print the password
if solver.check() == sat:
    model = solver.model()
    password = ''.join([chr(model.eval(c).as_long()) for c in s])
    print("Found password:", password)
else:
    print("No solution found.")
