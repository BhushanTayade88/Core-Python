def outer_func(func):
    def inner_func(a,b):
        print("before calling the actual function")
        func(a,b)
        #func2(a,b)
        print("after calling actual function")
    return inner_func

@outer_func
def m1(a,b):
    print(a+b)
    
##@outer_func
##def m2(a,b):
##    print((a*b)
##          
m1(20,30)
