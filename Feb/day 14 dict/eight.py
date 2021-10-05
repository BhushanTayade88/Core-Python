'''
8.Get the key corresponding to the minimum value from the following dictionary
sampleDict = {'Physics': 82,'Math': 65,'history': 75}

Expected output:
Math
'''
'''
d= {'Physics': 82,'Math': 65,'history': 75}
l=[]

for k,v in d.items():
    l.append(v)
print(l)

print("minimum item is",min(l))
    
A-Z 65-90    
a-z 97-122
0-9 48-57

'''
d= {'Physics': 82,'Math': 65,'history': 75}
print(min(d))# by default works on keys
print(min(d,key=d.get))
