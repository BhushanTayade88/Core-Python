def add(a,b):
	c=a+b
	return c
def sub(a,b):
	c=a-b
	return c
def mul(a,b):
	c=a*b
	return c

print("----Statements----\n" \
      "1.Addition--\n" \
      "2.Subtraction--\n" \
      "3.Multiplication--\n" \
      "4.Exit--\n")
while True:
	
	ch=int(input("Enter your Choice"))
	'''
                if ch<=3:
		x=int(input("Enter First no"))
		y=int(input("Enter Second no"))
        '''

	if ch==1:
		s=add(20,30)
		print("Addition--",s)
	elif ch==2:
		s=sub(40,10)
		print("Subtraction--",s)
	elif ch==3:
		s=mul(45,2)
		print("Multiplication--",s)
	elif ch==4:
                break
	
        
	else:
                print("Wrong choice")
