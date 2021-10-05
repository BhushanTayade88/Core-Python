class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name

s1=Student(1,"xyz")
s2=Student(2,"abc")
l=[s1,s2]

stu=l[0]
print(stu.rollno)
print(stu.name)
stu=l[1]
print(stu.rollno)
print(stu.name)
