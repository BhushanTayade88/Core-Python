class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
l=[]
s1=Student(1,"xyz")
l.append(s1)
s2=Student(2,"abc")
l.append(s2)

for stu in l:
	print(stu.rollno)
	print(stu.name)
if s1 in l:
        print("yes,s1 is in list l")
else:
        print("not present")
