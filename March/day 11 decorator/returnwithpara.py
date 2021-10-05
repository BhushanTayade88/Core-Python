def outer_func(func):
    def inner_func(a,b):
        print("before calling the actual function")
        result=func(a,b)
        print("after calling actual function")
    return inner_func

@outer_func
def m1(a,b):
    c=a+b
    return c
    
ans = m1(20,30)
print(ans)
