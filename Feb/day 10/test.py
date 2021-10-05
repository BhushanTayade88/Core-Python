from emp import *

print("----Statements----\n" \
      "1.Enter details--\n" \
      "2.display--\n" \
      "3.Exit--\n")
while True:
	ch=int(input("Enter Your choice----:"))
	if ch<=2:
		pass
		
	if ch==1:
		l=[]
		n=int(input("enter no. do u want to add"))

		for i in range(n):
			e=Employee(int(input("Enter Employee ID :")),input("Enter name :"),int(input("Enter salary  :")))
			l.append(e)


	elif ch==2:
		for emp in l:
			print(emp)
		
		             
	elif ch==3:
		break

	else:
		print("***Wrong Choice***")


