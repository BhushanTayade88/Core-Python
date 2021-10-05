'''
4.Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
'''

tuple1 = (11, [22, 33], 44, 55)

a,b,c,d=tuple1
b[0]=222
tuple1=a,b,c,d
print(tuple1)


tuple1[1][1]=222
print(tuple1)

        

