
class Student:
##    __strollno = 0
##    __stname = ' '
##    __physics = 0
##    __chemistry = 0
##    __biology = 0
##    __math = 0

    def setRollno(self,rn):
        self.__strollno = rn
    def setName(self,nm):    
        self.__stname = nm
    def setPhysics(self,ph):
        self.__physics = ph
    def setChemistry(self,ch):
        self.__chemistry = ch
    def setBiology(self,bio):
        self.__biology = bio
    def setMath(self,mt):
        self.__math = mt

    def getRollno(self):
        return self.__strollno
    def getName(self):    
        return self.__stname 
    def getPhysics(self):
        return self.__physics 
    def getChemistry(self):
        return self.__chemistry 
    def getBiology(self):
        return self.__biology 
    def getMath(self):
        return self.__math 

