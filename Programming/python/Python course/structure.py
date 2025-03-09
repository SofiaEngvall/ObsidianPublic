# ----------------------------------------------
print('\nif')
x = 5
if (x == 0):
    print('x is 0')
elif (x == 1):
    print('x is 1')
else:
    print('x is not 0 or 1')

print("woo") if x==0 else print("naaah") if x==1 else print("whatever")

# ----------------------------------------------
print('\nswitch - match case')
x = 0
match x:
    case 1:
        print('x is 1')
    case 2:
        print('x is 2')
    case 3:
        print('x is 3')
    case _:  # default, if none above matched
        print('x is not 1, 2 or 3')

# ----------------------------------------------
print('\nfor')
for i in range(5):
    print(i)

# range(startvalue, stopvalue, step)

vegies = ['broccoli', 'paprika', 'cucumber']
for vegie in vegies:
    print(vegie)

# ----------------------------------------------
print('\nwhile')
x = 5
while (x > 0):
    print(x)
    x -= 1

# ----------------------------------------------
print('\nbreak')
while (True):
    print('hi')
    break  # breaks out of the loop

# ----------------------------------------------
print('\ncontinue')
for i in range(5):
    if i == 2:
        continue  # continues to the next lap of the loop = 2 won't be printed
    print(i)

# ----------------------------------------------
print('\nbreak nested loop')
for i in range(6):
    for j in range(6):
        print(f"{i}*{j}={i*j}")
        if i*j == 10:
            print("10! Breaking out of the loops!")
            break
    else:  # only done when not breaking
        print("continue")
        continue
    print("break")
    break

# ----------------------------------------------
print("\nkey value pair loop")
for key, value in {"a":1,"b":2,"c":3}.items()
  print(key, value)



# ----------------------------------------------
print('\nfunction')
# define function


def my_function():
    print('This is my function')
    print('doing stuff')


# obs that this is not a part of the function due to not indented
print('what about this')
# calling function
my_function()
my_function()

print(type(my_function))

# ----------------------------------------------
print('\nreturn value')


def add_stuff(a, b):
    return a+b


print("sum =", add_stuff(1, 2))


# ----------------------------------------------
print('\nrecursive function')


def recursion(n):
    if (n <= 0):
        print('Done')
    else:
        print("before", n)
        recursion(n-1)
        print('after', n)


recursion(3)

# ----------------------------------------------

def naming(name,age):
  print("{}: {}".format(name, age))

naming(age=5, name="Kalle")

# ----------------------------------------------

def defaultparam(name = "default name"):
  print("{}".format(name))

defaultparam()

# ----------------------------------------------

#variable number of args function!!
def star(name, *more)
  print("{} {}".format(name, " ".join[s for s in more]))

star("a")
star("a", "b")
star("a", "b", "c")
#all ok

# ----------------------------------------------

#dictionary argument
def dicargs(**ks):
  for a in ks:
    print(a, ks[a])

dicargs(a="1", b="2", c="3")

# ----------------------------------------------

#lambdas - functions without "names"?

add_10 = lambda x:x+10
print(add_10(1)) #11

#can be written as:
def add_10(x):
  return x+10

add = lambda x,y:x+y
print(add(1,2)) #3

print(lambda x,y:x+y)(1,2) #3

is_even = lambda x: x%2==0

blocks = lambda x,y:[x[i:i+y] for i in range(0, len(x), y)
print(blocks("string",2)) #["st", "ri", "ng"]

to_ord = lambda x:[ord(i) for i in x]
print(to_ord("ABCD")) #65, 66, 67, 68

#can also be a normal function
def to_ord2(x):
  ret = []
  for i in x:
    ret.append(ord(i))
  return ret




