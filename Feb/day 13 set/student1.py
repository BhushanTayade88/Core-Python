class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def __str__(self):
		return "Student Roll no :{} and Student Name :{}".format(self.rollno,self.name)


eng=set()
comp=set()
mech=set()
n=int(input("How many student u want add for comp :"))
for i in range(n):
	s1=Student(int(input("Enter roono  :")),(input("Enter name  :")))
	comp.add(s1)
n=int(input("How many student u want add for mech :"))
for i in range(n):
	s1=Student(int(input("Enter roono  :")),(input("Enter name  :")))
	mech.add(s1)

compf=frozenset(comp)
mechf=frozenset(mech)

eng=(compf,mechf)	

for stud in eng:
	for stu in stud:
		print(stu)
		

