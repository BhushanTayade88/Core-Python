class employee:
	def __init__(self,empid,empname,sal,city):
		self.empid=empid
		self.empname=empname
		self.sal=sal
		self.city=city

emp=employee(101,"bhushan",600000,"yavatmal")
emp1=employee(102,"xyz",500000,"pune")
print(emp.empid)
print(emp.empname)
print(emp.sal)
print(emp.city)
print(emp1.empid)
print(emp1.empname)
print(emp1.sal)
print(emp1.city)

