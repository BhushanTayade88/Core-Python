class A:
    def __init__(self,func):
        self.func=func
    def __call__(self,a):
        print("before calling actual function")
        s=self.func(a)#m1()
        print("after calling the actual function")
        return s 
@A
def m1(x):
    print("m1-----",x)
    return "cjc"

    
v=m1(100)
print(v)


