# /////////////////Dimand shape inheritance//////////////////////////
# in this tutorial class A inherit class B and C and class B and C is inherit class D
# when we print d class variables then first of all check it in own class than check it base class and than chk it super class
# multilevel inheritance couldnot supported some languages but python manage this inheritance very easily
# diamond shap inheritance control some difficult because it has some issue and create problems


class A:
    def net(self):
        print("this is the variable of class A")
class B(A):
    def net(self):
        print("this is the variable of class B")
class C(A):
    def net(self):
        print("this is the variable of class C")
class D(B,C):
    def net(self):
        print("this is the variable of class D")

# instance variables
a = A()
b= B()
c= C()
d= D()

d.net()

