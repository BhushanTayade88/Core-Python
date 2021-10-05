'''
55555
45555
34555
23455
12345
'''
n = 5
no = 4

for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end="")
        #print("5"*no,end="")
        #"5"*(i-1)
        
    print("5"*no)
    no -= 1
