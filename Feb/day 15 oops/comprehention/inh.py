class A:
    x = 10
    y = 20

    def m1(self):
        print("m1---A")

    def m2(self):
        print("m2---A")

class B:
    x = 50
    z = 100

    def m2(self):
        print("m2---B")

    def m3(self):
        print("m3---B")

class C(A,B):
    y = 200
    p = 300

    def m2(self):
        print("m2---C")

    def m4(self):
        print("m4---C")

    def m5(self):
        print("m5---C")
               
class D(C):
    p = 800
    y = 900

    def m4(self):
        print("m4---D")

    def m6(self):
        print("m6---D")

class E(C):
    w = 600
    q = 700
    p = 300

    def m4(self):
        print("m4---E")

    def m7(self):
        print("m7---E")


