'''
Neon no-Squre of no-sum digits of squre is ssame as original
'''
n=int(input("Enter a number :"))
num = n
sqr = n*n
sum1=0
print(f"squre of {n} is :{sqr}")  
while sqr > 0:
    rem = sqr % 10
    sum1 += rem    
    sqr //= 10
    
if num == sum1:
    print(num,"is a Neon no")
else:
    print(num,"is not a Neon no")

