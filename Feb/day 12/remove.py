'''
10.Remove completely the 5's from the list.
l = [1,5,6,7,5,2,7,8,5,9,5,4,5]
***  try with while loop***
'''
l = [1,5,6,3,3,3,3,7,5,2,7,4,4,4,8,5,9,5,4,5]

#l.remove(5)

for i in l:
        if i==5:
                l.remove(i)
                

print(l)


while 3 in l:
        l.remove(3)
print(l)

