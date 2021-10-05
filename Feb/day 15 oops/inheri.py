class A:
    a=10


    def m1(self):
        print("m1----A")
class B(A):
    
    def m2(self):
        print("m2----B")
        self.m1()
        

b=B()
b.m2()
print(b.a)
