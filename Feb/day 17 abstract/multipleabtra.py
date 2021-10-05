from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("m3----A")

class B(ABC):               #not necesary for class B to inherit ABC class
    @abstractmethod
    def m3(self):
        print("m1-----B")
    @abstractmethod    
    def m4(self):
        pass

    


class C(A,B):
    def m2(self):
        print("m2----C")
        
    def m4(self):
        print("m4-----C")
    def m1(self):
        print("m1----C")
##    def m3(self):
##        print("m3----C")
        

m=C()
m.m3()
m.m2()
              
