

class MyClass():
    """A test class"""

    # class variables
    var = 1
    test = 2
    # but only as far as having the same initial value
    class_variable = "shared, not  unique"

    # but for a list or dictionary declared here will indeed be common
    common = []
    # unique lists HAVE to be declared in __init__!!!

    _non_public = 1
    # python might change the name of class varsstarting with __ to _classname__varname to avoid name clashes
    __non_public_and_ok_to_be_name_mangled = 1

    def __init__(self, var, test, unique):  # constructor
        # instance variables
        self.var = var
        self.test = test
        self.data = []
        instance_variable = unique

    def __str__(self):  # text representation of the class
        return f"{self.var}({self.test})"

    def testfunc(self):
        print("I'm a class function!")

    # it doesn't have to be called self,  but the first argument is always the one used as a ref to the current instance
    def another_func(me_myself_and_i):
        print(me_myself_and_i.test)

    def add_common(self, to_add):
        self.common.append(to_add)

    def add_data(self, to_add):
        self.data.append(to_add)

    def add_standard(self):  # can access other methods
        self.add_data("standard data")


print(MyClass.test)

a1 = MyClass(5, "hi", "myname")

print(a1.var)
print(a1.test)

print(a1)

a1.testfunc()
a1.another_func()

a1.test = "qwerty"

# The class itself works as an instatiated object!
MyClass.var = 5

print(MyClass.var)

a2 = MyClass(1, 2, "to be deleted")

print(a2.test)
del a2.test  # should work but doesn't?
# del a2 #works
print(str(a2.test)+" not deleted!?")

print("docstring: "+a1.__doc__)

print(a1.data)

# not declared data attributes will be created as with normal local variables
a1.qwe = 5
print(a1.qwe)

a3 = MyClass(1, 2, 3)

a1.class_variable = "shared?"
print(a3.class_variable)

a3.add_common("added one thing")
a1.add_common("added another thing")
print(a1.common)  # both listed!

a3.add_data("added one thing")
a1.add_data("added another thing")
print(a1.data)  # just one!

a3.add_standard()
print(a3.data)

print(a3.__class__)


class SpecialMyClass(MyClass):
    special_var = "hello"

    # when you add an init to the class, the parents init will no longer be run so add it like this
    def __init__(self, var, test, unique,  childvar):
        super().__init__(var, test, unique)
        self.childvar = childvar

    def another_func(me_myself_and_i):  # overriding base class method
        print("this is an overridden method")

    def print_childvar(self):
        print(self.childvar)


s1 = SpecialMyClass(1, 2, 3, 4)
print(s1.var)
print(s1.special_var)
s1.another_func()

# Obs  that this is true though s1 is a SpecialMyClass
print(isinstance(s1, MyClass))
print(issubclass(SpecialMyClass, MyClass))

# class test(A,B,C) is possible = multible inheritance

s1.print_childvar()
