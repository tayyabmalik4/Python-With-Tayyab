# ///////////////tutorial of coroutines////////////
# coroutines method is very help full in machine learning or any pythonic way
# coroutine the achully work when the code is very big and we want that the program is run very speedy because speed is very matter in this field
# achully when one code is very big for example we creat a dictionary or create a big book like 5000 pages
# than first of program run as the required time but then program is run very speedly because then program use a loop
# this is very pythonic way 
# example is below

def big_code():
    # this is starting very big code but at this time as a practice we use time module at the place of big code
    import time
    # here book variable is like a very big book or very big data 
    # as we know big data required a  exicuted time to solve the problem we use time.sleep module
    # in this 4 sec means the time taking as the book read time and we just let it.
    book="i am tayyab and i want to build a AI ROBORT.i wish it.and ALLAH is helping me"
    time.sleep(4)

    # we need a coroutines function use
    # while function and at the end yield function is use as a coroutine 
    # we run while loop infinite time
    while(True):
        task=(yield)
        if task in book:
            print("your task in the book")
        else:
            print("your task is not a in this book")
code=big_code()
# next is a function which is use in the genrators as a itrator
next(code)
# send is a function which is use in the yield function
# the send()method return a next value yielded by the genrator exits without yielded another value
# when send() is called to start the generator it must be called with none as the argument, because there is no yield expression that could receive the value
code.send("tayyab")
input("enter any key:   ")
code.send("AI")
# this is the user input which we want to search the any name or code
a=input("enter which is search:    ")
code.send(a)
print("this is the very great work in the machine learning")
