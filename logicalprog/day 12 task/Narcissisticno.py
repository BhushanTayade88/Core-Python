'''
Narcissistic no - sum of its own digits each raised to power of no digits
1634--->no of digits 4
    --->1^4 + 6^4 + 3^4 + 4^4 = 1634
'''
n=int(input("Enter a number  :"))
num = n
no = num
digits = 0
sum1 = 0
while n>0:
    rem = n % 10
    digits += 1   
    n //= 10
while num>0:
    qu = 1
    rem = num % 10
    for i in range(1,digits+1):
        qu = qu * rem
    sum1 += qu
    num //= 10

print(sum1)
print(digits)
if no == sum1:
    print(no,"is a Narcissistic no")
else:
    print(no,"is not a Narcissistic no")

