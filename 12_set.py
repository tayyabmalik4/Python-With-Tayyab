# this is the set tutorial
# set is a datatype .stes always add a uniq value and just one value in one time and it is aranged the data automatically
s= set()
s.add(2)
s.add(2)
s.add(1)
s.remove(2)
# these are the functions of the set
print(len(s))
print(max(s))
print(min(s))
print(type(s))
# s1 = s.union({1,2,3,4})
s2 = s.intersection({1,2,3,4,5})
print(s,s2)
# print(s,s1)
# print(type(s))
# l= [1,3,7,4,9,11,1]
# s_from_list = set(l)
# s_from_list = set([1,3,5,7])
# print(s_from_list) 