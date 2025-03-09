# scope example from python docs, my comments

def scope_test():
    def do_local():
        spam = "local spam"  # new local var created that does not affect outer scope

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"  # uses var from outer scope

    def do_global():
        global spam
        # creates new var in global scope since there's not one there with this name
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)



#observe that a global variable can be accessed for reading from a function but to write to it we need the "global varname"
