# the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number
import os.path

with open(os.path.join(os.path.dirname(__file__), "aoc1-input.txt")) as file:

    sum = 0
    for line in file:
        print(line.strip())

        first = ""
        for char in line:
            if char.isdigit():
                if first == "":
                    first = char
                    last = char
                else:
                    last = char

        print(f"first: {first}")
        print(f"last: {last}\n")
        sum += int(first+last)

    print(f"{sum}")
