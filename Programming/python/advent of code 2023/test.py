"""
Day 3 of Advent of code
"""
import re


def symbol_search(lines: list[str], row, start, end) -> bool:
    for line in lines[max(0, row-1):min(row+2, len(lines))]:
        if re.search(r'([^\d.])', line[max(0, start-1):min(end+1, len(lines))]):
            return True
    return False


def gear_search(lines: list[str], row, col) -> int:
    matches = []
    for line in lines[max(0, row-1):min(row+2, len(lines))]:
        for match in re.finditer(r'(\d+)', line):
            start, end = match.span()
            if start <= col+1 and end-1 >= col-1:
                matches.append(match)
    if len(matches) == 2:
        return int(matches[0].group(0)) * int(matches[1].group(0))
    return 0


def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    lines: list[str] = [line.strip() for line in file.readlines()]
    sum: int = 0
    for row, line in enumerate(lines):
        for match in re.finditer(r'(\d+)', line):
            if symbol_search(lines, row, match.start(), match.end()):
                sum += int(match.group(0))
    return sum


def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    lines: list[str] = file.readlines()
    sum: int = 0
    for row, line in enumerate(lines):
        for match in re.finditer(r'(\*)', line):
            sum += gear_search(lines, row, match.span()[0])
    return sum


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 ----")
    test = part2("test_data_1.txt")
    print(f" Test:  {test}")
    final = part2("input.txt")
    print(f" Final: {final}")
