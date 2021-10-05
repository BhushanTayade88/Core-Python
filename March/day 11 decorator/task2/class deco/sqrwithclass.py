class A:
    def __init__(self,func):
        self.func=func
    def __call__(self,n,m):
        
        s=self.func(n,m)
        
def squre(func): 
        def inner(args): 
            x = args 
            y = x * x
            func(y,x)
            
        return inner 
      
def multiply(func): 
        def inner(args): 
            x = args
            y = x * 2
            print("multiplication is   :",y)
            func(y)
        return inner
@multiply  
@squre
@A
def num(sqr,a): 
    print(sqr)
    print(a)
  
n=int(input("Enter a number  :"))
v=num(n) 
