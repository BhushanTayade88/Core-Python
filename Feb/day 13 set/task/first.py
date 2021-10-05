'''
1.Return a set of identical items from a given two Python set
set1 = [10, 20, 30, 40, 50]
set2 = [30, 40, 50, 60, 70]

Expected output:
{40, 50, 30}
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

s3=set()
s3=set1.intersection(set2)
print(s3)

s4=set()
s4=set1-set2
print(s4)
