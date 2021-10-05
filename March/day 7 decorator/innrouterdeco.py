def m1():
    print("m1----")

    def m2():
        print("m2-----inner")
    m2()
    print("m1-----outer function end")
    return m2


m2=m1()
m2()
