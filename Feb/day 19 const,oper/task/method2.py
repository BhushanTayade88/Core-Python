class A:
    def m1(self,*a):
        s=0
        for i in a:
            s=s+i
        print(s)
            
a=A()
a.m1()
a.m1(5,6)
a.m1(9,10,12,6,8)
