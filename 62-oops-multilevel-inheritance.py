# ////////////////////////////////Multi level inheritance////////////////////////////////
# multilevel inheritance is define as classes are inherit each other
# for example one class inherit 2nd class and 2nd class inherit 3rd class and soo onn
# when 1st class inherit 2nd class then 2nd class all data access and when 2nd class inherit 3rd class then 2nd class data transfor in 3rd class.
# and 3rd class automatically acces all the 1st class
# /////////////////////END/////////////////////////////////////  

class dad:
    football = "very good played"
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def details(self):
        return f"your name is {self.name} and your age is {self.age}"

class son(dad):
    criket="Awosom player"
    def __init__(self, nname, aage, exp):
        self.name = nname
        self.age = aage
        self.exp = exp
    def printdet(self):
        return f"your name is {self.name}.your age is {self.age} and your exp is {self.exp}"

class grandsun(son):
    bedmintan = "very good and awosome player"
    def __init__(self, nname, aage, exp, dance):
        self.name = nname
        self.age = aage
        self.exp = exp
        self.dance= dance
    def det(self):
        return f"your name is {self.name}. your age is {self.age}, your experince is {self.exp} and your dance is {self.dance}"

zahid= son("zahid",21,34)
print(zahid.printdet())