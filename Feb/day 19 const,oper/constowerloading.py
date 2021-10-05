class A:
    def __init__(self,a=None,b=None):
        if a!=None and b!=None :
            print(" u enter two parameter")
        elif a!=None:
            print("u enter single parameter")
        else:
            print(" no argument pass")
a=A()
a=A(2,3)

a=A(5)
