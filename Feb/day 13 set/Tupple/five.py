'''
5.Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))
'''

def Sort(tuple1):  
  
    
    return(sorted(tuple1, key = lambda x: x[1]))   
  

tuple1 =  (('a', 23),('b', 37),('c', 11), ('d',29))


print(Sort(tuple1))





