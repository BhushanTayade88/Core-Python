#1.Program to create odd-even elements list from given list.

l=[2,5,6,3,4,89,12,36,37,39,11,13,16]
odd=[]
eve=[]

for i in l:
	if i%2==0:
		eve.append(i)
	else:
		odd.append(i)
print("Exiting list is :",l)
print("Even no are  :",eve)
print("Odd no are  :",odd)
