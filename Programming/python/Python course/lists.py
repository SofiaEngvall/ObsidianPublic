
to add/merge to the below

three types of collections:
tuples = ("q","w") #not changeble = immutable
lists = ["q","w"]
dictionaries = {"q":5, "w":1}

lists[1]
lists[1:5]
dictionaries["q"] refed by key

del
len
min
max
.clear()


----------------

numbers=[4,41,9,3,5,23]
animals=['dog','cat']
print(numbers)
print(numbers[4])
diff=[1,'a',[45,65],'kalle']  #allowed but should be avoided except special cases
print(diff[2][1])
empty=[]

animals[1]='fish'

if 9 in numbers:
    print('Yay, 9 found')

for number in numbers:
    print(number)

for i in range(len(numbers)):
    print(i,'*',numbers[i],'=',i*numbers[i])

print('\n')

print('here')
print(numbers)
print(numbers[1:])
numbers+=[8,32,5] #appending
print(numbers)
print(numbers*2)
print((numbers*2)[5:-2])
print(numbers[3:6]) #works as for strings

print('\n')

#Stuff you can't do with strings but with lists !
numbers[2]=-9
print(numbers)

numbers[5:7]=[0,7] #replaces
print(numbers)

numbers[5:7]=[0,1,2,3,4,5,6,7] #inserts and replaces
print(numbers)

numbers.append(5)  #adds the the end of the list
print(numbers)

numbers.extend([1,2,3]) #appends the list
print(numbers)

numbers.sort()
print(numbers)

print(numbers.pop(0)) #returns element and then deleted it from the list
print(numbers)

print('\n')

del(numbers[2])
print(numbers)

del(numbers[3:5])
print(numbers)

numbers.remove(5) #removes the first 5 in the list
print(numbers)

index=6
addition=99
numbers.insert(index,addition) #inserts at index
print(numbers)

print(numbers.count(4)) #how many 4s

#range(startvalue, stopvalue (not included), step)
print(list(range(3,19,2))) #3,5,7,9,11,13,17 - not 19

print('\n')

#Lists as arguments

def initList():
    return [1,2,3]#["apple", "banana", "cherry", 3, 5]
    
def printList(list):
  for item in list:
    print(item)

def changeListBad(list):
  for item in list:
    item = 3

def changeList(list):
  for item in list:
    item = 3

items = initList()

printList(items)

changeList(items)

printList(items)


items2=['1.1','4.6','3.3']
print(items2)
for i in range(len(items2)):
    items2[i]=float(items2[i])
print(items2)





# Tuples (immutable = do not change)
grades = ('a','b','c','d','e','f')
#grades.append('g') #'tuple' object has no attribute 'append'
print('\n'+str(grades))
print(grades[2])

