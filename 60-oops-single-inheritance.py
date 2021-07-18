# /////////////////////////sigle inheritance///////////////////
# sigle inheritance is define as inherit one class to other class
# thats means all acces of the inherited class in this class
# inherit means acces 
# ///////////////////////END///////////////////////////////

class Employee:
    field = "IT professional"
    
    def __init__(self, aname, ssallry, jjob):
        self.name = aname
        self.sallry = ssallry
        self.job = jjob

    def printdetails(self):
        return f"your name is {self.name}. your sallry is {self.sallry} and your job is {self.job}"

    @classmethod
    def chang_field(cls, newfield):
        cls.field= newfield
    
    @classmethod
    def chang_const(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def man(string):
        return ("your name is "+ string)

zahid = Employee("zahid Gafoor", 459900, "programmer")
junaid = Employee.chang_const("junaid-560000-specialist")
# print(junaid.printdetails())
# print(junaid.man("junaid"))


class prog(Employee):
    def __init__(self, aname, ssallry, jjob,llanguage):
        self.name = aname
        self.sallry = ssallry
        self.job = jjob
        self.lang = llanguage

    def printprog(self):
        return f"your name is {self.name}. your sallry is {self.sallry} , your roll is {self.job} and your learn languages {self.lang}"

    @classmethod
    def chang_construct(cls, string):
        return cls(*string.split("-"))

tayyab = prog("tayyab", 4500, "programmer", ["python","php"])
uzair = prog.chang_construct("uzair ahmad-45890-scientist-not IT RElated")

print(tayyab.printprog())
print(uzair.printprog())
        
