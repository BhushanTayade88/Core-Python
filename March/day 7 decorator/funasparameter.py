# function as parameter

def m1():
    print("m1....start")

def m2(func):
    print("m2-------")
    func()
m2(m1)

def m3(a):
    print("m3....start")
    print(a)

def m4(func):
    print("m4-------")
    func(5)
m4(m3)
    
