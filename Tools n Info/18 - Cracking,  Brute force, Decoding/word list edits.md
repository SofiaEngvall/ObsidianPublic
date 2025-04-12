
Adding year numbers to the end of words in a list:
```sh
awk '{print; for(y=2019; y<=2025; y++) print $0 y}' input.txt > output.txt
```

Also changing the case so that only the first letter is upper case (this one also skips words with spaces):
```sh
awk '
{
    # Skip lines with spaces
    if ($0 ~ / /) next;

    # Convert to title case (first letter uppercase, rest lowercase)
    word = tolower($0);
    word = toupper(substr(word,1,1)) substr(word,2);

    # Print the original and append years
    print word;
    for(y=2019; y<=2025; y++) print word y;
}' input.txt > output.txt

```

the same in bash:
```sh
while IFS= read -r word; do
  # Skip lines with spaces
  [[ "$word" =~ \  ]] && continue
  
  # Convert to title case
  word=$(echo "$word" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}')

  # Print original and with years
  echo "$word"
  for year in {2019..2025}; do
    echo "${word}${year}"
  done
done < input.txt > output.txt
```

the same in python:
```python
with open("input.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        word = line.strip()

        # Skip words containing spaces
        if " " in word:
            continue

        # Convert to title case (first letter uppercase, rest lowercase)
        word = word[:1].upper() + word[1:].lower()

        # Write original and with years
        outfile.write(word + "\n")
        for year in range(2019, 2026):
            outfile.write(f"{word}{year}\n")
```
