# thefuzz, old name fuzzywuzzy - for inexact strting matching
# python-Levenshtein & python-Levenshtein-wheels

from thefuzz import fuzz, process

s1 = "first string"
s2 = "second string"
s3 = "string first"
s4 = "string first first"

print(fuzz.ratio(s1, s2))
print(fuzz.partial_ratio(s1, s2))
print(fuzz.token_sort_ratio(s1, s3))
print(fuzz.token_set_ratio(s1, s4))

list1 = ["hello list", "hello world", "hello everybody", "testing", "wohoo"]

print(process.extract("hello", list1, limit=2))
print(process.extractOne("hello", list1))

# can search in a long list for stuff case insensitive, word order insensitive...
print(process.extract("wo h", list1, limit=3, scorer=fuzz.token_sort_ratio))
