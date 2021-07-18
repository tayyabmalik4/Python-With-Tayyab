# publis----- the data which every one acces it is cllad private data and this is easy to use and in python it is simple
# protected-----the data which just acces in class and this is denoted in python "_first"----
# ----first of all one underscore in fisrt in the variable
# private---- which is just acces a admin panal
# private is denoted by "__secend"
# private variable can access doudle underscore at the start of variable
# every class access public variable
# just super and driverd class acces protected variable
# just super class access private variable but in this case one candition apply
# if we use private variable then we use one underscore(_) and then class name which we creat private variable
# in python when we create private variable--tis is the name is name-angaling

class Employee:
    field = "Software Emgineer"
    # this is the protected example
    _prot= "this is the best example of protected"
    # this is the example of 
    __privatevar= "this is the best example of private variabal"

class prog(Employee):
    pass
zahid = Employee()
print(zahid._Employee__privatevar)

