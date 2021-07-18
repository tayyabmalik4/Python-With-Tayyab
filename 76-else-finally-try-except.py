# ////////////this is the else, finally and try excpt tutorial////////////////
#//////////////// first of all we understand the concept of else
# else means that if except condition is false means not run than else condition is true and it is run 
# and if except codition is true than else is not work
# except is exicute when try condition is false
# when try condition is true than else condition is also true and exicuted
# //////////////finally condition///////////////////
# finally condition is absolute run other condtions run or not run it is absolute run
# we handle errors are errors are IO()ERROR and EOF(End of file)ERROR and so onn

print("this is the else and finally module in try execpt conditions")
try:
    # /////this is the existing file
    file=open("junaid-exe.txt")
    # //////this is not existing file
    f=open("tayyab.py")
except Exception as e:
    print(e)
else:
    print("importent documents")

finally:
    print("this is the finally function which is exicuted obviosly")

print("hey there i wish to build a AI in future ")
file.close()

