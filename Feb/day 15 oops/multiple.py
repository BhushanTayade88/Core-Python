class A:
    a=10
    def m1(self):
        print("m1.......A")
class B():
    def m1(self):
        print("m1.......B")
        super().m1
class C(B,A):
    def m1(self):
        print("m1.......C")
        super().m1()

a=C()
a.m1()
print(C.__mro__)
