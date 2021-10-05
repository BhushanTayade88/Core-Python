'''
'''
n=10
for i in range(n + 1,1,-1): 
        a = i
        for j in range(1, i + 1,2): 
            if a % 2 == 0 :
                print(j, end = '') 
            
        print("")

##for i in range(n,0,-1):
##    for j in range(1,6,-1):
##        print(j,end="")
##    print(""),
