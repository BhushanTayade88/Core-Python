##import copy
##l=[1,2,3,4,5,6,7,8,9]

##l3=copy.deepcopy(l)
##l.clear()
##for x in l3:
##    l.insert(0,x)
##    
##print(l)
l2=[1,2,3,4,5,6,7,8,9,10]
l=[1,2,3,4,5,6,7,8,9,10]
print(len(l)/2)

##for i in range(int(len(l)/2)):
##    #print(l[i])
##    #print(l[len(l)-(i+1)])
##    x=l[i]
##    l[i] =l[len(l)-(i+1)]
##    l[len(l)-(i+1)] = x
## 
##print(l)

for i in range(len(l)//2):
    l[len(l)-(i+1)],l[i]=l[i],l[len(l)-(i+1)]
print(l)
    
