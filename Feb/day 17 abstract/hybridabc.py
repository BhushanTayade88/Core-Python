from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        print("m1---A")

    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("m3----A")

class B(A):

    pass
        
    



class C(A):
    def m1(self):
        
        super().m1()
    def m2(self):
        print("m2----C")
        
    def m4(self):
        print("m4-----C")



class D(C,B):
    pass
d=D()
d.m1()
              
