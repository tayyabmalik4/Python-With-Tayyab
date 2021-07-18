class Employee:
    field= "IT Professional"

    def __init__(self, nname, ssallry, jjob):
        self.name= nname
        self.sallry= ssallry
        self.job = jjob

    def printdetails(self):
        return f"your name is {self.name}. your sallry is {self.sallry} and your job is {self.job}"

    @classmethod
    def chang_val(cls, string):
        cls.field = string
    
    @classmethod
    def chang_cont(cls, string):
        # params= string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))


# this is the static method tutorial
# in this tutorial he says that the static mrthod function is works through calling class and other way to tell making decorators of the class
# static method basically works as a class variable 
# in simple static method is just to make a vvariable which helps to make one time and usee the 
    @staticmethod
    def stat(simple):
        print("your name is "+ simple)
    


zahid = Employee("zahid Gafoor", 45000 , "A Good Dream A Good Life")
junaid = Employee.chang_cont("junaid-4500-professional")

zahid.chang_val("spacialist programmer")
zahid.stat(" Gafoor sab")
print(zahid.field)
print(junaid.job)