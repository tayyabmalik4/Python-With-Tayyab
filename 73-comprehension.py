#/////////definotion of dictionary comprehension////// The way to do dictionary comprehension in Python is to be able to access the key objects and the value objects of a dictionary. ... In the comprehension code above, you create a new dictionary double_dict1 from a dictionary dict1 by simply doubling each value in it. You can also make changes to the key values.

# lst = []
# for i in range(100):
#     if i%3==0:
#         lst.append(i)
# print(lst)

# /////////////comprehension means the short code or smart code 
# /////////////comprehension for list
# ls =[i for i in range(3,90) if i%4==0]
# print(ls)

# ////////////comprehension of the dictionary
# dict1={i:f"item{i}" for i in range(7)}
# dict2={value:key for key,value in dict1.items()}

# print(dict1,dict2)

# ////////////comprehension of the set
# S={color for color in ["red","black","blue","red"]}
# print(type(S))

# ///////////comprehension for generator
# generator use a yield function and this is use using the itrator
# if we itrate a generator function then we use __next__() function for genrating one value
# and if want to print all the values then we use for loop
# even=(i for i in range(15,50) if i%2==0)
# print(even.__next__())
# for item in even:
#     print(item)
# print(type(even))


# def ls(n):
    # lst=[i for i in str(num)]
    # values=[]
    # for i in values:
    #     values.append(i)
    # again=input("to run again press 1 and for exit press any key")
    # if again==1:
    #     ls(n)
    # else:
    #     print("thanks!")
# num=input("Enter any names which we want to comprehansion:   ")
# lst=ls(num)
# print(lst)


# /////////////this is the quiz first of all we enter values then select which the directry enter the values
values=input("Enter any names which we want to comprehansion:   ")
lst=values.split( )
choose=int(input("for store value list press 1, press 2 to store values in dictionary and press 3 to store vales in sets:  "))
if choose==1:
    ls=[i for i in lst]
    print(ls)
elif choose==2:
    dic={i:f"item {i}" for i in lst}
    print(dic)
elif choose==3:
    s={i for i in lst}
    print(s)