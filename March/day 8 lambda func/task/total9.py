'''
9.li = [5, 8, 10, 20, 50, 100] Find out sum of elements of list
'''
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
total=reduce(lambda a,b:a+b ,li)
print(total)
