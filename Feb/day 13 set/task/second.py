'''
2.Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Expected output:
{70, 40, 10, 50, 20, 60, 30}
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s3=set()
#s3=set1.union(set2)
#union
s3=set1 | set2
print(s3) 

#intersection
print(set1.intersection(set2))#print(set1 & set2)

#Difference
print(set1.difference(set2))#print(set1 - set2)

#Symetric-Difference
print(set1.symmetric_difference(set2))