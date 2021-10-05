class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name

	def __str__(self):
		return "Student rollno :{} and Student name  :{}".format(self.rollno,self.name)

s1=Student(1,"abc")
s2=Student(2,"xyz")

t=(s1,s2)

for stu in t:
	print(stu)
