#//////////definition of the generator////// Python provides a generator to create your own iterator function. A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator function, a yield statement is used rather than a return statement.

# itrable ------itrable functions define who is "__iter__() or __getitem__"
# itrater ------itrator functions define who start "-__next__()"
# itration ----- itration means the values is going to next value exammple is write in the below

# this is the example of itration
# n=int(input("Enter the value:   "))
# for i in range(1,n):
#     print(i)

# this is the genrater function call
# in this function yield means a genrator and it return just a name of genrator
# remember that yield, return and print are the different functions 
# yield tells us a generator 
# return means that the function is return the value and end of the function and print function return the values
# when we want just one value print than use __next__() fuction
# we also print value using the for loop but when we use for loop then __next__() function did not work
# __next__() function is use just when yield is use in the function 
# and when we use return function in the for loop then its just first value printed

# def gen(n):
#     for i in range(n):
#         print(i)
        # return i
        # yield i
# g= gen(23)
# print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# /////////using for loop to output the factorial
# def recur(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac

# number=int(input("Enter the number:  "))
# print(recur(number))

# //////////using resursion method to output a factorial
# def recursive(n):
#     if n<=1:
#         return 1
#     else:
#         n=n*recursive(n-1)
#     return n
# num=int(input("Enter the value:  "))
# print(recursive(num))

# ///////////////using recursive to get a fabbonachhi
# def fabb(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     else:
#         n=fabb(n-1)+fabb(n-2)
#     return n
# num=int(input("Enter the number:   "))
# print(fabb(num))

# ////////////print stars
# *
# **
# ***
# ****
# *****

# //////////////for print star ulat
def star(n):
    for i in range(n,1,-1):
        print(i*"*")
        # n=n-1
num=int(input("Enter the Nunmber:   "))
print(star(num))

# ////////////for print star 
# def star(n):
    # for i in range(1,n+1):
    #     print(i*"*")
#         # for j in range(1,i+1):
#         #     print("*", end=" ")
#         # print()
# num = int(input("Enter the number:   "))
# star(num)
    



