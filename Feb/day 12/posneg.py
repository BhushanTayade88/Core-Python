#2.Program to create positive-negative elements list from given list.

list1 = [0,11, -21, 6, 45, 66, -93] 
pos=[]
neg=[] 

for num in list1: 
      
    
        if num >= 0: 
                pos.append(num)
        else:
                neg.append(num)

print("+ve nos are  :",pos)
print("-ve nos are  :",neg)
