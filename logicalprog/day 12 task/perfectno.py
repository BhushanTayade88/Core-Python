'''
Perfect no = sum of factors is same
6 = 1+2+3 excluding 6
'''
n=int(input("Enter a number to check it is a Perfect no :"))
num = n
fact1 = 0
while n>0:
    fact = 0
    rem = n % 10
    for i in range(1,rem):
        
        if n % i == 0:
            fact += i
    fact1 += fact    
    n //= 10
    
print(fact1)
if num == fact1:
    print(num,"is a Perfect no")
else:
    print(num,"is not a Perfect no")

