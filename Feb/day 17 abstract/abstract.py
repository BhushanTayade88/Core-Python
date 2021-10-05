from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    def m2(self):
        print("m2-----A")
   
    @abstractmethod
    def m3(self):
        pass
       

class B(A):
    def m1(self):
        print("m1-----B")
    def m3(self):
        print("m3----B")
b=B()
b.m2()
b.m1()    
