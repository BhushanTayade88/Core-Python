'''
* 
* * 
* - * 
* - - * 
* - - * * 
* - - - - * 
* - - - - - * 
* * * * * * * *
'''

row = 8
for i in range(row):
   
    for j in range(i+1):
        
        if j==0 or j==i  or i==row-1 :
            print('*',end=" ")
        else:
            print(" ", end=" ")
   
    print(" ")
    
