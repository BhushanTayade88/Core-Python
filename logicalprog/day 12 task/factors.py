'''
Factors of a no
6 = 1*2*3 and 6
'''
n=int(input("Enter a number  :"))
num = n
print("factors of a number",n)
while n>0:
    fact = 1
    #rem = n % 10
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
            
    n = 0 
   # n //= 10
    


