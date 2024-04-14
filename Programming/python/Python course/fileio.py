
file=open('words.txt')
print(file)

#for line in file:
#    print(line.strip())

def has_no_letters(word,letters):
    found_a_letter = False
    for letter in letters:
        if letter in word:
            found_a_letter=True
    return not found_a_letter

letters = input('Letters to exclude:')

word_count=0
for line in file:
    if has_no_letters(line.strip(),letters):
        word_count +=1

print('I found',word_count,'words without',letters+'.')

file.close()

#open(filename, 'r', encoding = 'utf-8-sig')
