# lambda basically is a one line function and following these 2 functions are same one is official and other is lambda function means one line function
# def add(a,b):
#     return a+b
# add = lambda x,y: x+y
# num1 = int(input("enter 1st number: "))
# num2 = int(input("enter 2nd number: "))
# print("the sum is: ",add(num1,num2))

# this is the sorting of a function
# these are 2 functions are same one for manually and 2nd for using lambda
# def sorting(a):
#     return a[1]
a=[[1,4],[5,7],[8,23]]
# a.sort(key=sorting)
a.sort(key=lambda x:x[1])
print(a)