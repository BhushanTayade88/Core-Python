class A:
    def m1(self,a=0,b=0):
        if a!=0 and b!=0:
            print(" double argument pass")
        elif a!=0:
            print("single argument pass")
        else:
            print("noo argument")

a=A()
a.m1()
a.m1(5,6)
a.m1(9)
