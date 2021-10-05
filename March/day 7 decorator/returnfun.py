# return functio

def m1():
    print("m1-----start")
def m2():
    print("m2-----")
    return m1
x=m1()
x()



# x= m1()
# x()----------->error
