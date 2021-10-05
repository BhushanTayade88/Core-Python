from calculation import *
print("----Statements----\n" \
      "1.Addition--\n" \
      "2.Subtraction--\n" \
      "3.Multiplication--\n" \
      "4.Division--\n" \
      "5.FloorDivision--\n" \
      "6.Power--\n" \
      "7.Modulus--\n" \
      "8.Exit--\n")
while True:	
    ch=int(input("Enter your Choice :"))
    if ch<=7:
         x=int(input("Enter First no :"))
         y=int(input("Enter Second no :"))
        
    if ch==1:
        print("you enter value for addition")
        s=A(x)
        s1=A(y)
        print(s+s1)
    elif ch==2:
        print("you enter value for subtraction")
        s=A(x)
        s1=A(y)
        print(s-s1)
    elif ch==3:
        print("you enter value for Multiplication")
        s=A(x)
        s1=A(y)
        print(s*s1)
    elif ch==4:
        print("you enter value for Division")
        s=A(x)
        s1=A(y)
        print(s/s1)
    elif ch==5:
        print("you enter value for FooloorDivision")
        s=A(x)
        s1=A(y)
        print(s//s1)
    elif ch==6:
        print("you enter value for Power")
        s=A(x)
        s1=A(y)
        print(s**s1)
    elif ch==7:
        print("you enter value for Modulus")
        s=A(x)
        s1=A(y)
        print(s%s1)
    elif ch==8:
        
        print("progeam end")
        break
    else:
        print("Wrong choice")
