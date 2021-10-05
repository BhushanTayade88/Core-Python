def squre(func): 
    def inner(args): 
        x = func(args)
##        y = x * x
##        func(y)
##        print("squre is  :",x*x)
        return x*x
    return inner 
    
def multiply(func): 
    def inner(args): 
        x = func(args)
##        y = x * 2
##        print("multiplication is   :",x*2)
##        func(y)
        return x*2
    return inner

@multiply  
##@squre
def num(no): 
    return no
  
n=int(input("Enter a number  :"))
print(num(n)) 
