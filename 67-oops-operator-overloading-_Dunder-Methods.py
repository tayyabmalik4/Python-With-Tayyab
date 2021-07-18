# ///////////////operators overloading and dunder methods tutorails//////////////////
# functions who start or end double underscore(__)are called dundar methods
# for example __init__() , __add__() etc
# operators overloading means two or more operators are creators in one function and than use various
# when we use just as a name of instance variable than we use __repr__ function or __str__ function 
# if we use repr and str at a same time than python prefer str function first
# repr function only use when we wish to call him and str function is not present in the program
#below explain it with example

class Employee:
    field = "IT Professional"
    def __init__(self,nname, ssallry,jjob):
        self.name= nname
        self.sallry = ssallry
        self.job = jjob
    def details(self):
        return f"your name is {self.name}.your sallry is {self.sallry} and your job is {self.job}"
    def __add__(self,other):
        # return self.sallry + other.sallry
        return self.name + other.name
    def __truediv__(self,other):
        return self.sallry / other.sallry
    def __mul__(self,other):
        return self.sallry *other.sallry
    def __pow__(params,other):
        return params.sallry ** other.sallry
    def __mod__(param1,param2):
        return param1.sallry % param2.sallry
    def __sub__(param1,param2):
        return param1.sallry -param2.sallry
    # use __repr__ function
    def __repr__(self):
        return f"Employee ('{self.name}',{self.sallry},'{self.job}')"
    
    # use __str__ function
    def __str__(self):
        return f"your name is {self.name}. Your sallry is {self.sallry} and your job is {self.job}"
    # inthis case all data convert into one string and this is not use any operator to other but use only string to
    @classmethod
    def const(cls, string):
        return cls(*string.split("-"))

        
        # return 678        # //////////this is the default set value
zahid = Employee("zahid Gafoor", 48, "web developer")
junaid= Employee("junaid latif",2, "professional")
tayyab = Employee("Tayyab Ashraf",46, "programmer")
osama = Employee.const("osama aslam-5678-doce")

print(zahid +junaid)
print(zahid /junaid)
print(zahid *junaid)
print(zahid **junaid)
print(zahid%junaid)
print(junaid-tayyab)
print(zahid)
print(tayyab)
print(osama)
# this is not use because osama constructor has one string but just use as string to string not at all
print(osama +zahid)


