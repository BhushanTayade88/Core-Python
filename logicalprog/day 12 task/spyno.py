'''
Spy no :- addition and multiplication of digits is same
2411
'''
n=int(input("Enter a number :"))
num = n
sum1 = 0
mul = 1
while n>0:
    rem = n % 10
    mul = mul * rem
    sum1 += rem    
    n //= 10
    
if mul == sum1:
    print(num,"is a Spy no")
else:
    print(num,"is not a Spy no")

