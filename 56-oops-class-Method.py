# //////////////////////////class method /////////////////////////
# class method hum class ka variables ko change krna ka leya use krta han using class and also using instace variables sa be
# for example field ek class variable ha
# es ko hum wasa instance variables sa change nai kr skta but class method ka through hum change kr skta han
# class method ma sab sa pahla hum decoraters means @ use kr ka class ko integrate krta han
# pher ek new function bnaty han jis ma ek variable cls hota jo k object ko call krwata ha
# or next wo hota jis ke hum na value change krni hoty
# last ma hum esa call krwa lata han or sath ma change kr lata han
# ager hum instance variable ka through wasa class variables ko change krna ke koshish kran to ek new variable ban jata ha



class Employee:
    field = "IT professionals------A Good Dream A Good Life"

    def __init__(self, aname, ajob, aroll):
        self.name = aname
        self.job = ajob
        self.roll = aroll
        # ////////starting class Method function////////////
    @classmethod
    def chang_field(cls, newfield):
        cls.field = newfield
# /////////////////// End function////////////////
    def printdetails(self):
        return f"your name is {self.name }. Your job is {self.job} and your roll is {self.roll}"
    
zahid = Employee("zahid Gafoor", "IT professional", "web Developer")
junaid = Employee("Junaid Lateef", "IT spachalist", "Full stack developer")

zahid.chang_field("Artificial Intaligance -----A Good dream a good life")

print(junaid.printdetails())
print(zahid.field)
