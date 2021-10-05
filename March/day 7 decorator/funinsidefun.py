#function insie fun

def m1():
    print("m1----start")
    def m2():
        print("m2---inside m1 function")

    m2()
    print("m1-----end")

m1()
