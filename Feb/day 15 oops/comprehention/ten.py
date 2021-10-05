'''
10.Print 5's table
Multiplication Table
[5, 1, 5]
[5, 2, 10]
[5, 3, 15]
[5, 4, 20]
[5, 5, 25]
[5, 6, 30]
[5, 7, 35]
[5, 8, 40]
[5, 9, 45]
[5, 10, 50]
'''
n=5
l=[]
for i in range(1,11,1):
    z=n*i
    l.append(z)
print(l)
l2=[[n,i,n*i] for i in range(1,11)]

for i in l2:
    print(i)
