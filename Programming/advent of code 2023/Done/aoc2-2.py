# In each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
import os.path

with open(os.path.join(os.path.dirname(__file__), "aoc2-input.txt")) as file:

    sum = 0
    for line in file:
        line = line.strip()
        print(line)

        split = line.split(": ")
        game_number = split[0].split(" ")[1]

        required = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for set in split[1].split("; "):
            print("Set:")

            for value_and_color in set.split(", "):
                value_and_color = value_and_color.split(" ")
                value = value_and_color[0]
                color = value_and_color[1]
                print(f"{color}: {value}")

                if required[color] < int(value):
                    required[color] = int(value)
                    print(f"{color} = {value}")

        sum += required["red"]*required["green"]*required["blue"]

        print()

    print(f"{sum}")
