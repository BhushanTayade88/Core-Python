class employee:
	def __init__(self,empid,empname,sal,city):
		self.empid=empid
		self.empname=empname
		self.sal=sal
		self.city=city
	def showemp(self):
		print("Employee ID    :",self.empid)
		print("Employee Name  :",self.empname)
		print("Salary         :",self.sal)
		print("city           :",self.city)
	def __str__(self):
		return "Employee id:{},Employee name:{},salary:{}and City:{}".format(self.empid,self.empname,self.sal,self.city)


if  __name__ == '__main__':

        a=int(input("Enter Employee ID\t:"))
        b=input("Enter EMP Name\t:")
        c=int(input("Enter salary\t:"))
        d=input("Enter City\t:")
        emp=employee(a,b,c,d)

        a=int(input("Enter Employee ID\t:"))
        b=input("Enter EMP Name\t:")
        c=int(input("Enter salary\t:"))
        d=input("Enter City\t:")
        emp1=employee(a,b,c,d)

if  __name__ == '__main__':
        emp.showemp()
        emp1.showemp()


