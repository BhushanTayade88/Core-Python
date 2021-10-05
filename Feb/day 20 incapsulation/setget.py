class Student:
    __rn=1
    __name=' '
    __maarks=85

    def  setRn(self,r):
        self.__rn=r

    def getRn(self):
        return self.__rn

s1=Student()
s1.setRn(101)
print(s1.getRn())
