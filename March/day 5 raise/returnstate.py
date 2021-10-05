def m1():
    print("m1-------------")
    a=10

    try:
        print("try --block")
        return a
    finally:
        a=20
        print("fianally block")
        #return a
x=m1()
print(x)
