class Employee:
    # field is the class variable which we use all the objects but don't change using objects
    field= "information tecnology A good dream A good life"
    pass
tayyab=Employee()
junaid=Employee()
zahid = Employee()

tayyab.name = "arman"
tayyab.roll = "programmer"
tayyab.sallry ="none"
tayyab.dream= "A good bussness man"

junaid.name = "janta"
junaid.roll = "Good programmer"
junaid.sallry = "none"
junaid.dream = "Go to jurmany"

zahid.name = "zahid"
zahid.roll = "best programmer"
zahid.sallary = "none"
zahid.dream= "Go to jurmany"

#///////////////////// .__dict__ function is return the dictionary 
print(junaid.__dict__)

print(zahid.dream)
print(junaid.roll)
print(tayyab.field)