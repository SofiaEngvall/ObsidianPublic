# A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together
# you need to find the gear ratio of every gear and add them all up
import os.path
import re

data = []

with open(os.path.join(os.path.dirname(__file__), "aoc3-short.txt")) as file:
    for line in file:
        line = line.strip()
        data.append(line)

sum = 0
for i in range(len(data)):
    print(f"line: {data[i]}")

    matches = re.finditer(r'\*', data[i])
    for match in matches:
        number = match.group()
        print(f"Number: {number}")
        start = match.start()
        end = match.end()
        print(match.span())
        # print(data[i][start:end])

#         adjacent_symbol = False

#         # left
#         if start != 0:
#             print(f"left:  {data[i][start-1]}")
#             if data[i][start-1] not in not_symbols:
#                 adjacent_symbol = True
#             start -= 1
#         # right
#         if end != len(data[i]):
#             print(f"right: {data[i][end]}")
#             if data[i][end] not in not_symbols:
#                 adjacent_symbol = True
#             end += 1
#         # up
#         if i != 0:
#             print(f"up:   {data[i-1][start:end]}")
#             for char in data[i-1][start:end]:
#                 if char not in not_symbols:
#                     adjacent_symbol = True
#         # down
#         if i != len(data)-1:
#             print(f"down:  {data[i+1][start:end]}")
#             for char in data[i+1][start:end]:
#                 if char not in not_symbols:
#                     adjacent_symbol = True

#         print(f"adjacent_symbol = {adjacent_symbol}")
#         if adjacent_symbol:
#             sum += int(number)
#         # print(f"sum = {sum}")

# print(f"Summa: {sum}")
