
l1 = ["Hello","Bye"]
l2 = ["Pune","Mumbai"]

l3=[l1[0]+l2[0],l1[0]+l2[1],l1[1]+l2[0],l1[1]+l2[1]]
print(l3)
l4=[l1[i]+l2[j] for i in range(len(l1)) for j in range(len(l1))]
print(l4)
'''

result_str=""   
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column ==5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+"-"    
    result_str=result_str+"\n"    
print(result_str)
'''