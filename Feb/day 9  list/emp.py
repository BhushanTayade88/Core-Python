class Employee:
	def __init__(self,empid,empname):
		self.empid=empid
		self.empname=empname

e1=Employee(1,"abc")
e2=Employee(2,"pqr")

dev=[e1,e2]

e3=Employee(3,"xyz")
e4=Employee(4,"asd")

tes=[e3,e4]

soft=[dev,tes]

for l in soft:
	for emp in l:
		print(emp.empid)
		print(emp.empname)