
to add/merge to the below

three types of collections:
tuples = ("q","w") #not changeble = immutable
lists = ["q","w"]
dictionaries = {"q":5, "w":1}

---

tuples

tuples1, tuples2 = tuples
print(tuple1)
print(tuple2)
if "w" in tuples:
  print(tuples.index("w"))

print(tuples[0]) #prints the first one
print(tuples[-1]) #prints the last one
print(tuples[0:2]) #prints the first two
print(tuples[:2]) #the same as above
print(tuples[-5:-3]) #prints starting at the 5th from the end and prints to the 4th (3rd not included)


---


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

numbers.sort(reverse=True)
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

print(max(numbers))
print(min(numbers))


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


numbers.reverse()
print(numbers)
numbers = numbers[::-1] #the same as reverse

print(numbers.count(9)) #how many 9 in the list

numbers.pop() #removes last
print(numbers)

newlist = ["A","B","C"]
numbers.entend(newlist)
print(numbers)

numbers.clear() #empty the list
print(numbers)


list2 = numbers #this is just a reference copy = changes made to either will be made in both
list2 = numbers.copy() #makes a copy


# Tuples (immutable = do not change)
grades = ('a','b','c','d','e','f')
#grades.append('g') #'tuple' object has no attribute 'append'
print('\n'+str(grades))
print(grades[2])


---

dictionaries

mydict = {} #can define before we know the data

mydict = {"a":1, "b":2, "c",3}
print(mydict)
print(type(mydict))

print(mydict["b"]) #2
print(mydict.get["c"]) #3

print(mydict.keys())
print(mydict.values())

mydict["d"] = 4 #adds key+value pair

mydict["a"] = 3 #update
mydict.update({"a",3}) #also update

mydict.pop("d")

del mydict["c"]


-------

sets!

myset = {"a", "b", "c"}
print(type(myset))

there are no order - if we print it several times we will get them ordered differently!
print(myset)
print(myset)
print(myset)

can't have duplicates so adding several of the same will make no difference, also both true and false can't be in a set

myset.add("d")

myset.discard("c") #will remove d if it is in the set but not error if it's not there as .remove would






