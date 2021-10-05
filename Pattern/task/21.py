'''
1 
1 2 3 
1 2 3 4 5 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
'''
n = 10
for i in range(1,n,2):  
    for j in range(1,i+1):  
        print(j, end=' ')    
    print("")  
