l=[1,2,3,4]


num = 2
l2=[]
for i in range(0,len(l)):
    if l[i]==num:
        l2.append(i)
print(l2)
for i in l2:
    print(i)
    del l[(i-1):(i+2)]
print(l)




