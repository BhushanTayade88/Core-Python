'''
10.lis = [ 1 , 3, 5, 6, 2, ]  Find out the maximum element of the list using lambd function.
'''
from functools import reduce

lis = [ 1 , 3, 5, 6, 2, 8]
l2=[ 1 , 3, 5, 6, 2, 8]
total2=list(map (lambda a,b:a if a>=b else b , lis,l2))

print(total2)


maxl=reduce(lambda a,b:a if a>b else b ,lis)
print(maxl)


#print(max(maxl))
