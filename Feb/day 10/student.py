class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name

l=[]
n=int(input("enter no. do u want to add"))

for i in range(n):
	s=Student(int(input("Enter rollno :")),input("Enter name :"))
	l.append(s)

for stud in l:
	print(stud.rollno)
	print(stud.name)
