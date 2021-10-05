from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        print("m1-----of A")

    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("m3----A")

class B(A):

    def m1(self):
        print("m1-----B")
        super().m1()
    @abstractmethod
    def m5(self):
        pass

##o=B()
##o.m1()


class C(B):
    def m2(self):
        print("m2----C")
        
    def m4(self):
        print("m4-----C")
    def m5(self):
        pass

m=C()
m.m1()
m.m3()
              
