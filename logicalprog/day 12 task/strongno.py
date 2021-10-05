'''
strong no = sum of factorials of digit is same
145=1!+4!+5!=145
'''
n=int(input("Enter a number to whether it is Palindrome no or not :"))
num = n
fact1 = 0
while n>0:
    fact = 1
    rem = n % 10
    for i in range(rem,0,-1):
        fact = fact * i
    fact1 += fact    
    n //= 10
    
if num == fact1:
    print(num,"is a Strong no")
else:
    print(num,"is not a Strong no")

