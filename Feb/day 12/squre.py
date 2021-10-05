#5.Program to turn every element of list into its square.


l=[2,6,8,9,12,45,13,7,85,20,46]
squre=[]

for num in l:
	z=num*num
	
	squre.append(z)
print(l)
print(squre)
sqr = [x*x for x in l if x%2==1]
print(sqr)
for i in range(len(l)):
        l[i]=l[i]*l[i]
        

print(l)

'''
for num in :

        z=num*num
        l.insert(num,z)
                 
        

print(l)
'''
