'''
Armstrong no: sum of cube of digits is equal to the original no.
153= 1^3+5^3+3^3
eg. 0,1,370,153,371,407
'''
n=int(input("Enter a number to whether it is Armstrong no or not :"))
num = n
sum=0
while n>0:
    rem= n % 10
    sum += rem**3
    
    n //= 10
if num == sum:
    print(num,"is a Armstrong no ")
else:
    print(num,"is not a Armstrong no ")
