# in this tutorial we learn about self and __init__ function constructor 
# ///////////////////////////////////self concept//////////////////
# sab sa pahla ek function bnaty han os ma ek argument data han
#  pher os ka through variables ko integrate kr data han 
# pher jab function ko run krta waqat function ma argument nai data kue k ye automatic he argument da data ha in just python
# ////////////////////////////consructor concept////////////////////////////
# constructor ka sab sa bara faida ye hota ha k hum ek he dafa variables set kr data han 
# ek function hota ha __init__(self) or ye class ka ander banta ha
# es ma self ek object ko call krwata ha or es ka aga sara variables laga data han jin ke huma zrort hoty ha
# pher os ka through hum necha values set kr data han or 
# pher necha function ma jo hum na bnaya hota ha os ma sab values lekh data han
# es sa huma faida ye hota ha k ek to humra program short hota ha 
# dosra hum sab ka differnce asani sa kr lata han
# or huma bht asani hoty ha koi be chz add ya remove krna sa
# achully constuctor arguments ana ma humry help krta ha or wo function __init__ ka through krta han wasa hum loi argument nai laa skta
 
class Employee:
    field = "information Tecnology. A good dream A good life"
    # in variables ma sab ka sath a es leya lagaya k koi confusion na ho
    def __init__(self, aname, ajob , aroll) :
        self.name =aname
        self.job = ajob
        self.roll = aroll

    def printdetails(self):
        return f"The name of the student is {self.name}. the job of the {self.job} and the roll of {self.roll} "

zahid =Employee("zahid Gafoor", "IT professional","Web Developer")
# junaid = Employee()

# zahid.name = "zahid-Gafoor"
# zahid.job= "web developer"
# zahid.roll = "front end"

# junaid.name = "junaid lateef"
# junaid.job = "full stack web developer"
# junaid.roll = "front end and backend developer"

# print(junaid.printdetails())
# print(zahid.field)

# ///////es ko ab hum jasa marzy tread kr skta han means ek dafa he ma be sab print krwa skta han or alag alag be chooice is yours
print(zahid.job)
print(zahid.printdetails())