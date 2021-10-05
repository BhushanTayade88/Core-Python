class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name

	def __str__(self):
		return "Roll No :-{} and Name :-{}".format(self.rollno,self.name)

def getrollno(obj):
	return obj.rollno
def getname(obj):
	return obj.name

s1=Student(2,"aaa")
s2=Student(1,"ccc")
s3=Student(3,"bbb")
l=[s1,s2,s3]

for stu in l:
	print(stu)

l=sorted(l,key=getname,reverse=True)
for stu in l:
        print(stu)
