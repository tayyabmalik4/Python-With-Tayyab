class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"email is {self.fname}{self.lname}@codewithtayyab.com"
    
    def explain(self):
        return f"your email is now {self.fname}.{self.lname}"
    
zahid=Employee("zahid","gafoor")

print(zahid.email)
# these are the methods which we check the variable,instance variable ,function and etc which are exit class which the type of variable or etc
# achully every variable or instance variable or function has diff id which the save as the backend in the server
# dir function use which all functions are exit in the class
# inspect function is achully a module which is import it and than use it 
# and also use inspect function which also use show all the functions and module with id which is used in the class
# inspect functions has many types and the roll is different at any type
# below are the examples and explain it 
# print(type(zahid))
# print(dir(zahid))
# print(id(zahid))

import inspect
print(inspect.getmembers(zahid))
# it is use which check the instance variable is true or false
# print(inspect.isbuiltin(zahid))
# print(inspect.getfile(zahid))
 