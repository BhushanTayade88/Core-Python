l=[1,2,1,2]

num=2
l2=[]
for i in range(0,len(l)):
    if l[i]==num:
        l2.append(i)
print(l2)
for i in l2:
    #del l[(i-1):(i+2)]
    l[i-1]=0
    l[i]=0
    if (i+1) == len(l):
        l[-1]=0
    else:
        l[i+1]=0
total=sum(l)
print(total)
