'''
8. l1 = ["M","na","i","Em"]
   l2 = ["y","me","s","ma"]

o/p : ["My","name","is","Emma"]  without using any built-in function.
try with list comprehention
'''
l1 = ["M","na","i","Em"]
l2 = ["y","me","s","ma"]
l3=[]
for x,y in zip(l1,l2):
    z=x+y
    l3.append(z)
print(l3)
l4=[]
for i in range(len(l1)):
    l4.append(l1[i]+l2[i])

print(l4)               
l5 = [i + j for i, j in zip(l1, l2)]
print(l5)
l6=[l1[i]+l2[i] for i in range(len(l1))]
print(l6)
a=zip(l1,l2)
for i,j in a:
    print(i+j,end =" ")