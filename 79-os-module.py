# ////////////////os module////////////////
# os means that operating system
# os handle all the satuation about machine and it is a head of a machine 
# achully os is communicate between user and machine
# in this os modue in the python, the python developer provide some function using operating system and this is very helpful
# help means to ecces the files and folders and rename of the file or folder creating the file ,open the file and also changing the file and very other functions
# os module is a very complex module and it is provide in the python website
# os mofule can help in Artificial intalligance and also very helpful in machine learning
# os module is helping to acces the directory and also to very other functions so it is very helpful

import os
# print(dir(os))
# //////getcwd function is help to chk the current working directory
# print(os.getcwd())
# /////////chdir function is help to go to the new directory
# os.chdir("C://")
# print(os.getcwd())
# /////////////listdir function is use to acces all the files and folders
# print(os.listdir("C://"))
# ////////////if we want to creat a folder than we use the mkdir function
# os.mkdir("this")
# ///////////and if we want to creat more than one folders than we use makedirs function
# os.makedirs("this/that")
# //////////if we want to remane of the file than we use the remane(current name,changed name) function
# os.rename("test5_health.py","test05_gym_app.py")
# //////////if we want to handle the environment veriables and read it then we use this function os.environ.get("filename")
# print(os.environ.get('path'))
# //////////if we want to join to directorys than we use this function. the main function is use the function is ignore the mistaskes
# print(os.path.join("C://","/tayyab.txt"))
# /////////if we want to check that the folders exist or not than we use this function 
# /////////and if file is exits than return true other wise return false
# print(os.path.exists("C://"))
# /////////if we want to check the file exists or not than we use os.path.isfile(filename)
# print(os.path.isfile("C://xampp"))