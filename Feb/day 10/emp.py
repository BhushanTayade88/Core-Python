class Employee:
	def __init__(self,empid,empname,sal):
		self.empid=empid
		self.empname=empname
		self.sal=sal
		
	def __str__(self):

                return "Employee ID: {},Employee name  :{} and Employee salary :{}".format(self.empid,self.empname,self.sal)
		
		


