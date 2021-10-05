class student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
 	

stud=student(101,"xyz")
stud1=student(102,"abc")
print("Student Roll no  :",stud.rollno)
print("Student Name  :",stud.name)
print("Student Roll no  :",stud1.rollno)
print("Student Name :",stud1.name)