'''
Program to cube each number of the list using Lambda function
'''

l=[1,2,3,4,5,6,7,8,9]

cube=list(map(lambda a:a*a*a ,l))
print(cube)
