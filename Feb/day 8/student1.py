class Student:
	def  __init__(self,srollno,sname):
		self.srollno=srollno
		self.sname=sname
	def display(self):
		return "Student Rollno:{1} and Student Name{0}:".format(self.srollno,self.sname)

stud=Student(101,"bhushan")
stud1=Student(102,"xyz")

print(stud.display())
print(stud1.display())
	