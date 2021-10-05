'''
1.Accept string from a user and display only those characters which are present at an even index number.
do with for loop
'''

a=input("Enter your name  :")
b=a[ : :2]
print(b)

for i in range(0, len(a), 2):
    print(i,a[i] )
