
l=[1,7,3,4,1,7,10,5]


num=7
l2=[]
for i in range(0,len(l)):
    if l[i]==num:
        l2.append(i)
print(l2)
for i in l2:
    l[i-1]=0
    l[i]=0
    l[i+1]=0
total=sum(l)
print(total)
