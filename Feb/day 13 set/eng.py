
class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name


eng=set()
comp=set()

n=int(input("How many student u want add for comp :"))
for i in range(n):
        stu=Student(int(input("Enter rollno  :")),(input("Enter name  :")))
        comp.add(stu)

mech=set()
n=int(input("How many student u want add for mech :"))
for i in range(n):
        stu=Student(int(input("Enter rollno  :")),(input("Enter name  :")))
        mech.add(stu)

compf=frozenset(comp)
mechf=frozenset(mech)

eng=(compf,mechf)	

for stud in eng:
	for stu in stud:
		print(stu.rollno)
		print(stu.name)

