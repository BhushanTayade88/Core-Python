n=15
b = 9
for i in range(1, 8):
    print(" "*n, "* "*(i)) 
    #print("* "*(i)) 
    n-=1
    
for i in range(8,0,-1):
    print(" "*b, end="")
    print("* "*(i))
    b +=1
