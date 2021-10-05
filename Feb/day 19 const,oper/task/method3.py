from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def  m1(self,a,b):
        print(a)
        print(b)


a=A()
a.m1(1,3)
