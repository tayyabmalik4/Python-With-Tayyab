class Employee:
    field = "IT professional . A Good Dream A Good Life"
    
    def __init__(self, nname, ssallry, rroll):
        self.name = nname
        self.sallry = ssallry
        self.roll = rroll

    def printdetails(self):
        return f"the name is {self.name}. The sallary is {self.sallry} and the roll is {self.roll}"

    @classmethod
    def chang_field(cls, newfield):
        cls.field = newfield

# this is the class methods as alternative constructors tutorail
# es tutorail ka sab sa main kam ye ha k hum ek asa constructor bna skta han jis ma ek string ka through jitni marzy values print krwa skta han
# sab sa pahla ek class method bnata han os ka bd ek function bnata han
# os function ma ek array ka through values jaty ha 
# for example ek params variable bnaya os ko array ma set kr dia 
# if we want to solve in one line than "cls(*string.split("-"))" code is written
# in this code * means the args-----who learn in previous tutorial
# in this code its help about the pythonic way and much code reuseability
    
    @classmethod
    def chang_construct(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))



    
    
    
zahid = Employee("zahid Gafoor", 500000, "programmer")
junaid = Employee("junaid Lateef", 132300 ,"full kstack")
tayyab = Employee.chang_construct("tayyabmalik-56800-Artifial Inteligancer")

# zahid.chang_field("spacialist")
# print(zahid.field)
# print(zahid.sallry)
print(tayyab.printdetails())