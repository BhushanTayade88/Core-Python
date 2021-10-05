def outer_func(func):
    def inner_func():
        print("before calling the actual function")
        func()
        print("after calling actual function")
    return inner_func

@outer_func
def m1():
    print("m1--function")

#m1=outer_func(m1)--------->
m1()
