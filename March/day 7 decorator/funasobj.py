def m1():
    print("M1-----start")

m1()
m2=m1
m2()
del m1
m2()
