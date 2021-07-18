# f string basically sum of all the variables is one string

# this is the the %s method to attach the values
# me = "tayyab"
# a=40
# z = "zahid"
# a1="this is the %s %s %s"%(me , a ,z)
# print(a1)

# this is the .format method to attach the values
# me = "tayyab"
# a=40
# z = "zahid"
# a1 = "This is the {} {} {}"
# b = a1.format(me,a,z)
# print(b)

# finally this is the f string method to attch the values
me = "tayyab"
a=40
z = "zahid"
b = f"this is the f string pattern and it is soo easy {me} {a} {z}"
print(b)
