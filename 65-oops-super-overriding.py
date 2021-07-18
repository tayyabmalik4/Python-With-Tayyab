# ///////////////////////super() and overriding tutorial//////////////
# overriding means 2 or more variables created in same name and previos variables are override 
# in overriding programn check first of all instane variables or function
# than if instance variable are not awailable then check it simple variables
# 
class Employee:
    var= "this is the variable of class Employee"
    def __init__(self):
        self.var1="this is the instance variable"
        self.var="instance variable"
        self.spacial= "spacial variable"
    
class prog(Employee):
    var2="this is the class variavle of class programming"
    var="class b"
    # now constractor is override and now previous constructor is not awailabel at this time--
    # if we use previous constructor calling than we use "super()" function--
    # if super function run at the first and we wish to run var1 and var than program run at the class b --
    # because b program first go to class Employee but than go to class prog and than override these variables--
    # but the condition is to run prog class if we run Employee class than run automatically class Employee.
    # if we wish run variables of class Employee than super function run at the end of constructor of prog class
    def __init__(self):
        super().__init__()
        self.var1= "this is class b variable"
        self.var="class b"
        # super().__init__()
        print(super().var)

zahid = Employee()
junaid = prog()
print(junaid.spacial,junaid.var1,junaid.var)
print(zahid.spacial,zahid.var1,zahid.var)