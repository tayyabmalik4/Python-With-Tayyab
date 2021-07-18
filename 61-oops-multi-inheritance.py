#//////////////////////// this is the multiple inheritance tutorial ////////////////////////////
# multiple inheritance is define as two or more than two classes inherit in one class
# in this inheritance we acces all the properties in class who inherit the upper classes 
# the simply to say that all aecces of upper classes in one class
# //////////////////////////// END//////////////////////


class Employee:
    field = "IT Professional"

    def __init__(self, nname, ssallry):
        self.name = nname
        self.sallry= ssallry
    def printdetails(self):
        return f"your name is {self.name} and your sallry is {self.sallry}"
    @classmethod
    def change_classvar(cls, newfield):
        cls.field = newfield
    @classmethod
    def change_const(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1])
        return cls(*string.split("-"))
    @staticmethod
    def simple(string):
        return ("your name is "+ string)



zahid = Employee("Zahid Gafoor", 5600)
junaid= Employee.change_const("junaid Latif-56779")
# print(junaid.printdetails())
# print(zahid.simple("zahid Gafoor"))


class player:
    members = 12
    def __init__(self,playername,age,experince):
        self.name = playername
        self.age= age
        self.experince= experince

    def details(self):
        return f"player name is {self.name}.player age is {self.age} and your experince is {self.experince}"

osama = player("osama",20,4)
print(osama.details())



class programmer(Employee,player):
    exp = "2 years"

tayyab=programmer.change_const("tayyab malik-56099")
print(tayyab.printdetails())

        