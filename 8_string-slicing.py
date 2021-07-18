#this is the string slicing tutorial
tayyab="this is the python programming language" 
#len is to find lenght in variable
print(len(tayyab))
print(tayyab[0:10])
#these two codes are the same 
print(tayyab[0:39:2])
print(tayyab[::2])

#this is to read to of the back
print(tayyab[-10:])
print(tayyab[-4::-1])

#threse are the functions
print(tayyab.isalnum())
print(tayyab.isalpha())
print(tayyab.endswith("language"))
print(tayyab.count("a"))
print(tayyab.capitalize())
print(tayyab.find("is"))
print(tayyab.lower())
print(tayyab.upper())
print(tayyab.replace("language" , "not compilar"))
