class A:
    def  m1(self):
        print("m1---of A")


class B:
    def m2(self):
        print("m2--- of B")


def comman(obj):
    if hasattr(obj,"m1"):
        obj.m1()
    elif hasattr(obj,"m2"):
        obj.m2()

comman(B())
comman(A())
