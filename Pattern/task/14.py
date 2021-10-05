'''
     5
    54
   543
  5432
 54321
'''
space = 5
n = 5
for i in range(n,0,-1):
    print(" "*space,end="")
    for j in range(n,i-1,-1):
        print(j,end="")  
    space -= 1    
    print("")
