class A:
    a=10
    def m1(self):
        print("m1.......A")
class B(A):
    def m1(self):
        print("m1.......B")
class C(A):
    def m1(self):
        print("m1.......C")
class D(B,C):
    
    
    def m1(self):
        print("m1.......D")
        print(self.a)
        super().m1()
        A.m1(self)


a=D()
a.m1()
print(D.mro())

    
