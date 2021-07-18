# # n! = n* (n-1) * (n-2) *(n-3)......1
# # n! = n* (n-1)!

# this is the itrative method
# def factorial_itrative(n):
#     """
#     :param n:Integrate
#     :return n*(n-1)*(n-2)....1
#     """
#     fac =1
#     for i in range(n):
#         fac= fac* (i+1)
#     return fac
# number = int(input("pleas enter the number: "))
# print("factorial using itrative method" , factorial_itrative(number))

# this is the recursive method
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# 5* factorial_recursive(4)
# 5*4* factorial_recursive(3)
# 5*4*3* factorial_recursive(2)
# 5*4*3*2* factorial_recursive(1)
# 5*4*3*2*1 =120
# number = int(input("Enter the number: "))
# print("Factorial using recursive Method",factorial_recursive(number))


# this is the fabonacci method
# fabochacci is define as add previos 2 numbers
# 0 1 1 2 3 5 8 13 21 36.....
def febonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)
number= int(input("Enter the number: "))
print("this is return febonacci number", febonacci(number))

# this is the junaid's work
# def factorial(num) :
#     if (num <= 1) :
#         return 1
#     return num *factorial(num - 1)


# a = int(input("Enter a Number = "))

# print("The Factorial = " , factorial(a))


