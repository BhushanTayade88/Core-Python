class A:
    def  m1(self):
        print("m1---of A")


class B:
    def m1(self):
        print("m1 of B")


def comman(obj):
    obj.m1()

comman(A())
