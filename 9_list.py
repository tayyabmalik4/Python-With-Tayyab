# this is the list tutorial in python-----list is a mutable
glosry = ['harpic', 'vim bar', 'shampoo', 'soap' , 'chikan' , 'lollypop' , 55]
# print(glosry[6])

numbers = ['3','5', '7','9', '4', '2', '1']
# numbers.sort()
# numbers.reverse()
# numbers.append(71)
# numbers.append(7)
# numbers.append(1)
# numbers.insert(2,67)
# numbers.remove(1)
# numbers.pop()
# numbers[1]= 47
# print(numbers)
# print(numbers[:4])
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))


# mutable--->can change
# immutable--->cannot be changed

# this is the tupal tutorial start in python-----tupal is a immutable 
# we are not changed valu in tupal in python language
# tp =(1,2,3)
# tp[1] = 8
# print(tp)
a=2
b=7

# these two steps are same=
a,b = b,a
# temp = a
# a=b
# b=temp
print(a,b)

# -------------when we want to input from user and show the values using list
# //////this is the empty list now
lst=[]
# //////this is input from user and user tell about that how many numbers are store in the list
l=int(input("Enter Values"))
# /////this is the for loop to itrate the numbers 
# /////we can't input without range function if we input in the integers
# /////if we want to spacific number of indexs in the list than we use num in the place of l
for i in range(0,l):
    # /////unsing input function to the user which is store the values in the list
    inp=int(input())
    # /////using append function to append the values in the lists
    lst.append(inp)
print(lst)
