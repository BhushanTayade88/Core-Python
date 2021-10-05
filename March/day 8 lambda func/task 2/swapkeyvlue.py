d = {1:'a' , 2:'b' , 3:'c' , 4:'b' , 5:'a'}
d2={}
for k,v in d.items():
    d2[v]=k

print(d2)

d3={1:'a' , 2:'b' , 3:'c' , 4:'b' , 5:'a'}
d4={}


for key, value in d3.items():
   if value in d4:
       d4[value].append(key)
   else:
       d4[value] = [key]
        
print(d4)       

