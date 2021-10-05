class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name


s = set()

s1=Student(1,"abc")       #(int(input("Enter roono  :")),(input("Enter name  :"))
s.add(s1)           
s2=Student(2,"xyz")
s.add(s2)
for stud in s:
	print(stud.rollno)
	print(stud.name)

