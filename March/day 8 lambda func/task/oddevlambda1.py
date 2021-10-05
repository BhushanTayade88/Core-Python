'''
1.Program to find odd and even elements list from given list using Lambda function.
'''
l=[1,2,3,4,5,6,7,8,9]

even=list(filter(lambda a:a%2 == 0 ,l))
print(even)
odd=list(filter(lambda a:a%2 != 0 ,l))
print(odd)
