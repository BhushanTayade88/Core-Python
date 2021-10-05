'''
5.Given a string input,count all lower case, upper case and digits without using built-in functions.
e.g s = "HelLo12"
o/p: uppercase:2, lowercase:3, digits:2
'''
s= "HelLo12"
upper=[]
lower=[]
digits=[]

for i in s:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    else:
        digits.append(i)
print("Uppercase  :",len(upper))
print("Lowercase  :",len(lower))
print("Digits  :",len(digits))

s2 = "HelLo12"
l = 0
u = 0
n = 0
for i in s: 
    if (i>='a'and i<='z'):
        l=l+1                     
    elif  (i>='A'and i<='Z'):
        u=u+1
    else:
        n=n+1
print("Lower case characters:",l) 
print("Upper case characters: ",u) 
print("numbers are  :",n)        
