class Student:
    __rn=1
    marks=80
    def __m1(self):
        print("m1 method")
    def m2(self):
        print("m2 method")
        print(self.__rn)
        self.__m1()

s1=Student()
s1.m2()
#print(s1.m1)
#print(s1.__rn)
print(s1.marks)
