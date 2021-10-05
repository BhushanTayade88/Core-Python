class employee:
	def __init__(self,empid,empname,sal,city):
		self.empid=empid
		self.empname=empname
		self.sal=sal
		self.city=city
	def disp(self):
		print("Employee ID    :",self.empid)
		print("Employee Name  :",self.empname)
		print("Salary         :",self.sal)
		print("city           :",self.city)

a=employee(101,"bhushan",600000,"yavatmal")
b=employee(102,"xyz",500000,"pune")
'''
emp.disp()
emp1.disp()
'''
'''
print(emp.empid)
print(emp.empname)
print(emp.sal)
print(emp.city)
print(emp1.empid)
print(emp1.empname)
print(emp1.sal)
print(emp1.city)
'''
