'''
8.Given a list,
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 

Expected output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
l=[]
for i in matrix:
    for a in i:
        l.append(a)
print(l)
l2=[a for i in matrix for a in i]
print(l2)
