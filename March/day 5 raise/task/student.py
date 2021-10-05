class Student:
    __strollno = 0
    __stname = ' '
    __stmarks = 0
    def setRollno(self,rn):
        self.__strollno = rn
    def setName(self,nm):
        self.__stname = nm
    def setMarks(self,mk):
        self.__stmarks = mk

    def getRollno(self):
        return self.__strollno
    def getName(self):
        return self.__stname
    def getMarks(self):
        return self.__stmarks


