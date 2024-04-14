# Basic Characters:
#     Characters match themselves: abc matches the exact sequence "abc."

# Character Classes:
#     [abc] matches any one of the characters a, b, or c.
#     [^abc] matches any character except a, b, or c.

# Quantifiers:
#     *: Matches 0 or more occurrences of the preceding character or group.
#     +: Matches 1 or more occurrences of the preceding character or group.
#     ?: Matches 0 or 1 occurrence of the preceding character or group.
#     {n}: Matches exactly n occurrences.
#     {n,}: Matches n or more occurrences.
#     {n,m}: Matches between n and m occurrences.

# Anchors:
#     ^: Anchors the match at the beginning of the string.
#     $: Anchors the match at the end of the string.

# Wildcards:
#     .: Matches any single character except a newline.

# Escape Characters:
#     \: Escapes a metacharacter, allowing it to be treated as a literal character.

# Grouping:
#     (): Groups patterns together. (abc)+ matches one or more occurrences of "abc."

# Alternation:
#     |: Acts like a logical OR. cat|dog matches either "cat" or "dog."

# Character Escapes:
#     \d: Matches any digit (0-9).
#     \w: Matches any word character (alphanumeric + underscore).
#     \s: Matches any whitespace character.

# Negation:
#     \D: Matches any non-digit.
#     \W: Matches any non-word character.
#     \S: Matches any non-whitespace character.

# Quantifier Modifiers:
#     *?, +?, ??: Lazy quantifiers, matching as little text as possible.

# Assertions:
#     (?=...): Positive lookahead assertion.
#     (?!...): Negative lookahead assertion.
#     (?<=...): Positive lookbehind assertion.
#     (?<!...): Negative lookbehind assertion.

import re

text = "The car is parked in the garage."

# Match words starting with "car"
regex = r'\bcar\w*\b'
matches = re.findall(regex, text)

print(matches)


text = "oneightwothreefourfivesixseveneightnine"

pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine))'

# Find all matches
all_matches = re.findall(pattern, text)

print("All Matches:", all_matches)

# Find overlapping matches using finditer
overlapping_matches = [match.group(1) for match in re.finditer(pattern, text)]
print("Overlapping Matches (finditer):", overlapping_matches)

# Find non-overlapping matches using findall
non_overlapping_matches = [match[0] for match in re.finditer(
    r'(?:one|two|three|four|five|six|seven|eight|nine)', text)]
print("Non-Overlapping Matches (findall):", non_overlapping_matches)

# ---


text = "oneightwothreefourfivesixseveneightnine"

# Using non-capturing group for non-overlapping matches
non_overlapping_matches = [match.group() for match in re.finditer(
    r'(?:one|two|three|four|five|six|seven|eight|nine)', text)]

print("Non-Overlapping Matches:", non_overlapping_matches)
