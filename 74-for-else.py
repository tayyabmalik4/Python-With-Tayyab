# ////////////for ka sath else
# in this for loop we use else just at this time when for loop properly ended and exicuted
# but when we use break statment then else did not work
# examples are explain in the following


lst= ["zahid","tayyab","junaid","uzair","zaheer","mohsin","zulafqar","shahzaib"]

# /////////else has properly working
for i in lst:
    # print(i)
# /////////////else has not working because break statment is used and for loop break
    if i=="uzair":
        print(i)
        break

else:
    print("you are for loop is exicuted properly")