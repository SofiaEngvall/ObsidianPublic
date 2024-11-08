#fixit42 simple wheel cipher solver

message = "RKPUYPFCIAKKJMYZZJT"

wheel1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
wheel2 = "ABJICOSDHG{QNFUVWLEZYXPTKMR}"

print("message = "+message)
print("wheel1 = "+wheel1)
print("wheel2 = "+wheel2)

wheel2 = wheel2*2
new_message = ""

for a in range(len(wheel1)):   # Go through all possible rotations
    new_message = ""
    for letter in message:        # Go through the letters in the message
        position = wheel1.rfind(letter)
        new_letter = wheel2[position+a]
        new_message += new_letter
    print("new_message = "+new_message)
