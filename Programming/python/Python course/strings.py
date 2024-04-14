
print('Hi')

print("Hiya!")

print('Sofia\'s computer')

print('Please answer \"Yes\" or \"No\"')

print('These\nare\nseveral\nlines!')

print('\tTabs are great\tAgree?')

print('Carriage return is funny\r  Uh, might not work in all python environments')

print('Newline is \\n')

print("""This is a
multiline
text""")

print('''Another
one''')

print('''It's funny,
but these quotes don't
need to be escaped''')

print("Concatenate"+"strings")

string="hello"
print(string)
print(string[0])
print(string[3])
#print(string[len(string)]) #IndexError: string index out of range, since we start at 0
print(string[len(string)-1])

for i in range(len(string)):
    print(i,string[i])

#special for loop
for letter in string:
    print(letter)

print(string[2:4])  #Gets char 2 untill four, counting from 0, char 23
                    #Observe that the ending index is not included!
print(string[:3])   #Starts from the beginning, char 012
print(string[2:])   #Stopps at the end, char 234 (same as [2:5])
print(string[2:5])  #Obs there is no index 5

print(string[:-1])  #beginning until 1 from the end
print(string[-4:-1])#4 from the end until 1 from the end

#Strings in python can't be modified on character level
#string[2]='x'      #'str' object does not support item assignment

#A new string has to be built from parts of the old string, messy!
string2 = string[:2]+'x'+string[3:]
print(string2)

#We can do the same and put it into the same straing variable though:
string = string[:2]+'x'+string[3:]
print(string)

print(string.upper())
print(string.capitalize())

string='hello'
if 'x' in string:
    print('I love the letter X!')
else:
    print('Man, these are boring letters!')

if string == 'hello':
    print('string == hello')

string='alfa'
if string < 'g':
    print('first letter before g')

long_string = 'This is a longer string'
split_str = long_string.split()
print('_'.join(split_str))

str1 = '        sdfsdf   '
print(str1.strip())

string = 'hello'
print('My string: {} world!'.format(string))

#f'' strings
num = 5.6
f'hello {string} hello again {num:.1f} and again'
#but doesn't do anything if you don't print it or use it in some other way
print(f'hello {string} hello again {num:.1f} and again')
#https://peps.python.org/pep-0498/#format-specifiers
width = 10
precision = 4
value = 12.34567
print(f'result: {value:{width}.{precision}}')
print(f'{value:<8.2f}') #width 8, left margin
print(f'{value:>8.2f}') #right margin
print(f'{value:^8.2f}') #centered

#Char conversion
print(ord('A'))
print(chr(65))

print(len('my little test sting'))
