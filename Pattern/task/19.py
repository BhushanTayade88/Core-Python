'''
     1
    12
   123
  1234
 12345
'''
space = 5
n = 5
for i in range(1,n+1):
    print(" "*space,end="")
    for j in range(1,i+1):
        print(j,end="")  
    space -= 1    
    print("")
