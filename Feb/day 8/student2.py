class Student:
	def  __init__(self,srollno,sname):
		self.srollno=srollno
		self.sname=sname
	def __str__(self):
		return "Student Rollno:{} and Student Name:{}".format(self.srollno,self.sname)

stud=Student(101,"bhushan")
stud1=Student(102,"xyz")

print(stud)
print(stud1)
	
