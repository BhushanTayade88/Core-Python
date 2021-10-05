#1.Program to create odd-even elements list from given list.
l=[]
eve=[]
odd=[]
n=int(input("How many no u wants add in list  :"))
for i in range(n):
    a=int(input("Enter Numbers  :"))
    l.append(a)
for i in l:
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
    
print("----Statements----\n" \
      "1.List elemets--\n" \
      "2.Display Even no on list--\n" \
      "3.Display Odd no on list--\n" \
      "4.Exit--\n")


while True:
    ch=int(input("Enter your choice  :"))
    if ch<=3:
        pass
    if ch==1:
        print(l)
    elif ch==2:
        print(eve)
    elif ch==3:
        print(odd)
    elif ch==4:
        break
    else:
        print("wrong choiice")
        
        


    
    
    







    

    
