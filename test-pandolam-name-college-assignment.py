# this is the college assignment 
# assigment is check that the num is pandolam or not
# pandolam means if we reverse the name than if the name is same after the reversing the name than it is pandolam



num=input("enter the any name:   ")
lst1=[item for item in num]
lst=[i for i in num]
# print(lst)
lst.reverse()
# print(lst1)
if lst1==lst:
     print("the num is pandolam")
else:
    print("try Again")

   
