# /////////////////////setter and property of decorators tutorial//////////////
# setter means a value is set at the top
# and by the help of property of decorators we covert the function to simple variable like below
# by the help of function we change the value anywhere with in the class
# when we made in the constractor variable than we can't change the values at any point in this class
#  when we use a new email than first of all creat decorator with the name of upper function and also use the .setter property
# and the condotion is the uper function is also created as the same name and the setter property function is also created same function
# its created when we wish to creat again email
# when we created then use with the help of setter module name and when we wish to delete the function than we use del function
# otherwise it is not working and arrer here 

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email= f"your email is now {fname}.{lname}@codewithtayyab.com"

    def explain(self):
        return f"your full name is {self.fname}.{self.lname}"
# at the starting of property of decorators

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "your email has not set at right now"
        return f"your email is now {self.fname}.{self.lname}@codewithtayyab.com"
    # starting using setter property 
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname= name.split(".")[0]
        self.lname=name.split(".")[1]
    # starting using delete property
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None



    @classmethod
    def const(cls,string):
        return cls(*string.split("-"))
    # def __str__(self):
    #     return f"Employee({self.fname},{self.lname})"

zahid= Employee("zahid","Gafoor")
# junaid=Employee.const("junaid-Latif")
junaid=Employee("junaid","Lateef")
print(junaid.email)
junaid.fname="janta"
print(junaid.email)
junaid.email= "janta.jano@junaid.com"
print(junaid.email)
del(junaid.email)
print(junaid.email)
