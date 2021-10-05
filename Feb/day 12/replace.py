'''
l=[2,6,10,9,10,45,13,7,10,20,10]
l2=[]

for num,i in enumerate(l):
        


        if i==10:
                l[num]=100
                #l[10].replace[100]
			
                
        
print(l2)
print(l)
'''

l=[10,2,3,4,5,7,10,2,3,10]

for i in range(len(l)):
    if l[i]==10:
        l.pop(i)
        l.insert(i,100)
                   
                  
print(l)                   
a=10
b=100
l2=[10,2,3,4,5,7,10,2,3,10]
for i in range(len((l2))):
               if l2[i]==a:
                   l2[i]=100
               
print(l2)


