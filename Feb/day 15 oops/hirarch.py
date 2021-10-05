class A:
    a=10
    def m1(self):
        print("m1.......A")
class B(A):
    def m1(self):
        print("m1.......B")
        super().m1
class C(A):
    def m1(self):
        print("m1.......C")
        super().m1()

a=C()
a.m1()
b=B()
b.m1()
print(C.__mro__)
