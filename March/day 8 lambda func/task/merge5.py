'''
5.Python program to add two given lists using Lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
Result: after adding two list
[5, 7, 9]
'''
from functools import reduce
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

##total=list(reduce(lambda a,b:a+b , nums1,nums2)))
##
##print(total)

total2=list(map(lambda a,b:a+b , nums1,nums2))

print(total2)



