#///////////// the result is false as we print b is a but return true when b==a because the values are same but refrance is not same 
# ////////////// ----------------------   "==" means value equality and "is" means that refrance equality


# //////////in this program values are equal but refrence are difference
# a= [5,7,"tayyab"]
# b=[5,7,"tayyab"]
# a= [2,4,5,3]
# b=[2,4,5,3]
# print(b is a)
# print(b==a)

# ///////////in this program values and refrance are same
a=[23,45,3,1]
b=a
print(b is a)
print(b==a)