#4.Program to check elements of list are divisible by a number taken by user and create a separate list of divisible elements.
l=[10,12,45,63,89,78,10,-3,-74,25,50,46]
l2=[]
l3=[]
print(l)
a=int(input("Enter a no :"))
for i in l:
    if i%a==0:
        l2.append(i)
    else:
        l3.append(i)
        
print("List elements divisible by ",a,"are",l2)
