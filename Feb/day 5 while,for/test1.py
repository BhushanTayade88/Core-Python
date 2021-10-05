from cal2 import *
print("----Statements----\n" \
      "1.Addition--\n" \
      "2.Subtraction--\n" \
      "3.Multiplication--\n" \
      "4.Exit--\n")
while True:
	
	ch=int(input("Enter your Choice"))
	if ch<=3:
		x=int(input("Enter First no"))
		y=int(input("Enter Second no"))

	if ch==1:
		s=add(x,y)
		print("Addition--",s)
	elif ch==2:
		s=sub(x,y)
		print("Subtraction--",s)
	elif ch==3:
		s=mul(x,y)
		print("Multiplication--",s)
	elif ch==4:
		break
	else:
		print("Wrong choice")
