class student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
 	
x=int(input("Enter Roll no :"))
y=input("Enter Student Name  :")
stud=student(x,y)
x=int(input("Enter Roll no :"))
y=input("Enter Student Name  :")
stud1=student(x,y)
print("Student Roll no\t:",stud.rollno)
print("Student Name\t:",stud.name)
print("Student Roll no\t:",stud1.rollno)
print("Student Name\t:",stud1.name)
