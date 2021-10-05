'''
Palindrome no = reverse is same as original no
121,1221,343
'''
n=int(input("Enter a number to whether it is Palindrome no or not :"))
num = n
rev = 0
while n>0:
    rem = n % 10
    rev =rev * 10 + rem
    n //= 10
if num == rev:
    print(num,"is a Palindrome no")
else:
    print(num,"is not a Palindrome no")
