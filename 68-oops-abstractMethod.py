#  //////////////////////////////      using abc module use abstractmethod base class     ////////////////////
# achully its use when we want to more than one class and we wish wvery class use the same function as use abstrat method
# if after the abstratmethod making we don't use this function than we face some error
# and they is apply just which classes which we inherit it 
# in this method we use 'abc' module and import ABCMeta and abstractmethod instance of import ABCand abstractmethod
# ABC module apply who the python version 3.4 above
# which class is base class which we define abc module this class has not to made any instance varyable 




# from abc import ABCMeta,abstractmethod
from abc import ABC, abstractmethod
class shap(ABC):
    @abstractmethod
    def printrec(self):
        return 0

class Rectangular(shap):
    sides = 4
    def __init__(self):
        self.lenght= 6
        self.width= 7
    def printrec(self):
        return self.lenght *self.width

ract1= Rectangular()
shape1=shap()
print(ract1.printrec())
# print(shape1.printrec())
