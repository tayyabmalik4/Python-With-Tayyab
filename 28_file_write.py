# this tutorial is to creat a new file and write a file and also appending a data to a file 
# if file is already exit then file is reset when we use write function
# f = open("readfile.txt","w")
# f = open("readfile.txt","a")
# a=f.write("but junaid is my fried \n")
# print(a)
# f.close()

# f= open("readfile2.txt","w")
# f.write("this is the readfile2 file is creat and write it this content")
# f.close()

# handle read and write to use r+ function
f = open("readfile2.txt" , "r+")
print(f.read())
f.write("\nthank you for this")