class  employee:
	pass

emp=employee()
a=int(input("Enter Employee ID  :"))
b=input("Enter Employee Name   :")
c=input("Enter Employee Designation   :")
emp.id=a
emp.name=b
emp.desg=c

emp1=employee()
a=int(input("Enter Employee ID  :"))
b=input("Enter Employee Name   :")
c=input("Enter Employee Designation   :")

emp1.id=a
emp1.name=b
emp1.desg=c


print("Employee ID  :",emp.id)
print("Employee Name  :",emp.name)
print("Employee Designation  :",emp.desg)
print("Employee ID  :",emp1.id)
print("Employee Name  :",emp1.name)
print("Employee Designation  :",emp1.desg)
