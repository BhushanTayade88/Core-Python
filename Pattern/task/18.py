'''
11111
2222
333
44
5
'''
n = 5
a = 0
for i in range(n,0,-1):
    a += 1
    for j in range(0,i,1):
        print(a,end="")
    print("")
