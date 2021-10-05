def m1():
    print("m1----")

    def m2():
        print("m2-----inner")
    m2()
    print("m1-----outer function end")



m1()
