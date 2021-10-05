l=[10,12,13,10,5,5,6,7,8,7,2,3,2,5,10]
print("List elements are :",l)
a=int(input("choose no u want  to replace :"))
b=int(input("Choose no u want to place at that position :"))
for i in range(len(l)):
    if l[i]==a:
        l[i]=b

print("After replace with new element :",l)
