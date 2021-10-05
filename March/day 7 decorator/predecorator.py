def outer_f(func):
    def inner_f(a,b):
        print("inner--function---start")
        func(a,b)
        c=a+b
        print(c)
        print("inner--function---End")
    return inner_f

@outer_f
def m1(a,b):
    print("m1----")

m1(5,10)
