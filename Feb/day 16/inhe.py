class Grandfather:
    z=30
class Father(Grandfather):

    x=10
    def m1(self):
        pass

class Mother(Grandfather):
    y=20
    def m2(self):
        pass



class child(Father,Mother):
    pass




c=child()
print(c.x)
print(c.y)
