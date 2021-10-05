from operator import attrgetter
class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name

	def __str__(self):
		return "Roll No :-{} and Name :-{}".format(self.rollno,self.name)

s1=Student(2,"bbb")
s2=Student(1,"aaa")
s3=Student(3,"ccc")
l=[s1,s2,s3]

for stu in l:
	print(stu)

l.sort(key=attrgetter('rollno'))

for stu in l:
        print(stu)

	
