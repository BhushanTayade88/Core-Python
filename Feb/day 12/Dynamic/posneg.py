#2.Program to create positive-negative elements list from given list.
l=[]
pos=[]
neg=[]
n=int(input("Enter How many no u wanrt to add  :"))
for i in range(n):
    b=int(input("add nos to list  :"))
    l.append(b)
for i in l:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print("----Statements----\n" 
      "1.Dispaly List elemets--\n" 
      "2.Display +ve no on list--\n" 
      "3.Display -ve no on list--\n" 
      "4.Exit--\n")
while True:
    no=int(input("Enter ur choice  :"))
    if no>=3:
        pass
    if no==1:
        print(l)
    elif no==2:
        print(pos)
    elif no==3:
        print(neg)
    elif no==4:
        break
    else:
        print("wrong choice")
