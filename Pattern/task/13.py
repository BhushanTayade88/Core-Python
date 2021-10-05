'''
1
2
13
24
135
246
1357
2468
'''
n=10
for i in range(1, n ): 
        k = i 
        for j in range(1, i + 1): 
            if k % 2 == 0:  
                print(j, end = '') 
            else: 
                print('', end = '') 
            k -= 1 
        print("")
