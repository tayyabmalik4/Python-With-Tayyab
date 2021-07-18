with open("readfile.txt","rt") as f:
    a = f.readlines()
    print(a)

f = open("readfile.txt" , "rt")
print(f.readline())
f.close()