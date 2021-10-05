from emp2 import *

print("----Statements----\n" \
      "1.Enter details--\n" \
      "2.display--\n" \
      "3.Exit--\n")
while True:
	ch=int(input("Enter Your choice----:"))
	if ch<=2:
		pass
		
	if ch==1:
		a=int(input("Enter Employee ID:"))
		b=input("Enter EMP Name  :")
		c=int(input("Enter salary  :"))
		d=input("Enter City  :")
		emp1=employee(a,b,c,d)

	elif ch==2:
		# emp1=employee(a,b,c,d)
		emp1.showemp()
		#a.disp()
		#b.disp()
	
	elif ch==3:
		break

	else:
		print("***Wrong Choice***")

