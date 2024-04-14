# which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
import os.path

required = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open(os.path.join(os.path.dirname(__file__), "aoc2-input.txt")) as file:

    sum = 0
    for line in file:
        line = line.strip()
        print(line)

        split = line.split(": ")
        game_number = split[0].split(" ")[1]

        game_matches_requireds = True

        for set in split[1].split("; "):
            print("Set:")

            for value_and_color in set.split(", "):
                value_and_color = value_and_color.split(" ")
                value = value_and_color[0]
                color = value_and_color[1]
                print(f"{color}: {value}")

                if required[color] < int(value):
                    game_matches_requireds = False
                    print(f"{required[color]} < {value}")

        if game_matches_requireds:
            sum += int(game_number)

        print()

    print(f"{sum}")
