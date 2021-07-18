# -----------------started maping function--------------
# numbers = ["3","34","64"]

# this is the mapiny function using
# numbers=list(map(int,numbers))

# -----------------this is using for loop function
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])


# using map function creat square and also using simple function
# def sq(a):
#     return a*a 
# num =[2,3,4,5,6,7,8,9,10]
# square = list(map(sq,num))
# print(square)

# using map function creat square and also using lambda function

# num = [2,4,6,7,8,9,5,6,3]
# square = list(map(lambda x:x*x ,num))
# print(square)

# -----using 2 arguments in maping function
# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[sq,cube]
# num=[0,1,2,3,4,5,6,7,8,9]
# for i in num:
#     value =list(map(lambda x:x(i),func))
#     print(value)


# -------started filter function----filter function has 2 values one is function and other is list
# lst = [1,2,3,4,5,6,7,8,8,9]
# def greater(num):
#     return num>5
# greater1 = list(filter(greater,lst))
# print(greater1)


# ---------------------------started reduce function ------------
#----------- this is the simplw way
# lst = [1,2,3,4,5]
# num=0
# for i in lst:
#     num = num +i
# print(num)
# -----------this is the reduce function using
from functools import reduce
lst = [1,2,3,4,5]
num = reduce(lambda x,y:x+y ,lst)
print(num)