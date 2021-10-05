'''
def m1():
    print("m1---start")
    if True:
        return 10
    print("Hello")
    return 30
x=m1()
print(x)
'''
def m1():
    x=10
    try:
        print("try=---block")

        return x
    finally:

        print("finally---Block")


x=m1()
print(x)
