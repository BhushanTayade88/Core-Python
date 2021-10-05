'''
Cdegrees=[]  [20,30,45,56]
Fdegrees=[]---> 
F = (9.0/5)*C + 32

table=[Cdegrees,Fdegrees]
Print the values
'''
cdegrees=[20,30,45,56]
fdegrees=[]
table=[cdegrees,fdegrees]
for  i in cdegrees:
	f=(9/5)*i+32
	fdegrees.append(f)

print("F Deegree is  :",fdegrees)
print("Cdegree and fdegree is  :",table)
