# there are 2 types of functions
# 1:build in function 
# 2: user define function 

# build in fuinction
# a =3
# b= 4
# c= sum((a,b))
# print(c)

# user definr function
def function1(a,b):
    print("Hellow, this is the function tutorial and i learn function",a+b)

# function1(7,8)
def function2(a,b):
    """this is a function which will calculate average of two numbers
    this function dosn't work with three numbers"""
    avg = (a+b)/2
    # print(avg)
    return avg

v = function2(6,9)
print(v)
print(function2.__doc__)