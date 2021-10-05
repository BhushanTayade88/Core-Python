def outer_f(func):
    def inner_f():
        print("Hi")
        func()
        print("Hello")
    return inner_f

@outer_f
def m1():
    print("m1----")
#m1=outer_f(m1)
m1()
