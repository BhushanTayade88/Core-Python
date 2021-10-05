'''
1.Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

Expected output:
20
'''
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
a,b,c=aTuple
for i in aTuple:
    for n in i:
        if n==20:
            print(n)
    
print(aTuple[1][1])
