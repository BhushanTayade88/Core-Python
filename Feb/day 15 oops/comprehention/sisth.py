'''
6.matrix = [[1, 2], [3,4], [5,6], [7,8]]
Expected output:
[[1, 3, 5, 7], [2, 4, 6, 8]]
'''
matrix = [[1, 2], [3,4], [5,6], [7,8]]

l=[k for k,v in matrix ]
print(l)
a=[[row[i] for row in matrix]for i in range(2)]
print(a)
