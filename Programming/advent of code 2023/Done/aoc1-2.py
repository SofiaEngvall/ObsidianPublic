# the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number

import os.path
import re

num_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open(os.path.join(os.path.dirname(__file__), "aoc1-input.txt")) as file:

    sum = 0
    for line in file:
        line = line.strip()
        print(line)

        regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))'
        matches = re.findall(regex, line)
        print(matches)

        first = matches[0]
        last = matches[-1]

        if (not first.isnumeric()):
            first = num_map[first]
        if (not last.isnumeric()):
            last = num_map[last]

        print(f"first: {first}")
        print(f"last:  {last}")
        print(f"to add {int(first+last)}\n")
        sum += int(first+last)

    print(f"{sum}")
