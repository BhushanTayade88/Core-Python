'''
5
44
333
2222
11111
'''
n = 5
for i in range(n,0,-1):
    for j in range(n+1-i):
        print(i,end="")
    print("")
