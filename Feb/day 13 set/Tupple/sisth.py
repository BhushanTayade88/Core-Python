'''
6.Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)Expected output:True
'''
'''
t1=(45,45,46,45)
def check(t1):
    return all(i == t1[0] for i in t1)
print(check(t1))
tuple1 = (45, 45, 45, 45)

no=tuple1[0]
cond=True
for i in tuple1:
    if no != i:
        cond=False
        break
if (cond==True):
    print("True")
else:
    print("false")
'''
t=(45,45,45,45)
t1=(45,45,46,45)
t2=[]
s=set(t)

if len(s)==1:
    print("same")
else:
    print("diff")

for i in t1:
    if i==45:
        z=True
        t2.append(z)
    else:
        z=False
        t2.append(z)
x=all(t2)
print(x)
   



   
